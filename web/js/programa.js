const PROGRAMA = (() => {
    let currentLeadId = null;
    let currentReadonly = false;

    const TIPOS_PROYECTO = ['Vivienda unifamiliar','Vivienda plurifamiliar','Departamento','Casa habitación','Oficina','Local comercial','Restaurante','Hotel','Otro'];
    const PRECIOS_NIVEL = { esencial: 250, integral: 350, ejecutivo: 850 };

    async function abrir(id, readonly) {
        currentLeadId = id;
        currentReadonly = readonly;
        const lead = LEADS.getLeads().find(l => l.id === id);
        if (!lead) return;
        document.getElementById('modal-prog-titulo').textContent = lead.nombre_proyecto || lead.nombre_cliente || lead.temp_id || '---';
        document.getElementById('modal-prog-id').textContent = `${lead.temp_id || '---'} · ${lead.fecha ? new Date(lead.fecha).toLocaleString() : ''}`;

        const precios = PRECIOS_NIVEL;
        const pM2 = precios[lead.nivel_proyecto || 'esencial'] || 250;
        const honorarios = lead.honorarios_diseno || 0;
        const m2 = lead.m2 || 0;

        const ro = (editable) => readonly && editable ? '' : readonly ? 'readonly' : '';
        const dis = (editable) => readonly && !editable ? '' : readonly ? 'disabled' : '';
        const selRO = readonly ? 'disabled' : '';

        document.getElementById('modal-prog-header').innerHTML = `
            <div class="cols-2-rev" style="gap:10px;margin-bottom:10px;">
                <div class="form-group" style="gap:4px;">
                    <label>Nombre</label>
                    <input type="text" id="prog-nombre" value="${API.esc(lead.nombre_cliente || '')}" placeholder="p. ej. Juan Pérez" ${ro(true)}>
                    <label>Teléfono</label>
                    <input type="text" id="prog-telefono" value="${API.esc(lead.contacto || '')}" readonly style="background:var(--surface2);">
                    <label>Proyecto</label>
                    <input type="text" id="prog-proyecto" value="${API.esc(lead.nombre_proyecto || '')}" placeholder="p. ej. Casa Habitación" ${ro(true)}>
                    <label>Tipo de Proyecto</label>
                    <select id="prog-tipo" ${selRO}>
                        <option value="">— Seleccionar —</option>
                        ${TIPOS_PROYECTO.map(t => `<option value="${t}" ${lead.tipo_proyecto === t ? 'selected' : ''}>${t}</option>`).join('')}
                    </select>
                </div>
                <div class="form-group" style="gap:4px;">
                    <label>Nivel</label>
                    <select id="prog-nivel" ${selRO} onchange="PROGRAMA.actualizarPrecio()">
                        ${['esencial','integral','ejecutivo'].map(n =>
                            `<option value="${n}" ${lead.nivel_proyecto === n ? 'selected' : ''}>${n.charAt(0).toUpperCase()+n.slice(1)} (${PRECIOS_NIVEL[n]}/m²)</option>`
                        ).join('')}
                    </select>
                    <label>m²</label>
                    <input type="number" id="prog-m2" value="${m2}" readonly style="background:var(--surface2);">
                    <label>Honorarios</label>
                    <input type="number" id="prog-honorarios" value="${honorarios}" readonly style="background:var(--surface2);">
                </div>
            </div>
            <div class="cols-2-rev" style="gap:10px;margin-bottom:10px;">
                <div class="form-group" style="gap:4px;">
                    <label>Calle y Número</label>
                    <input type="text" id="prog-calle" value="${API.esc(lead.calle_numero || '')}" placeholder="p. ej. Calle 74 #767" ${ro(true)}>
                    <label>Colonia</label>
                    <input type="text" id="prog-colonia" value="${API.esc(lead.colonia || '')}" placeholder="p. ej. Centro" ${ro(true)}>
                </div>
                <div class="form-group" style="gap:4px;">
                    <label>Ciudad</label>
                    <input type="text" id="prog-ciudad" value="${API.esc(lead.ciudad || '')}" placeholder="p. ej. Mérida" ${ro(true)}>
                    <label>Estado</label>
                    <input type="text" id="prog-estado" value="${API.esc(lead.estado_ubic || '')}" placeholder="p. ej. Yucatán" ${ro(true)}>
                </div>
            </div>`;

        UI.openModal('modal-programa');
        mostrarSeccion('programa');
    }

    async function cerrar() {
        const id = currentLeadId;
        if (id) await guardarDatos(true);
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

    let activeTipo = 'Deseado';

    async function cargarPrograma(leadId, containerId) {
        const el = document.getElementById(containerId);
        el.innerHTML = '<p class="loading-text">Cargando programa...</p>';
        try {
            const espacios = await API.getPrograma(leadId);
            const tipos = ['Deseado', 'Complementario', 'Lujo'];
            el.innerHTML = `<div style="display:flex;gap:6px;margin-bottom:10px;flex-wrap:wrap;">
                ${tipos.map(t => `<button class="cand-btn ${activeTipo === t ? 'btn-green' : 'btn-dark'}" style="flex:1;font-size:.6rem;" onclick="PROGRAMA.mostrarTipo(${leadId},'${t}','${containerId}')">${t}</button>`).join('')}
            </div><div id="prog-tipo-content"><p class="loading-text">Selecciona un tipo</p></div>`;
            mostrarTipo(leadId, activeTipo, containerId);
        } catch (_) {
            el.innerHTML = '<p class="loading-text">Error al cargar programa</p>';
        }
    }

    async function mostrarTipo(leadId, tipo, containerId) {
        activeTipo = tipo;
        const btnContainer = document.querySelector('#prog-tipo-content')?.parentElement?.querySelector('div:first-child');
        if (btnContainer) {
            btnContainer.querySelectorAll('button').forEach(b => {
                b.className = b.textContent === tipo ? 'cand-btn btn-green' : 'cand-btn btn-dark';
            });
        }
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
                    ${currentReadonly ? '' : `<td><button class="cand-btn btn-close" style="padding:2px 6px;font-size:.5rem;" onclick="PROGRAMA.eliminarEspacio(${e.id},${leadId},'${containerId}','${tipo}')">✕</button></td>`}
                </tr>`).join('')}
                <tr style="border-top:2px solid #000;font-weight:600;"><td><strong>Total ${tipo}</strong></td><td style="text-align:right;"><strong>${totalArea.toFixed(1)} m²</strong></td><td></td><td></td><td></td></tr>
            </table>`;

            // Form to add new space
            html += `<div style="margin-top:8px;display:flex;gap:8px;flex-wrap:wrap;font-size:.55rem;font-family:'Courier New',monospace;color:var(--text2);">
                <span style="display:inline-flex;align-items:center;gap:3px;"><span style="width:10px;height:10px;border-radius:2px;background:#4d7ae6;display:inline-block;"></span> 1 Social</span>
                <span style="display:inline-flex;align-items:center;gap:3px;"><span style="width:10px;height:10px;border-radius:2px;background:#e6cc33;display:inline-block;"></span> 2 Operativa</span>
                <span style="display:inline-flex;align-items:center;gap:3px;"><span style="width:10px;height:10px;border-radius:2px;background:#e64d4d;display:inline-block;"></span> 3 Descanso</span>
                <span style="display:inline-flex;align-items:center;gap:3px;"><span style="width:10px;height:10px;border-radius:2px;background:#e68033;display:inline-block;"></span> 4 Soporte</span>
                <span style="display:inline-flex;align-items:center;gap:3px;"><span style="width:10px;height:10px;border-radius:2px;background:#9933cc;display:inline-block;"></span> 5 Transición</span>
            </div>`;

            if (!currentReadonly) {
                html += `
                <div class="form-panel" style="margin-top:10px;">
                    <h4>Agregar espacio</h4>
                    <div class="form-group">
                        <input type="text" id="prog-nuevo-espacio" placeholder="Nombre">
                        <div style="display:flex;gap:6px;">
                            <input type="number" id="prog-nuevo-area" placeholder="m²" style="flex:1;">
                            <input type="number" id="prog-nuevo-zona" placeholder="Zona 1-5" style="flex:0 0 80px;">
                            <input type="text" id="prog-nuevo-clave" placeholder="Clave" style="flex:0 0 70px;">
                        </div>
                        <button class="cand-btn btn-green" onclick="PROGRAMA.agregarEspacio(${leadId},'${tipo}','${containerId}')">+ Agregar</button>
                    </div>
                </div>`;
                
                html += `<button class="cand-btn btn-green" style="width:100%;font-size:.65rem;padding:6px;margin-top:12px;" onclick="PROGRAMA.guardarDatos()">💾 GUARDAR DATOS Y PROGRAMA</button>`;
            }

            content.innerHTML = html;
        } catch (_) {
            content.innerHTML = '<p class="loading-text">Error al cargar</p>';
        }
    }

    async function agregarEspacio(leadId, tipo, containerId) {
        if (currentReadonly) return;
        const espacio = document.getElementById('prog-nuevo-espacio').value.trim();
        const area = parseFloat(document.getElementById('prog-nuevo-area').value) || 0;
        const zona = parseInt(document.getElementById('prog-nuevo-zona').value) || 1;
        const clave = document.getElementById('prog-nuevo-clave').value.trim();
        if (!espacio) { UI.notify('Ingresa el nombre del espacio', 'warning'); return; }
        if (clave) {
            const existentes = await API.getPrograma(leadId);
            if (existentes.some(e => e.clave && e.clave.toUpperCase() === clave.toUpperCase())) {
                UI.notify('Esa clave ya existe', 'error'); return;
            }
        }
        try {
            await API.crearEspacio(leadId, { tipo, espacio, area, zona, clave });
            UI.notify('Espacio agregado');
            mostrarTipo(leadId, tipo, containerId);
            actualizarM2yHonorarios(leadId);
        } catch (e) { UI.notify(e.message, 'error'); }
    }

    async function eliminarEspacio(espacioId, leadId, containerId, tipo) {
        if (currentReadonly) return;
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
                <div>Cliente: <strong>${API.esc(data.nombre_proyecto || data.nombre_cliente || data.contacto || '')}</strong></div>
                <div>Nivel: <strong>${(data.nivel||'').toUpperCase()}</strong></div>
                <div>m² Programa Real: <strong style="color:#2e7d32;">${data.m2_programa_real || 0}</strong></div>
            </div>
            <table class="data-table" style="margin-bottom:10px;">
                ${tiposHtml}
                <tr style="border-top:2px solid #000;font-weight:600;"><td>Total Programa</td><td class="right">${data.m2_programa_real || 0} m²</td></tr>
            </table>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;font-family:'Courier New',monospace;font-size:.6rem;background:var(--surface2);padding:10px;border-radius:4px;border:1px solid var(--border);">
                <div style="color:var(--text3);">Honorarios x $${data.precio_m2}/m²</div>
                <div style="text-align:right;font-weight:600;">$${Number(data.honorarios_reales || 0).toLocaleString()}</div>
                <div>Obra estimada (mín)</div>
                <div style="text-align:right;">$${Number(data.obra_min_estimada || 0).toLocaleString()}</div>
                <div>Obra estimada (máx)</div>
                <div style="text-align:right;">$${Number(data.obra_max_estimada || 0).toLocaleString()}</div>
            </div>
            <button class="cand-btn btn-green" style="width:100%;font-size:.65rem;padding:6px;margin-top:12px;" onclick="PROGRAMA.guardarDatos()">💾 GUARDAR DATOS Y PROGRAMA</button>`;
        } catch (_) {
            el.innerHTML = '<p class="loading-text">Primero guarda el programa arquitectónico.</p>';
        }
    }

    async function guardarDatos(silent) {
        if (currentReadonly) return;
        const id = currentLeadId;
        if (!id) return;
        const data = {
            nombre_cliente: document.getElementById('prog-nombre').value,
            nombre_proyecto: document.getElementById('prog-proyecto').value,
            tipo_proyecto: document.getElementById('prog-tipo').value,
            nivel_proyecto: document.getElementById('prog-nivel').value,
            honorarios_diseno: parseFloat(document.getElementById('prog-honorarios').value) || 0,
            m2: parseInt(document.getElementById('prog-m2').value) || 0,
            calle_numero: document.getElementById('prog-calle').value,
            colonia: document.getElementById('prog-colonia').value,
            ciudad: document.getElementById('prog-ciudad').value,
            estado_ubic: document.getElementById('prog-estado').value,
            ubicacion: {
                calle_numero: document.getElementById('prog-calle').value,
                colonia: document.getElementById('prog-colonia').value,
                ciudad: document.getElementById('prog-ciudad').value,
                estado: document.getElementById('prog-estado').value
            }
        };
        try {
            await API.guardarDatosProyecto(id, data);
            // Update local cache so re-open shows latest data
            const leads = LEADS.getLeads();
            const idx = leads.findIndex(l => l.id === id);
            if (idx !== -1) {
                Object.assign(leads[idx], data);
            }
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


    return {
        abrir, cerrar, mostrarSeccion,
        cargarPrograma, mostrarTipo,
        agregarEspacio, eliminarEspacio,
        generarCotizacion, guardarDatos,
        actualizarPrecio, actualizarM2yHonorarios,
        TIPOS_PROYECTO, PRECIOS_NIVEL
    };
})();
