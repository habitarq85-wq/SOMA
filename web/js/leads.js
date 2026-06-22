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
        if (l.respuestas_json && l.respuestas_json !== '{}')
            parts.push('🧠 Inmersión ✓');
        if (l.m2_original && l.nivel_original)
            parts.push(`📐 ${l.m2_original} m² · ${l.nivel_original}`);
    } else {
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
    return `<select style="padding:3px;border:1px solid #ddd;border-radius:2px;font-size:.55rem;font-family:'JetBrains Mono',monospace;"
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
        const ok = await UI.confirmDialog('¿Eliminar definitivamente este proyecto?');
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
            <div style="margin-top:15px;padding:10px;background:#f4f1ea;border-radius:4px;">
                <span style="font-family:'JetBrains Mono';font-size:.65rem;">Honorarios: <strong>$${Number(honorarios).toLocaleString()}</strong></span><br>
                <span style="font-family:'JetBrains Mono';font-size:.65rem;color:#2e7d32;">Anticipo 30%: <strong>$${Math.round(anticipo).toLocaleString()}</strong></span>
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

        let html = `<div style="font-family:'JetBrains Mono',monospace;font-size:.6rem;">
            <p><strong>Honorarios:</strong> $${Number(honorarios).toLocaleString()}</p>
            <p><strong>Inversión obra:</strong> $${Number(lead.inversion_obra_estimada || 0).toLocaleString()}</p>
            <p><strong>Nivel:</strong> ${nivel.toUpperCase()} · <strong>m²:</strong> ${m2}</p>
            <hr style="border:none;border-top:1px solid #eee;margin:10px 0;"></div>`;

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
                if (analisis.inmersion) {
                    html += `<h4 style="font-size:.7rem;margin:10px 0 5px;">Respuestas de Inmersión</h4>
                        <table class="data-table">
                        ${Object.entries(analisis.inmersion).map(([k,v]) => `<tr><td>${API.esc(k)}</td><td>${API.esc(v)}</td></tr>`).join('')}
                        </table>`;
                }
            } catch (_) {}
        }

        // Cobros
        html += `<h4 style="font-size:.7rem;margin:15px 0 5px;">Cobros</h4>
            <div id="exp-cobros-${id}"><p class="loading-text">Cargando...</p></div>`;

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

    return {
        load, getLeads,
        renderCandidatos, renderClientesMomento2, renderMomento3,
        avanzar, regresar, cerrar, eliminar,
        pagarCobroDirecto, pagarCobroExpediente,
        abrirContratar, confirmarContratar, cerrarContratar,
        cambiarEstadoContacto, abrirExpediente
    };
})();
