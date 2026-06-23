const PIPELINE = {
    estados: ['lead', 'entrevistado', 'programado', 'cotizado', 'contratado', 'primera_entrega', 'entrega_final', 'terminado'],
    fases: {
        contratado:      { label: 'Fase 1 · Anticipo',  color: '#1565c0' },
        primera_entrega: { label: 'Fase 2 · 1ra Entrega', color: '#6a1b9a' },
        entrega_final:   { label: 'Fase 3 · Entrega Final', color: '#1b5e20' },
        terminado:       { label: 'Terminado',           color: '#555' }
    }
};

function ubicStr(ubic) {
    if (!ubic) return '';
    try { const u = typeof ubic === 'string' ? JSON.parse(ubic) : ubic;
        return [u.calle_numero, u.colonia].filter(Boolean).join(', '); }
    catch { return ''; }
}

function cardHtml(l) {
    const fase = l.pipeline_estado || 'lead';
    const color = (PIPELINE.fases[fase] || {}).color || '#888';
    const nombre = l.nombre_cliente || '';
    const dir = ubicStr(l.ubicacion);
    return `<div class="cand-card ${fase === 'terminado' ? 'momento3-card' : ''}" style="border-color:${color};">
        <div class="card-header" onclick="toggleCard(this)" style="color:${color};">
            <div>
                <span class="cand-id" style="color:${color};">${API.esc(l.temp_id || '---')}</span>
                ${nombre ? ` <span style="font-weight:500;">${API.esc(nombre)}</span>` : ''}
            </div>
            <span class="card-toggle">▶</span>
        </div>
        <div class="card-body">
            <div class="card-body-inner">
                ${dir ? `<div class="card-detail">${API.esc(dir)}</div>` : ''}
                ${buildCardDetails(l)}
                ${buildCardActions(l)}
            </div>
        </div>
    </div>`;
}

function buildCardDetails(l) {
    const fase = l.pipeline_estado || 'lead';
    const nivel = l.nivel_proyecto || '';
    const m2 = l.m2 || 0;
    const honorarios = l.honorarios_diseno || 0;
    let parts = [];
    if (['lead','entrevistado','programado','cotizado'].includes(fase)) {
        const respCount = l.respuestas_json && l.respuestas_json !== '{}' ? Object.keys(JSON.parse(l.respuestas_json)).length : 0;
        if (respCount >= 10) parts.push('🧠 Inmersión ✓');
        else if (respCount > 0) parts.push('🧠 Inmersión ⚠');
        if (l.m2_original && l.nivel_original)
            parts.push(`📐 ${l.m2_original} m² · ${l.nivel_original}`);
        if (l.presupuesto) parts.push(`💰 $${Number(l.presupuesto).toLocaleString()}`);
    } else {
        if (l.nombre_proyecto) parts.push(`🏗 ${API.esc(l.nombre_proyecto)}`);
        if (nivel) parts.push(`📐 ${m2} m² · ${nivel}`);
        if (honorarios) parts.push(`💰 $${Number(honorarios).toLocaleString()}`);
    }
    return parts.length ? `<div class="card-detail">${parts.join(' &nbsp;|&nbsp; ')}</div>` : '';
}

function buildCardActions(l) {
    const fase = l.pipeline_estado || 'lead';
    let b = '';

    if (fase === 'contratado') {
        b += btn('REGRESAR', 'btn-gray', `onclick="LEADS.regresar(${l.id})"`);
        b += btn('ANTICIPO', 'btn-gold', `onclick="LEADS.pagarCobroDirecto(${l.id},'Anticipo')"`);
    }
    b += btn('EXPEDIENTE', 'btn-dark', `onclick="LEADS.abrirExpediente(${l.id})"`);
    b += btn('PROGRAMA', 'btn-green', `onclick="PROGRAMA.abrir(${l.id},true)"`);

    if (fase === 'lead' || fase === 'entrevistado' || fase === 'programado' || fase === 'cotizado') {
        if (l.respuestas_json && l.respuestas_json !== '{}')
            b += btn('CONTRATAR', 'btn-blue', `onclick="LEADS.abrirContratar(${l.id})"`);
    } else if (fase === 'contratado') {
        b += btn('1RA ENTREGA', 'btn-blue', `onclick="LEADS.avanzar(${l.id},'primera_entrega','Anticipo')"`);
    } else if (fase === 'primera_entrega') {
        b += btn('PAGO 1RA', 'btn-gold', `onclick="LEADS.pagarCobroDirecto(${l.id},'40%')"`);
        b += btn('ENTREGA FINAL', 'btn-purple', `onclick="LEADS.avanzar(${l.id},'entrega_final','40%')"`);
    } else if (fase === 'entrega_final') {
        b += btn('PAGO FINAL', 'btn-gold', `onclick="LEADS.pagarCobroDirecto(${l.id},'Tercer')"`);
        b += btn('TERMINADO', 'btn-red', `onclick="LEADS.cerrar(${l.id})"`);
    } else if (fase === 'terminado') {
        b += btn('EXPEDIENTE', 'btn-dark', `onclick="LEADS.abrirExpediente(${l.id})"`);
        b += btn('ELIMINAR', 'btn-close', `onclick="LEADS.eliminar(${l.id})"`);
    }
    return `<div class="card-actions">${b}</div>`;
}

function btn(text, cls, attrs) {
    return `<button class="cand-btn ${cls}" style="flex:1;font-size:.6rem;" ${attrs}>${text}</button>`;
}

function toggleCard(el) {
    const card = el.closest('.cand-card');
    const body = card.querySelector('.card-body');
    const toggle = card.querySelector('.card-toggle');
    body.classList.toggle('open');
    toggle.classList.toggle('open');
}

// ---- Estado de contacto ----
function estadoContactoSelect(l) {
    const estados = ['no programado', 'programado', 'contactado', 'cerrado'];
    return `<select class="estado-select"
        onchange="LEADS.cambiarEstadoContacto(this,${l.id})">
        ${estados.map(e => `<option value="${e}" ${l.estado_contacto === e ? 'selected' : ''}>${e}</option>`).join('')}
    </select>`;
}

const LEADS = (() => {
    let leadsData = [];
    let contratarLeadId = null;

    async function load() {
        await cargarMetrics();
        leadsData = await API.getLeads();
        renderCandidatos();
        renderClientesMomento2();
        renderMomento3();
        return leadsData;
    }

    function getLeads() { return leadsData; }

    // ---- RENDER ----
    function renderCandidatos() {
        const estados = ['lead','entrevistado','programado','cotizado'];
        const items = leadsData.filter(l => estados.includes(l.pipeline_estado));
        const container = document.getElementById('candidatos-container');
        if (!items.length) {
            container.innerHTML = '<p class="loading-text">Sin candidatos.</p>';
            return;
        }
        container.innerHTML = items.map(l => {
            const extra = `<div class="card-detail" style="margin-top:4px;">${estadoContactoSelect(l)}</div>`;
            return cardHtml(l).replace('</div></div>', extra + '</div></div>');
        }).join('');
    }

    function renderClientesMomento2() {
        const fases = ['contratado', 'primera_entrega', 'entrega_final'];
        fases.forEach(fase => {
            const items = leadsData.filter(l => l.pipeline_estado === fase);
            const container = document.getElementById(`fase-${fase}-container`);
            if (!container) return;
            container.innerHTML = items.length
                ? items.map(cardHtml).join('')
                : '<p class="loading-text">Sin proyectos en esta fase.</p>';
        });
    }

    function renderMomento3() {
        const items = leadsData.filter(l => l.pipeline_estado === 'terminado');
        const container = document.getElementById('momento3-container');
        if (!container) return;
        container.innerHTML = items.length
            ? items.map(cardHtml).join('')
            : '<p class="loading-text">Sin proyectos concluidos.</p>';
    }

    // ---- PIPELINE ACTIONS ----
    async function avanzar(leadId, nuevoEstado, conceptoCheck) {
        if (conceptoCheck) {
            try {
                const cobros = await API.getCobros(leadId);
                const cobro = cobros.find(c => c.concepto && c.concepto.includes(conceptoCheck));
                if (cobro && cobro.estado !== 'pagado') {
                    const ok = await UI.confirmDialog(`El pago de "${cobro.concepto}" no está registrado. ¿Avanzar de todas formas?`);
                    if (!ok) return;
                }
            } catch (_) {}
        }
        try {
            await API.updatePipeline(leadId, nuevoEstado);
            const reciboUrl = nuevoEstado === 'primera_entrega'
                ? `/lead/${leadId}/recibo-segundo-pago`
                : nuevoEstado === 'entrega_final'
                ? `/lead/${leadId}/recibo-tercer-pago`
                : null;
            if (reciboUrl) window.open(reciboUrl, '_blank');
            UI.notify(`Proyecto avanzó a ${nuevoEstado}`);
            await App.refresh();
        } catch (e) { UI.notify(e.message, 'error'); }
    }

    async function regresar(leadId) {
        const ok = await UI.confirmDialog('¿Regresar este proyecto a Candidatos (Momento 1)? Se eliminarán los cobros pendientes.');
        if (!ok) return;
        try {
            await API.regresarLead(leadId);
            UI.notify('Proyecto regresado a Candidatos');
            await App.refresh();
        } catch (e) { UI.notify(e.message, 'error'); }
    }

    async function cerrar(leadId) {
        try {
            const cobros = await API.getCobros(leadId);
            const cobro = cobros.find(c => c.concepto && c.concepto.includes('Tercer'));
            if (cobro && cobro.estado !== 'pagado') {
                const ok = await UI.confirmDialog(`El pago de "${cobro.concepto}" no está registrado. ¿Cerrar de todas formas?`);
                if (!ok) return;
            }
        } catch (_) {}
        const ok = await UI.confirmDialog('¿Cerrar y archivar este proyecto?');
        if (!ok) return;
        try {
            await API.updatePipeline(leadId, 'terminado');
            UI.notify('Proyecto concluido');
            await App.refresh();
        } catch (e) { UI.notify(e.message, 'error'); }
    }

    async function eliminar(leadId) {
        const abrirPDF = await UI.confirmDialog('¿Descargar PDF de cierre antes de eliminar?');
        if (abrirPDF) window.open(`/lead/${leadId}/cierre-pdf`, '_blank');
        const ok = await UI.confirmDialog('⚠️ ¿Eliminar definitivamente este proyecto? Esta acción no se puede deshacer.');
        if (!ok) return;
        try {
            await API.eliminarProyecto(leadId);
            UI.notify('Proyecto eliminado');
            await App.refresh();
        } catch (e) { UI.notify(e.message, 'error'); }
    }

    // ---- PAGO DIRECTO ----
    async function pagarCobroDirecto(proyectoId, substring) {
        try {
            const cobros = await API.getCobros(proyectoId);
            const cobro = cobros.find(c => c.concepto && c.concepto.includes(substring));
            if (!cobro) { UI.notify(`No hay cobro pendiente para este concepto`, 'warning'); return; }
            if (cobro.estado === 'pagado') { UI.notify(`El cobro ya está pagado`, 'warning'); return; }
            await API.pagarCobro(cobro.id);
            UI.notify('Pago registrado');
            await App.refresh();
        } catch (e) { UI.notify(e.message, 'error'); }
    }

    // ---- CONTRATAR ----
    function abrirContratar(id) {
        const lead = leadsData.find(l => l.id === id);
        if (!lead) return;
        const faltantes = [];
        if (!lead.nombre_cliente) faltantes.push('Nombre del cliente');
        if (!lead.nombre_proyecto) faltantes.push('Nombre del proyecto');
        if (!lead.tipo_proyecto) faltantes.push('Tipo de proyecto');
        if (!lead.ubicacion || lead.ubicacion === '{}') faltantes.push('Ubicación completa');
        else {
            try {
                const u = JSON.parse(lead.ubicacion);
                if (!u.calle_numero || !u.colonia || !u.ciudad || !u.estado)
                    faltantes.push('Ubicación completa');
            } catch { faltantes.push('Ubicación completa'); }
        }
        if (faltantes.length) {
            UI.notify('Completa los datos en PROGRAMA primero:\n- ' + faltantes.join('\n- '), 'warning');
            return;
        }
        const m2 = lead.m2 || 0;
        const nivel = lead.nivel_proyecto || 'esencial';
        const precios = { esencial: 250, integral: 350, ejecutivo: 850 };
        const precioM2 = precios[nivel] || 250;
        const honorarios = lead.honorarios_diseno || Math.max(m2 * precioM2, 6500);
        const anticipo = honorarios * 0.3;
        contratarLeadId = id;
        document.getElementById('cont-resumen').innerHTML =
            `${API.esc(lead.temp_id)}<br><strong>${API.esc(lead.nombre_cliente)}</strong><br>
            <span style="font-size:.7rem;color:#666;">${API.esc(lead.nombre_proyecto)}</span>
            <div style="margin-top:15px;padding:10px;background:var(--surface2);border-radius:4px;border:1px solid var(--border);">
                <span style="font-family:'Courier New',monospace;font-size:.65rem;">Honorarios: <strong>$${Number(honorarios).toLocaleString()}</strong></span><br>
                <span style="font-family:'Courier New',monospace;font-size:.65rem;color:#4caf50;">Anticipo 30%: <strong>$${Math.round(anticipo).toLocaleString()}</strong></span>
            </div>`;
        UI.openModal('modal-contratar');
    }

    async function confirmarContratar() {
        const id = contratarLeadId;
        if (!id) return;
        try {
            await API.contratarLead(id);
            window.open(`/lead/${id}/recibo-anticipo`, '_blank');
            UI.notify('Proyecto contratado');
            UI.closeModal('modal-contratar');
            contratarLeadId = null;
            await App.refresh();
        } catch (e) { UI.notify(e.message, 'error'); }
    }

    function cerrarContratar() {
        UI.closeModal('modal-contratar');
        contratarLeadId = null;
    }

    // ---- ESTADO CONTACTO ----
    async function cambiarEstadoContacto(el, id) {
        try {
            await API.updateEstadoContacto(id, el.value);
        } catch (_) {}
    }

    // ---- EXPEDIENTE ----
    async function abrirExpediente(id) {
        const lead = leadsData.find(l => l.id === id);
        if (!lead) return;
        document.getElementById('modal-titulo').textContent = lead.nombre_cliente || lead.temp_id || '---';
        document.getElementById('modal-id').textContent = `${lead.temp_id || '---'} · ${lead.fecha ? new Date(lead.fecha).toLocaleString() : ''}`;

        const m2 = lead.m2 || 0;
        const nivel = lead.nivel_proyecto || 'esencial';
        const precios = { esencial: 250, integral: 350, ejecutivo: 850 };
        const honorarios = lead.honorarios_diseno || Math.max(m2 * (precios[nivel] || 250), 6500);
        const tieneOriginal = lead.m2_original && lead.nivel_original;

        let html = '';

        // Comparativa Original vs Modificado
        if (tieneOriginal) {
            html += `<div style="display:grid;grid-template-columns:1fr 1fr;gap:15px;margin-bottom:15px;">
                <div style="padding:12px;background:var(--surface2);border-radius:4px;border:1px solid var(--border);">
                    <h4 style="font-family:'Courier New',monospace;font-size:.55rem;color:var(--text3);text-transform:uppercase;margin-bottom:8px;">▼ Inmersión (original)</h4>
                    <div style="font-family:Georgia,'Times New Roman',serif;font-size:.75rem;color:var(--text);">
                        <span style="color:var(--text2);">${lead.m2_original} m² · ${lead.nivel_original||'---'}</span><br>
                        <span style="font-weight:600;">$${(lead.honorarios_original||0).toLocaleString()}</span>
                    </div>
                </div>
                <div style="padding:12px;background:rgba(30,80,40,0.2);border-radius:4px;border:1px solid #2e7d32;">
                    <h4 style="font-family:'Courier New',monospace;font-size:.55rem;color:#4caf50;text-transform:uppercase;margin-bottom:8px;">▲ PROGRAMA (modificado)</h4>
                    <div style="font-family:Georgia,'Times New Roman',serif;font-size:.75rem;color:var(--text);">
                        <span style="color:var(--text2);">${m2} m² · ${nivel.charAt(0).toUpperCase()+nivel.slice(1)}</span><br>
                        <span style="font-weight:600;color:#4caf50;">$${honorarios.toLocaleString()}</span>
                    </div>
                </div>
            </div>`;
        } else {
            html += `<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:15px;">
                <div class="kpi-card"><span class="label">Paquete</span><p class="value" style="font-size:.9rem;text-transform:capitalize;">${nivel}</p></div>
                <div class="kpi-card"><span class="label">Metros²</span><p class="value" style="font-size:.9rem;">${m2} m²</p></div>
                <div class="kpi-card"><span class="label" style="color:#2e7d32;">Honorarios</span><p class="value" style="font-size:.9rem;color:#2e7d32;">$${honorarios.toLocaleString()}</p></div>
            </div>`;
        }

        // Programa arquitectónico (solo para terminados)
        if (lead.pipeline_estado === 'terminado') {
            try {
                const espacios = await API.getPrograma(lead.id);
                if (espacios && espacios.length) {
                    const agrupados = {};
                    espacios.forEach(e => {
                        if (!agrupados[e.tipo]) agrupados[e.tipo] = [];
                        agrupados[e.tipo].push(e);
                    });
                    html += Object.keys(agrupados).map(tipo => `
                        <div style="margin-bottom:8px;">
                            <h5 style="font-family:'Courier New',monospace;font-size:.6rem;color:var(--accent);text-transform:uppercase;margin-bottom:4px;">${tipo}</h5>
                            <table class="data-table">
                                ${agrupados[tipo].map(e => `<tr><td style="padding:2px 4px;">${e.clave||''}</td><td style="padding:2px 4px;">${e.espacio}</td><td style="padding:2px 4px;text-align:right;">${e.area} m²</td></tr>`).join('')}
                            </table>
                        </div>
                    `).join('');
                }
            } catch(_) {}
        }

        // Análisis multidimensional
        if (lead.analisis_procesado && lead.analisis_procesado !== '{}') {
            try {
                const analisis = JSON.parse(lead.analisis_procesado);
                if (analisis.multidimensional) {
                    html += `<h4 style="font-size:.7rem;margin:10px 0 5px;">Análisis Multidimensional</h4>
                        <table class="data-table">
                        ${analisis.multidimensional.map(d => `<tr><td>${API.esc(d.eje||'')}</td><td class="right">${d.valor||''}</td><td>${API.esc(d.justificacion||'')}</td></tr>`).join('')}
                        </table>`;
                }
            } catch (_) {}
            html += `<pre style="background:var(--surface2);padding:10px;font-family:'Courier New',monospace;font-size:.6rem;white-space:pre-wrap;max-height:300px;overflow-y:auto;margin-top:10px;border:1px solid var(--border);border-radius:4px;color:var(--text2);">${API.esc(lead.analisis_procesado)}</pre>`;
        }

        // Cobros
        html += `<h4 style="font-size:.7rem;margin:15px 0 5px;">Cobros</h4>
            <div id="exp-cobros-${id}"><p class="loading-text">Cargando...</p></div>`;

        // Cobros management (only for non-terminado)
        if (lead.pipeline_estado !== 'terminado') {
            html += `<div style="margin-top:10px;padding:10px;background:var(--surface2);border-radius:4px;border:1px solid var(--border);">
                <div style="display:flex;gap:8px;margin-bottom:8px;">
                    <button class="cand-btn btn-green" style="font-size:.6rem;padding:4px 10px;" onclick="LEADS.toggleFormCobro(${id})">+ Nuevo Cobro</button>
                    <button class="cand-btn btn-gold" style="font-size:.6rem;padding:4px 10px;" onclick="LEADS.generarEsquema(${id})">⚡ 30/40/30</button>
                </div>
                <div id="form-cobro-${id}" style="display:none;border-top:1px solid #ddd;padding-top:8px;margin-top:8px;">
                    <div class="form-group" style="gap:4px;">
                        <input type="text" id="cobro-concepto-${id}" placeholder="Concepto" style="padding:4px;border:1px solid #ddd;border-radius:3px;font-size:.65rem;">
                        <input type="number" id="cobro-monto-${id}" placeholder="Monto $" style="padding:4px;border:1px solid #ddd;border-radius:3px;font-size:.65rem;">
                        <input type="date" id="cobro-vencimiento-${id}" style="padding:4px;border:1px solid #ddd;border-radius:3px;font-size:.65rem;">
                        <button class="cand-btn btn-green" style="font-size:.6rem;padding:4px;" onclick="LEADS.registrarCobro(${id})">+ Registrar</button>
                    </div>
                </div>
            </div>`;
        }

        // PDF Cierre button for terminados
        if (lead.pipeline_estado === 'terminado') {
            html += `<div style="margin-top:15px;border-top:2px solid var(--border);padding-top:12px;">
                <button class="cand-btn btn-dark" style="font-size:.7rem;padding:6px 16px;" onclick="window.open('/lead/${lead.id}/cierre-pdf','_blank')">📄 PDF de Cierre</button>
            </div>`;
        }

        document.getElementById('modal-body').innerHTML = html;
        UI.openModal('modal-expediente');
        cargarCobrosExpediente(id);
    }

    async function cargarCobrosExpediente(proyectoId) {
        const el = document.getElementById(`exp-cobros-${proyectoId}`);
        if (!el) return;
        try {
            const cobros = await API.getCobros(proyectoId);
            if (!cobros.length) {
                el.innerHTML = '<p class="loading-text">Sin cobros registrados.</p>';
                return;
            }
            el.innerHTML = `<table class="data-table">
                <tr><th>Concepto</th><th class="right">Monto</th><th class="center">Estado</th><th class="right">Pago</th><th class="center"></th></tr>
                ${cobros.map(c => `<tr>
                    <td>${API.esc(c.concepto)}</td>
                    <td class="right">$${Number(c.monto).toLocaleString()}</td>
                    <td class="center"><span class="badge ${c.estado === 'pagado' ? 'badge-green' : 'badge-red'}">${c.estado.toUpperCase()}</span></td>
                    <td class="right">${c.fecha_pago ? new Date(c.fecha_pago).toLocaleDateString() : '---'}</td>
                    <td class="center">${c.estado === 'pendiente' ? `<button class="cand-btn btn-green" style="padding:2px 6px;font-size:.5rem;" onclick="LEADS.pagarCobroExpediente(${c.id},${proyectoId})">✓</button>` : ''}</td>
                </tr>`).join('')}
            </table>`;
        } catch (_) {
            el.innerHTML = '<p class="loading-text">Usa el botón ANTICIPO/PAGO de la tarjeta para registrar pagos.</p>';
        }
    }

    async function pagarCobroExpediente(cobroId, proyectoId) {
        try {
            await API.pagarCobro(cobroId);
            UI.notify('Pago registrado');
            cargarCobrosExpediente(proyectoId);
            await App.refresh();
        } catch (e) { UI.notify(e.message, 'error'); }
    }

    // ---- COBROS MANUALES ----
    function toggleFormCobro(proyectoId) {
        const form = document.getElementById(`form-cobro-${proyectoId}`);
        if (form) form.style.display = form.style.display === 'none' ? 'block' : 'none';
    }

    async function registrarCobro(proyectoId) {
        const concepto = document.getElementById(`cobro-concepto-${proyectoId}`).value.trim();
        const monto = parseFloat(document.getElementById(`cobro-monto-${proyectoId}`).value);
        const vencimiento = document.getElementById(`cobro-vencimiento-${proyectoId}`).value;
        if (!concepto || !monto) { UI.notify('Completa concepto y monto', 'warning'); return; }
        try {
            await API.crearCobro(proyectoId, { concepto, monto, fecha_vencimiento: vencimiento });
            UI.notify('Cobro registrado');
            document.getElementById(`cobro-concepto-${proyectoId}`).value = '';
            document.getElementById(`cobro-monto-${proyectoId}`).value = '';
            document.getElementById(`cobro-vencimiento-${proyectoId}`).value = '';
            document.getElementById(`form-cobro-${proyectoId}`).style.display = 'none';
            cargarCobrosExpediente(proyectoId);
            await App.refresh();
        } catch (e) { UI.notify(e.message, 'error'); }
    }

    async function generarEsquema(proyectoId) {
        const ok = await UI.confirmDialog('¿Generar esquema de pagos 30/40/30? Se crearán 3 cobros (Anticipo, 40%, 30%).');
        if (!ok) return;
        try {
            const res = await API.generarEsquemaPagos(proyectoId);
            UI.notify(`Esquema generado: 3 cobros (Total: $${(res.total||0).toLocaleString()})`);
            cargarCobrosExpediente(proyectoId);
            await App.refresh();
        } catch (e) { UI.notify(e.message, 'error'); }
    }

    return {
        load, getLeads,
        renderCandidatos, renderClientesMomento2, renderMomento3,
        avanzar, regresar, cerrar, eliminar,
        pagarCobroDirecto, pagarCobroExpediente,
        abrirContratar, confirmarContratar, cerrarContratar,
        cambiarEstadoContacto, abrirExpediente,
        toggleFormCobro, registrarCobro, generarEsquema
    };
})();
