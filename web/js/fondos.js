const FONDOS = (() => {
    async function load() {
        const tarjetas = document.getElementById('fnd-tarjetas');
        try {
            const fondos = await API.getFondos();
            if (!fondos.length) {
                tarjetas.innerHTML = '<p class="loading-text">Sin fondos creados.</p>';
                document.getElementById('fnd-total-acumulado').textContent = '$0';
                return;
            }
            const totalAcumulado = fondos.reduce((s, f) => s + (f.balance_actual || 0), 0);
            document.getElementById('fnd-total-acumulado').textContent = '$' + totalAcumulado.toLocaleString();
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
                    <div class="fund-aportar">
                        <input type="number" id="fnd-aportar-${f.id}" placeholder="$ Aportar" style="flex:1;">
                        <button class="cand-btn btn-green" style="padding:4px 10px;font-size:.65rem;" onclick="FONDOS.aportar(${f.id})">+</button>
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

    async function aportar(id) {
        const input = document.getElementById(`fnd-aportar-${id}`);
        const monto = parseFloat(input.value);
        if (!monto || monto <= 0) { UI.notify('Ingresa un monto válido', 'warning'); return; }
        try {
            await API.apartarFondo(id, { monto, concepto: 'Aportación mensual' });
            input.value = '';
            UI.notify('Aportación registrada');
            await load();
        } catch (e) { UI.notify(e.message, 'error'); }
    }

    return { load, crear, eliminar, aportar };
})();
