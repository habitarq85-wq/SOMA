const PROGRAMA = (() => {
    let currentLeadId = null;

    const TIPOS_PROYECTO = ['Vivienda unifamiliar','Vivienda plurifamiliar','Departamento','Casa habitación','Oficina','Local comercial','Restaurante','Hotel','Otro'];
    const PRECIOS_NIVEL = { esencial: 250, integral: 350, ejecutivo: 850 };

    async function abrir(id, readonly) {
        currentLeadId = id;
        const lead = LEADS.getLeads().find(l => l.id === id);
        if (!lead) return;
        document.getElementById('modal-prog-titulo').textContent = lead.nombre_cliente || lead.temp_id || '---';
        document.getElementById('modal-prog-id').textContent = `${lead.temp_id || '---'} · ${lead.fecha ? new Date(lead.fecha).toLocaleString() : ''}`;

        const precios = PRECIOS_NIVEL;
        const pM2 = precios[lead.nivel_proyecto || 'esencial'] || 250;
        const honorarios = lead.honorarios_diseno || 0;
        const m2 = lead.m2 || 0;

        document.getElementById('modal-prog-header').innerHTML = `
            <div class="cols-2-rev" style="gap:10px;margin-bottom:10px;">
                <div class="form-group" style="gap:4px;">
                    <label style="font-size:.6rem;color:#888;">Nombre</label>
                    <input type="text" id="prog-nombre" value="${API.esc(lead.nombre_cliente || '')}" style="padding:4px;border:1px solid #ddd;border-radius:3px;font-size:.7rem;">
                    <label style="font-size:.6rem;color:#888;">Teléfono</label>
                    <input type="text" id="prog-telefono" value="${API.esc(lead.contacto || '')}" readonly style="padding:4px;border:1px solid #ddd;border-radius:3px;font-size:.7rem;background:#f4f1ea;">
                    <label style="font-size:.6rem;color:#888;">Proyecto</label>
                    <input type="text" id="prog-proyecto" value="${API.esc(lead.nombre_proyecto || '')}" style="padding:4px;border:1px solid #ddd;border-radius:3px;font-size:.7rem;">
                    <label style="font-size:.6rem;color:#888;">Tipo de Proyecto</label>
                    <select id="prog-tipo" style="padding:4px;border:1px solid #ddd;border-radius:3px;font-size:.7rem;">
                        <option value="">— Seleccionar —</option>
                        ${TIPOS_PROYECTO.map(t => `<option value="${t}" ${lead.tipo_proyecto === t ? 'selected' : ''}>${t}</option>`).join('')}
                    </select>
                </div>
                <div class="form-group" style="gap:4px;">
                    <label style="font-size:.6rem;color:#888;">Nivel</label>
                    <select id="prog-nivel" style="padding:4px;border:1px solid #ddd;border-radius:3px;font-size:.7rem;" onchange="PROGRAMA.actualizarPrecio()">
                        ${['esencial','integral','ejecutivo'].map(n =>
                            `<option value="${n}" ${lead.nivel_proyecto === n ? 'selected' : ''}>${n.charAt(0).toUpperCase()+n.slice(1)} (${PRECIOS_NIVEL[n]}/m²)</option>`
                        ).join('')}
                    </select>
                    <label style="font-size:.6rem;color:#888;">m²</label>
                    <input type="number" id="prog-m2" value="${m2}" readonly
                        style="padding:4px;border:1px solid #ddd;border-radius:3px;font-size:.7rem;background:#f4f1ea;">
                    <label style="font-size:.6rem;color:#888;">Honorarios</label>
                    <input type="number" id="prog-honorarios" value="${honorarios}"
                        style="padding:4px;border:1px solid #ddd;border-radius:3px;font-size:.7rem;">
                </div>
            </div>
            <div class="cols-2-rev" style="gap:10px;margin-bottom:10px;">
                <div class="form-group" style="gap:4px;">
                    <label style="font-size:.6rem;color:#888;">Calle y Número</label>
                    <input type="text" id="prog-calle" value="${API.esc(ubicCalle(lead.ubicacion))}" style="padding:4px;border:1px solid #ddd;border-radius:3px;font-size:.7rem;">
                    <label style="font-size:.6rem;color:#888;">Colonia</label>
                    <input type="text" id="prog-colonia" value="${API.esc(ubicColonia(lead.ubicacion))}" style="padding:4px;border:1px solid #ddd;border-radius:3px;font-size:.7rem;">
                </div>
                <div class="form-group" style="gap:4px;">
                    <label style="font-size:.6rem;color:#888;">Ciudad</label>
                    <input type="text" id="prog-ciudad" value="${API.esc(ubicCiudad(lead.ubicacion))}" style="padding:4px;border:1px solid #ddd;border-radius:3px;font-size:.7rem;">
                    <label style="font-size:.6rem;color:#888;">Estado</label>
                    <input type="text" id="prog-estado" value="${API.esc(ubicEstado(lead.ubicacion))}" style="padding:4px;border:1px solid #ddd;border-radius:3px;font-size:.7rem;">
                </div>
            </div>
            <button class="cand-btn btn-green" style="width:100%;font-size:.65rem;padding:6px;margin-bottom:10px;" onclick="PROGRAMA.guardarDatos()">GUARDAR DATOS</button>`;

        UI.openModal('modal-programa');
        mostrarSeccion('programa');
    }

    function cerrar() {
        UI.closeModal('modal-programa');
        currentLeadId = null;
    }

    function mostrarSeccion(seccion) {
        const id = currentLeadId;
        if (!id) return;
        guardarDatos(true);
        if (seccion === 'programa') {
            cargarPrograma(id, 'modal-prog-body');
        } else {
            generarCotizacion(id, 'modal-prog-body');
        }
    }

    async function cargarPrograma(leadId, containerId) {
        const el = document.getElementById(containerId);
        el.innerHTML = '<p class="loading-text">Cargando programa...</p>';
        try {
            const espacios = await API.getPrograma(leadId);
            const tipos = ['Deseado', 'Complementario', 'Lujo'];
            el.innerHTML = `<div style="display:flex;gap:6px;margin-bottom:10px;flex-wrap:wrap;">
                ${tipos.map(t => `<button class="cand-btn btn-dark" style="flex:1;font-size:.6rem;" onclick="PROGRAMA.mostrarTipo(${leadId},'${t}','${containerId}')">${t}</button>`).join('')}
            </div><div id="prog-tipo-content"><p class="loading-text">Selecciona un tipo</p></div>`;
        } catch (_) {
            el.innerHTML = '<p class="loading-text">Error al cargar programa</p>';
        }
    }

    async function mostrarTipo(leadId, tipo, containerId) {
        const content = document.getElementById('prog-tipo-content');
        if (!content) return;
        content.innerHTML = '<p class="loading-text">Cargando...</p>';
        try {
            const espacios = await API.getPrograma(leadId);
            const filtrados = espacios.filter(e => e.tipo === tipo);
            const totalArea = filtrados.reduce((s, e) => s + (e.area || 0), 0);
            let html = `<table class="data-table">
                <tr><th>Espacio</th><th>Área m²</th><th>Zona</th><th>Clave</th><th></th></tr>
                ${filtrados.map(e => `<tr>
                    <td>${API.esc(e.espacio || '')}</td>
                    <td>${Number(e.area || 0).toFixed(1)}</td>
                    <td>${e.zona || ''}</td>
                    <td>${API.esc(e.clave || '')}</td>
                    <td><button class="cand-btn btn-close" style="padding:2px 6px;font-size:.5rem;" onclick="PROGRAMA.eliminarEspacio(${e.id},${leadId},'${containerId}','${tipo}')">✕</button></td>
                </tr>`).join('')}
                <tr style="border-top:2px solid #000;font-weight:600;"><td><strong>Total ${tipo}</strong></td><td style="text-align:right;"><strong>${totalArea.toFixed(1)} m²</strong></td><td></td><td></td><td></td></tr>
            </table>`;

            // Form to add new space
            html += `<div style="margin-top:8px;display:flex;gap:8px;flex-wrap:wrap;font-size:.55rem;font-family:'JetBrains Mono',monospace;">
                <span style="display:inline-flex;align-items:center;gap:3px;"><span style="width:10px;height:10px;border-radius:2px;background:#4d7ae6;display:inline-block;"></span> Social</span>
                <span style="display:inline-flex;align-items:center;gap:3px;"><span style="width:10px;height:10px;border-radius:2px;background:#e6cc33;display:inline-block;"></span> Operativa</span>
                <span style="display:inline-flex;align-items:center;gap:3px;"><span style="width:10px;height:10px;border-radius:2px;background:#e64d4d;display:inline-block;"></span> Descanso</span>
                <span style="display:inline-flex;align-items:center;gap:3px;"><span style="width:10px;height:10px;border-radius:2px;background:#e68033;display:inline-block;"></span> Soporte</span>
                <span style="display:inline-flex;align-items:center;gap:3px;"><span style="width:10px;height:10px;border-radius:2px;background:#9933cc;display:inline-block;"></span> Transición</span>
            </div>
            <div style="margin-top:10px;padding:10px;background:#f9f9f9;border-radius:4px;">
                <h4 style="font-size:.6rem;margin-bottom:6px;">Agregar espacio</h4>
                <div style="display:flex;gap:6px;flex-wrap:wrap;">
                    <input type="text" id="prog-nuevo-espacio" placeholder="Nombre" style="padding:4px;border:1px solid #ddd;border-radius:3px;font-size:.65rem;flex:2;">
                    <input type="number" id="prog-nuevo-area" placeholder="m²" style="padding:4px;border:1px solid #ddd;border-radius:3px;font-size:.65rem;width:70px;">
                    <input type="number" id="prog-nuevo-zona" placeholder="Zona 1-5" style="padding:4px;border:1px solid #ddd;border-radius:3px;font-size:.65rem;width:80px;">
                    <input type="text" id="prog-nuevo-clave" placeholder="Clave" style="padding:4px;border:1px solid #ddd;border-radius:3px;font-size:.65rem;width:70px;">
                    <button class="cand-btn btn-green" style="padding:4px 10px;font-size:.6rem;" onclick="PROGRAMA.agregarEspacio(${leadId},'${tipo}','${containerId}')">+</button>
                </div>
            </div>`;

            content.innerHTML = html;
        } catch (_) {
            content.innerHTML = '<p class="loading-text">Error al cargar</p>';
        }
    }

    async function agregarEspacio(leadId, tipo, containerId) {
        const espacio = document.getElementById('prog-nuevo-espacio').value.trim();
        const area = parseFloat(document.getElementById('prog-nuevo-area').value) || 0;
        const zona = parseInt(document.getElementById('prog-nuevo-zona').value) || 1;
        const clave = document.getElementById('prog-nuevo-clave').value.trim();
        if (!espacio) { UI.notify('Ingresa el nombre del espacio', 'warning'); return; }
        try {
            await API.crearEspacio(leadId, { tipo, espacio, area, zona, clave });
            UI.notify('Espacio agregado');
            mostrarTipo(leadId, tipo, containerId);
            actualizarM2yHonorarios(leadId);
        } catch (e) { UI.notify(e.message, 'error'); }
    }

    async function eliminarEspacio(espacioId, leadId, containerId, tipo) {
        const ok = await UI.confirmDialog('¿Eliminar este espacio?');
        if (!ok) return;
        try {
            await API.eliminarEspacio(espacioId);
            UI.notify('Espacio eliminado');
            mostrarTipo(leadId, tipo, containerId);
            actualizarM2yHonorarios(leadId);
        } catch (e) { UI.notify(e.message, 'error'); }
    }

    async function generarCotizacion(leadId, containerId) {
        const el = document.getElementById(containerId);
        el.innerHTML = '<p class="loading-text">Generando cotización...</p>';
        try {
            const data = await API.getCotizacion(leadId);
            const tiposHtml = data.totales_por_tipo
                ? Object.entries(data.totales_por_tipo).map(([t, a]) =>
                    `<tr><td>${t}</td><td class="right">${a.toFixed(1)} m²</td></tr>`
                  ).join('')
                : '';
            el.innerHTML = `
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
                <h4 style="font-family:'JetBrains Mono';font-size:.65rem;color:#2e7d32;text-transform:uppercase;">Cotización Formal</h4>
                <button class="cand-btn btn-dark" style="font-size:.55rem;padding:6px 12px;width:auto;" onclick="window.open('/cotizacion/${leadId}/pdf','_blank')">📄 PDF</button>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;font-family:'JetBrains Mono';font-size:.6rem;margin-bottom:10px;">
                <div>Cliente: <strong>${API.esc(data.contacto || '')}</strong></div>
                <div>Nivel: <strong>${(data.nivel||'').toUpperCase()}</strong></div>
                <div>m² Web (estimado): <strong>${data.m2_lead_original || 0}</strong></div>
                <div>m² Programa Real: <strong style="color:#2e7d32;">${data.m2_programa_real || 0}</strong></div>
            </div>
            <table class="data-table" style="margin-bottom:10px;">
                ${tiposHtml}
                <tr style="border-top:2px solid #000;font-weight:600;"><td>Total Programa</td><td class="right">${data.m2_programa_real || 0} m²</td></tr>
            </table>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;font-family:'JetBrains Mono';font-size:.6rem;background:#f4f1ea;padding:10px;border-radius:4px;">
                <div>Honorarios x $${data.precio_m2}/m²</div>
                <div style="text-align:right;font-weight:600;">$${Number(data.honorarios_reales || 0).toLocaleString()}</div>
                <div>Obra estimada (mín)</div>
                <div style="text-align:right;">$${Number(data.obra_min_estimada || 0).toLocaleString()}</div>
                <div>Obra estimada (máx)</div>
                <div style="text-align:right;">$${Number(data.obra_max_estimada || 0).toLocaleString()}</div>
            </div>`;
        } catch (_) {
            el.innerHTML = '<p class="loading-text">Primero guarda el programa arquitectónico.</p>';
        }
    }

    async function guardarDatos(silent) {
        const id = currentLeadId;
        if (!id) return;
        const ubicacion = JSON.stringify({
            calle_numero: document.getElementById('prog-calle').value,
            colonia: document.getElementById('prog-colonia').value,
            ciudad: document.getElementById('prog-ciudad').value,
            estado: document.getElementById('prog-estado').value
        });
        const data = {
            nombre_cliente: document.getElementById('prog-nombre').value,
            nombre_proyecto: document.getElementById('prog-proyecto').value,
            tipo_proyecto: document.getElementById('prog-tipo').value,
            nivel_proyecto: document.getElementById('prog-nivel').value,
            honorarios_diseno: parseFloat(document.getElementById('prog-honorarios').value) || 0,
            m2: parseInt(document.getElementById('prog-m2').value) || 0,
            ubicacion
        };
        try {
            await API.guardarDatosProyecto(id, data);
            if (!silent) {
                UI.notify('Datos guardados');
                await App.refresh();
            }
        } catch (e) { if (!silent) UI.notify(e.message, 'error'); }
    }

    function actualizarPrecio() {
        const id = currentLeadId;
        if (!id) return;
        actualizarM2yHonorarios(id);
    }

    async function actualizarM2yHonorarios(id) {
        try {
            const espacios = await API.getPrograma(id);
            const totalM2 = espacios.reduce((s, e) => s + (e.area || 0), 0);
            const m2Input = document.getElementById('prog-m2');
            if (m2Input) m2Input.value = totalM2;
            const nivel = document.getElementById('prog-nivel')?.value || 'esencial';
            const precios = { esencial: 250, integral: 350, ejecutivo: 850 };
            const honorariosInput = document.getElementById('prog-honorarios');
            if (honorariosInput && !honorariosInput.dataset.manual) {
                honorariosInput.value = Math.max(totalM2 * (precios[nivel] || 250), 6500);
            }
        } catch (_) {}
    }

    // Helpers
    function ubicCalle(ubic) { try { const u = JSON.parse(ubic); return u.calle_numero || ''; } catch { return ''; } }
    function ubicColonia(ubic) { try { const u = JSON.parse(ubic); return u.colonia || ''; } catch { return ''; } }
    function ubicCiudad(ubic) { try { const u = JSON.parse(ubic); return u.ciudad || ''; } catch { return ''; } }
    function ubicEstado(ubic) { try { const u = JSON.parse(ubic); return u.estado || ''; } catch { return ''; } }

    return {
        abrir, cerrar, mostrarSeccion,
        cargarPrograma, mostrarTipo,
        agregarEspacio, eliminarEspacio,
        generarCotizacion, guardarDatos,
        actualizarPrecio, actualizarM2yHonorarios,
        TIPOS_PROYECTO, PRECIOS_NIVEL
    };
})();
