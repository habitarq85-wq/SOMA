const App = (() => {
    let refreshTimer = null;
    let isLoading = false;

    async function refresh() {
        if (isLoading) return;
        isLoading = true;
        try {
            await Promise.race([
                (async () => {
                    await LEADS.load();
                    await EGRESOS.load();
                    await EGRESOS.loadSalarios();
                    await FONDOS.load();
                    updateClock();
                })(),
                new Promise((_, reject) => setTimeout(() => reject(new Error('Refresh timeout')), 15000))
            ]);
        } catch (e) {
            if (e.message === 'Refresh timeout') console.error('Refresh timed out after 15s');
            else console.error('Refresh error:', e);
        } finally {
            isLoading = false;
        }
    }

    function updateClock() {
        const el = document.getElementById('last-update');
        if (el) el.textContent = new Date().toLocaleString();
    }

    function init() {
        const mes = localStorage.getItem('soma-period-mes') || '';
        const ano = localStorage.getItem('soma-period-ano') || String(new Date().getFullYear());
        const mesSel = document.getElementById('period-mes');
        const anoSel = document.getElementById('period-ano');
        if (mesSel) mesSel.value = mes;
        if (anoSel) anoSel.value = ano;

        refreshTimer = setInterval(() => {
            if (!document.querySelector('.modal-overlay.active')) refresh();
        }, 30000);
        refresh();
    }

    return { init, refresh };
})();

async function cargarMetrics() {
    try {
        const mesEl = document.getElementById('period-mes');
        const anoEl = document.getElementById('period-ano');
        if (!mesEl || !anoEl) { console.warn('period-mes/ano not found'); return; }
        const mes = mesEl.value;
        const ano = anoEl.value;
        const d = await API.getMetrics(ano, mes);
        const setText = (id, val) => { const el = document.getElementById(id); if (el) el.innerText = val; };
        setText('gp-total-clientes', d.total_clientes);
        setText('gp-anticipos', '$' + Number(d.anticipos).toLocaleString());
        setText('gp-primera-entrega', '$' + Number(d.primera_entrega).toLocaleString());
        setText('gp-pagos-finales', '$' + Number(d.pagos_finales).toLocaleString());
        setText('gp-ingresos-periodo', '$' + Number(d.ingresos_periodo).toLocaleString());
        setText('gp-gasto-operacion', '$' + Number(d.gasto_operacion).toLocaleString());
        const pl = document.getElementById('periodo-label');
        if (pl) pl.textContent = d.periodo;
    } catch (e) { console.error('Metrics error:', e); }
}

function cambiarPeriodo() {
    const mes = document.getElementById('period-mes').value;
    const ano = document.getElementById('period-ano').value;
    localStorage.setItem('soma-period-mes', mes);
    localStorage.setItem('soma-period-ano', ano);
    cargarMetrics();
    App.refresh();
}

window.onload = () => App.init();
