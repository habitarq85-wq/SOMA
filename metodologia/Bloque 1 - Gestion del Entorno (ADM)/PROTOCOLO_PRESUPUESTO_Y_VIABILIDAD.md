# PROTOCOLO 03: PRESUPUESTO Y VIABILIDAD
## Bloque 1 — Gestion del Entorno (ADM)

---

## 1. El Triangulo de Equilibrio

Toda decision de diseno en SOMA debe ser validada por la relacion:

**ESCALA (m2)   CALIDAD (Especificaciones)   INVERSION (Presupuesto)**

---

## 2. Paquetes de Diseno (Escala Oficial SOMA v3.0)

Tres niveles de servicio basados en la profundidad de la informacion tecnica.
**La calidad de diseno es constante en todos los niveles.** Lo que varia es el
alcance de los entregables.

| Paquete | Precio | Entregables |
|---------|--------|-------------|
| **SOMA Esencial** | $250/m2 | Diseno arquitectonico, plantas, alzados, analisis de sitio y normativa, perspectiva de proyecto. |
| **SOMA Integral** | $350/m2 | Esencial + moodboard de acabados, criterio de ingenierias, planos de permiso, perspectivas adicionales. |
| **SOMA Ejecutivo** | $850/m2 | Integral + planos tecnicos ejecutivos, detalles constructivos, coordinacion integral de ingenierias. |

### Reglas de visualizacion en el cotizador (SOLOJUAN 2026-05-15)
- En los entregables **no deben aparecer los precios de los paquetes**.
  Solo los nombres: SOMA ESENCIAL, SOMA INTEGRAL, SOMA EJECUTIVO.
- El precio lo ve el sistema internamente.
- El cliente no debe ver explicaciones tecnicas del cargo minimo.

### Cargo Minimo Operativo
- **$6,500 MXN** — se aplica silenciosamente para proteger la viabilidad de
  proyectos pequenos. El cliente no ve esta regla.

---

## 3. Subsidio Cruzado (Modelo de Negocio)

El nivel **Ejecutivo** y los proyectos de gran escala financian la inclusividad
de los niveles **Esencial** e **Integral**.

El impacto social de resolver bien un espacio pequeno con alta calidad de diseno
es fundamental para la tesis de SOMA. El lujo paga por la democratizacion.

---

## 4. Rangos de Construccion (Terceros, Referencia 2026)

Estimados de ejecucion de obra para calculo de viabilidad.
La construccion la ejecuta un externo, no SOMA.

| Paquete de Diseno | Rango de Obra (m2) |
|-------------------|-------------------|
| SOMA Esencial | $14,000 – $16,500/m2 |
| SOMA Integral | $18,500 – $23,000/m2 |
| SOMA Ejecutivo | $28,000 – $40,000/m2 |

---

## 5. Algoritmo de Validacion (Dashboard)

Para cada lead, el sistema calcula:

1. `m2_teoricos = Presupuesto_Cliente / Costo_Construccion_Elegido`
2. `honorarios_estimados = m2_teoricos * Precio_Paquete_Elegido`
3. `viabilidad = proporcion entre m2_teoricos vs m2_deseados`

---

## 6. Notas de Implementacion

- **Cotizador web:** primer apartado debe ser "Por Programa (Espacios)".
- **Mensaje post-contacto:** "Te damos un estimado parametrico por m2. Nosotros
  disenamos, un constructor externo ejecuta."
- **WhatsApp:** la notificacion llega a Juan via Twilio. El cliente NO abre
  WhatsApp al finalizar — solo se envian datos al servidor.
- **Twilio:** se usara mientras dure el credito gratuito (~$15 USD). Migrar a
  Telegram cuando se agote (gratis 100%).
