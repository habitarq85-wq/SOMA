export default {
  async scheduled(event, env, ctx) {
    const targets = [
      'https://soma-853c.onrender.com',
      'https://soma-853c.onrender.com/keepwarm',
    ];

    const results = await Promise.allSettled(
      targets.map(url =>
        fetch(url, { method: 'GET', headers: { 'User-Agent': 'Cloudflare-Worker' } })
          .then(r => ({ url, status: r.status, ok: r.ok }))
          .catch(e => ({ url, error: e.message }))
      )
    );

    for (const r of results) {
      if (r.status === 'fulfilled') {
        console.log(r.value.ok ? `OK ${r.value.status} ${r.value.url}` : `FAIL ${r.value.status} ${r.value.url}`);
      } else {
        console.log(`ERROR ${r.reason?.url || 'unknown'}: ${r.reason?.error || r.reason}`);
      }
    }
  },

  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    if (url.pathname === '/__ping') {
      const r = await fetch('https://soma-853c.onrender.com');
      return new Response(`Render status: ${r.status}`, { status: 200 });
    }
    return new Response('SOMA Keep Warm Worker — usa el cron cada 5 min', { status: 200 });
  },
};
