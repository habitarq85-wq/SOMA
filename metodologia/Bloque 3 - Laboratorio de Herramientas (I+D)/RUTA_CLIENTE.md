# RUTA DEL CLIENTE — SOMA Taller Virtual de Arquitectura

Checklist de extremo a extremo: del primer contacto al proyecto terminado.

```
CLIENTE ──> INMERSIÓN ──> PROGRAMA ──> CONTRATO ──> DISEÑO ──> ENTREGA
```

---

## FASE 0 — ATRACCIÓN (MKT)

- [ ] Cliente encuentra SOMA (web / Instagram / Google / referido)
- [ ] Ve el sitio en `soma.onrender.com`
- [ ] (Opcional) Descarga lead magnet "10 errores al construir"
- [ ] Decide iniciar el cotizador

**Referencias:** `web/Pagina Web 6.html`, `web/lead_magnet_10_errores.html`, `metodologia/Bloque 4 - Marketing y Comunicacion (MKT)/`

---

## FASE 1 — INMERSIÓN (F1)

- [ ] Cliente completa **Inmersión Web** (10 pasos visuales A/B)
- [ ] Ingresa contacto (WhatsApp o correo)
- [ ] Sistema guarda lead en DB (`POST /save_immersion`)
- [ ] Llega notificación a Juan (Twilio/SendGrid)
- [ ] Juan agenda **Entrevista Presencial** (6 temas, 45-60 min)
- [ ] Entrevista se registra en App (puerto 5050)
- [ ] Pipeline → **entrevistado**

**Referencias:** `web/Pagina Web 6.html:694-792`, `backend/server.py`, `PROTOCOLO_02_ENTREVISTA_INMERSION.md`

---

## FASE 2 — PROGRAMA + VIABILIDAD (F2)

- [ ] Se captura **Programa Arquitectónico** (deseado + complementario + lujo)
- [ ] Se asignan claves de espacio `E{1..n}`
- [ ] Se calcula **m² total** y nivel de paquete
- [ ] Sistema genera cotización (escala + honorarios + rango obra)
- [ ] Se valida contra el mínimo operativo ($6,500)
- [ ] Pipeline → **programado**

**Referencias:** `Dashboard.html`, `PROTOCOLO_PRESUPUESTO_Y_VIABILIDAD.md`, `01_PROTOCOLO_ANALISIS.md`

---

## FASE 3 — COMERCIAL / CONTRATO (F3)

- [ ] Juan presenta **carta de presentación** SOMA
- [ ] Explica niveles: Esencial / Integral / Ejecutivo
- [ ] Entrega **cotización formal**
- [ ] Firma **Convenio de Anticipo**
- [ ] Firma **Contrato de Diseño**
- [ ] Cliente paga **anticipo 30%**
- [ ] Se genera esquema de pagos 30/40/30 en sistema
- [ ] Pipeline → **contratado**

**Referencias:** `CARTA_PRESENTACION_SOMA.md`, `CONVENIO_ANTICIPO_PAGOS.md`, `CONTRATO_DISENO_SOMA.md`, `Dashboard.html:677`

---

## FASE 4 — INVESTIGACIÓN PREVIA

- [ ] **Sitio:** topografía, orientación, fotografía, acceso
- [ ] **Clima:** asoleamiento, vientos dominantes, precipitación
- [ ] **Normativa:** usos de suelo, restricciones, COS/CUS, límites
- [ ] **Contexto:** vecinos, vialidades, infraestructura
- [ ] **Usuario:** UserEntity, Activity Matrix, 10 Ejes Creativos

**Referencias:** `PROTOCOLO_INVESTIGACION_PREVIA.md`, `PROTOCOLO_01_RECEPCION.md`

---

## FASE 5 — ANÁLISIS

- [ ] **Análisis de Sitio:** zonificación maestra, accesos, asoleamiento
- [ ] **Análisis del Usuario:** perfil, estilo de vida, necesidades
- [ ] **Análisis Bioclimático:** carta solar, ventilación, zonificación térmica
- [ ] **Análisis Contextual:** lenguaje urbano, alturas, materiales
- [ ] **Diagrama Espacial SOMA:** grafo de relaciones entre espacios
- [ ] Se genera Guía de Diseño

**Referencias:** `01_PROTOCOLO_ANALISIS.md`, `DiagramaSoma.html`, `EJEMPLO_GUIA_DISENO.md`

---

## FASE 6 — CONCEPTUALIZACIÓN

- [ ] Definir **Idea Matriz** (concepto rector del proyecto)
- [ ] Redactar **Mensaje Arquitectónico** (qué cuenta el espacio)
- [ ] Establecer **Intenciones de Diseño** (3-5 ejes)
- [ ] **Moldeado Formal:** volumetría, proporciones, piel

**Referencias:** `01_PROTOCOLO_CONCEPTUALIZACION.md`

---

## FASE 7 — MODELADO + VISUALIZACIÓN

- [ ] **Modelado 3D:**
  - Esencial: LOD 200
  - Integral: LOD 300
  - Ejecutivo: LOD 350+
- [ ] Flujo Revit → D5 Render
- [ ] **Renders:** 2-5 vistas según paquete (estilo SOMA)
- [ ] **Dossier editorial** (Representación Integral)
- [ ] **Evaluación de habitabilidad:** térmica, acústica, iluminación, proxémica

**Referencias:** `02_PROTOCOLO_MODELADO.md`, `03_PROTOCOLO_VISUALIZACION.md`, `04_PROTOCOLO_REPRESENTACION_INTEGRAL.md`, `05_PROTOCOLO_EVALUACION.md`

---

## FASE 8 — ANTEPROYECTO

- [ ] Plantas arquitectónicas formales
- [ ] Cortes y alzados
- [ ] Planta de conjunto
- [ ] Revisión con cliente
- [ ] Ajustes post-revisión
- [ ] Aprobación del cliente
- [ ] **Pago 2 — 40%** (se entrega anteproyecto)
- [ ] Pipeline → estado intermedio

**Referencias:** `06_PROTOCOLO_ANTEPROYECTO.md`, `RECIBO_PAGO_PARCIAL.md`

---

## FASE 9 — PLANOS TÉCNICOS (solo Ejecutivo)

- [ ] Planos de albañilería
- [ ] Planos de acabados
- [ ] Detalles constructivos
- [ ] Criterios de ingenierías (estructural, hidrosanitaria, eléctrica)
- [ ] Coordinación con especialistas externos

**Referencias:** `07_PROTOCOLO_PLANOS_TECNICOS.md`, `08_PROTOCOLO_COORDINACION.md`

---

## FASE 10 — CIERRE

- [ ] Proyecto terminado y entregado
- [ ] Cliente recibe planos (digital + impresión opcional)
- [ ] **Pago 3 — 30%** (liberación final)
- [ ] Se genera CFDI / recibo de honorarios
- [ ] Liberación de Propiedad Intelectual (planos pasan a ser del cliente)
- [ ] Pipeline → **pagado**
- [ ] Se archiva proyecto en Dashboard
- [ ] (Opcional) Se publica en portafolio SOMA

**Referencias:** `CONTRATO_DISENO_SOMA.md:80-87`, `Dashboard.html`, `RECIBO_PAGO_PARCIAL.md`

---

## MAPA DE PAGOS

| Pago | % | Monto | Disparador |
|------|---|-------|------------|
| Anticipo | 30% | $____ | Firma de contrato |
| Segundo | 40% | $____ | Entrega de anteproyecto |
| Tercero | 30% | $____ | Entrega final |
| **Total** | **100%** | **$____** | |

---

## TIEMPO ESTIMADO

| Etapa | Duración |
|-------|----------|
| Recepción y análisis | 1 semana |
| Propuesta de diseño (anteproyecto) | 2-3 semanas |
| Revisión con cliente | 1 semana |
| Entregables finales | 2-3 semanas |
| **Total** | **6-8 semanas** |

---

## PIPELINE (Dashboard)

```
lead ──> entrevistado ──> programado ──> cotizado ──> contratado ──> pagado
  F0         F1              F2             F3          F4-F9           F10
```

Cada flecha representa una acción concreta de Juan. El tablero Kanban en el Dashboard refleja en tiempo real dónde está cada proyecto.
