const API = (() => {
    const BASE = window.location.origin;

    async function request(url, options = {}) {
        try {
            const controller = new AbortController();
            const timer = setTimeout(() => controller.abort(), 10000);
            const res = await fetch(url, {
                headers: { 'Content-Type': 'application/json', ...options.headers },
                signal: controller.signal,
                ...options
            });
            clearTimeout(timer);
            if (!res.ok) {
                const body = await res.json().catch(() => ({}));
                throw new Error(body.message || `Error ${res.status}`);
            }
            return res.status === 204 ? null : await res.json();
        } catch (e) {
            if (e.name === 'TypeError' && e.message.includes('fetch')) {
                throw new Error('Error de conexión con el servidor');
            }
            if (e.name === 'AbortError') {
                throw new Error('La solicitud tardó demasiado. Verifica que el servidor esté corriendo.');
            }
            throw e;
        }
    }

    function esc(str) {
        if (str == null) return '';
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
    }

    return {
        esc,

        // ---- Leads ----
        getLeads() {
            return request(`${BASE}/get_leads`);
        },

        // ---- Metrics ----
        getMetrics(year, month) {
            let url = `/metrics/bloque01?year=${year}`;
            if (month) url += `&month=${month}`;
            return request(url);
        },

        // ---- Pipeline ----
        updatePipeline(leadId, estado) {
            return request(`${BASE}/lead/${leadId}/pipeline`, {
                method: 'PATCH',
                body: JSON.stringify({ pipeline_estado: estado })
            });
        },
        regresarLead(leadId) {
            return request(`${BASE}/lead/${leadId}/regresar`, { method: 'POST' });
        },
        contratarLead(leadId) {
            return request(`${BASE}/lead/${leadId}/contratar`, { method: 'POST' });
        },
        updateEstadoContacto(leadId, estado) {
            return request(`${BASE}/lead/${leadId}/estado-contacto`, {
                method: 'PATCH',
                body: JSON.stringify({ estado_contacto: estado })
            });
        },

        // ---- Cobros ----
        getCobros(proyectoId) {
            return request(`${BASE}/cobros/${proyectoId}`);
        },
        pagarCobro(cobroId, fechaPago) {
            return request(`${BASE}/cobros/${cobroId}/pagar`, {
                method: 'PATCH',
                body: JSON.stringify({ fecha_pago: fechaPago || new Date().toISOString() })
            });
        },
        crearCobro(proyectoId, data) {
            return request(`${BASE}/cobros/${proyectoId}`, {
                method: 'POST',
                body: JSON.stringify(data)
            });
        },
        generarEsquemaPagos(proyectoId) {
            return request(`${BASE}/cobros/${proyectoId}/generar-esquema`, { method: 'POST' });
        },

        // ---- Egresos ----
        getEgresos() {
            return request(`${BASE}/egresos`);
        },
        crearEgreso(data) {
            return request(`${BASE}/egresos`, {
                method: 'POST',
                body: JSON.stringify(data)
            });
        },
        eliminarEgreso(id) {
            return request(`${BASE}/egresos/${id}`, { method: 'DELETE' });
        },

        // ---- Fondos ----
        getFondos() {
            return request(`${BASE}/api/fondos`);
        },
        crearFondo(data) {
            return request(`${BASE}/api/fondos`, {
                method: 'POST',
                body: JSON.stringify(data)
            });
        },
        eliminarFondo(id) {
            return request(`${BASE}/api/fondos/${id}`, { method: 'DELETE' });
        },
        apartarFondo(fondoId, data) {
            return request(`${BASE}/api/fondos/${fondoId}/apartar`, {
                method: 'POST',
                body: JSON.stringify(data)
            });
        },
        retirarFondo(fondoId, data) {
            return request(`${BASE}/api/fondos/${fondoId}/retirar`, {
                method: 'POST',
                body: JSON.stringify(data)
            });
        },
        getMovimientosFondo(fondoId) {
            return request(`${BASE}/api/fondos/${fondoId}/movimientos`);
        },

        // ---- Programa ----
        getPrograma(leadId) {
            return request(`${BASE}/programa/${leadId}`);
        },
        crearEspacio(leadId, data) {
            return request(`${BASE}/programa/espacio`, {
                method: 'POST',
                body: JSON.stringify({...data, lead_id: leadId})
            });
        },
        eliminarEspacio(espacioId) {
            return request(`${BASE}/programa/espacio/${espacioId}`, { method: 'DELETE' });
        },
        guardarRelaciones(espacioId, data) {
            return request(`${BASE}/programa/espacio/${espacioId}/relaciones`, {
                method: 'PUT',
                body: JSON.stringify(data)
            });
        },
        getCotizacion(leadId) {
            return request(`${BASE}/cotizacion/${leadId}`);
        },
        guardarDatosProyecto(leadId, data) {
            return request(`${BASE}/lead/${leadId}/datos-proyecto`, {
                method: 'PATCH',
                body: JSON.stringify(data)
            });
        },
        eliminarProyecto(leadId) {
            return request(`${BASE}/lead/${leadId}`, { method: 'DELETE' });
        }
    };
})();
