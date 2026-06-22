const FONDOS = (() => {
    async function load() {
        const tarjetas = document.getElementById('fnd-tarjetas');
        const select = document.getElementById('fnd-select');
        try {
            const fondos = await API.getFondos();
            if (!fondos.length) {
                tarjetas.innerHTML = '<p class="loading-text">Sin fondos creados.</p>';
                select.innerHTML = '<option value="">— Seleccionar fondo —</option>';
                return;
            }
            select.innerHTML = '<option value="">— Seleccionar fondo —</option>' +
                fondos.map(f => `<option value="${f.id}">${API.esc(f.nombre)}</option>`).join('');
            tarjetas.innerHTML = fondos.map(f => `
                <div class="fund-card">
                    <div class="fund-header">
                        <strong>${API.esc(f.nombre)}</strong>
                        <button class="cand-btn btn-close" style="padding:2px 6px;font-size:.5rem;" onclick="FONDOS.eliminar(${f.id})">✕</button>
                    </div>
                    <div class="fund-balance">
                        Balance: <strong style="color:${f.balance_actual >= 0 ? '#2e7d32' : '#c62828'};">$${Number(f.balance_actual).toLocaleString()}</strong>
                        <span style="color:#999;margin-left:15px;">Aportación mensual: $${Number(f.monto_mensual).toLocaleString()}</span>
                    </div>
                </div>
            `).join('');
        } catch (e) {
            tarjetas.innerHTML = '<p class="loading-text" style="color:#c62828;">Error al cargar fondos</p>';
        }
    }

    async function crear() {
        const nombre = document.getElementById('fnd-nombre').value.trim();
        const monto = parseFloat(document.getElementById('fnd-mensual').value) || 0;
        if (!nombre) { UI.notify('Ingresa un nombre', 'warning'); return; }
        try {
            await API.crearFondo({ nombre, monto_mensual: monto });
            document.getElementById('fnd-nombre').value = '';
            document.getElementById('fnd-mensual').value = '';
            UI.notify('Fondo creado');
            await load();
        } catch (e) { UI.notify(e.message, 'error'); }
    }

    async function eliminar(id) {
        const ok = await UI.confirmDialog('¿Eliminar este fondo y todos sus movimientos?');
        if (!ok) return;
        try {
            await API.eliminarFondo(id);
            UI.notify('Fondo eliminado');
            await load();
        } catch (e) { UI.notify(e.message, 'error'); }
    }

    async function apartar() {
        const fondoId = document.getElementById('fnd-select').value;
        const monto = parseFloat(document.getElementById('fnd-monto').value);
        const concepto = document.getElementById('fnd-concepto').value.trim() || 'Aportación';
        if (!fondoId || !monto) { UI.notify('Selecciona un fondo e ingresa un monto', 'warning'); return; }
        try {
            await API.apartarFondo(fondoId, { monto, concepto });
            document.getElementById('fnd-monto').value = '';
            document.getElementById('fnd-concepto').value = '';
            UI.notify('Aportación registrada');
            await load();
        } catch (e) { UI.notify(e.message, 'error'); }
    }

    async function retirar() {
        const fondoId = document.getElementById('fnd-select').value;
        const monto = parseFloat(document.getElementById('fnd-monto').value);
        const concepto = document.getElementById('fnd-concepto').value.trim() || 'Retiro';
        if (!fondoId || !monto) { UI.notify('Selecciona un fondo e ingresa un monto', 'warning'); return; }
        try {
            await API.retirarFondo(fondoId, { monto, concepto });
            document.getElementById('fnd-monto').value = '';
            document.getElementById('fnd-concepto').value = '';
            UI.notify('Retiro registrado');
            await load();
        } catch (e) { UI.notify(e.message, 'error'); }
    }

    return { load, crear, eliminar, apartar, retirar };
})();
