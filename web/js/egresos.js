const EGRESOS = (() => {
    async function load() {
        const lista = document.getElementById('egr-lista');
        try {
            const egresos = await API.getEgresos();
            if (!egresos.length) {
                lista.innerHTML = '<p class="loading-text">Sin gastos registrados.</p>';
                document.getElementById('egr-total-mes').textContent = '$0';
                return;
            }
            const ahora = new Date();
            const mesActual = `${ahora.getFullYear()}-${String(ahora.getMonth()+1).padStart(2,'0')}`;
            const delMes = egresos.filter(e => e.fecha && e.fecha.startsWith(mesActual));
            const totalMes = delMes.reduce((s, e) => s + (e.monto || 0), 0);
            document.getElementById('egr-total-mes').textContent = '$' + totalMes.toLocaleString();
            lista.innerHTML = `<table class="data-table">
                <tr><th>Fecha</th><th>Categoría</th><th>Concepto</th><th class="right">Monto</th><th class="center"></th></tr>
                ${egresos.map(e => `<tr>
                    <td>${API.esc(e.fecha || '---')}</td>
                    <td>${API.esc(e.categoria)}</td>
                    <td>${API.esc(e.concepto)}</td>
                    <td class="right">$${Number(e.monto).toLocaleString()}</td>
                    <td class="center"><button class="cand-btn btn-close" style="padding:2px 6px;font-size:.5rem;" onclick="EGRESOS.eliminar(${e.id})">✕</button></td>
                </tr>`).join('')}
            </table>`;
        } catch (e) {
            lista.innerHTML = '<p class="loading-text" style="color:#c62828;">Error al cargar egresos</p>';
        }
    }

    async function registrar() {
        const categoria = document.getElementById('egr-categoria').value;
        const concepto = document.getElementById('egr-concepto').value.trim();
        const monto = parseFloat(document.getElementById('egr-monto').value);
        const fecha = document.getElementById('egr-fecha').value || new Date().toISOString().slice(0,10);
        if (!categoria || !concepto || !monto) { UI.notify('Completa todos los campos', 'warning'); return; }
        const btn = document.querySelector('#egr-registrar-btn');
        if (btn) btn.disabled = true;
        try {
            await API.crearEgreso({ categoria, concepto, monto, fecha });
            document.getElementById('egr-categoria').value = '';
            document.getElementById('egr-concepto').value = '';
            document.getElementById('egr-monto').value = '';
            UI.notify('Gasto registrado');
            await load();
            await App.refresh();
        } catch (e) { UI.notify(e.message, 'error'); }
        finally { if (btn) btn.disabled = false; }
    }

    async function eliminar(id) {
        const ok = await UI.confirmDialog('¿Eliminar este gasto?');
        if (!ok) return;
        try {
            await API.eliminarEgreso(id);
            UI.notify('Gasto eliminado');
            await load();
            await App.refresh();
        } catch (e) { UI.notify(e.message, 'error'); }
    }

    return { load, registrar, eliminar };
})();
