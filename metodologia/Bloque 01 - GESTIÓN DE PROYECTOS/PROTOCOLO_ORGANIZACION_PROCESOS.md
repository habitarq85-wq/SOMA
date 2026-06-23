# PROTOCOLO 04: ORGANIZACION DE PROCESOS
## Bloque 1 — Gestion del Entorno (ADM)

*Mapeo formal del flujo: Lead → Proyecto → Entrega → Cierre*

---

## 1. MACROFLUJO SOMA (Vista General)

```
                    PROCESO SOMA - FLUJO COMPLETO
               ┌──────────────────────────────────────┐
               │         BLOQUE 4 (MKT)               │
               │  Web / Redes / Referidos → LEAD      │
               └────────────┬─────────────────────────┘
                            ▼
               ┌──────────────────────────────────────┐
               │      BLOQUE 2 (TALLER) - ETAPA 1     │
               │         Recepción de Datos           │
               │     (Inmersión Web + Entrevista)      │
               └────────────┬─────────────────────────┘
                            ▼
               ┌──────────────────────────────────────┐
               │     BLOQUE 1 (ADM) - PRE-VENTA       │
               │      Programa Arquitectónico          │
               │   (Deseado + Complementario + Lujo)   │
               └────────────┬─────────────────────────┘
                            ▼
               ┌──────────────────────────────────────┐
               │     BLOQUE 1 (ADM) - COMERCIAL       │
               │    Cotización → Contrato + Anticipo   │
               └────────────┬─────────────────────────┘
                            ▼
               ┌──────────────────────────────────────┐
               │      BLOQUE 2 (TALLER) - ETAPA 2-3   │
               │      Investigación + Análisis         │
               │   (Sitio, Normativa, Activity Matrix)  │
               └────────────┬─────────────────────────┘
                            ▼
               ┌──────────────────────────────────────┐
               │      BLOQUE 2 (TALLER) - ETAPA 4-10  │
               │  Conceptualización → Coordinación     │
               │  (Diseño, Modelado, Planos, Entrega)  │
               └────────────┬─────────────────────────┘
                            ▼
               ┌──────────────────────────────────────┐
               │     BLOQUE 1 (ADM) - CIERRE          │
               │  Cobro Final + CFDI + Archivo        │
               └──────────────────────────────────────┘
```

---

## 2. FASES DETALLADAS DEL PROCESO

### FASE 0: GENERACION DE LEAD (MKT)
*Responsable: Mercadotecnia / Sistema*

| Actividad | Medio | Trigger | Documento Generado |
|-----------|-------|---------|-------------------|
| Captura web | Pagina Web 6 (Inmersion 10 pasos) | Usuario completa los 10 pasos + contacto | `captura_web` en DB |
| Lead manual | Dashboard (creacion directa) | Arquitecto registra lead manualmente | `captura_web` en DB |
| Referido | Contacto directo | Cliente existente recomienda | `captura_web` en DB |

**Estado en sistema:** `pipeline_estado = 'lead'`
**Notificacion:** WhatsApp a Juan (Twilio) + reporte en `backend/reportes/` + correo SMTP

**Criterio de avance:** Se asigna lead y se agenda primera cita para entrevista.

---

### FASE 1: RECEPCION (Taller — Etapa 1)
*Responsable: Arquitecto*
*Pipeline: `entrevistado`*

| Actividad | Herramienta | Duracion Estimada |
|-----------|-------------|-------------------|
| 1.1 Entrevista de Inmersion | App de Entrevista (puerto 5050) — grabacion + 6 topicos | 45-60 min presencial |
| 1.2 Post-formulario | App de Entrevista — datos estructurados | 5 min post-entrevista |
| 1.3 Procesamiento IA (opcional) | Whisper + DeepSeek Flash | 5-10 min automatico |

**Documentos generados:**
- `backend/proyectos/SOMA-YYYYMMDD-XXXX/entrevista.webm` — audio crudo
- `backend/proyectos/SOMA-YYYYMMDD-XXXX/transcripcion.txt` — transcripcion Whisper
- `backend/proyectos/SOMA-YYYYMMDD-XXXX/guia_de_diseno.md` — guia unificada
- `backend/proyectos/SOMA-YYYYMMDD-XXXX/datos_estructurados.json` — Activity Matrix + ejes

**Criterio de avance:** Entrevista realizada y datos estructurados disponibles.

---

### FASE 2: PROGRAMA ARQUITECTONICO (ADM - Pre-venta)
*Responsable: Arquitecto*
*Pipeline: `programado`*

| Actividad | Herramienta | Duracion |
|-----------|-------------|----------|
| 2.1 Captura de Programa Deseado | Dashboard — modulo PROGRAMA, pestana Deseado | 20 min con lead |
| 2.2 Captura de Programa Complementario | Dashboard — modulo PROGRAMA, pestana Complementario | 10 min |
| 2.3 Captura de Programa de Lujo | Dashboard — modulo PROGRAMA, pestana Lujo | 10 min |
| 2.4 Definicion de Claves E{n} y Relaciones | Dashboard — boton 🔗 en cada fila | 5 min |
| 2.5 Calculo de m2 totales por nivel | Sistema — automatico | Instantaneo |

**Reglas del programa:**
- Zonas: 1=Social, 2=Operativa, 3=Descanso, 4=Soporte, 5=Transicion
- Clave: E{n} — solo se ingresa el numero, el prefijo E es automatico
- Relaciones: se editan despues de crear todos los espacios (diferidas)
- NO incluye investigacion de sitio ni analisis profundo — eso va despues del contrato

**Documentos generados:**
- `programa_arquitectonico` en DB (espacios con clave E{n}, zonas, relaciones)
- Totales parciales por tipo de programa (Deseado / Complementario / Lujo)

**Criterio de avance:** Lista de espacios completa con areas, zonas y claves.

---

### FASE 3: COMERCIALIZACION (ADM)
*Responsable: Arquitecto / Sistema*
*Pipeline: `cotizado`*

| Actividad | Herramienta | Duracion |
|-----------|-------------|----------|
| 3.1 Cotizacion Formal | Dashboard — modulo COTIZACION (calcula honorarios) | Automatico |
| 3.2 Entrega de Cotizacion | Dashboard — boton PDF (formato imprimible) | Instantaneo |
| 3.3 Negociacion | Presencial / llamada | Variable |
| 3.4 Contrato | CONTRATO_DISENO_SOMA.md (plantilla) | 1 sesion |
| 3.5 Esquema de Pagos 30/40/30 | Dashboard — boton "Generar 30/40/30" | Automatico |

**Reglas de la cotizacion (SOLOJUAN 2026-05-19):**
- NO mostrar precio por m2 al cliente
- NO mostrar cargo minimo de $8,000
- NO mostrar estimacion de obra
- SI mostrar: datos del cliente, tabla de programa, total honorarios, esquema 30/40/30, vigencia 30 dias

**Documentos generados:**
- PDF de cotizacion (HTML imprimible)
- 3 registros en tabla `cobros` (30%, 40%, 30%) via endpoint `POST /cobros/generar_esquema/<id>`

**Criterio de avance:** Cotizacion entregada al cliente.

---

### FASE 4: CONTRATACION (ADM)
*Responsable: Arquitecto / Cliente*
*Pipeline: `contratado`*

| Actividad | Detalle |
|-----------|---------|
| 4.1 Firma de Contrato | CONTRATO_DISENO_SOMA.md firmado por ambas partes |
| 4.2 Pago de Anticipo (30%) | Transferencia o deposito — registrado en Dashboard |
| 4.3 Recepcion de Informacion del Cliente | Planos del terreno, escrituras, restricciones, levantamiento topografico |
| 4.4 Confirmacion de Inicio | Arquitecto confirma en Dashboard: se activa cronometro de entrega |

**Reglas de cancelacion:**
- Cancelacion antes de iniciar diseno: reembolso 100% del anticipo
- Cancelacion despues de anteproyecto: no reembolso (30% + 40% retenidos)

**Criterio de avance:** Anticipo registrado en sistema + informacion del cliente completa.

---

### FASE 5: INVESTIGACION Y ANALISIS (Taller — Etapas 2-3)
*Responsable: Arquitecto / Sistema*
*Se ejecuta DESPUES del contrato*

| Actividad | Herramienta | Duracion |
|-----------|-------------|----------|
| 5.1 Analisis de Sitio | PROTOCOLO_ANALISIS_SITIO.md + consulta externa | 1-2 dias |
| 5.2 Analisis Normativo | Reglamentos municipales, COS, CUS, restricciones | 1 dia |
| 5.3 Activity Matrix (detalle) | Dashboard — boton MATRIZ (grid 24h) | 30 min |
| 5.4 Ejes de Inmersion (refinamiento) | Dashboard — barras de polaridad (10 ejes) | 30 min |
| 5.5 Diagrama Espacial | DiagramaSoma.html — grafo interactivo | 1-2 horas |
| 5.6 Analisis del Programa (complementos) | Cruce de datos: deseado vs. normativa vs. presupuesto | 1 dia |

**Documentos generados:**
- Reporte de analisis de sitio (bioclimatica, normativa, Genius Loci)
- Activity Matrix visual en Dashboard
- Diagrama de relaciones espaciales
- Programa evolucionado (con complementos tecnicos identificados)

**Criterio de avance:** Investigacion completa y analisis listo para comenzar el diseno.

---

### FASE 6: DISENO Y ENTREGA (Taller — Etapas 4-10)
*Responsable: Arquitecto*

| Etapa Taller | Actividad | Entregable | Duracion Estimada |
|-------------|-----------|------------|-------------------|
| **4. Conceptualizacion** | Mensaje arquitectonico, Intenciones, CreativeCore, Moldeado Formal | Partido de diseno + croquis conceptuales | 1 semana |
| **5. Visualizacion** | Modelado 3D, perspectivas de autor, moodboard | Renders de autor + maqueta virtual | 1 semana |
| **6. Representacion Integral** | Dossier editorial con memoria descriptiva | PDF de presentacion tipo revista | 3-4 dias |
| **7. Evaluacion** | Auditoria de Indicadores de Habitabilidad (termica, acustica, iluminacion) | Tabla de indicadores + ajustes | 2-3 dias |
| **8. Anteproyecto** | Ajuste fino basado en evaluacion, planos de anteproyecto | Plantas, alzados, cortes del anteproyecto | 1 semana |
| **9. Planos Tecnicos** | Documentacion automatizada (solamente paquete Ejecutivo) | Planos ejecutivos, detalles constructivos | 1-2 semanas |
| **10. Coordinacion** | Gestion con especialistas externos (solamente paquete Ejecutivo) | Ingenierias coordinadas | 1 semana |

**Hito de segundo pago (40%):** Se dispara al entregar el **Anteproyecto** (Etapa 8).
*El segundo pago debe estar liquidado antes de avanzar a Planos Tecnicos.*

**Documentos generados por proyecto:**
```
proyectos/SOMA-YYYYMMDD-XXXX/
├── info.json
├── entrevista.webm
├── transcripcion.txt
├── guia_de_diseno.md
├── datos_estructurados.json
├── anteproyecto/
│   ├── plantas.pdf
│   ├── alzados.pdf
│   └── cortes.pdf
├── renders/
│   ├── exterior_01.png
│   └── interior_01.png
├── dossier_editorial.pdf
├── planos_ejecutivos/   (solo Ejecutivo)
│   ├── estructurales.pdf
│   ├── hidrosanitarias.pdf
│   └── electricas.pdf
└── coordinacion/        (solo Ejecutivo)
    └── memorias_tecnicas.pdf
```

**Estado en sistema:** `pipeline_estado` se mantiene como `'contratado'` durante todo el proceso de diseno.

---

### FASE 7: CIERRE (ADM)
*Responsable: Arquitecto / Sistema*
*Pipeline: `pagado`*

| Actividad | Detalle |
|-----------|---------|
| 7.1 Pago Final (30%) | Tercer pago al entregar diseno final |
| 7.2 CFDI / Factura | Generar factura por el monto total (cuando Juan tenga RFC) |
| 7.3 Liberacion de Propiedad Intelectual | Planos pasan a ser propiedad del cliente |
| 7.4 Encuesta Post-ocupacion (opcional) | Contactar al cliente 6 meses despues para POE |
| 7.5 Archivo de Proyecto | Mover a `backend/proyectos/archivados/` |
| 7.6 Publicacion en Portafolio | Agregar renders al carrusel de la pagina web (si aplica) |

**Criterio de cierre:** Todos los pagos registrados + entregables finales entregados.

---

## 3. MAPA DE TRANSICION DE ESTADOS (Dashboard)

```
                    PIPELINE SOMA (6 Estados)

    LEAD ─────► ENTREVISTADO ─────► PROGRAMADO ─────► COTIZADO
      │              │                  │                 │
      │              │                  │                 │
      ▼              ▼                  ▼                 ▼
    PAGADO ◄──── CONTRATADO ◄────────────────────────────┘
```

| Estado | Fase | Descripcion | Accion Requerida | Responsable |
|--------|------|-------------|------------------|-------------|
| **Lead** | F0 | Captura web inicial | Contactar para entrevista | Sistema / Arquitecto |
| **Entrevistado** | F1 | Entrevista realizada | Capturar programa arquitectonico | Arquitecto |
| **Programado** | F2 | Programa completo | Generar cotizacion | Sistema |
| **Cotizado** | F3 | Cotizacion entregada | Seguimiento para contratacion | Arquitecto |
| **Contratado** | F4-F6 | Contrato + anticipo | Investigar, analizar, disenar | Arquitecto |
| **Pagado** | F7 | Proyecto completado | Archivar y publicar | Sistema |

---

## 4. REGLAS DE NEGOCIO TRANSVERSALES

### 4.1 Subsidio Cruzado
- El nivel **Ejecutivo** y proyectos de gran escala financian la accesibilidad de los niveles **Esencial** e **Integral**.
- El cargo minimo de $8,000 se aplica silenciosamente (el cliente no lo ve).
- La calidad de diseno es la misma en todos los niveles; lo que varia es la profundidad tecnica.

### 4.2 Esquema de Pagos 30/40/30
| Pago | % | Disparador |
|------|---|------------|
| Anticipo | 30% | Firma de contrato |
| Segundo pago | 40% | Entrega de anteproyecto |
| Tercer pago | 30% | Entrega final |

### 4.3 Tiempos de Entrega Estimados
| Desde | Hasta | Duracion |
|-------|-------|----------|
| Firma de contrato | Entrega de anteproyecto | 3-4 semanas |
| Entrega de anteproyecto | Entrega final | 3-4 semanas |
| **Total** | | **6-8 semanas** |

*Los tiempos se cuentan a partir del pago del anticipo y la entrega de informacion completa del cliente.*

### 4.4 Notificaciones Automaticas
| Evento | Canal | Destino |
|--------|-------|---------|
| Nuevo lead | WhatsApp (Twilio) | Juan |
| Nuevo lead | Correo SMTP | habitarq85@gmail.com |
| Nuevo lead | Reporte en disco | `backend/reportes/` |
| Pago registrado | Correo SMTP | habitarq85@gmail.com |
| Proyecto completado | Correo SMTP | habitarq85@gmail.com |

### 4.5 Propiedad Intelectual
- Los planos, renders y documentos de diseno son propiedad de SOMA hasta liquidacion total.
- Una vez pagados en su totalidad, el cliente tiene derecho a usar los planos para construir.
- SOMA se reserva el derecho de publicar imagenes del proyecto en portafolio y redes sociales, a menos que el cliente solicite confidencialidad por escrito.

---

## 5. DIAGRAMA DE RESPONSABILIDADES

| Fase | Sistema (Automatizado) | Arquitecto | Cliente |
|------|----------------------|------------|---------|
| F0: Lead | Captura web, notificacion Twilio/SMTP | Asigna lead, agenda cita | Completa inmersion web |
| F1: Recepcion | Grabacion, post-formulario, IA (opcional) | Conduce entrevista 6 topicos | Responde entrevista |
| F2: Programa | Calculo de m2, claves E{n} | Captura espacios con lead | Define espacios deseados |
| F3: Comercial | Calculo cotizacion, PDF, esquema 30/40/30 | Presenta cotizacion, negocia | Decide paquete, firma contrato |
| F4: Contrato | Registro de cobros en DB | Recibe anticipo, confirma inicio | Paga 30%, entrega docs del predio |
| F5: Investigacion | Activity Matrix, Ejes, Diagrama | Analisis sitio, normativa, programa | — |
| F6: Diseno | — | Ejecuta diseno (Etapas 4-10) | Retroalimenta en hitos |
| F7: Cierre | — | Entrega final, recibe pago, archiva | Paga 30%, recibe planos |

---

## 6. INDICADORES DE GESTION (Dashboard)

| Indicador | Formula | Donde se ve |
|-----------|---------|-------------|
| Leads activos | COUNT(pipeline_estado != 'pagado') | Header Dashboard |
| Tasa de conversion | leads_contratados / leads_totales | Panel ADMIN |
| Tiempo promedio lead→contrato | AVG(fecha_hoy - fecha_lead) | Panel ADMIN |
| Ingresos del mes | SUM(cobros.monto WHERE MONTH(fecha_pago)) | Resumen Financiero |
| Cuentas por cobrar | SUM(cobros.monto WHERE estado='pendiente') | Resumen Financiero |
| Proyectos activos en diseno | COUNT(pipeline_estado = 'contratado') | Kanban columna Contratado |

---

## 7. FLUJO DE ARCHIVADO

Al completar un proyecto (pipeline_estado = 'pagado'):

1. Mover carpeta `proyectos/SOMA-XXXX/` a `proyectos/archivados/SOMA-XXXX/`
2. Respaldar DB (automatico via `backend/backup_db.sh`)
3. Si el cliente autoriza, agregar renders al portafolio web
4. Actualizar estado en Dashboard (permanece visible en historico)

**Politica de respaldos:**
- Script `backend/backup_db.sh` — respaldo diario con timestamp
- Limpieza automatica de backups >30 dias
- Carpeta: `backend/backups/`

---

## 8. NOTAS DE IMPLEMENTACION

- **Dashboard** servido desde Flask (puerto 8080) para evitar CORS
- **App de Entrevista** servidor independiente (puerto 5050) — comparten DB
- **Twilio** activo con credito gratuito (~$15 USD). Migrar a Telegram cuando se agote
- **DeepSeek Flash + Whisper:** pendientes de configurar (sin costo hasta agotar credito gratuito)
- **RFC de Juan:** pendiente de alta en RESICO para emitir CFDI

---

*Documento creado: 21/05/2026*
*Ultima actualizacion: 21/05/2026*
*Versión: 1.1*
