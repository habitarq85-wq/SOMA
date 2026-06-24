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
            const operativos = egresos.filter(e => e.categoria !== 'Salario');
            const mesEl = document.getElementById('period-mes');
            const anoEl = document.getElementById('period-ano');
            const mes = mesEl ? mesEl.value : '';
            const ano = anoEl ? anoEl.value : String(new Date().getFullYear());
            const prefix = mes ? `${ano}-${String(mes).padStart(2,'0')}` : ano;
            const delMes = operativos.filter(e => e.fecha && e.fecha.startsWith(prefix));
            const totalMes = delMes.reduce((s, e) => s + (e.monto || 0), 0);
            document.getElementById('egr-total-mes').textContent = '$' + totalMes.toLocaleString();
            if (!delMes.length) {
                lista.innerHTML = '<p class="loading-text">Sin gastos en este período.</p>';
                return;
            }
            lista.innerHTML = `<table class="data-table">
                <tr><th>Fecha</th><th>Categoría</th><th>Concepto</th><th class="right">Monto</th><th class="center"></th></tr>
                ${delMes.map(e => `<tr>
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

    // ---- SALARIOS ----
    async function loadSalarios() {
        const lista = document.getElementById('sal-lista');
        try {
            const egresos = await API.getEgresos();
            const salarios = egresos.filter(e => e.categoria === 'Salario');
            const mesEl = document.getElementById('period-mes');
            const anoEl = document.getElementById('period-ano');
            const mes = mesEl ? mesEl.value : '';
            const ano = anoEl ? anoEl.value : String(new Date().getFullYear());
            const prefix = mes ? `${ano}-${String(mes).padStart(2,'0')}` : ano;
            const delMes = salarios.filter(e => e.fecha && e.fecha.startsWith(prefix));
            const totalMes = delMes.reduce((s, e) => s + (e.monto || 0), 0);
            document.getElementById('sal-total-mes').textContent = '$' + totalMes.toLocaleString();
            if (!delMes.length) {
                lista.innerHTML = '<p class="loading-text">Sin salarios registrados en este período.</p>';
                return;
            }
            lista.innerHTML = `<table class="data-table">
                <tr><th>Fecha</th><th>Nombre</th><th class="right">Monto</th><th class="center"></th></tr>
                ${delMes.map(e => `<tr>
                    <td>${API.esc(e.fecha || '---')}</td>
                    <td>${API.esc(e.concepto)}</td>
                    <td class="right">$${Number(e.monto).toLocaleString()}</td>
                    <td class="center"><button class="cand-btn btn-close" style="padding:2px 6px;font-size:.5rem;" onclick="EGRESOS.eliminarSalario(${e.id})">✕</button></td>
                </tr>`).join('')}
            </table>`;
        } catch (e) {
            lista.innerHTML = '<p class="loading-text" style="color:#c62828;">Error al cargar salarios</p>';
        }
    }

    async function registrarSalario() {
        const nombre = document.getElementById('sal-nombre').value.trim();
        const monto = parseFloat(document.getElementById('sal-monto').value);
        const fecha = document.getElementById('sal-fecha').value || new Date().toISOString().slice(0,10);
        if (!nombre || !monto) { UI.notify('Completa nombre y monto', 'warning'); return; }
        const btn = document.querySelector('#sal-registrar-btn');
        if (btn) btn.disabled = true;
        try {
            await API.crearEgreso({ categoria: 'Salario', concepto: nombre, monto, fecha });
            document.getElementById('sal-monto').value = '';
            document.getElementById('sal-fecha').value = '';
            UI.notify('Salario registrado');
            await loadSalarios();
            await App.refresh();
        } catch (e) { UI.notify(e.message, 'error'); }
        finally { if (btn) btn.disabled = false; }
    }

    async function eliminarSalario(id) {
        const ok = await UI.confirmDialog('¿Eliminar este salario?');
        if (!ok) return;
        try {
            await API.eliminarEgreso(id);
            UI.notify('Salario eliminado');
            await loadSalarios();
            await App.refresh();
        } catch (e) { UI.notify(e.message, 'error'); }
    }

    return { load, registrar, eliminar, loadSalarios, registrarSalario, eliminarSalario };
})();
