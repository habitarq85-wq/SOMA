const BASE = 'https://soma-853c.onrender.com';

// Estado persistente entre invocaciones (Cache API de Cloudflare Workers).
// cachePut/cacheGet devuelven una promesa para evitar race conditions en el cron.
function cacheGet(key) {
  return caches.default.match(`https://soma-cache.local/${key}`).then(r => r ? r.text() : null);
}

function cachePut(key, value) {
  return caches.default.put(
    `https://soma-cache.local/${key}`,
    new Response(String(value))
  ).then(() => true).catch(() => false);
}

async function notify(component, detail) {
  const sent = await cacheGet(`alert_${component}`);
  if (sent) return; // ya se avisó y sigue el problema
  try {
    const r = await fetch(`${BASE}/health/alert`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ component, detail }),
    });
    const j = await r.json();
    if (j.status === 'sent') {
      // marcar avisado por 30 min (mismo window que el servidor)
      await cachePut(`alert_${component}`, Date.now());
      console.log(`ALERT sent: ${component}`);
    }
  } catch (e) {
    console.log(`ALERT failed: ${component} — ${e.message}`);
  }
}

async function checkHealth() {
  let j;
  try {
    const r = await fetch(`${BASE}/health`, { headers: { 'User-Agent': 'Cloudflare-Worker' } });
    j = await r.json();
  } catch (e) {
    await notify('server', `No responde /health: ${e.message}`);
    return;
  }

  const checks = j.checks || {};
  for (const comp of ['server', 'db', 'brevo']) {
    const val = checks[comp];
    if (!val || val === 'ok') {
      // componente recuperado: limpiar estado de alerta
      await caches.default.delete(`https://soma-cache.local/alert_${comp}`).catch(() => {});
    } else {
      await notify(comp, val);
    }
  }
}

export default {
  async scheduled(event, env, ctx) {
    // 1. keep-warm: mantener Render y BD vivos (como antes)
    const targets = [
      BASE,
      `${BASE}/keepwarm`,
    ];
    await Promise.allSettled(targets.map(url =>
      fetch(url, { method: 'GET', headers: { 'User-Agent': 'Cloudflare-Worker' } })
        .then(r => ({ url, status: r.status, ok: r.ok }))
        .catch(e => ({ url, error: e.message }))
    ));

    // 2. health: detectar fallas y alertar por correo
    await checkHealth();
  },

  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    if (url.pathname === '/__ping') {
      const r = await fetch(BASE);
      return new Response(`Render status: ${r.status}`, { status: 200 });
    }
    if (url.pathname === '/__health') {
      try {
        const r = await fetch(`${BASE}/health`);
        return new Response(await r.text(), { status: r.status, headers: { 'Content-Type': 'application/json' } });
      } catch (e) {
        return new Response(JSON.stringify({ status: 'degraded', error: e.message }), { status: 200 });
      }
    }
    return new Response('SOMA Keep Warm + Health Worker — cron cada 5 min', { status: 200 });
  },
};
