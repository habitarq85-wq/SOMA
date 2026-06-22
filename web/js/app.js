const App = (() => {
    let refreshTimer = null;
    let isLoading = false;

    async function refresh() {
        if (isLoading) return;
        if(document.querySelector('.modal-overlay.active')) return;
        isLoading = true;
        try {
            await LEADS.load();
            await EGRESOS.load();
            await FONDOS.load();
            updateClock();
        } catch (e) {
            console.error('Refresh error:', e);
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

        refreshTimer = setInterval(refresh, 30000);
        refresh();
    }

    return { init, refresh };
})();

async function cargarMetrics() {
    const mes = document.getElementById('period-mes').value;
    const ano = document.getElementById('period-ano').value;
    try {
        const d = await API.getMetrics(ano, mes);
        document.getElementById('gp-total-clientes').innerText = d.total_clientes;
        document.getElementById('gp-anticipos').innerText = '$' + Number(d.anticipos).toLocaleString();
        document.getElementById('gp-primera-entrega').innerText = '$' + Number(d.primera_entrega).toLocaleString();
        document.getElementById('gp-pagos-finales').innerText = '$' + Number(d.pagos_finales).toLocaleString();
        document.getElementById('gp-ingresos-periodo').innerText = '$' + Number(d.ingresos_periodo).toLocaleString();
        document.getElementById('gp-gasto-operacion').innerText = '$' + Number(d.gasto_operacion).toLocaleString();
        document.getElementById('periodo-label').textContent = d.periodo;
    } catch (e) { console.error('Metrics error:', e); }
}

function cambiarPeriodo() {
    const mes = document.getElementById('period-mes').value;
    const ano = document.getElementById('period-ano').value;
    localStorage.setItem('soma-period-mes', mes);
    localStorage.setItem('soma-period-ano', ano);
    cargarMetrics();
}

window.onload = () => App.init();
