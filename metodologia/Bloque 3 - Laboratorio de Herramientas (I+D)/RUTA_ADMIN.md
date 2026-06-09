# RUTA DE ADMINISTRACIÓN — SOMA Taller Virtual de Arquitectura

Checklist de gestión del taller: finanzas, pipeline, legal, infraestructura y métricas.

```
DÍA A DÍA ──> SEMANAL ──> MENSUAL ──> TRIMESTRAL ──> ANUAL
```

---

## ⚡ DIARIO (5-10 min)

- [ ] Revisar Dashboard — ¿nuevos leads en las últimas 24h?
- [ ] Contestar WhatsApp de clientes activos
- [ ] Verificar notificaciones de cobros (transferencias)
- [ ] Dar seguimiento a leads en **entrevistado** y **cotizado** (no dejar enfriar)
- [ ] Si hay pago pendiente → recordatorio amable al cliente

**Herramientas:** Dashboard, WhatsApp, App Entrevista

---

## 📅 SEMANAL (30-60 min)

### Pipeline
- [ ] Mover leads/proyectos a su estado correcto en Kanban
- [ ] Identificar cuellos de botella (ej. muchos en **cotizado** sin pasar a **contratado**)
- [ ] Revisar leads perdidos — ¿por qué no cerraron?

### Finanzas
- [ ] Total cobrado vs pendiente de cobro (Dashboard)
- [ ] ¿Algún pago próximo a vencer? Recordar al cliente
- [ ] Registrar cobros manuales que no se hayan capturado

### Proyectos activos
- [ ] ¿Cada proyecto avanza según sus tiempos estimados?
- [ ] ¿Algún cliente necesita una actualización?

**Herramientas:** Dashboard (pipeline, finanzas, proyectos)

---

## 📆 MENSUAL (2-3 hrs)

### Cierre financiero
- [ ] Sumar ingresos del mes (todos los cobros)
- [ ] Registrar egresos:
  - [ ] Servidores (Railway / Render)
  - [ ] Dominios
  - [ ] Software (Revit, D5, Adobe)
  - [ ] Herramientas (SendGrid, Twilio)
  - [ ] Gastos operativos
- [ ] Calcular margen del mes
- [ ] Alimentar **Fondo Social** (si aplica porcentaje)
- [ ] Actualizar fondo social en Dashboard

### Dashboard
- [ ] Revisar y limpiar leads zombies (>30 días sin avance)
- [ ] Archivar proyectos completados
- [ ] Verificar que todos los proyectos tengan esquema de cobros

### Marketing
- [ ] ¿Funcionó lo que publicaste esta semana? Revisar métricas
- [ ] Publicar 1 caso / avance / reflexión en Instagram
- [ ] Actualizar portafolio si hay proyecto nuevo terminado

### Legal-Fiscal
- [ ] Facturar (CFDI) los pagos recibidos en el mes
- [ ] Declaración mensual RESICO (si aplica)
- [ ] Revisar buzón tributario SAT

**Herramientas:** Dashboard, SAT, Instagram, Google My Business

---

## 📊 TRIMESTRAL (4-6 hrs)

### Estrategia
- [ ] ¿Cuántos leads entraron? Tasa de conversión: lead → contratado
- [ ] Ingreso promedio por proyecto
- [ ] Paquete más vendido (Esencial / Integral / Ejecutivo)
- [ ] ¿El precio por m² sigue siendo competitivo? Investigar mercado
- [ ] Ajustar precios si es necesario (registrar en `SOLOJUAN.md`)

### Sistema
- [ ] Backup completo de la base de datos
- [ ] Revisar logs del servidor (errores, uptime)
- [ ] Actualizar dependencias (Flask, librerías)
- [ ] Verificar que SendGrid y Twilio tengan saldo

### Proyectos
- [ ] Pedir testimonio o reseña a clientes satisfechos
- [ ] Publicar proyecto completo en portafolio web
- [ ] Evaluar si los tiempos de entrega estimados se cumplieron

**Herramientas:** Dashboard, Railway/Render dashboard, Google My Business, SAT

---

## 🏆 ANUAL (1 día)

### Cierre del año fiscal
- [ ] Declaración anual RESICO
- [ ] Balance de ingresos vs egresos del año
- [ ] Calcular % de subsidio cruzado real (Ejecutivo → Esencial)

### Proyección
- [ ] Definir metas del próximo año (ej. N leads, N proyectos, ingreso meta)
- [ ] ¿Ajustar modelo de precios?
- [ ] ¿Migrar de tecnología? (Railway → Render, SQLite → PostgreSQL, etc.)
- [ ] ¿Contratar apoyo? (delineante, community manager, ingeniero fijo)

### Documentación
- [ ] Actualizar `SOMA_SNAPSHOT.md` con estado del año
- [ ] Actualizar `SOMA_CORE_INDEX.md`
- [ ] Revisar y actualizar `SOLOJUAN.md` — ¿siguen vigentes las decisiones?
- [ ] Archivar proyectos del año en carpeta de respaldo

**Herramientas:** SAT, Dashboard, Railway/Render, Google Drive

---

## MAPA DE HERRAMIENTAS ADMINISTRATIVAS

| Herramienta | Para qué | Frecuencia |
|------------|----------|-----------|
| **Dashboard** | Pipeline, cobros, leads, fondo social | Diario |
| **WhatsApp** | Comunicación con clientes, seguimiento | Diario |
| **App Entrevista** | Registrar inmersiones | Semanal |
| **Railway / Render** | Server status, logs, DB backup | Mensual |
| **SendGrid** | Correos transaccionales (notificaciones) | Mensual |
| **Twilio** | WhatsApp API (notificaciones automáticas) | Mensual |
| **SAT** | CFDI, declaraciones, buzón tributario | Mensual |
| **Instagram / GMB** | Marketing, portafolio público | Semanal |
| **Google Drive** | Archivo de proyectos, respaldos | Mensual |
| **SOLOJUAN.md** | Decisiones estratégicas, ajustes de precio | Trimestral |
| **SOMA_SNAPSHOT.md** | Estado actual del sistema | Anual |

---

## INDICADORES CLAVE (KPI)

| Indicador | Cómo se mide | Objetivo |
|-----------|-------------|----------|
| **Leads/mes** | Nuevos registros en Dashboard | > 3/mes |
| **Tasa conversión** | contratados / leads | > 30% |
| **Ticket promedio** | Ingreso total / proyectos cerrados | — |
| **Ciclo promedio** | Días de contrato a entrega | < 8 semanas |
| **Margen operativo** | (Ingresos - gastos) / ingresos | > 60% |
| **Fondo social** | Dashboard fondo social | Creciente |
| **Morosidad** | Pagos vencidos / total cobros | 0% |

---

## RECORDATORIOS FIJOS

| Fecha | Qué hacer |
|-------|-----------|
| **Día 1 de cada mes** | Declaración RESICO + CFDI del mes anterior |
| **Día 15 de cada mes** | Revisar saldo SendGrid + Twilio |
| **Cada trimestre** | Backup de DB + revisión de precios |
| **31 diciembre** | Cierre fiscal anual + proyección del próximo año |

---

*Ni el mejor diseño paga las cuentas si la administración no existe.*
