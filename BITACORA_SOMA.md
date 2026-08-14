# MEMORIA EVOLUTIVA - SOMA TALLER VIRTUAL DE ARQUITECTURA

## Sesión: 2026-08-13 — Cotizadores BIM y Planos alineados en grid (mismo criterio que el de renders) y botón COTIZADOR SOMA robusto en móvil

### Contexto
Juan pidió aplicar a los cotizadores de BIM y Planos Ejecutivos el mismo criterio ya aplicado al de renders: botones del mismo tamaño, alineados y sin salirse del borde. Además reportó que en su celular (vertical) el botón COTIZADOR SOMA se veía más ancho que la imagen y tardaba en desaparecer al cambiar de servicio.

### Solución implementada
1. **BIM convertido a `.rc-grid-4`** (4 columnas): "Tipo de proyecto" con 4 botones uniformes (VIVIENDA/RESIDENCIAL/COMERCIAL/INDUSTRIAL), luego "Disciplina" (span-2) + "Superficie" (span-2) con el campo (input + m²) en la misma fila de los 2 botones de disciplina.
2. **Planos convertido a `.rc-grid`** (3 columnas) con `.plano-grid` (gap 6px): "Tipo de proyecto" (span-2) + campo Superficie (span-1, `.rc-cell` input 62×22px) en la fila 1; luego 3 botones de tipo; luego "Complejidad del proyecto" (span-3); luego 3 botones de complejidad (SIMPLE/ESTÁNDAR/COMPLEJO con tooltips).
   - Se corrigió un bug del primer armado: faltaba el botón COMERCIAL y el panel excedía el borde (337px vs 290px). Reubicando "Superficie" a la fila 1 y compactando el campo, el panel mide **289px desktop** (dentro de 290) y **292px tablet/móvil** (dentro de 320).
3. **Agrupación por `data-grp`**: `bimSelect` y `planoSelect` ahora usan `data-grp` (como `rcSelect`) para que al hacer clic solo se ilumine el botón de su grupo, independientemente del contenedor.
4. **Botón COTIZADOR SOMA robusto en móvil**: `.sv-caption` con `max-width: 150px; overflow: hidden; transition: none` y `opacity: 0; pointer-events: none` cuando oculto; `.sv-btn` con `max-width: 150px; overflow: hidden; text-overflow: ellipsis` para que el texto nunca desborde los 150px de la imagen. Regla de refuerzo `.services-visual.cotizador-on .sv-caption { visibility: hidden !important }` para ocultado instantáneo. `backdrop-filter` eliminado en breakpoints móviles por lentitud de render en Android.

### Verificación
- Puppeteer en 4 viewports (1366/768/390/480): los 3 cotizadores caben dentro del borde (RENDER 289/292, BIM 282/292, PLANOS 289/292) y los botones son uniformes por grupo (mismo ancho y alto 30px).
- Anchura del botón en 320/360/375/390px: botón 150px = imagen 150px, `scrollWidth=150` (sin desborde aunque JetBrains Mono no cargue), desaparición instantánea (60ms, transition none).

### Archivos creados/modificados
- `web/Pagina Web 6.html` — grids de BIM/Planos, `data-grp` en bimSelect/planoSelect, botón COTIZADOR SOMA robusto, backdrop-filter off en móvil.
- `AGENTS.md` — bitácora de sesión actualizada.
- `BITACORA_SOMA.md` — Esta entrada.

### Pendientes
- Verificar en el celular de Juan el botón COTIZADOR SOMA (ancho y desaparición).
- Revisar el cambio en vivo tras deploy a Render.
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD.
- Lead magnet — decidir ubicación en página web.

---

## Sesión: 2026-08-13 — Sección Servicios pulida: imagen en proporción, botón COTIZADOR SOMA bajo la imagen y sección centrada verticalmente

### Contexto
Juan pidió ajustar la sección de Servicios (04. Alcance y Contacto) para que: la imagen de Diseño Arquitectónico se viera en su proporción original dentro de la rejilla, el botón COTIZADOR SOMA quedara debajo de la imagen, el contacto no se saliera del borde inferior, y los espacios superior e inferior de la sección quedaran equilibrados. También reportó que el borde del contenedor de la imagen se veía blanco semitransparente.

### Solución implementada
1. **Imagen en su proporción original (150×210)**: antes se estiraba a 420×290 (tamaño de los cotizadores). Ahora se centra dentro del contenedor transparente 420×290 (desktop) / 320px alto (móvil), sin cambiar el layout al alternar servicios.
2. **Botón COTIZADOR SOMA dentro de `#services-visual`**: `.sv-caption` pasó a `position: absolute; top: calc(50% + 105px); left: 50%; translateX(-50%)` — queda exactamente pegado debajo de la imagen (`gapImgBtn = 0px`). En los breakpoints móviles la imagen pasó de `height: 100%` (se estiraba a 318px) a `height: 210px` fija para mantener la proporción. Solo se muestra en Diseño (índice 0); en cotizadores queda oculto y no interfiere con el panel.
3. **Borde del contenedor transparente**: `.services-visual` border de `rgba(255,255,255,0.05)` → `transparent`. En cotizadores se mantiene el borde terracota (`border-color: var(--accent)`).
4. **Bloque de servicios compactado y subido**: se eliminó un `<p>` vacío que separaba el título del menú (hueco título→menú pasó de 170px → 15px). Se corrigieron los selectores `.services-wrapper > div > div:last-child` → `.contacto-block` (la regla le daba `margin-top: 45px` y `padding-left: 25px` al `.services-row`, empujando el grid hacia abajo). `.services-row` pasó de `align-items: center` → `start`.
5. **Sección centrada verticalmente**: `section:last-of-type` con `justify-content: center` (desktop y breakpoint móvil `padding: 2vh 4%`), logrando espacios superior e inferior **iguales**: 132px=132px (desktop 1366/1024), 149px=150px (móvil 390×844), 123px=124px (móvil 480×800). El contacto ya no se sale del borde inferior (antes quedaba ~68px fuera).

### Verificación
- Puppeteer en servidor local (`http://127.0.0.1:8080/`): botón centrado y pegado a la imagen (gap 0px) en desktop y móvil; sin solape con el cotizador; contacto cabe con aire abajo en todos los viewports (desktop 242px, móvil 291px tras compactar); después del centrado vertical espacios superior=inferior (132/149/123px).
- Viewports probados: 1366×768, 1024×768, 844×390, 390×844, 480×800, 667×375, 1024×768.

### Archivos creados/modificados
- `web/Pagina Web 6.html` — imagen en proporción, botón COTIZADOR SOMA dentro del contenedor, borde transparente, bloque compactado, sección centrada verticalmente.
- `AGENTS.md` — bitácora de sesión actualizada.
- `BITACORA_SOMA.md` — Esta entrada.

### Pendientes
- Revisar el cambio en vivo tras deploy a Render.
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD.
- Lead magnet — decidir ubicación en página web.

---

## Sesión: 2026-08-13 — Cotizador de renders rediseñado (sin Aéreo, "Nivel de ambientación", tooltips) y sección Servicios estática al cambiar de servicio

### Contexto
Juan pidió rediseñar el cotizador de renders (Visualización): eliminar el botón AÉREO, renombrar "Complejidad" a "Nivel de ambientación" con Básico/Medio/Alto, botones uniformes estilo calculadora y tooltips redefinidos. Además reportó que el menú de servicios y la sección Contacto se desplazaban al alternar entre Diseño Arquitectónico y Visualización.

### Solución implementada
1. **Cotizador de renders**: botón AÉREO eliminado (solo INTERIOR/EXTERIOR). Label "Nivel de ambientación" con botones BÁSICO/MEDIO/ALTO (`data-complejidad` 0.8/1/2.5). `RENDER_PRECIOS = { interior: 2500, exterior: 3000 }`. Botones uniformes que llenan el ancho en fila (tipo 2 columnas, nivel 3 columnas).
2. **Tooltips por tipo** (`RENDER_TIPS` + `actualizarTipsRender()`): al cambiar de interior/exterior se actualizan los tooltips de BÁSICO/MEDIO/ALTO:
   - Interior: "Un ambiente con mobiliario esencial…" / "Ambiente completo, bien amueblado…" / "Interiores ricos en detalles, acabados finos, texturas y vegetación".
   - Exterior: "Fachada o exterior sencillo…" / "Exterior con paisajismo, mobiliario…" / "Exteriores detallados con vegetación abundante…".
3. **Alturas de cotizadores igualadas**: se eliminó el CSS `#render-cotizador .rc-block { flex-direction: column }` (de la prueba anterior) que hacía el panel de renders 60px más alto que BIM/Planos. Los 3 paneles miden ahora **290px** (desktop) y **292px** (móvil).
4. **Contenedor visual de tamaño fijo**: `.services-visual` siempre 420×290px en desktop y 320px de alto en tablet/móvil (ya no 150×210 en imagen vs 420×283 en cotizador). El `.sv-caption` (botón COTIZADOR SOMA) usa `visibility` en vez de `display:none` para reservar su espacio sin provocar salto.
5. **Menú y contacto estáticos**: verificado en 7 viewports (1366×768, 1024×768, 834×1112, 768×1024, 390×844, 844×390, 667×375) — `menuY` y `contactoY` idénticos al alternar entre los 4 servicios, sin errores JS ni overflow horizontal. En landscape (`max-height:520px`) la fila de servicios pasó a `1fr` con visual fijo a 320px.
6. **Móvil**: `.rc-opts.four` ya no se envuelve a 2 columnas (era la causa de que el cotizador BIM midiera 320px vs 282px de renders/planos); se fijó `repeat(4, 1fr)` y min-height de panel 292px.

### Verificación
- JS validado con `new Function` (script 0 OK).
- Puppeteer en servidor local: tooltips cambian interior↔exterior; totales correctos (Interior $2,500, Interior+Alto $6,250, Exterior $3,000). Altura de los 3 cotizadores 290px desktop / 292px móvil.
- Estabilidad del menú y contacto confirmada en 7 viewports (sin saltos al alternar servicios).

### Archivos creados/modificados
- `web/Pagina Web 6.html` — rediseño del cotizador de renders (HTML+JS+CSS), contenedor visual de tamaño fijo, breakpoints móvil/landscape ajustados.
- `BITACORA_SOMA.md` — Esta entrada.

### Pendientes
- Revisar el cambio en vivo tras deploy a Render.
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Lead magnet — decidir ubicación en página web

---

## Sesión: 2026-08-13 — Ajustes de cotizadores a medio camino: regla BIM LOD 300 alineada a m², copy unificado a "renders", limpieza de imágenes de servicios

### Contexto
Juan reportó que varios ajustes de los cotizadores de la sección Servicios quedaron a medio camino. Se auditaron los 3 cotizadores contra la documentación (AGENTS/SNAPSHOT) y se encontraron inconsistencias.

### Hallazgos y solución
1. **Cotizador BIM LOD 300 (la más grave)**: el código `calcBim()` aplicaba descuentos por honorarios totales (>$40,000 −5%, >$80,000 −10%) con tarifa mínima $9,000, pero la decisión documentada del 11 Ago era por superficie (>500 m² −5%, >1,000 m² −10%) con mínimo **$12,000**. Corregido:
   - `calcBim()` ahora aplica `m2 > 1000 → ×0.9`, `m2 > 500 → ×0.95`, mínimo `12000`.
   - Default del HTML `#bimTotal` pasó de `$9,000` a `$12,000`.
   - Hint de términos actualizado: "Descuento por superficie: >500 m² −5% · >1,000 m² −10%. Tarifa mínima $12,000 MXN."
2. **Copy D5 unificado a "renders"** (cambios sin commitear de sesión previa, ahora completos y consistentes):
   - h3: "COTIZADOR D5" → **"COTIZADOR DE RENDERS"**; subtítulo "Render arquitectónico — precios MXN por imagen".
   - Complejidad: se eliminó la opción "Integrado" (×1.65); queda **Básico ×0.8 / Medio ×1.0 / Cargado ×2.5**. El label pasó de "Tipo de vista" a "Tipo de render".
   - "Cantidad de vistas / uds" → "Número de renders / rnds"; tiempos y paquetes en términos reescritos de "vistas" a "renders".
   - `RENDER_COMPLEJIDAD_NOMBRE` actualizado a `{0.8: 'Básico', 1: 'Medio', 2.5: 'Cargado'}`.
3. **Imágenes de servicios**: por indicación de Juan, solo la imagen de **Diseño Arquitectónico** es útil; Visualización, Modelado BIM y Planos fueron reemplazadas por los cotizadores. Se eliminaron las 3 `<img>` restantes del HTML (los archivos quedan en disco). `changeService()` sigue funcionando porque solo usa `images[index]` para index 0.
4. **Documentación sincronizada**: AGENTS.md, SOMA_SNAPSHOT.md y SOMA_CORE_INDEX.md actualizados (se quitaron referencias a ×1.65/"Integrado"/"por vista" y se reflejó la regla m² del BIM).

### Verificación
- JS del HTML validado con `new Function` (script 0 OK).
- Pruebas funcionales con Puppeteer en servidor local: BIM default **$12,000**, 600 m² → **$51,300** (90×600×0.95), 1,500 m² → **$121,500** (90×1500×0.9); D5 default **$2,500**, Cargado → **$6,250**; Planos default **$13,000**, 400 m² → **$49,400** (130×400×0.95). Sin errores JS, overflow horizontal 0 en desktop y móvil (390×844, 844×390).

### Archivos creados/modificados
- `web/Pagina Web 6.html` — regla BIM m², copy D5 a renders, eliminadas 3 imágenes de servicios.
- `AGENTS.md`, `SOMA_SNAPSHOT.md`, `SOMA_CORE_INDEX.md` — Documentación alineada.
- `BITACORA_SOMA.md` — Esta entrada.

### Pendientes
- Revisar el cambio en vivo tras deploy a Render.
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Lead magnet — decidir ubicación en página web

---

## Sesión: 2026-08-11 — Revisión en vivo de formatos: rectángulos de cotizadores unificados, sección contacto con aire, fix desborde vertical y deploy a Render

### Contexto
Tras revisar en vivo los 3 cotizadores de la sección Servicios, cada panel tenía un ancho distinto en desktop (causado por la columna `auto` del grid: D5 316px, BIM 388px, Planos 342px), los campos se veían apiñados y el bloque de contacto quedaba pegado a los cotizadores. En pantallas verticales cortas, además, el contacto se salía del fondo naranja y aparecía una franja negra debajo.

### Solución implementada
1. **Rectángulos de cotizadores unificados en desktop**: `.services-visual.cotizador-on { max-width: 440px; min-width: 420px; height: auto; }` → los 3 paneles miden ahora **418-419×281px** idénticos (antes D5 316, BIM 388, Planos 342). En móviles se resetea `min-width: 0` para no forzar 420px.
2. **Más aire dentro de cada panel**: padding del panel 16×18px, gap del cuerpo 12px, entre bloque y bloque 12px, entre opciones 8px, botones de opción más holgados (7×10px), inputs y botón "VER COTIZACIÓN" con más espaciado. Arregla el D5 "achocado", los campos pegados del BIM y los botones juntos de Planos.
3. **Sección contacto bajada**: `margin-top` del bloque de contacto subió a 45px en desktop (40px en tablet, ajustado en landscape). El último texto queda con aire hasta el borde inferior de la sección en todos los formatos.
4. **Fix desborde vertical (franja negra)**: conflicto de especificidad CSS — la regla base `section:last-of-type { height: 100vh }` (0,1,1) vencía a `section { height: auto }` (0,0,1) del media query `≤768px`, dejando la sección naranja clavada en 100vh y el contacto desbordando sobre el fondo negro. Se cambió el media query a `section, section:last-of-type { min-height: 100vh; height: auto; }` para igualar especificidad.
5. **Landscape compactado**: padding del cotizador reducido dentro de `max-height:520px` (10×12px, gaps menores) para que la sección vuelva a caber en 100vh (movil_h: sección 390px, contacto bottom 378; movil_h_small: 380/375).
6. **Deploy a Render**: commit `b2a0d43` pusheado a `main` (6 archivos). Verificado en línea: HTML con corrección `section:last-of-type` y cotizadores presentes, endpoint `POST /cotizar_planos` respondiendo (`email: sent`).

### Verificación
- Capturas en `recursos_graficos/_revision_formatos/`: `laptop_cotizador_{d5,bim,planos}.png`, `movil_v_sec4_{diseno,visual,bim,planos}.png` y capturas de todos los formatos (desktop 1366×768, tablet 768×1024, móvil vertical 390×844, horizontal 844×390 y 667×375).
- Barrido de tamaños verticales (320×568 a 414×896): **todos sin desborde** — la sección ahora crece con su contenido. Caso crítico 320×568: sección 592-625px (crece) y contacto dentro del fondo naranja.
- Overflow horizontal 0px y sin errores JS en laptop, tablet, movil_v, movil_h, movil_h_small. Test funcional (portafolio, filosofía, slider, cotizador D5) pasando.

### Archivos creados/modificados
- `web/Pagina Web 6.html` — rectángulos de cotizadores unificados, espaciado interno, sección contacto con aire, fix `section:last-of-type` en media query `≤768px`, landscape compactado.
- `AGENTS.md`, `BITACORA_SOMA.md`, `SOMA_SNAPSHOT.md`, `SOMA_CORE_INDEX.md` — Actualizados.
- Commit `b2a0d43` desplegado a Render (soma-853c.onrender.com).

### Pendientes
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD.
- Lead magnet — decidir ubicación en página web.
- Definir tiempos de entrega formales en `TIEMPOS_ENTREGA_BASE.md` para proyectos SOMA completos (los cotizadores ya muestran referencia de mercado).

---

## Sesión: 2026-08-11 — Cotizador Planos Ejecutivos Arquitectónicos (actividades y precios definidos)

### Contexto
Se agregó un tercer mini-cotizador a la sección Servicios: **Planos Ejecutivos Arquitectónicos**, para completar la oferta de servicios técnicos. Antes de implementarlo se validaron los rangos de precios contra fuentes de mercado 2026 (Arqbeat, Ernesto Resendiz, Arqzon, PE BIM, Cronoshare Mérida, Habitissimo Mérida). **Por decisión de Juan se excluye industrial/naves industriales.**

### Solución implementada
1. **Nuevo servicio** "PLANOS EJECUTIVOS" en index 3 de `changeService` (reemplaza a "PLANOS DE ANTEPROYECTO", que se eliminó de la lista).
2. **Precios base por m²** (rango bajo del mercado, validado):
   - Vivienda **$130** · Residencia **$160** · Comercial **$190**. **Sin industrial** (decisión de Juan).
3. **Complejidad de acabados**: Básico ×0.85 · Estándar ×1.0 · Alto ×1.6 (carpinterías a medida, cancelería, detalles finos).
4. **Reglas**: descuentos >300 m² −5%, >600 m² −10%. Tarifa mínima **$10,000 MXN**. Precios + IVA.
5. **Entregables**: planos en **PDF y DWG** (plantas de conjunto y por nivel, cortes, fachadas, acabados, carpinterías/cancelería, detalles constructivos, especificaciones). 2 rondas de revisiones.
6. **Tiempos (referencia de mercado)**: 3-4 semanas ≤300 m² · 4-6 semanas 300-600 m² · 6-8 semanas >600 m². Compromiso real en entrevista de alcance.
7. **Esquema de pago dinámico**: 50/50 < $15,000; 30/40/30 ≥ $15,000 (consistente con D5 y BIM).
8. **Nuevo endpoint público `POST /cotizar_planos`** (espejo de `/cotizar_bim`, `public_paths` actualizado).

### Verificación
- Sintaxis `server.py` validada (`ast.parse` OK) y JS del HTML validado (`new Function` OK).
- Cálculos probados: Vivienda 100 m² Estándar $13,000 · Básico $11,050 · Alto $20,800 · mínimo 60 m² → $10,000 · Comercial 400 m² → $72,200 (−5%) · Residencia 700 m² → $100,800 (−10%).

### Archivos creados/modificados
- `web/Pagina Web 6.html` — cotizador Planos Ejecutivos (HTML+JS), `changeService` index 3 (reemplaza "PLANOS DE ANTEPROYECTO"), tiempos de mercado, pago dinámico, "+ IVA", entregables PDF+DWG.
- `backend/server.py` — endpoint `POST /cotizar_planos` + `public_paths`.
- `AGENTS.md`, `BITACORA_SOMA.md`, `SOMA_SNAPSHOT.md`, `SOMA_CORE_INDEX.md` — Actualizados.

### Pendientes
- Revisar los 3 cotizadores en vivo y pulir copy de Servicios.
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Lead magnet — decidir ubicación en página web

---

## Sesión: 2026-08-11 — Cotizadores D5 + BIM LOD 300 en web (actividades y precios definidos)

### Contexto
Se continuó con la web: se terminó el cotizador D5 (perspectivas) iniciado el 07/08 y se creó un segundo cotizador para el servicio de Modelado BIM LOD 300. Se definieron formalmente actividades, precios, tiempos de entrega (con referencia de mercado) y esquemas de pago, tras un análisis crítico de las versiones iniciales.

### Solución implementada
1. **Cotizador D5 completado** (botón "VER COTIZACIÓN"):
   - Validación de contacto real: correo con formato válido o teléfono con ≥10 dígitos.
   - Precio oculto hasta presionar el botón; muestra total + IVA.
   - `POST /cotizar_perspectivas` → correo a `habitarq85@gmail.com` vía Brevo (endpoint ya existía).
2. **Nuevo cotizador BIM LOD 300** (`#bim-cotizador`, index 2 en `changeService`):
   - Precios base por m² (rango bajo del mercado): Vivienda **$90**, Residencial **$110**, Comercial **$130**, Industrial **$150**.
   - Disciplinas: **solo Arquitectura y Estructura, mismo precio, sin MEP** (decisión de Juan).
   - Descuentos: >500 m² −5%, >1,000 m² −10%. Tarifa mínima **$12,000 MXN**.
   - Entregable: **solo archivo Revit (RVT)**.
   - Nuevo endpoint público `POST /cotizar_bim` (espejo de `/cotizar_perspectivas`, `public_paths` actualizado).
3. **Análisis crítico de los cotizadores** (formas de pago y tiempos) con investigación de mercado 2026:
   - Renders MX: interior 3-5 días, exterior 5-10 días, paquete desarrollo 2-4 semanas (Carnet 3D, myarchitectai).
   - BIM LOD 300: <1,000 m² 2-3 semanas, 1,000-3,000 m² 3-4 semanas, >3,000 m² 4-6 semanas; scan-to-BIM referencia 3-18 días hábiles según tamaño (ENGINYRING), modelo desde cero 2-4 semanas (Arrival 3D).
   - Decisiones de Juan: el cotizador es **referencia**; el plazo definitivo se compromete en la **entrevista de alcance**.
4. **Cambios aplicados a ambos cotizadores**:
   - **Tiempos de entrega** actualizados a referencia de mercado (ver arriba), con leyenda de que el compromiso real se confirma tras la entrevista.
   - **Esquema de pago dinámico**: 50/50 si total < $15,000; 30/40/30 si ≥ $15,000 (umbral definido por Juan). Solo transferencia.
   - **IVA explícito**: los totales muestran "+ IVA" (se quitó el ambiguo "No incluye IVA").

### Verificación
- `POST /cotizar_bim` probado localmente → `email: sent`, reporte correcto en `backend/reportes/`.
- Sintaxis de `server.py` validada y servidor reiniciado (`soma-flask`), `/health` → ok.
- Selectores HTML/JS verificados (bimSelect, calcBim, verCotizacionBim, PagoScheme).

### Archivos creados/modificados
- `web/Pagina Web 6.html` — cotizador BIM LOD 300 (HTML+JS), `changeService` index 2, tiempos de mercado, esquema de pago dinámico, "+ IVA", entregable solo RVT.
- `backend/server.py` — endpoint `POST /cotizar_bim` + `public_paths`.
- `AGENTS.md`, `BITACORA_SOMA.md`, `SOMA_SNAPSHOT.md`, `SOMA_CORE_INDEX.md` — Actualizados.

### Pendientes
- Continuar con la web: revisar cotizadores en vivo y pulir copy de Servicios.
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Crear tabla `algoritmo_contenido` para outputs de cada estación
- Lead magnet — decidir ubicación en página web

---

## Sesión: 2026-08-05 (noche) — Monitoreo de salud: endpoint /health + alertas por correo

### Contexto
Tras varias "sorpresas" del free tier (Supabase pausada, Render, SendGrid sin créditos, sender no verificado), se implementó monitoreo preventivo para detectar fallas en minutos, no en días.

### Solución implementada
1. **Endpoint `GET /health`** (público) en `server.py` — chequea y reporta:
   - `server`: el proceso Flask responde
   - `db`: `SELECT 1` real + `db_backend` indica si usa PostgreSQL (Supabase) o SQLite (fallback)
   - `brevo`: `GET /v3/account` para confirmar que el correo puede enviar
   - Devuelve `status: ok` o `degraded` con el detalle de qué falló.
2. **Endpoint `POST /health/alert`** (público, con rate-limit) — envía correo de alerta a `habitarq85@gmail.com` vía Brevo. Throttle de 30 min por componente (`_ALERT_STATE`) para no spamear.
3. **Worker keep-warm actualizado** (`workers/keep-warm/src/index.js`):
   - Mantiene su función de keep-warm (Render + `/keepwarm`)
   - Cada 5 min consulta `/health`
   - Si un componente falla → `POST /health/alert` (una vez cada 30 min, estado en Cache API)
   - Si un componente se recupera → limpia el estado de alerta
   - Endpoints manuales: `__ping` y `__health` (proxy al health de Render)

### Verificación
- Local: `/health` → `status: ok`, alerta enviada y throttled correctamente
- Online: Render `/health` → `status: ok`; worker `__health` → JSON de salud OK
- Alerta de prueba → `event: delivered` en Brevo

### Archivos creados/modificados
- `backend/server.py` — `/health`, `/health/alert`, import `_use_postgres` y `time`
- `workers/keep-warm/src/index.js` — health check + alertas + Cache API
- `AGENTS.md`, `BITACORA_SOMA.md` — Actualizados

### Pendientes
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Crear tabla `algoritmo_contenido` para outputs de cada estación
- Lead magnet — decidir ubicación en página web

---

## Sesión: 2026-08-05 — Correo Brevo: sender no verificado (el correo no llegaba aunque no había error)

### Diagnóstico
- Después de migrar a Brevo (04/08), el correo del cotizador seguía sin llegar: la web respondía sin error (`email: sent`) pero `habitarq85@gmail.com` no recibía nada.
- **Causa raíz encontrada:** el sender `info@soma-arquitectura.com` **NO estaba verificado** en Brevo. Brevo acepta la petición (status 201) pero **descarta silenciosamente** el correo en su cola (`event: error` — "sender not valid"). Por eso no aparecía ningún error en la página.
- Confirmado consultando `GET /v3/smtp/statistics/events`: los envíos con `info@` daban `event: error`, los de `habitarq85@gmail.com` (único sender activo) daban `event: delivered`.

### Soluciones aplicadas
1. **Dominio autenticado en Brevo:** registrado `soma-arquitectura.com` (id `6a72ab58668a28afd40c4697`) y añadidos en Cloudflare los 4 registros DNS:
   - CNAME `brevo1._domainkey` → `b1.soma-arquitectura-com.dkim.brevo.com`
   - CNAME `brevo2._domainkey` → `b2.soma-arquitectura-com.dkim.brevo.com`
   - TXT `@` → `brevo-code:2bf45070a3e8ed77548a4fb34e7577d0`
   - TXT `_dmarc` → `v=DMARC1; p=none; rua=mailto:rua@dmarc.brevo.com`
   - SPF actualizado a `v=spf1 include:_spf.mx.cloudflare.net include:spf.brevo.com ~all`
2. **Sender creado y verificado:** `POST /v3/senders` creó `info@soma-arquitectura.com` (id 2) y se validó con el código OTP de 6 dígitos que Brevo envió por email (`PUT /v3/senders/2/validate` → 204). El sender quedó `active: true`.
3. **Verificación final:** envío real desde Render (`SOMA-05082026-0352`) → `event: delivered`. Lead de prueba eliminado de Supabase (id 30).
4. **Nota:** los registros DNS individuales marcaron `status: true` casi de inmediato, pero el dominio tardó más en quedar `authenticated`. La vía rápida fue la verificación del sender por OTP.

### Archivos creados/modificados
- `AGENTS.md`, `BITACORA_SOMA.md` — Actualizados
- `render.yaml` — Pendiente limpiar SMTP/SendGrid obsoletos (no afecta al código, ya solo usa BREVO_API_KEY)

### Pendientes
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Crear tabla `algoritmo_contenido` para outputs de cada estación
- Lead magnet — decidir ubicación en página web

---

## Sesión: 2026-08-04 — Correo del Cotizador: SendGrid → Brevo (SendGrid sin créditos, Gmail SMTP bloqueado por Render)

### Diagnóstico
- El envío de correo del cotizador (`/save_immersion`) fallaba online. El lead sí se guardaba en BD, solo fallaba el correo de notificación a `habitarq85@gmail.com`.
- Causa 1: la cuenta **SendGrid gratis se quedó sin créditos** → `401 Maximum credits exceeded` (`remain: 0`, `is_hard_limit: true`).
- Causa 2 (al intentar Gmail SMTP): **Render NO puede alcanzar los puertos SMTP de Gmail** (587 STARTTLS y 465 SSL ambos dan `timed out` desde Render).

### Lección aprendida (CRÍTICA — ya nos había pasado antes)
- **Render free no enruta ciertos protocolos/IPs de datacenter.** Antes falló con IPv6 de Supabase (`Network is unreachable`) y ahora con SMTP de Gmail (`timed out` en puertos 587/465).
- **Regla para servicios externos desde Render:** usar SIEMPRE APIs por **HTTPS (puerto 443)** — es lo único garantizado alcanzable. Ejemplos que SÍ funcionaron: SendGrid API, Supabase pooler IPv4, Brevo API.
- **Regla para SMTP:** Gmail SMTP (`smtp.gmail.com`) resuelve a IPv6 primero y Gmail ralentiza/bloquea IPs de datacenter → no usar SMTP directo desde Render. Preferir API por HTTPS.

### Soluciones aplicadas
1. **Verificación:** `GET /v3/scopes` de SendGrid confirmó key válida; `GET /v3/verified_senders` mostró `verified: false`; `GET /v3/user/credits` mostró `total: 0`. El dominio `soma-arquitectura.com` sí estaba autenticado (DKIM/SPF válido), el problema era solo saldo.
2. **Código:** `backend/server.py` — `enviar_correo()` reescrito de SendGrid a SMTP (`smtplib`), luego reforzado con conexión forzada IPv4 y fallback 587/465. Verificado que ambos tiempos de espera agotan desde Render.
3. **Email público `info@soma-arquitectura.com`:** NO se tocó — sigue gestionado por Cloudflare Email Routing (MX = `mx.cloudflare.net`) y reenvía a `habitarq85@gmail.com`. Es independiente del sistema de notificaciones.
4. **SOLUCIÓN FINAL — Brevo API:** `enviar_correo()` usa `POST https://api.brevo.com/v3/smtp/email` por HTTPS (443), con `urllib` (sin dependencias nuevas). Remitente `info@soma-arquitectura.com` verificado por clic. Cuenta free: 300 correos/día (se reinicia diario, no hay créditos de por vida como SendGrid).
5. **Verificado online:** `/notificaciones/status` → `conectado: true`. Envío real desde Render → `email: sent`. Lead de prueba borrado de Supabase (id 27); se conservaron leads reales de hoy.

### Archivos creados/modificados
- `backend/server.py` — `enviar_correo()` vía Brevo API + `/notificaciones/status` (GET `/v3/account`). Eliminados `_smtp_connect()`, SMTP y SendGrid.
- `.env` — `BREVO_API_KEY` configurada; SMTP app password y `SENDGRID_API_KEY` eliminadas
- `.env.example` — actualizado con `BREVO_API_KEY`
- `AGENTS.md`, `BITACORA_SOMA.md` — Actualizados

### Pendientes
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Crear tabla `algoritmo_contenido` para outputs de cada estación
- Lead magnet — decidir ubicación en página web

---

## Sesión: 2026-07-21 — Supabase Paused + Fallback Local + Keepwarm

### Diagnóstico
- El proyecto de Supabase (`dejojumyyydrlqoegqnf`) fue pausado por inactividad. Dashboard y algoritmo en Render no leían datos.
- Causa: el worker keep-warm pingueaba solo el API REST de Supabase, no la BD directamente — Supabase mide inactividad a nivel de PostgreSQL, no de hits HTTP.

### Soluciones aplicadas
1. **Reactivación:** Juan resumió el proyecto desde el dashboard de Supabase. Datos intactos (3 leads, 17 programa_arquitectonico, 24 algoritmo_progreso, 6 matriz_inversion, 5 egresos, 2 fondos, 3 movimientos_fondo).
2. **Keep-warm real:** Se agregó endpoint público `/keepwarm` en `server.py` que ejecuta `SELECT 1` en la BD. Worker actualizado para pinguear este endpoint en vez del API de Supabase.
3. **Backup local:** `backend/backup_pg_to_sqlite.py` — exporta todas las tablas de Supabase → SQLite local en `web/EjemploBD/proyectos_arquitectonicos.db` y backups con timestamp en `antecedentes/backups_sqlite/`.
4. **Fallback automático:** `db.py` modificado — si PostgreSQL falla, usa SQLite local automáticamente. No requiere cambios de configuración.
5. **Cron diario:** Backup automático cada 12pm (mediodía).

### Archivos creados/modificados
- `backend/backup_pg_to_sqlite.py` — Nuevo (backup Supabase→SQLite)
- `backend/db.py` — Modificado (fallback automático PG→SQLite)
- `backend/server.py` — Modificado (endpoint `/keepwarm` público)
- `workers/keep-warm/src/index.js` — Modificado (ping a `/keepwarm` con query SQL)
- `.env` — DATABASE_URL re-activado
- `AGENTS.md`, `BITACORA_SOMA.md`, `SOMA_CORE_INDEX.md`, `SOMA_SNAPSHOT.md` — Actualizados

### Pendientes
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Crear tabla `algoritmo_contenido` para outputs de cada estación
- Lead magnet — decidir ubicación en página web

---

## [Evolución de la Visión]
El proyecto nace de la necesidad de democratizar la arquitectura de alta calidad. La tesis central es: **"Lo protocolario se programa, lo creativo se libera"**. SOMA no busca repetir edificios, sino repetir la excelencia mediante procesos industrializados para resultados artesanales y únicos. 

---

## [Módulo 1: La Inteligencia del Negocio (Efecto de Red)]
SOMA se establece como un modelo **AaaP (Architecture as a Product)**. 
- **La Idea:** Utilizar proyectos de alto nivel para financiar el desarrollo tecnológico. 
- **La Integración:** Cada proyecto no es un fin en sí mismo, sino un donante de datos. El "Lujo" financia la "Eficiencia", permitiendo que en el futuro los estratos sociales bajos accedan a un diseño optimizado que no dependa de licencias costosas (transición a Blender/Open Source).

---

## [Módulo 2: El Sistema de Captura y el Objeto Usuario]
Hemos pasado de una "entrevista improvisada" a una **Ingeniería de Requerimientos**. 
- **El Hallazgo:** El usuario no es un cliente, es un "Objeto Complejo" en Programación Orientada a Objetos.
- **Protocolización:** Se divide la captura en tres filtros:
    1. **Pre-filtro Digital (Web):** Codificación visual de atmósfera, materialidad y presupuesto. Es pragmático para celulares.
    2. **Entrevista de Inmersión:** Extracción del "Mensaje Creativo" y "Complementos No Evidentes" (hábitos, miedos, aspiraciones poéticas).
    3. **Procesamiento IA:** El puente que une los deseos humanos con los parámetros técnicos de Revit/Blender.

---

## [Módulo 3: Lógica Algorítmica de las Preguntas]
Cada pregunta del Pre-filtro Web tiene un "Dato Semilla" vinculado:
- **Luz vs Sombra:** Inyecta parámetros al modelo de análisis bioclimático.
- **Apertura vs Privacidad:** Define la tipología de la planta (Introvertida vs. Extrovertida).
- **Inversión:** Establece el techo de la "Red de Relaciones" entre materialidad y escala.

---

## [Módulo 4: Estética como Fundamento (Dashboard Editorial)]
Se determinó que la estética no es un adorno, sino parte del protocolo. 
- **La Idea:** La documentación de SOMA debe ser una revista de diseño. 
- **La Integración:** El uso de HTML/CSS con tipografías serif (*Playfair Display*) y técnicas (*JetBrains Mono*) refleja el equilibrio entre la poesía y el código.

---

## [Próximos Hitos en Desarrollo]
1. **Protocolo 02 (Ambiente):** Investigación automatizada de condicionales de sitio.
2. **Esquematización IA:** Cómo la red de relaciones genera los primeros volúmenes.
3. **Persistencia de Datos:** Conexión del Front-end (Web) con el Back-end (Protocolos).

## [Módulo 5: Evolución de la Captura V2]
Se han integrado 10 ejes de decisión técnica camuflados en comparativas visuales:
1. **Privacidad:** Relación Fachada/Calle.
2. **Jerarquía:** El ritual del acceso.
3. **Legibilidad:** Fluidez vs. Compartimentación.
4. **Flexibilidad:** Adaptabilidad temporal del espacio.
5. **Encuadre:** Control de vanos.
6. **Tectónica:** Visibilidad estructural.
7. **Ocupación:** Huella en el terreno (COS).
8. **Cinemática:** Geometría del recorrido.
9. **Volumetría:** Proporción de la sección.
10. **Conectividad:** Relación interior/exterior total.

---

## [Perfil del Fundador]

- **Experiencia:** Arquitecto (UADY) con Maestría en Tecnología (UNAM). 6 años en Duarte Aznar (Diseño/Visualización).
- **Hardware:** PC Gamer y Laptop Ideapad.
- **Contexto:** Solo-Founder — la automatización es vital para la escala.

---

## [Ciclo de 10 Etapas del Taller SOMA]

El proceso de diseño completo que SOMA debe cubrir:

1. **Recepción:** Captura de datos de usuario (Web + Llamada/Entrevista).
2. **Investigación:** Sitio, Normativa, Contexto y Realidad.
3. **Análisis:** Premisas automáticas, Programa Evolucionado y Grafos de Relación.
4. **Conceptualización:** CreativeCore y moldeado (Protocolo de Modelado).
5. **Visualización:** Estilo mecánico/sistemático. La arquitectura comunica el mensaje.
6. **Representación Integral:** Dossier editorial elegante y estandarizado.
7. **Evaluación:** Auditoría de Indicadores de Habitabilidad (Térmica, Acústica, etc.).
8. **Anteproyecto:** Ajuste fino basado en la evaluación.
9. **Planos Técnicos:** Documentación automatizada (Protocolo POO).
10. **Coordinación:** Gestión con especialistas externos.

*Nota: Actualmente existen protocolos para las etapas 1–3 (Recepción, Investigación, Análisis). Las etapas 4–10 están pendientes de protocolizar.*

---

## Sesión: 2026-05-06 (Integración de Datos y Protocolo de Inmersión)

### 12. Logros de la Sesión
- **Redefinición de Pendientes:** Foco en Backend de datos, Protocolo de Entrevista y Presupuesto.
- **Evolución del Pre-filtro Web:** Cambio de la pregunta de "Cocina" por "Cromatismo" y actualización del JS para captura de respuestas A/B.
- **Arquitectura de Persistencia:** 
    - Creación de tabla `captura_web` en `proyectos_arquitectonicos.db` para leads temporales.
    - Servidor Flask (`server.py`) operativo con motor de traducción de datos a directrices de diseño.
    - Entorno virtual (`venv`) configurado para ejecución segura.
- **Protocolo de Entrevista Presencial:** 
    - Creación de `PROTOCOLO_02_ENTREVISTA_INMERSION_PROFUNDA.md`.
    - Desarrollo de `Entrevista_Guion.html`: Herramienta interactiva casual y técnica dividida en 5 pilares: Perfil (incluye mapa de usuarios), Características, Comportamientos, Necesidades e Inversión, y Cierre (Proceso y Certezas Administrativas).

### 13. Punto de Partida para la Siguiente Sesión
1. **Pruebas de Campo:** Ejecutar el flujo completo desde Web -> Backend -> DB.
2. **Protocolo 03 (Presupuesto):** Definir la lógica de desglose financiero y equilibrio Escala vs. Calidad.
3. **Módulo de Análisis de Sitio:** Protocolizar la investigación técnica del terreno (Vientos, Asoleamiento, Normativa).

---
## Sesión: 2026-05-07 (Protocolos de Viabilidad y Análisis de Sitio)

### 14. Logros de la Sesión
- **Protocolización Financiera:** Creación de `PROTOCOLO_03_PRESUPUESTO_Y_VIABILIDAD.md` definiendo el triángulo de equilibrio (Escala, Calidad, Inversión) y paramétricos 2026.
- **Protocolización de Sitio:** Creación de `PROTOCOLO_04_ANALISIS_SITIO.md` integrando análisis bioclimático (específico para Mérida), normativa (COS/CUS) y Genius Loci.
- **Verificación de Sistemas:** 
    - Test exitoso del flujo de datos: Web -> Backend (Flask) -> SQLite.
    - Confirmación de persistencia de leads en la tabla `captura_web`.

### 15. Punto de Partida para la Siguiente Sesión
1. **Esquematización Automática (V1):** Definir cómo los datos de la inmersión y el sitio se traducen en volúmenes básicos (Bounding Box).
2. **Dashboard de Gestión:** Crear una interfaz simple para que el arquitecto visualice los leads y sus análisis procesados.
3. **Refinamiento de Algoritmos:** Mejorar el "Traductor" en `server.py` para incluir sugerencias de m² basadas en el presupuesto.

---
## Sesión: 2026-05-08 (Arquitectura Emergente e Integración Sistémica)

### 16. Logros de la Sesión
- **Evolución Filosófica:** Redefinición de SOMA como un sistema de *Surgimiento de Complejidad* (Adiós al concepto de "Producto"). Tesis central: "Lo sublime para todos" (Lujo financia Eficiencia).
- **Consolidación del Bloque 1 (Adm):** 
    - Definición de 3 niveles de Inversión en el Surgimiento (Anteproyecto Básico, Integral, Ejecutivo).
    - Establecimiento de precios de lanzamiento ponderados por nivel de Maestría y experiencia.
    - Clarificación de alcances: Criterios SOMA (incluidos) vs. Cálculos Especializados (externos).
- **Desarrollo del Bloque 3 (I+D):**
    - Backend: Implementación de endpoint `/get_leads` para lectura de datos persistentes.
    - Dashboard: Creación de la Consola de Leads dinámica con calculadora de viabilidad y honorarios integrada.
- **Estructura de Control:** Creación de `SOMA_CORE_INDEX.md` y actualización del Mapa Visual para gestión por bloques.

### 17. Punto de Partida para la Siguiente Sesión
1. **Protocolo 04 (Sitio):** Desarrollo de la matriz de análisis bioclimático y normativo como patrones de entrada.
2. **Evolución del Traductor:** Integrar la lógica de "Lo Sublime" en la generación de principios rectores de diseño.
3. **Consolidación Administrativa:** Formatos de ingresos y organización de carpetas de proyecto (Bloque 1).

---

## Sesión: 2026-05-11 (Corrección de Rumbo y Registro de Fallos)

### 18. Observaciones Críticas Detectadas

- **Pérdida de Integridad:** El dashboard se convirtió en una herramienta cosmética, ignorando procesos profundos del Bloque 02 (UserEntity, ActivityMatrix). ⚠️ En Corrección.
- **Complacencia del Agente:** El asistente AI estaba aceptando decisiones sin análisis crítico, convirtiéndose en un riesgo para la precisión del sistema. ✅ Mitigado.
- **Desconexión de Datos:** El esquema actual de SQLite no soportaba la complejidad de los protocolos 01 y 02. ✅ Corregido.
- **Decisión:** Se decide priorizar la estructura de datos sobre la interfaz visual. Se crea `SOMA_LOG.md` para evitar pérdida de información valiosa.

### 19. Notas de Sesión

- Se estableció el sistema de lo general a lo particular.
- Se definió que la visualización no debe ser un cuello de botella artístico, sino un proceso mecánico/sistemático.
- Se identificó la Etapa 4 (Modelado) como el punto crítico para que la automatización técnica funcione.

---

## Sesión: 2026-05-12 (Implementación de Estructura Relacional)

### 20. Logros de la Sesión

- **Estructura Relacional en DB:** Se implementaron tablas para `Habitantes`, `Actividades` y `Ejes de Diseño`, resolviendo la desconexión de datos detectada el 11/05.

---

## Sesión: 2026-05-13 (Evolución Académica y Captura Proactiva)

### 21. Logros de la Sesión (Continuación Tarde)
- **Infraestructura de Inmersión:** Actualización del backend con 10 ejes de diseño y matriz de 24 slots operativos.
- **Implementación de Multimedia de Autor:**
    - Se sustituyó el video de portada por una **Playlist Cinematográfica** de 4 videos en bucle (`Video_Fondo`).
    - El carrusel de proyectos ahora utiliza renders reales de autor con nombres sincronizados.
- **Perfeccionamiento Estético y Proporcional:**
    - Se restauró el **ritmo visual variado** del carrusel original (mezcla de formatos).
    - Se implementó el respeto estricto a las **proporciones nativas** de cada imagen, incluyendo una clase especial para el ratio 1.79 de *Casona Cristi*.
- **Interactividad Avanzada en Portafolio:**
    - Se desarrolló el sistema de **Inyección Dinámica de Imágenes** para el carrusel vertical del modal. Cada proyecto ahora carga sus propios interiores y detalles al ser seleccionado.
- **Lanzamiento de Aplicación de Inmersión (Bloque 3):**
    - Se creó la estructura base en `aplicaciones_python/app_inmersion/` (Flask + Recorder JS) para grabaciones de audio en sitio y seguimiento de tópicos deslizables basados en `Entrevista_Guion.html`.

---
## Sesión: 2026-05-14 (Consolidación del Motor de Taller)

### 22. Logros de la Sesión
- **Evolución del Cotizador:**
    - Se eliminó el sesgo de "Producto" para reforzar la identidad de **Taller de Diseño**.
    - Implementación de **Honorarios por Alcance de Información** (Básico $250, Integral $450, Ejecutivo $1,000).
    - Establecimiento de un **Cargo Mínimo Operativo de $8,000** (oculto al usuario) para proteger la viabilidad de proyectos pequeños.
    - Sincronización de **Rangos de Construcción (Terceros)** vinculados al paquete de diseño.
- **Identidad y Narrativa:**
    - Neutralización del lenguaje: de "Casa" a "Proyecto/Objeto Arquitectónico".
    - Refinamiento de la Inmersión: preguntas enfocadas en la experiencia del habitar y la interacción espacial.
- **Arquitectura de Datos (Cerebro SOMA):**
    - Definición de la **Zonificación Maestra SOMA**:
        1. **Social** (Interacción/Público)
        2. **Descanso** (Introspección/Privado)
        3. **Operativa** (Producción/Trabajo)
        4. **Soporte** (Logística/Servicios)
        5. **Transición** (Conectividad/Cinemática)
- **Persistencia:** Sincronización completa de Web -> Flask -> SQLite con desglose de matriz de inversión.

### 23. Punto de Partida para la Siguiente Sesión
1. **Verificación de la Matriz de 24 Slots:** Implementar la interfaz para que el habitante asigne actividades a su cronología.
2. **Dashboard de Gestión:** Visualizar los nuevos campos de m² y Honorarios en la consola de leads.
3. **App de Inmersión:** Pruebas de audio y seguimiento de tópicos en dispositivo móvil.

---

## Sesión: 2026-05-15 (Reconstrucción y Corrección de la Página Web)

### 24. Logros de la Sesión
- **Reconstrucción completa de `Pagina Web 5.html`** desde la versión original, integrando los avances de cotizador e inmersión de forma limpia y sin código duplicado.
- **Corrección del carrusel vertical del portafolio:** las miniaturas ahora detectan la proporción de cada imagen y se muestran en tamaños acordes (t-16-9, t-9-16, t-3-2), centradas y sin recortes.
- **Corrección del reproductor de video:** se restauró el atributo `loop` y la playlist cinematográfica de 4 videos de fondo.
- **Corrección del archivo `diagnosticos_master.json`:** se eliminaron comas sobrantes que impedían su correcta lectura (pasos 5A y 8A).
- **Corrección del servidor `backend/server.py`:** se agregaron las constantes faltantes `MINIMO_TALLER` y `RANGOS_OBRA`, se eliminó el código inaccesible y se implementó el guardado de reportes en `backend/reportes/`.
- **Actualización de precios y entregables** según la escala oficial de SOLOJUAN.md (Esencial $250, Integral $400, Ejecutivo $1,000).
- **Rediseño del flujo de inmersión:**
  - Paso 11: validación de formato de correo/teléfono, envío al servidor y notificación por WhatsApp a Juan.
  - Paso 12: texto aclaratorio sobre el estimado paramétrico y que la construcción es por un tercero.
  - El cotizador ya no abre WhatsApp al finalizar; solo se envía la información al servidor.
- **Diagnóstico técnico en paso 15:** ahora muestra todos los campos del JSON (psicología ambiental, lenguaje de patrones, space syntax, conducta ambiental y POE).

### 25. Pendientes
1. Configurar envío real de correos SMTP (Gmail).
2. Implementar la Matriz de 24 Slots.
3. Dashboard de gestión con visualización de leads.

---
*Sesión finalizada. El sistema SOMA ha dejado de ser una herramienta de captura para convertirse en un motor de gestión creativa y financiera.*

---

## Sesión: 2026-05-26 — Detección de Tiempos de Entrega Placeholder

### 51. HALLAZGO CRÍTICO

Los **6-8 semanas** que aparecen en `CONTRATO_DISENO_SOMA.md:55-66` y `PROTOCOLO_ORGANIZACION_PROCESOS.md:284-291` como tiempo de entrega no tienen sustento. Fueron generados como placeholder por el agente AI sin intervención de Juan. No se encontró documentación que justifique esos números en SOLOJUAN.md, sesiones previas ni en la web.

### 52. DECISIONES DE LA SESIÓN

1. **No publicar plazos en la web** (práctica común del mercado).
2. **Definir plazos internos realistas** basados en la experiencia de Juan.
3. **Variables a contemplar:**
   - Tamaño del proyecto (m²)
   - Paquete de entregables (Esencial / Integral / Ejecutivo)
   - Iteraciones con el cliente (principal factor de alargue)
   - Trámites y permisos municipales (segundo factor)
   - Coordinación con ingenieros externos (tercer factor)
4. **Juan definirá los números** cuando los tenga claros; quedan como pendiente.

### 53. ARCHIVOS CREADOS/MODIFICADOS

| Archivo | Cambio |
|---------|--------|
| `TIEMPOS_ENTREGA_BASE.md` | **Creado** — Estructura base con tabla Paquete×m², factores de ajuste y preguntas guía |
| `SOMA_CORE_INDEX.md` | **Modificado** — Nuevo ítem pendiente en Bloque 1 |
| `SOMA_SNAPSHOT.md` | **Modificado** — Nuevo pendiente registrado, fecha actualizada |

### 54. PENDIENTES (nuevos)

1. **[ALTA] Definir tabla de tiempos de entrega** en `TIEMPOS_ENTREGA_BASE.md` (Juan completa con su experiencia).
2. **[ALTA] Actualizar CONTRATO_DISENO_SOMA.md** — reemplazar placeholder 6-8 semanas con los nuevos tiempos.
3. **[ALTA] Actualizar PROTOCOLO_ORGANIZACION_PROCESOS.md** — idem.
4. **[MEDIA] Definir regla de escala** para proyectos grandes (semanas base + factor por m²).

---

## Sesión: 2026-05-18 (Sprint Completo: Notificaciones, Dashboard, App de Entrevista v2)

### 26. CAMBIOS EN ARCHIVOS

#### `backend/server.py`
- **Añadido:** `import smtplib`, `from email.mime.text import MIMEText`, `from email.mime.multipart import MIMEMultipart`, `from twilio.rest import Client`
- **Añadidas constantes:** `SMTP_SERVER`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD` (Gmail app password)
- **Añadidas constantes:** `TWILIO_SID`, `TWILIO_TOKEN`, `TWILIO_WHATSAPP` (+14155238886), `NOTIFICACION_WHATSAPP` (+5219995314093)
- **Modificado:** `enviar_correo()` — ahora envía vía SMTP real además de guardar reporte en disco
- **Añadido:** `enviar_whatsapp(contacto, temp_id, nivel_key, m2)` — notificación Twilio
- **Modificado:** `/save_immersion` — ahora llama a `enviar_whatsapp()` y devuelve `whatsapp_status` en JSON
- **Comportamiento:** El envío de correo ya no es simulado. Usa Gmail SMTP con TLS puerto 587.

#### `dashboard/Dashboard.html`
- **Añadido:** `ENTREVISTA_API` apuntando a `http://localhost:5050`
- **Añadido:** `cargarProyectosEntrevista()` y `buscarProyecto()` para vincular leads con proyectos de entrevista
- **Añadido:** En cada lead card: badges de estado (WEB, ENTREVISTA, GUÍA, DATOS, TRANSCRITO)
- **Añadido:** Botón "GUÍA" que abre `{ENTREVISTA_API}/proyectos/{id}/guia`
- **Modificado:** `cargarLeads()` ahora carga ambos servidores simultáneamente
- **Modificado:** Traducción completa a español de toda la interfaz
- **Añadido:** Estado del servidor de entrevista en panel I+D
- **Ejes de inmersión renombrados:** Fachada/Cerrada-Abierta, Habitaciones/Separadas-Juntas, Ambiente/Dividido-Libre, Luz/Suave-Fuerte, Acabados/Lisos-Texturizados, Altura/Varios pisos-Un piso, Exterior/Piedra-Jardín, Sensación/Grande-Acogedor, Vida Social/Privada-Activa, Color/Llamativo-Neutral

#### `aplicaciones_python/app_inmersion/app.py` (reescrito completo)
- **Puerto:** 5050
- **Endpoints creados:**
  - `GET /` — sirve la app de entrevista
  - `POST /crear_proyecto` — crea carpeta en `backend/proyectos/SOMA-XXXX/` con `info.json`
  - `POST /guardar_entrevista` — guarda audio .webm en carpeta del proyecto
  - `POST /guardar_datos_entrevista` — guarda formulario post-entrevista (JSON anidado en `notas_arquitecto`)
  - `POST /procesar_entrevista` — lanza hilo background con transcripción (Whisper) + análisis (DeepSeek)
  - `GET /proyectos` — lista todos los proyectos con su info.json
  - `GET /proyectos/{id}/guia` — descarga `guia_de_diseno.md`
  - `GET /proyectos/{id}/audio` — descarga audio
  - `GET /proyectos/{id}/datos` — devuelve `datos_estructurados.json`
- **Flujo de procesamiento:** `transcripción (faster-whisper)` → `análisis (DeepSeek Chat API)` → genera `guia_de_diseno.md` + intenta guardar en DB
- **Dependencias:** `requests` (instalada), `faster-whisper` (no instalada por timeout de red — pendiente)
- **DeepSeek API:** Lee `DEEPSEEK_API_KEY` de variable de entorno. Sin key, genera guía stub indicando que falta configurar.

#### `aplicaciones_python/app_inmersion/templates/entrevista.html` (reescrito)
- **6 tópicos en lenguaje natural conversacional:**
  1. La razón de estar aquí (terreno, reglas, tomador de decisiones, presupuesto incluye terreno)
  2. Los habitantes (UserEntity: edades, salud, hobbies, quién pasa más tiempo, visitas que se quedan)
  3. El programa (recámaras, baños, PB, oficina, cochera, servicio, extras, colecciones — NO complementar)
  4. Dinámicas y rutinas (ActivityMatrix: despertar, comidas, trabajo, llegada, mascotas, orden, materiales, clima)
  5. Inversión (presupuesto realista, etapas, metros vs acabados, honorarios incluidos)
  6. La cereza del pastel (poética: emoción, recuerdo feliz, objeto que dicte diseño, miedos + cierre filosofía SOMA)
- **Grabación:** Una sola grabación continua al presionar INICIAR. Se detiene al presionar FINALIZAR.
- **Post-entrevista:** Formulario con campos: cliente, contacto, habitantes, programa, rutinas, inversión, notas adicionales, checkbox "Analizar con IA"
- **Responsive:** Diseñado para uso en celular durante la cita presencial.

#### `backend/proyectos/` (nueva estructura)
```
backend/proyectos/
└── SOMA-20260518-XXXX/
    ├── info.json              ← metadatos del proyecto (estado, cliente, fechas, notas)
    ├── entrevista.wav/.webm   ← grabación de la entrevista
    ├── transcripcion.txt      ← transcripción Whisper
    ├── guia_de_diseno.md      ← documento final para diseñadores
    └── datos_estructurados.json ← Activity Matrix, ejes, etc. (futuro)
```

### 27. DECISIONES DE ARQUITECTURA

1. **Separación de servidores:** `server.py` (puerto 8080) maneja web + cotizador + notificaciones. `app_inmersion/app.py` (puerto 5050) maneja entrevistas. Comparten la misma DB SQLite.
2. **Organización de datos de proyecto:** Cada proyecto tiene su propia carpeta en `backend/proyectos/`. El dashboard solo muestra indicadores; los documentos completos van en la carpeta del proyecto. Esto evita saturar el dashboard.
3. **Inmersión web + entrevista son complementarios:** Van juntos. La web captura los 10 ejes visuales. La entrevista captura el contexto profundo (habitantes, rutinas, poética). La guía de diseño unifica ambos.
4. **Procesamiento con IA:** Whisper (transcripción local) + DeepSeek Flash API (análisis). DeepSeek recibe un prompt con toda la base de conocimiento SOMA (Psicología Ambiental, Patrones Alexander, Space Syntax, Environmental Behavior, POE, Proxémica). Sin costo significativo (~$0.001/entrevista).
5. **Migración Twilio → Telegram:** Cuando se agote el crédito gratuito de Twilio (~$15 USD). Es decisión del usuario, no implementar hasta entonces.
6. **Sin costo hasta final:** No activar DeepSeek API ni otras herramientas de pago hasta que el usuario lo autorice.

### 28. PENDIENTES (ordenados por prioridad)

1. **[MEDIA] Instalar `faster-whisper`** en el venv (requiere conexión estable). Alternativa: `whisper` de OpenAI.
2. **[MEDIA] Configurar `DEEPSEEK_API_KEY`** como variable de entorno para que el análisis automático funcione.
3. **[MEDIA] Probar app de entrevista en celular real** — la grabación de audio en dispositivos móviles puede tener issues de formato (webm vs wav).
4. **[BAJA] Pruebas de campo completas** — flujo: web → lead → correo → WhatsApp → entrevista → guía de diseño.

### 29. ARCHIVOS DE REFERENCIA CREADOS

| Archivo | Propósito |
|---------|-----------|
| `metodologia/Bloque 2 - Taller SOMA (OPERACION)/EJEMPLO_GUIA_DISENO.md` | Ejemplo concreto de guía de diseño (caso Carlos y Laura Méndez) para que el usuario visualice el formato final |
| `SOLOJUAN.md` (secciones 2026-05-18) | Instrucciones literales del usuario registradas para consulta futura |
| `recursos_graficos/Inmersion/` | 40 imágenes placeholder (2 por opción de inmersión) descargadas de Unsplash para sustituir picsum.photos |

### 30. PROTOCOLOS CONSULTADOS

- `metodologia/Bloque 2 - Taller SOMA (OPERACION)/PROTOCOLO_01_RECEPCION.md` — UserEntity, Zonificación Maestra, 10 ejes, ActivityMatrix 24h, CreativeCore
- `metodologia/Bloque 2 - Taller SOMA (OPERACION)/PROTOCOLO_02_ENTREVISTA_INMERSION.md` — 6 tópicos conversacionales, grabación, post-formulario, procesamiento IA
- `metodologia/Bloque 1 - Gestion del Entorno (ADM)/PROTOCOLO_PRESUPUESTO_Y_VIABILIDAD.md` — Precios oficiales $250/$400/$1000, cargo mínimo, rangos obra
- `metodologia/Bloque 2 - Taller SOMA (OPERACION)/PROTOCOLO_ANALISIS_SITIO.md` — Bioclimática, normativa, Genius Loci, salida a Zonificación Maestra

### 31. SESIÓN 18/05/2026 (TARDE) — ACTIVITY MATRIX EN DASHBOARD + IMÁGENES INMERSIÓN

#### Activity Matrix visual en Dashboard
- **`backend/server.py`**: Nuevo endpoint `GET /activity_matrix/<temp_id>` que lee `datos_estructurados.json` del proyecto y devuelve la matriz con habitantes y slots.
- **`dashboard/Dashboard.html`**: Botón "MATRIZ" en cada lead card. Al presionarlo, carga y renderiza grid de 24h por habitante con colores SOMA (Social/Descanso/Operativa/Soporte/Transición/Vacío), tooltips con hora, zona, iluminación y aislamiento. Leyenda de colores debajo del grid. Merge automático de proyectos de app_inmersion que no están en captura_web.
- El endpoint se probó exitosamente con el proyecto `SOMA-20260518-1132` (Carlos y Laura, 24 slots c/u).

#### Imágenes de Inmersión
- Creado `recursos_graficos/Inmersion/` con 40 imágenes (2 por opción × 10 pasos × 2 opciones) de Unsplash vía picsum.photos.
- `Pagina Web 5.html`: Reemplazados los 20 URLs de picsum.photos placeholder por rutas locales `../recursos_graficos/Inmersion/{codigo}_1.jpg`. Se usa la variante `_1` en la web; la `_2` queda en carpeta como respaldo.
- Pendiente: Juan generará sus propias imágenes y las reemplazará en la carpeta.

---

## Sesión: 2026-05-19 (Sprint Administrativo: Cobros, Programa, Kanban, PDF)

### 32. NUEVAS TABLAS Y ENDPOINTS

#### `programa_arquitectonico` (tabla nueva en DB)
- **Campos:** id, lead_id, tipo (Deseado/Complementario/Lujo), espacio, area, zona (1-5), horario_inicio/fin, mobiliario, acontecimientos, patrones_espaciales, usuarios, clave (E{número}), relacion_directa (JSON array de claves)
- **Vinculada a:** `captura_web.id` (NO a la tabla `espacios` de la app Tkinter vieja)

#### `cobros` (tabla nueva en DB)
- **Campos:** id, proyecto_id, concepto, monto, fecha_vencimiento, fecha_pago, estado (pendiente/pagado), metodo_pago, notas
- **Vinculada a:** `captura_web.id`

#### `config_fiscal` (tabla nueva en DB)
- **Campos:** id, rfc, regimen, pac_api_key, activo
- **Estado:** Pendiente — Juan no tiene RFC aún

#### Endpoints nuevos en `server.py`
| Endpoint | Método | Propósito |
|---|---|---|
| `/programa/<lead_id>` | GET | Lista espacios del programa arquitectónico |
| `/programa/espacio` | POST | Crea un espacio (con clave E{número}) |
| `/programa/espacio/<id>` | PUT | Actualiza espacio (usado para relaciones) |
| `/programa/espacio/<id>` | DELETE | Elimina espacio |
| `/cotizacion/<lead_id>` | GET | Calcula m2 reales, honorarios, obra estimada |
| `/cotizacion/<lead_id>/pdf` | GET | HTML imprimible de la cotización formal |
| `/cobros/<proyecto_id>` | GET | Lista cobros de un proyecto |
| `/cobros` | POST | Registra un cobro |
| `/cobros/<id>/pagar` | PATCH | Marca cobro como pagado |
| `/resumen_financiero` | GET | Totales de pagado/pendiente por proyecto |
| `/leads/kanban` | GET | Leads agrupados por pipeline_estado (6 columnas) |
| `/lead/<id>/pipeline` | PATCH | Mueve un lead entre estados del pipeline |
| `/` | GET | Sirve el Dashboard.html desde Flask (evita CORS) |
| `/css/<path>` | GET | Sirve archivos CSS estáticos |

### 33. Dashboard — Módulos Nuevos

#### Cobros y Finanzas
- Bloque ADMIN con totales: cobrado, pendiente, RFC, régimen
- Modal de Expediente: tabla de cobros + formulario para registrar nuevos pagos
- Badge de "💰 COBRADO" y "$$$ PTE" en lead cards

#### Programa Arquitectónico
- Modal con 3 pestañas: Deseado / Complementario / Lujo
- Inputs: espacio, m2, zona (1=Social · 2=Operativa · 3=Descanso · 4=Soporte · 5=Transición)
- Clave auto-incremental como E{número} — solo se ingresa el número
- Tabla con columnas: Espacio, m2, Z, Clave, 🔗, ✕
- Botón 🔗: mini-modal flotante movible para editar relaciones (ej: 1,3,5 → E1,E3,E5)
- Totales parciales por tipo de programa

#### Cotización Formal
- Se genera desde datos reales del programa arquitectónico
- Botón "📄 PDF": HTML imprimible (Ctrl+P → PDF)
- **NO incluye** (oculto al cliente): precio por m2, cargo mínimo $8,000, ni estimación de obra

#### Kanban Pipeline
- Botón toggle Kanban/Lista en barra de filtros
- 6 columnas con scroll: Lead → Entrevistado → Programado → Cotizado → Contratado → Pagado
- Flechas ◀ ▶ para avanzar/retroceder entre estados
- Estados persisten en DB (columna `pipeline_estado`)

### 34. DECISIONES DE ARQUITECTURA
1. **Dashboard servido desde Flask** para evitar CORS con `file:///`.
2. **Formato de clave `E{número}`**: el usuario solo ingresa el número; el prefijo E se agrega automáticamente (como en Arquiprograma.py original).
3. **Relaciones diferidas**: se editan después de crear todos los espacios, mediante botón 🔗. Nunca se pregunta al crear.
4. **Sin obra ni precio/m² en PDF**: datos internos del taller. La cotización al cliente solo muestra honorarios de diseño.
5. **Flujo completo integrado**: Web → DB → Programa → Cotización → Cobros en una sola vista Dashboard.

### 35. PENDIENTES
1. **[ALTA] Migrar DiagramaEspacialSoma.py** para leer de `programa_arquitectonico` e integrarlo al Dashboard.
2. **[MEDIA] Instalar faster-whisper** en el venv.
3. **[MEDIA] Configurar DEEPSEEK_API_KEY**.
4. **[MEDIA] Registro RFC de Juan** en RESICO.
5. **[BAJA] Diagrama espacial de relaciones** como grafo en Dashboard.

---

## Sesión: 2026-05-21 (Imágenes Definitivas de Inmersión)

### 36. LOGROS DE LA SESIÓN
- **Imágenes de Inmersión actualizadas:** Las 40 imágenes placeholder fueron reemplazadas por 20 imágenes propias del usuario, organizadas en 10 carpetas temáticas (`01. fachada/` a `10.Color/`).
- **Rutas corregidas en `web/Pagina Web 6.html`:** Las 20 referencias `XXa_1.jpg` / `XXb_1.jpg` fueron actualizadas a las rutas reales con nombres de archivo y subcarpetas del usuario.
- **Verificación completada:** Los 20 archivos existen en disco y las rutas están correctas.

### 37. PENDIENTES
## Sesión: 2026-05-21 (Paso 2 — Gradientes de Privacidad)

### 38. CAMBIOS REALIZADOS
- **Paso 2 renombrado:** De "Habitaciones (Todas juntas/Separadas)" a **"Privacidad (Abierta/Recibidor)"**.
- **Pregunta actualizada:** "¿Cómo prefieres que te reciban?" con opciones "Abierta — que se vea todo desde la entrada" y "Con recibidor — que insinúe lo que hay detrás".
- **diagnosticos_master.json reescrito:** Análisis técnico de Transparencia Radical vs Gradación de Intimidad (Appleton, Space Syntax, Patrones 110/127/165).
- **PROTOCOLO_01_RECEPCION.md actualizado:** Eje 2 ahora es "Privacidad".
- **SOMA_SNAPSHOT.md actualizado:** Eje 2 actualizado en Inmersión Visual.
- **Dashboard.html actualizado:** Etiquetas en el array EJES.
- **extractor.py actualizado:** Keywords NLP para el nuevo eje.
- **EJEMPLO_GUIA_DISENO.md actualizado:** Tabla de ejemplo refleja nuevo eje.

## Sesión: 2026-05-21 (TARDE — Organización de Procesos + Trayectoria Web)

### 40. LOGROS DE LA SESIÓN

- **[NUEVO] PROTOCOLO_ORGANIZACION_PROCESOS.md:** Mapeo formal lead → proyecto → entrega → cierre en 7 fases. Incluye macroflujo, fases detalladas, mapa de transición de estados (pipeline), reglas de negocio (subsidio cruzado, 30/40/30, tiempos), matriz de responsabilidades sistema/arquitecto/cliente, indicadores de gestión y flujo de archivado.
- **Corrección de flujo:** Se reordenaron las fases para que Investigación y Análisis (sitio, normativa) ocurran **después** del contrato, no antes de la cotización. El orden correcto: Lead → Entrevista → Programa → Cotización → Contrato → Investigación → Diseño → Cierre.
- **Sección Trayectoria rediseñada:** De 3 items genéricos a una **línea de tiempo vertical** con 5 nodos conceptuales:
  - 2004-2010: Arquitecto UADY — "Introducción a la arquitectura y descubrimiento de la forma-espacio-orden"
  - 2014-2015: Maestro en Arquitectura UNAM — "Desarrollo filosófico y tecnológico"
  - 2016-2017: Proyectista CDMX (NODO + Soluciones Señaléticas) — "Ampliar la mirada"
  - 2018-2026: Proyectista/Renderista Duarte Aznar — "Aprendizaje profundo y real" (Casona 333, Neden RD, Hilton, Intercontinental, Casa Hogar)
  - 2026: Fundador SOMA — "Automatizar lo técnico, liberar lo creativo"
- **Email de contacto actualizado:** Eliminado `taller@virtual.lab`, agregado `habitarq85@gmail.com` en sección Contacto de la web.
- **SOMA_CORE_INDEX.md actualizado:** Tarea "Organización de Procesos" marcada como completada.

### 41. ARCHIVOS CREADOS/MODIFICADOS

| Archivo | Cambio |
|---------|--------|
| `metodologia/Bloque 1 - Gestion del Entorno (ADM)/PROTOCOLO_ORGANIZACION_PROCESOS.md` | **Creado** — 7 fases del proceso SOMA |
| `web/Pagina Web 6.html` | **Modificado** — Trayectoria expandida a timeline + email contacto actualizado |
| `SOMA_CORE_INDEX.md` | **Modificado** — Organización de Procesos marcado ✅ |

### 42. PENDIENTES
- Automatización de Impuestos: Cálculo ISR/IVA, CFDI, reportes fiscales (requiere RFC).
- Probar app de entrevista en celular real (grabación de audio).
- Instalar faster-whisper para transcripción local.
- Configurar DEEPSEEK_API_KEY para análisis automático.
- Registro RFC de Juan en RESICO.
- Reemplazar imágenes placeholder en Filosofía y Servicios.
- Agregar foto de retrato en sección Trayectoria.

---

## Sesión: 2026-05-22 — Organización de Bloques: Dashboard a Bloque 1

### 43. CAMBIOS REALIZADOS

- **Dashboard movido** de `dashboard/` (raíz del proyecto) a `metodologia/Bloque 1 - Gestion del Entorno (ADM)/dashboard/`.
- **Rutas Flask actualizadas** en `backend/server.py:654-668`:
  - `/` ahora sirve `metodologia/Bloque 1 - Gestion del Entorno (ADM)/dashboard/Dashboard.html`
  - `/css/<path>` ahora sirve desde `.../dashboard/css/`
- **Dashboard.html sin cambios internos** — el CSS sigue siendo relativo (`href="css/style.css"`) y funciona porque se movió con el HTML. Los `fetch` a `localhost:8080` no se modifican.
- **Base de datos confirmada en Bloque 3:** `backend/server.py` + `proyectos_arquitectonicos.db` se quedan en `backend/`. Los bloques no comparten archivos entre sí; solo hablan con el backend vía API.

### 44. DECISIÓN DE ARQUITECTURA

- **Cada bloque autocontenido:** sus herramientas viven dentro de su carpeta. La data compartida vive en `backend/` (Bloque 3) y se consume por API.
- **Patrón validado:** Bloque 2 ya tenía `DiagramaSoma.html` junto a sus protocolos. Ahora Bloque 1 tiene su Dashboard. Consistencia lograda.

### 45. SESIÓN B4 — ESTRATEGIA DE MARKETING Y BUYER PERSONA

Se trabajó el Bloque 4 (MKT) por primera vez. Se definió:

**Buyer Persona priorizado:**
- Buyer 1 (Local Mérida, 30-45 años, primera casa) — prioridad alta, meses 0-12
- Buyer 2 (Remoto LATAM) — prioridad media, probar mes 6+ 
- Buyer 3 (Arquitecto coadyuvante) — prioridad baja, mes 12+

**Filosofía vs realidad:** Se documentó que la democratización no es el punto de partida sino un destino por fases. El manifiesto de evolución hacia la accesibilidad describe 4 fases: construir motor (0-6), probar mecanismo (6-12), primer proyecto subsidiado (12-18), subsidio automático (18+).

**Diferenciadores traducidos:** Cada ventaja técnica de SOMA se tradujo a lenguaje que el Buyer 1 entiende (confianza, certeza, proceso claro).

**Instagram:** Calendario de 6 semanas definido. Primeras publicaciones escritas hasta Semana 3.

**Corrección de Filosofía:** Juan aclaró la interpretación correcta de la frase — el lujo y la sencillez no son opuestos, ambos son vehículos para un mensaje sublime. La arquitectura está en el mensaje, no en el material.

**Análisis de precios COTAPAREDES:** Se comparó la estructura de Cotaparedes (2019: $400/m² base, 50/65/100% paquetes) contra SOMA ajustando inflación ~45%. Conclusión: $250/m² SOMA es competitivo. El ejecutivo ($1,000) es muy superior al de él ($580) y necesita justificarse con el contenido del paquete.

**Google My Business:** Guía de configuración creada (pendiente de activar cuando la web esté publicada).

**Lead magnet:** Guía "10 errores al construir tu primera casa" creada en MD + HTML con formulario de captura. Endpoint `/save_lead_magnet` agregado a server.py.

**Convenio de anticipo:** Se creó CONVENIO_ANTICIPO_PAGOS.md (versión 1 hoja) + RECIBO_PAGO_PARCIAL.md (para pagos 2 y 3). El contrato completo ya existía.

**Valor legal:** Se discutió y concluyó que el contrato es simbólico para montos de diseño residencial. La protección real es cobrar antes de entregar y retener archivos editables hasta el último pago. Se deja pendiente crear formatos de pagaré.

**Instagram:** Se completaron los textos de las 6 semanas completas y se guardaron en el archivo de contenido.

**Reestructura Bloque 2 (Taller):** Se redujo de 6 archivos sueltos a 4 carpetas por etapa del diseño:

| Carpeta | Contenido |
|---------|-----------|
| 01 Recepción e Investigación | PROTOCOLO_01_RECEPCION + PROTOCOLO_02_ENTREVISTA |
| 02 Análisis | PROTOCOLO_ANALISIS_SITIO + DiagramaSoma.html |
| 03 Diseño | Vacío (se llena con expertise de Juan) |
| 04 Entregables | EJEMPLO_GUIA_DISENO.md |

`Ejemplo de bloques/` (prototipos viejos) movido a `antecedentes/`. Se corrigió ruta de DiagramaSoma.html en `server.py:674`.

### 46. ARCHIVOS CREADOS Y/O MODIFICADOS

| Archivo | Cambio |
|---------|--------|
| `Bloque 4/BUYER_PERSONA.md` | **Nuevo** — Definición y priorización de buyer personas |
| `Bloque 4/MANIFIESTO_ACCESIBILIDAD.md` | **Nuevo** — Evolución de la accesibilidad por fases |
| `Bloque 4/CONTENIDO_INSTAGRAM.md` | **Nuevo** — Estrategia + textos completos de 6 semanas |
| `Bloque 4/GOOGLE_MY_BUSINESS.md` | **Nuevo** — Guía de configuración |
| `web/lead_magnet_10_errores.md` | **Nuevo** — Guía descargable (markdown) |
| `web/lead_magnet_10_errores.html` | **Nuevo** — Página con formulario de captura |
| `backend/server.py` | **Modificado** — Nuevo endpoint `/save_lead_magnet` |
| `Bloque 1/CONVENIO_ANTICIPO_PAGOS.md` | **Nuevo** — Convenio de 1 hoja para anticipo |
| `Bloque 1/RECIBO_PAGO_PARCIAL.md` | **Nuevo** — Recibo para pagos 2 y 3 |
| `SOLOJUAN.md` | **Modificado** — Instrucciones literales de la sesión |
| `backend/server.py` | **Modificado** — Ruta de DiagramaSoma actualizada a `02 Análisis/` |
| `BITACORA_SOMA.md` | **Modificado** — Esta entrada de sesión |

## Sesión: 2026-05-25 — Planeación de Etapas 6, 7 y 8 (Visualización, Representación Integral, Evaluación)

### 47. LOGROS DE LA SESIÓN

- **Visualización (Etapa 6) planeada:** Protocolo de 9 secciones. Flujo Revit→D5→Photoshop (Linux). Vistas obligatorias por paquete (Esencial/Integral/Ejecutivo). Estilo SOMA (fondos oscuros, acento #bc4b21, vegetación regional). Catálogo de materiales reutilizables. Postproducción mínima. Checklist de entrega con naming estándar. Archivo en carpeta `renders/`.
- **Representación Integral (Etapa 7) planeada:** Dossier editorial en HTML con efectos scroll-reveal (Intersection Observer). Template parametrizable vía bloque JSON de datos. Misma identidad visual que la web (Unbounded, JetBrains Mono, #bc4b21, fondo oscuro). Exportación a PDF con `window.print()` + `@media print`.
- **Evaluación (Etapa 7 del taller) planeada:** Auditoría de indicadores de habitabilidad. Térmicos, iluminación, acústicos, programa, proxémica, normativos. Tabla de resultados ✅/⚠️/❌ con ajustes. 2-3 días.

### 48. ARCHIVOS PLANEADOS

| Archivo | Estado |
|---------|--------|
| `03 Diseño/PROTOCOLO_VISUALIZACION.md` | Planeado |
| `03 Diseño/dossier/plantilla_dossier.html` | Planeado |
| `03 Diseño/PROTOCOLO_EVALUACION.md` | Planeado |

---

## Sesión: 2026-05-25 (Tarde) — Ajustes y Correcciones en Página Web

### 49. CAMBIOS REALIZADOS EN `web/Pagina Web 6.html`

- **Retrato en Trayectoria:** Reemplazado placeholder por `retrato final.png` (1264x2048). Recorte del 20% superior vía `object-fit: cover` + `object-position: 50% 100%`. Efecto hover (escala de grises → color + scale).
- **Video Filosófico:** Eliminado placeholder "Próximamente" de la sección Filosofía.
- **Carrusel de Filosofía:** Redimensionado (400px por slide vs 320px), centrado con padding lateral, velocidad reducida (maxScroll 8 vs 20).
- **Frase de portada:** Reemplazada "La arquitectura de alta calidad no debería ser un privilegio" por "Que la buena arquitectura no sea la excepción, sino el punto de partida."
- **Texto de Filosofía:** Reformulado "No necesitamos lujos para que la arquitectura de alta calidad exista y llegue a todos" por "La calidad en la arquitectura no está en el costo, sino en la claridad del mensaje." Eliminada repetición de "mensaje" en la frase anterior.
- **Botón Finalizar (Inmersión):** Agregado `AbortController` con timeout de 3s para evitar que el botón se trabe si el servidor no responde. Protección contra doble clic.

### 50. PENDIENTES (sin cambios)

- Automatización de Impuestos: Cálculo ISR/IVA, CFDI, reportes fiscales (requiere RFC).
- Instalar faster-whisper para transcripción local.
- Configurar DEEPSEEK_API_KEY.
- Registro RFC de Juan en RESICO.
- Reemplazar imágenes placeholder en Servicios (verificar).
- Implementar PROTOCOLO_VISUALIZACION.md, plantilla_dossier.html, PROTOCOLO_EVALUACION.md.

---

## Sesión: 2026-05-26 — Detección de Tiempos de Entrega Placeholder

### 51. HALLAZGO CRÍTICO

Los **6-8 semanas** que aparecen en `CONTRATO_DISENO_SOMA.md:55-66` y `PROTOCOLO_ORGANIZACION_PROCESOS.md:284-291` como tiempo de entrega no tienen sustento. Fueron generados como placeholder por el agente AI sin intervención de Juan. No se encontró documentación que justifique esos números en SOLOJUAN.md, sesiones previas ni en la web.

### 52. DECISIONES DE LA SESIÓN

1. **No publicar plazos en la web** (práctica común del mercado).
2. **Definir plazos internos realistas** basados en la experiencia de Juan.
3. **Variables a contemplar:**
   - Tamaño del proyecto (m²)
   - Paquete de entregables (Esencial / Integral / Ejecutivo)
   - Iteraciones con el cliente (principal factor de alargue)
   - Trámites y permisos municipales (segundo factor)
   - Coordinación con ingenieros externos (tercer factor)
4. **Juan definirá los números** cuando los tenga claros; quedan como pendiente.

### 53. ARCHIVOS CREADOS/MODIFICADOS

| Archivo | Cambio |
|---------|--------|
| `TIEMPOS_ENTREGA_BASE.md` | **Creado** — Estructura base con tabla Paquete×m², factores de ajuste y preguntas guía |
| `SOMA_CORE_INDEX.md` | **Modificado** — Nuevo ítem pendiente en Bloque 1 |
| `SOMA_SNAPSHOT.md` | **Modificado** — Nuevo pendiente registrado, fecha actualizada |

### 54. Fuentes en Protocolos (agregado posterior)

Se revisaron los 10 protocolos de Bloque 2 para agregar sección **FUENTES**:
- `PROTOCOLO_CONCEPTUALIZACION.md` — fuentes agregadas.
- `PROTOCOLO_MODELADO.md` — fuentes agregadas.
- `PROTOCOLO_VISUALIZACION.md` — fuentes agregadas.
- `PROTOCOLO_REPRESENTACION_INTEGRAL.md` — fuentes agregadas.
- `PROTOCOLO_EVALUACION.md` — fuentes agregadas.
- `PROTOCOLO_ANTEPROYECTO.md` — fuentes agregadas.
- `PROTOCOLO_PLANOS_TECNICOS.md` — fuentes agregadas.
- `PROTOCOLO_COORDINACION.md` — fuentes agregadas.
- `PROTOCOLO_ANALISIS.md` — fuentes agregadas (Ching ×2, Deasy, Grillo, Hall, Alexander, Olgyay, Givoni, normativas).
- `PROTOCOLO_01_RECEPCION.md` — fuentes agregadas (Hall, Deasy, Alexander, Sommer, Ching).

### 55. Expansión Masiva de Referencias Canónicas (agregado posterior)

Por solicitud de Juan, se incorporaron todas las referencias canónicas mencionadas en la conversación + Holahan (Psicología Ambiental) a los protocolos correspondientes:

| Protocolo | Nuevas fuentes agregadas |
|-----------|--------------------------|
| `PROTOCOLO_01_RECEPCION.md` | Peña, Duerk, Cherry, Zeisel, Holahan |
| `PROTOCOLO_ANALISIS.md` | Norberg-Schulz, Arnheim, Clark & Pause, Zeisel, Newman, Gehl, Yeang, Alexander (Synthesis), Holahan |
| `PROTOCOLO_CONCEPTUALIZACION.md` | Norberg-Schulz, Arnheim, Aalto, Alexander (Synthesis), Holahan |
| `PROTOCOLO_MODELADO.md` | Deplazes, Allen |
| `PROTOCOLO_VISUALIZACION.md` | Arnheim |
| `PROTOCOLO_REPRESENTACION_INTEGRAL.md` | Arnheim |
| `PROTOCOLO_EVALUACION.md` | Neufert, Panero & Zelnik, Holahan, NMX-R-001; ASHRAE 55 actualizado a 2023 |
| `PROTOCOLO_ANTEPROYECTO.md` | Neufert, Panero & Zelnik, NMX-R-001 |
| `PROTOCOLO_PLANOS_TECNICOS.md` | Deplazes, Allen, IMCA, NMX-R-001 |
| `PROTOCOLO_COORDINACION.md` | Peña |

Se creó además `REFERENCIAS_CANONICAS.md` — tabla maestra con las 43 fuentes, su dominio y los protocolos donde se citan.

### 56. Dashboard: Fondo Democratización + Notificaciones

**Problema:** El Fondo Democratización se calculaba client-side con fórmula hardcodeada en `renderAdmin()`. Las notificaciones eran texto estático "CORREO + WHATSAPP" sin verificar.

**Solución:**
1. **Backend** (`server.py`):
   - Nuevo endpoint `GET /fondo_democratizacion` — calcula el fondo desde la DB (Ejecutivo $600/m², Integral $200/m²).
   - Nuevo endpoint `GET /notificaciones/status` — prueba conexión SMTP (login real) y Twilio (fetch account). Retorna `configurado` + `conectado` para cada uno.
2. **Frontend** (`Dashboard.html`):
   - `renderAdmin()` ahora es `async` y obtiene el fondo vía fetch.
   - Nueva función `verificarNotificaciones()` que colorea dinámicamente: ✅ CORREO + WHATSAPP / ❌ CORREO(FALLO) / ❌ SIN CONF.
   - Se llama en `cargarLeads()` y en el auto-refresh cada 30s.

**Verificación:** Ambos endpoints respondieron correctamente. SMTP conectado ✅, Twilio conectado ✅. Fondo real: $41,000 desde la DB.

### 57. ARCHIVOS CREADOS/MODIFICADOS (tercera parte)

| Archivo | Cambio |
|---------|--------|
| `backend/server.py` | **Modificado** — endpoints `/fondo_democratizacion` y `/notificaciones/status` agregados |
| `Dashboard.html` | **Modificado** — fondo vía API, notificaciones dinámicas |
| `BITACORA_SOMA.md` | **Modificado** — esta entrada |

### 58. PENDIENTES

1. **[ALTA] Definir tabla de tiempos de entrega** en `TIEMPOS_ENTREGA_BASE.md`.
2. **[ALTA] Actualizar CONTRATO_DISENO_SOMA.md** — reemplazar placeholder 6-8 semanas.
3. **[ALTA] Actualizar PROTOCOLO_ORGANIZACION_PROCESOS.md** — idem.
4. **[MEDIA] Definir regla de escala** para proyectos grandes.

---

## Sesión: 2026-05-27 — Deploy a Railway + Optimización Web

### 59. LOGROS DE LA SESIÓN

- **Web:** Botón "Iniciar Inmersión SOMA" renombrado a "COTIZADOR SOMA". Texto de opciones de inmersión agrandado (0.5rem → 0.7rem). Texto en paso 12 corregido: "cotiza y ejecuta". Botón "← Volver" agregado al paso 15.
- **Preparación para Railway:** Se crearon `requirements.txt`, `Procfile`, `railway.json`. `server.py` actualizado para servir `Pagina Web 6.html` en `/`, Dashboard en `/dashboard`, y rutas para assets estáticos (`/recursos_graficos/`, `/backend/`). URLs de frontend cambiadas a rutas relativas. Puerto usa `$PORT`.
- **GitHub:** Repositorio `habitarq85-wq/SOMA` creado y conectado. Primer push exitoso.
- **Railway:** Proyecto desplegado en Railway con dominio generado.
- **Optimización de imágenes:** 55 imágenes PNG (426 MB) convertidas a JPEG (28 MB) — ahorro del 93%. Caché de 24h agregada a rutas estáticas. Servidor con gthread + 4 threads.
- **Videos:** Archivos renombrados sin espacios ni caracteres especiales. Soporte de Range headers agregado para streaming de video.

### 60. PENDIENTES (nuevos)

1. **[ALTA] Subir videos a YouTube** como "No listado" y embeberlos con iframe (4 videos).
2. **[MEDIA] Activar WhatsApp** empresarial y actualizar número en la web.
3. **[BAJA] Migrar contraseñas SMTP/Twilio** a variables de entorno en Railway.
4. **[BAJA] Considerar PostgreSQL** para datos persistentes en Railway (SQLite es efímero).

### 61. ARCHIVOS MODIFICADOS/CREADOS

| Archivo | Cambio |
|---------|--------|
| `web/Pagina Web 6.html` | Botón Cotizador, fuente opciones, volver paso 15, textos paso 12, URLs relativas, videos renombrados |
| `backend/server.py` | Rutas web estáticas + Range headers video + caché + más threads |
| `backend/requirements.txt` | Creado — dependencias para Railway |
| `backend/Procfile` | Creado — gunicorn para Railway |
| `Procfile` | Creado — gunicorn con gthread |
| `requirements.txt` | Creado — dependencias en raíz |
| `railway.json` | Creado — configuración Railway |
| `.gitignore` | Creado — exclude venv, pycache, db |
| `SOMA_SNAPSHOT.md` | Actualizado — cambios de deploy

---

## Sesión: 2026-05-28 — Landscape responsive + SMTP Railway fix

### 62. LOGROS DE LA SESIÓN

- **Landscape Responsive:** Agregada media query `max-height: 520px` para celular horizontal. Hero (1ra sección) mantiene 100vh, secciones siguientes se adaptan con altura automática. Slide titles con font-size reducido para evitar solapamiento. Imágenes carrusel con `object-fit: contain`.
- **SMTP Railway:** Puerto cambiado de 587 (TLS) a 465 (SSL) porque Railway bloquea outbound en puerto 587. Agregada variable `SMTP_USE_SSL` (default true) para controlar SSL vs TLS.
- **Env vars:** `.strip()` agregado a todas las variables de entorno para eliminar trailing spaces del dashboard de Railway.
- **Debug SMTP:** Endpoint `/notificaciones/status` ahora devuelve `error` y `trace` con el mensaje de error real.
- **GitHub Token:** Se usó token `ghp_oQi...0QKX` para push (sin credential helper configurado).

### 63. PENDIENTES (nuevos)

1. **[ALTA] Verificar SMTP** — Railway desplegó con puerto 465, falta confirmar si conecta.
2. **[MEDIA] Migrar a PostgreSQL** — SQLite se pierde en cada reinicio de Railway.
3. **[MEDIA] Adquirir dominio propio** + Cloudflare CDN.
4. **[BAJA] Limpiar git history** — remover credenciales expuestas en commits anteriores.

### 64. ARCHIVOS MODIFICADOS

---

## Sesión: 2026-05-28 (Tarde/Noche) — Ajustes responsive + Imágenes comprimidas + Next bugs

### 65. LOGROS DE LA SESIÓN

- **Cotizador single POST:** Eliminado el doble envío. `registerContact()` ya no hace fetch; solo `finishImmersion()` al paso 12 o 15 guarda una vez.
- **Responsive portrait:** Hero `padding-top: 15vh`, overlay oscuro `0.95`, proyectos centrados, títulos carrusel al borde inferior.
- **Responsive landscape:** Modal portafolio flex column (imagen flex:1, thumbnails 70px). Carrusel filosofía forzado horizontal con `!important` + flecha `→` hint.
- **Servicios reestructurados:** `.services-row` agrupa imagen + lista en todas las breakpoints. Contacto fuera del row.
- **Trayectoria portrait:** Viñeta `::after` con `box-shadow: inset`. "M. en Arq." en una línea tanto en timeline como bajo la foto.
- **Carrusel filosofía:** Slide "CALIDAD SIN JERARQUÍAS" eliminado. Flecha `→` animada en mobile + máscara gradient fade.
- **WhatsApp:** Número `999 531 4093` visible en Contacto.
- **Imágenes comprimidas:** 110 archivos procesados con Pillow (JPG quality 80, WebP quality 70). Reducción 49→44 MB. Commit `0531ffe` pusheado a GitHub.

### 66. PENDIENTES (próxima sesión)

1. **[BUG] Botón cotizador oculto en landscape mobile** — posible z-index/overflow/posición del modal.
2. **[BUG] Página se traba en "Enviar"** — fetch a `/save_immersion` cuelga sin timeout ni catch. Agregar AbortController o timeout.
3. **[MEDIA] Instalar ffmpeg** para comprimir los 4 videos MP4 (~19 MB total).
4. **[BAJA] Probar SMTP en Railway** — confirmar que el puerto 465 SSL funciona en producción.

### 67. ARCHIVOS MODIFICADOS

| Archivo | Cambio |
|---------|--------|
| `web/Pagina Web 6.html` | Landscape responsive (max-height: 520px), slide titles más pequeños, hero mantiene 100vh |
| `backend/server.py` | SMTP_SSL puerto 465, .strip() en env vars, debug logging en /notificaciones/status |
| `web/Pagina Web 6.html` | Cotizador single POST (eliminado fetch en paso 12), hero padding-top 15vh, overlay 0.95, proyectos centrados, títulos carrusel borde inferior, landscape modal flex, carrusel filosofía horizontal !important + flecha, servicios .services-row, trayectoria viñeta ::after, WhatsApp contacto |
| `SOLOJUAN.md` | Instrucciones literales de la sesión agregadas |
| `SOMA_CORE_INDEX.md` | Nuevo Bloque 5 con checklist de sesión + bugs pendientes |
| `SOMA_SNAPSHOT.md` | 11 nuevos items + 2 bugs registrados |
| `BITACORA_SOMA.md` | Esta entrada de sesión |

---

## Sesión: 2026-05-29 — Video crossfade, SendGrid, Landscape compact, Immersion images fix

### 68. LOGROS DE LA SESIÓN

#### Video Hero
- **Crossfade:** Implementados dos elementos `<video>` con transición `opacity 0.8s`. Mientras uno se reproduce, el otro precarga el siguiente clip. Elimina el salto/pausa entre videos de la playlist.
- **Opacidad final:** Ajustada progresivamente por petición del usuario: 0.4 → 0.5 → 0.45 → **0.40** (filtro más oscuro).

#### Email (SendGrid)
- **Problema:** Railway bloquea todos los puertos SMTP salientes (587, 465, 25). El envío con `smtplib` fallaba con "Network is unreachable".
- **Solución:** Reemplazo de SMTP por **SendGrid API** (Twilio). Usa HTTPS (puerto 443), que Railway sí permite.
- **Cambios:**
  - `requirements.txt`: agregado `sendgrid>=6.0`
  - `server.py`: eliminados `smtplib`, `email.mime`; agregados `SendGridAPIClient`, `Mail`
  - `enviar_correo()` ahora usa SendGrid HTTP API
  - `notificaciones_status()` ahora verifica API key de SendGrid en vez de conexión SMTP
  - `smtp_error` incluido en respuesta JSON de `/save_immersion` para diagnóstico
  - `.env` y `.env.example`: reemplazadas variables SMTP por `SENDGRID_API_KEY`
- **Timeout cliente:** 5s → 20s para no abortar antes de respuesta del servidor.
- **Timeout SMTP removido:** Ya no aplica (SendGrid no tiene timeout análogo).

#### Landscape Mobile (Contacto invisible)
- **Compactación agresiva** para que el botón y textos de contacto quepan sin scroll:
  - Imagen servicios: 120px → 90px
  - Fuentes: lista `0.5rem`, contacto p `0.5rem`, botón `0.5rem` → todos a `0.45rem`
  - Grid gap servicios: 8px → 4px
  - Padding sección: `1.5vh 4% 4vh` → `1vh 4% 3vh`
  - Timeline compacto (`padding-bottom: 4px`)
  - Botón: `padding: 4px 10px`
- Removido `display: inline !important` del h2 de contacto (posible conflicto flex).

#### Immersion Images (Mobile Portrait)
- **Problema:** `object-fit: cover` + `aspect-ratio: 3/4` recortaba las imágenes en columna única.
- **Solución:** En 480px → `object-fit: contain; height: auto; max-height: 200px`. En 768px → mismo approach con `max-height: 180px`. Imágenes se muestran completas sin recorte.

#### Desktop Section:last-of-type
- Centrado (`justify-content: center; padding: 0 10%`) igual a las otras secciones.
- Título Contacto hereda `h2` global (`clamp(1.8rem, 4vw, 2.5rem)`) — mismo tamaño que Servicios.
- Textos contact alineados con lista servicios via `padding-left: 25px`.

### 69. BUGS RESUELTOS

| Bug | Estado |
|-----|--------|
| Botón cotizador oculto en landscape mobile | Resuelto (compactación extrema) |
| Página se traba en "Enviar" | Resuelto (timeout 20s + catch) |
| SMTP no conecta en Railway | Resuelto (migración a SendGrid) |
| Imágenes de inmersión recortadas en móvil vertical | Resuelto (object-fit: contain) |

### 70. PENDIENTES (próxima sesión)

1. **[MEDIA] Autenticar dominio** en SendGrid para evitar que correos vayan a spam.
2. **[MEDIA] Confirmar que landscape mobile** muestra correctamente el contacto en vivo.
3. **[BAJA] Actualizar contrato** con tiempos de entrega reales (cuando Juan los defina).
4. **[BAJA] PostgreSQL** en Railway (SQLite se pierde en reinicios).

### 71. ARCHIVOS MODIFICADOS

| Archivo | Cambio |
|---------|--------|
| `web/Pagina Web 6.html` | Video crossfade (2 players), landscape compact, immersion images contain, timeout 20s, smtp_error en toast |
| `backend/server.py` | SendGrid API (eliminado smtplib), respuesta con smtp_error, timeout SMTP 10s |
| `requirements.txt` | +sendgrid |
| `.env` / `.env.example` | SMTP_USER/PASSWORD → SENDGRID_API_KEY |
| `SOMA_SNAPSHOT.md` | Actualizado con todos los cambios de la sesión |
| `BITACORA_SOMA.md` | Esta entrada |

---

*Sesión cerrada. Sitio web completo y funcional: hero, portafolio, inmersión, cotizador, email, responsive landscape/portrait. Pendiente dominio propio + publicación formal.*

---

## Sesión: 2026-06-08 — PROCESO DE DISEÑO 2.0 + Biblioteca SOMA

### 77. LOGROS DE LA SESIÓN

- **[NUEVO] PROCESO DE DISEÑO 2.0 creado:** Expansión del índice original (143 líneas) a especificación completa (~1614 líneas) con INPUT/OPERA/OUTPUT/PROC para cada uno de los 143 items originales. Se corrigieron items que estaban fusionados erróneamente en la expansión automática. Cada item tiene:
  - **Clasificación por naturaleza:** `[REF]` (referencia/búsqueda), `[OUT]` (output/generación), `[DEC]` (decisión humana), `[ACC]` (acción técnica), `[EVA]` (evaluación), `[GUI]` (guía/consulta)
  - **Asignación de procesador:** `AI`, `HUMANO`, `AI→HUMANO`, `HUMANO→AI`
  - **Citas inline** con 13 referencias al final del documento
  - **PROTOCOLO cross-references** (10 protocolos mapeados a items específicos)
- **Corrección post-expansión:** Se corrigieron clasificaciones (5 items cambiados de AI a HUMANO/AI→HUMANO), se arregló 5.10 (AI→HUMANO), 2.2.3 (AI), y se re-clasificaron 6 items de Sección 2 de AI a HUMANO/AI→HUMANO. Se verificó que todos los items de Sección 2 outputean solo raw files y Sección 3 los procesa.
- **Biblioteca SOMA poblada:** 6 carpetas con contenido descargado, generado o referenciado:
  - `normativas/` — 8 PDFs (35 MB): Reglamento Construcción Mérida, Gaceta 932 (NTC), NMX-R-050 accesibilidad, NOM-020-ENER eficiencia, NOM-008-ENER envolvente, PMDU, PIMUS 2040, Plan Municipal Desarrollo
  - `clima/` — carta_solar_merida (PNG + PDF generados por script), rosa_vientos_merida (PNG + PDF generados por script), INDICE_CLIMA.md con tabla de datos históricos
  - `diseno/` — REFERENCIAS_BIBLIOGRAFICAS.md con ISBN y ubicaciones de Neufert, Panero, Ching (solo referencia por copyright)
  - `arquetipos/` — INDICE_ARQUETIPOS.md con 18 recursos open-access sobre casa maya, colonial, porfiriana y moderna
  - `repertorio/` — REPERTORIO_PROYECTOS.md con 15+ proyectos de referencia filtrados por clima cálido-húmedo / contexto patrimonial
  - `patrones/` — CATALOGO_PATRONES_DISENO.md (42 patrones SOMA en 5 categorías: SP, US, AC, BC, EC) + REFERENCIA_ALEXANDER.md (34 patrones de Alexander mapeados a Mérida)

### 78. HALLAZGOS Y DECISIONES

- **Copyright:** Neufert, Ching, Panero, Alexander no se descargan. Solo se referencian con ISBN y lugar de consulta.
- **CONAGUA Normales Climatológicas:** El sitio SMN bloquea descargas programáticas (mod_security, 301 redirects). Se usó link directo al sitio + tabla resumen en INDICE_CLIMA.md con datos de fuentes abiertas. La rosa de vientos de meteoblue está tras paywall → se generó sintética con datos realistas.
- **Biblioteca como repositorio central persistente:** Primer proyecto descarga, siguientes copian de la biblioteca. No se duplica esfuerzo de investigación.
- **Catálogo de Patrones = AI→HUMANO:** AI compila borrador inicial (42 patrones), humano cura y ajusta por proyecto. Documento vivo.
- **Arquetipos y Repertorio = AI→HUMANO:** AI busca recursos y proyectos candidatos, humano decide uso.

### 79. ARCHIVOS CREADOS/MODIFICADOS

| Archivo | Cambio |
|---------|--------|
| `metodologia/Bloque 2 - Taller SOMA (OPERACION)/PROCESO DE DISEÑO 2.0` | **Creado** — Expansión completa del PROCESO DE DISEÑO original |
| `biblioteca/normativas/` (8 PDFs) | **Creado** — Reglamento, NTC, NOMs, planes municipales |
| `biblioteca/clima/carta_solar_merida.png` | **Creado** — Carta solar generada por script |
| `biblioteca/clima/carta_solar_merida.pdf` | **Creado** — Versión PDF |
| `biblioteca/clima/rosa_vientos_merida.png` | **Creado** — Rosa de vientos generada por script |
| `biblioteca/clima/rosa_vientos_merida.pdf` | **Creado** — Versión PDF |
| `biblioteca/clima/INDICE_CLIMA.md` | **Creado** — Tabla de datos climáticos + fuentes |
| `biblioteca/diseno/REFERENCIAS_BIBLIOGRAFICAS.md` | **Creado** — Referencias de libros de diseño |
| `biblioteca/arquetipos/INDICE_ARQUETIPOS.md` | **Creado** — 18 recursos open-access |
| `biblioteca/repertorio/REPERTORIO_PROYECTOS.md` | **Creado** — 15+ proyectos de referencia |
| `biblioteca/patrones/CATALOGO_PATRONES_DISENO.md` | **Creado** — 42 patrones SOMA |
| `biblioteca/patrones/REFERENCIA_ALEXANDER.md` | **Creado** — 34 patrones Alexander mapeados |
| `SOMA_CORE_INDEX.md` | **Modificado** — Biblioteca agregada al inventario |
| `SOMA_SNAPSHOT.md` | **Modificado** — Sesión registrada |
| `BITACORA_SOMA.md` | **Modificado** — Esta entrada de sesión |

### 80. PENDIENTES (PRÓXIMA SESIÓN)

1. **[MEDIA] Revisar y alinear contenidos de protocolos individuales** contra PROCESO DE DISEÑO 2.0.
2. **[MEDIA] Mapear items restantes contra codebase** (Activity Matrix, Diagrama SOMA, Dashboard endpoints).
3. **[MEDIA] Integrar biblioteca SOMA en PROJECT TEMPLATE** — flujo de copia a `referencias/` de cada proyecto.
4. **[BAJA] Refinar catálogo de patrones** con cada proyecto completado (documento vivo).

---

## Sesión: 2026-06-02 — Precios v3.0, UX cotizador, scroll reveal bidireccional, fixes

### 72. LOGROS DE LA SESIÓN

#### Precios actualizados (v3.0)
- Integral: $400/m² → **$350/m²**
- Ejecutivo: $1,000/m² → **$850/m²**
- Mínimo taller: $8,000 → **$6,500**

#### Programa arquitectónico — Espacios mínimos
- Valores cambiados a dimensiones mínimas funcionales (sala 19, comedor 14, cocina 12, recámara 16, estudio 10, baño 5, 1/2 baño 2, cochera 30, bodega 7) con factor 1.35 **ya integrado**.
- `* 1.35` eliminado del JS para no duplicar.

#### Quote-type selector (3 tabs visibles)
- `<select>` reemplazado por 3 botones tipo tab en el paso de parámetros.
- Activo: acento `#d45e2c` + negrita + fondo tenue. Inactivos: gris translúcido.
- Nueva variable global `currentQuoteType` y función `setQuoteType()`.

#### Botón "volver" unificado
- Todos los pasos del cotizador (1–15) ahora usan `btn-back` con estilo: `background: transparent`, `border: 1px solid #333`, texto `← volver`.
- Posicionado abajo-centro con `left: 50%; transform: translateX(-50%)`.
- Se eliminó `backdrop-filter` de `.btn-back`.

#### Scroll reveal bidireccional + filosofía
- Proyectos y filosofía: `classList.toggle('revealed', entry.isIntersecting)` en vez de solo `add()`.
- Al subir, los elementos vuelven a su estado inicial con animación.
- Filosofía en mobile: `opacity: 0.5; transform: translateX(-15px)` → `opacity: 1; translateX(0)`.

#### Fixes alta prioridad (11/11)
| # | Issue | Fix |
|---|-------|-----|
| 1 | `type="button"` duplicado step 12 | Eliminado |
| 2 | `overflow:hidden` corta contenido en sections | → `overflow: visible` |
| 3 | Contraste `#bc4b21` (3.93:1) falla AA | → `#d45e2c` |
| 4 | Contraste `#555` (2.66:1) tl-detail | → `#999` |
| 5 | Contraste `#666` (3.45:1) texto info | → `#aaa` |
| 6 | 30+ imágenes sin `alt` | 31 con alt descriptivo |
| 7 | Sin `<noscript>` | Agregado |
| 8 | `backdrop-filter` sin `-webkit-` (5x) | Ambos prefijos |
| 9 | `outline:none` sin sustituto foco | `:focus-visible` agregado |
| 10 | `overflow:hidden` landscape modal | Revisado — era intencional |
| 11 | `scroll-snap-type: y mandatory` | → `y proximity` |

### 73. ARCHIVOS MODIFICADOS

| Archivo | Cambio |
|---------|--------|
| `web/Pagina Web 6.html` | Precios v3.0, quote tabs, btn volver unificado, scroll reveal bidireccional, filosofía reveal, fixes 11/11, programa mínimos, cochera 30m², threshold 0.65 |
| `SOMA_SNAPSHOT.md` | Precios v3.0, nuevos items sesión, última actualización 02/06/2026 |
| `SOLOJUAN.md` | Nueva sección [2026-06-02] con precios v3.0 y decisiones |
| `SOMA_CORE_INDEX.md` | Bloque 6 agregado con checklist 02/06/2026 |
| `BITACORA_SOMA.md` | Esta entrada de sesión |

---

## [2026-06-02 — Segunda Pasada] Hardening de precios v3.0 en todo el ecosistema

Se detectaron y corrigieron referencias heredadas a precios v2.1 ($400, $1,000, $8,000) que no se habían actualizado en la primera pasada.

| Archivo | Cambio |
|---------|--------|
| `backend/server.py` | `MINIMO_TALLER=6500` reemplazó `8000` hardcodeado en 2 `Math.max()` calls |
| `web/Pagina Web 5.html` | `setSomaLevel(400→350, 1000→850)`, `MINIMO_TALLER=8000→6500`, `promObra 400→350`, tabla de rangos |
| `Dashboard.html` | 3 ocurrencias de `400→350`, `1000→850`, `8000→6500` en cálculos de honorarios y kanban |
| `PROTOCOLO_PRESUPUESTO_Y_VIABILIDAD.md` | v2.1→v3.0, precios y mínimo actualizados |
| `CONVENIO_ANTICIPO_PAGOS.md` | Integral $400→$350, Ejecutivo $1,000→$850 |
| `CARTA_PRESENTACION_SOMA.html` | Precios y `accent #bc4b21→#d45e2c`, mínimo $8,000→$6,500 |
| `CARTA_PRESENTACION_SOMA.md` | Integral $400→$350, Ejecutivo $1,000→$850 |
| `CONTRATO_DISENO_SOMA.md` | Integral $400→$350, Ejecutivo $1,000→$850, mínimo $8,000→$6,500 |

**Resultado:** 8 archivos sincronizados. Cero referencias heredadas a v2.1 en el ecosistema SOMA.

---

## [2026-06-02 — Tercera Pasada] Optimización Web y Arquitectura de Algoritmo

Cambio estratégico hacia la estructuración del flujo operativo y la base algorítmica del diseño SOMA.

### 1. Optimización Hero Video
- Se detectó que cargar 4 videos separados (20MB) con lógica JS de transición cruzada podía causar lags y bloqueos en móviles.
- Se instaló ffmpeg y se generó un solo video: `hero_loop.mp4` (29s, 5.6MB) combinando los 4 clips con filtro `xfade` de 1s.
- **Impacto:** Peso reducido un 72%. Lógica JS compleja de `playlist` eliminada del index. Se usó el tag nativo `<video loop>`.

### 2. Definición del "Triángulo Operativo"
Se crearon tres documentos de control en Bloque 3:
- `RUTA_CLIENTE.md`: Mapeo del journey del cliente desde F0 (lead) hasta F10 (pago final).
- `RUTA_ARQUITECTO.md`: Flujo de diseño y uso de herramientas para cada fase interna (las que el cliente no ve).
- `RUTA_ADMIN.md`: Operaciones diarias, semanales, mensuales, anuales para sostener el taller virtual.

### 3. Fusión de Conceptualización (Pilar Algorítmico)
Se analizó la disonancia entre el `01_PROTOCOLO_CONCEPTUALIZACION.md` (puramente teórico) y el `CONTENIDO-DISEÑO` (pragmático de 17 pasos en Proyecto 1).
- Se creó `FUSION_CONCEPTUALIZACION.md` con **16 pasos**.
- **Cambios clave:** Pruebas de asoleamiento y estructura se adelantaron a la definición de escalas y materiales; se añadió una etapa explícita de "Validación del Concepto" como cortafuegos antes del Modelado.
- Se sentó la premisa de trabajo futuro: Convertir esta ruta de pasos en un **"Algoritmo de Diseño SOMA"** visual para automatizar las entradas y validaciones dejando "la creatividad como un nodo".

---

*Fin del día. La estructura conceptual está alineada con el despliegue técnico.*

---

## Sesión: 2026-06-05 — Diagnóstico del PROCESO DE DISEÑO

### 74. LOGROS DE LA SESIÓN

- **Análisis crítico del PROCESO DE DISEÑO:** Se examinó el documento empírico de Juan (`PROCESO DE DISEÑO`) y se comparó contra los 13 protocolos existentes del Bloque 2.
- **Naturaleza del documento redefinida:** Se estableció que el PROCESO DE DISEÑO no es un "cómo" sino un **índice de entregables + checklist formal + esqueleto de algoritmos**.
- **Concepto Constante vs Variable validado:** La organización de Investigación en Material Constante (clima, normas, repertorio) y Material Variable (usuario, sitio) se confirmó como eje estructural clave.
- **Contacto como paso transversal:** Se aclaró que el paso 1 es deliberadamente simple porque sus outputs viven en otros documentos (inmersión web, entrevista física).
- **Normativas específicas como Variable:** Se validó que normas de fraccionamientos/condominios son impredecibles por proyecto.
- **Diagnóstico guardado:** Se creó `DIAGNOSTICO_PROCESO_DISEÑO.md` con 16 problemas identificados (estructurales, formato, consistencia) + correspondencia con los 17 pasos de CONTENIDO-DISEÑO.
- **PROCESO DE DISEÑO formalizado como documento rector:** Se actualizó `SOMA_CORE_INDEX.md` y `SOMA_SNAPSHOT.md` para reflejar que el PROCESO DE DISEÑO es ahora el eje del Bloque 2.

### 75. ARCHIVOS CREADOS/MODIFICADOS

| Archivo | Cambio |
|---------|--------|
| `metodologia/Bloque 2 - Taller SOMA (OPERACION)/DIAGNOSTICO_PROCESO_DISEÑO.md` | **Creado** — Análisis crítico del PROCESO DE DISEÑO vs protocolos |
| `SOMA_CORE_INDEX.md` | **Modificado** — PROCESO DE DISEÑO y DIAGNOSTICO agregados como documentos principales |
| `SOMA_SNAPSHOT.md` | **Modificado** — Estado de Bloque 2 actualizado, nueva prioridad registrada |
| `BITACORA_SOMA.md` | **Modificado** — Esta entrada de sesión |

### 76. PENDIENTES (PRÓXIMA SESIÓN)

1. **[ALTA] Reestructura total de protocolos del Bloque 2** para alinearlos al PROCESO DE DISEÑO como eje rector.
2. **[ALTA] Mapear cada item del PROCESO contra protocolos existentes y faltantes.**
3. **[ALTA] Iniciar diseño del Algoritmo SOMA visual** usando el PROCESO DE DISEÑO como columna vertebral.
4. **[MEDIA] Resolver correspondencia entre CONTENIDO-DISEÑO (17 pasos) y sección 4 del PROCESO.**

---

## Sesión: 2026-06-09 — Migración a Render + PostgreSQL + Dominio propio

### 81. LOGROS DE LA SESIÓN

#### Infraestructura
- **Migración Railway → Render:** Creado `render.yaml` con web service + PostgreSQL gratis. Eliminado `railway.json`.
- **Abstracción DB (`backend/db.py`):** Capa que soporta SQLite (local) y PostgreSQL (producción) con detección automática via `DATABASE_URL`. Maneja placeholders (`?` → `%s`), funciones (`IFNULL` → `COALESCE`), y tipo de filas (dict access siempre).
- **server.py reescrito:** 30+ operaciones de BD migradas a `db.py`. Sin cambios en lógica de negocio.
- **Script de migración:** `backend/migrate_to_postgres.py` — exporta datos SQLite → PostgreSQL. Se corrigió parser de esquemas SQLite con comentarios `--`.
- **Dashboard con URLs relativas:** Usa `window.location.origin` en vez de `localhost:8080` hardcodeado.
- **Dependencias:** `psycopg2-binary` agregado a `requirements.txt`.

#### Datos
- **141 registros migrados** exitosamente de SQLite a PostgreSQL:
  - captura_web: 16, cobros: 9, programa_arquitectonico: 20
  - matriz_inversion: 26, habitantes: 2, actividades: 48, ejes_diseno: 20

#### Dominio y Email
- **Dominio registrado:** `soma-arquitectura.com` en Cloudflare (~$12/año).
- **DNS configurado:** CNAME a `soma.onrender.com` con proxy Cloudflare.
- **Custom Domain en Render:** `soma-arquitectura.com` + `www.soma-arquitectura.com` verificados.
- **Email Routing (Cloudflare → Gmail):** Correos a `@soma-arquitectura.com` redirigen a habitarq85@gmail.com.
- **SendGrid autenticado:** SPF + DKIM + DMARC configurados para `soma-arquitectura.com`. From_email actualizado a `info@soma-arquitectura.com`.
- **Web actualizada:** Email de contacto cambiado a `info@soma-arquitectura.com` en página web, lead magnet y PDF cotización.

### 82. ARCHIVOS CREADOS/MODIFICADOS

| Archivo | Cambio |
|---------|--------|
| `backend/db.py` | **Creado** — Abstracción SQLite/PostgreSQL |
| `backend/migrate_to_postgres.py` | **Creado** — Script de migración de datos |
| `render.yaml` | **Creado** — Configuración Render (web + DB) |
| `railway.json` | **Eliminado** — Ya no aplica |
| `backend/server.py` | **Modificado** — DB operations via db.py, from_email actualizado |
| `requirements.txt` | **Modificado** — +psycopg2-binary |
| `Procfile` | **Modificado** — Sin --chdir backend |
| `Dashboard.html` | **Modificado** — URLs relativas con window.location.origin |
| `Pagina Web 6.html` | **Modificado** — Email actualizado a info@soma-arquitectura.com |
| `lead_magnet_10_errores.html` | **Modificado** — Email actualizado |
| `SOLOJUAN.md` | **Modificado** — Referencia railway.app → onrender.com |
| `RUTA_CLIENTE.md` | **Modificado** — Referencia railway.app → onrender.com |
| `SOMA_CORE_INDEX.md` | **Modificado** — Prioridades actualizadas |
| `SOMA_SNAPSHOT.md` | **Modificado** — Sesión registrada con checklist |
| `BITACORA_SOMA.md` | **Modificado** — Esta entrada de sesión |

### 83. PENDIENTES (PRÓXIMA SESIÓN)

1. **[🔥 Crítica] Cerrar 1 cliente real** — Probar el ciclo completo valida o rompe supuestos.
2. **[🔥 Crítica] Conseguir RFC en RESICO** — Sin factura no hay cobro formal.
3. **[Alta] Dashboard con login** — Proteger `/dashboard` con contraseña.
4. **[Media] faster-whisper + DeepSeek** — Automatización real del análisis de entrevistas.
5. **[Media] Definir tiempos de entrega** en `TIEMPOS_ENTREGA_BASE.md` (Juan completa con su experiencia).
6. **[Media] Optimizar web: CDN Cloudflare** — Velocidad de carga en celular.

---

## Sesión: 2026-06-10 — Algoritmo SOMA Visual + Últimos Protocolos

### 84. LOGROS DE LA SESIÓN

#### Bloque 2 — Reestructura Completa
- **Últimos 5 protocolos reestructurados** al formato PROCESO DE DISEÑO 2.0:
  - `protocolo_5.3-5.11_visualizacion.md` — Exportación D5, iluminación, materiales, mobiliario, vegetación, decoración, personas, IA, postproducción
  - `protocolo_6-8_anteproyecto.md` — Planimetría básica + integral: plantas, alzados, acabados, ingenierías, planos de permiso
  - `protocolo_7.1-7.2_representacion.md` — Dossier editorial HTML + PDF con identidad SOMA
  - `protocolo_9.1-9.2_coordinacion.md` — Coordinación de especialistas externos, resolución de conflictos, bitácora
  - `protocolo_9.3_planos_tecnicos.md` — Planos ejecutivos, detalles constructivos, estructura de entrega

- **Total: 12 protocolos reestructurados** (7 de la sesión anterior + 5 de esta), todos con formato INPUT/OPERA/OUTPUT/PROC + referencias cruzadas al PROCESO DE DISEÑO 2.0.

#### Algoritmo SOMA Visual
- **Diseñado desde FUSION_CONCEPTUALIZACION.md:** Los 16 pasos de diseño se visualizaron en 4 fases (Fundamentos Conceptuales, Formalización Volumétrica, Ajuste y Precisión, Especialidades y Cierre).
- **Formato HTML interactivo:** `web/algoritmo_soma.html` con tarjetas clickeables que despliegan inputs, outputs y protocolos asociados. Etiquetas de procesador (HUMANO/AI/MIXTO). Responsive + print-friendly.
- **Formato SVG estático:** `recursos_graficos/algoritmo_soma_diagrama.svg` diseñado con la identidad visual SOMA (fondo #0a0a0a, acento #d45e2c, fases con código de color).

### 85. ARCHIVOS CREADOS/MODIFICADOS

| Archivo | Cambio |
|---------|--------|
| `03 Diseño/protocolo_5.3-5.11_visualizacion.md` | **Creado** — Visualización (exportación, iluminación, materiales, mobiliario, vegetación, decoración, personas, IA, postproducción) |
| `03 Diseño/protocolo_6-8_anteproyecto.md` | **Creado** — Anteproyecto (planimetría básica + integral, planos de permiso) |
| `03 Diseño/protocolo_7.1-7.2_representacion.md` | **Creado** — Representación (dossier HTML + PDF) |
| `03 Diseño/protocolo_9.1-9.2_coordinacion.md` | **Creado** — Coordinación de ingenierías |
| `03 Diseño/protocolo_9.3_planos_tecnicos.md` | **Creado** — Planos técnicos ejecutivos |
| `web/algoritmo_soma.html` | **Creado** — Visualización interactiva del Algoritmo SOMA |
| `recursos_graficos/algoritmo_soma_diagrama.svg` | **Creado** — Diagrama SVG del Algoritmo SOMA |
| `SOMA_SNAPSHOT.md` | **Modificado** — Nueva sesión registrada |
| `SOMA_CORE_INDEX.md` | **Modificado** — Algoritmo SOMA visual marcado como completado |
| `BITACORA_SOMA.md` | **Modificado** — Esta entrada de sesión |

### 86. PENDIENTES (PRÓXIMA SESIÓN)

1. **[Alta] Mapear items del PROCESO 2.0 contra codebase real** (Activity Matrix, Diagrama SOMA, Dashboard).
2. **[Alta] Integrar biblioteca SOMA en template de proyecto** — Flujo automático de copia de normativas/clima/patrones.
3. **[Media] Activar Google My Business** y subir renders como fotos de perfil.
4. **[Media] Publicar lead magnet** como pop-up en la web.
5. **[Media] Resolver bug cotizador** — Botón oculto en landscape mobile + página trabada en "Enviar".

---

## Sesión: 2026-06-23 — Dashboard: Scroll modal, Salarios, Fondos, Algoritmo estación 1

### 87. LOGROS DE LA SESIÓN

- **Fix scroll modal:** `document.body.style.overflow = 'hidden'` se restaura al cerrar cualquier modal (ui.js). Bug que dejaba la página estática sin scroll.
- **Egresos filtrados por período:** Bloque 02 ahora usa el selector de mes/año (period-mes/period-ano) en lugar de `new Date()`. La tabla y total cambian al cambiar el período en Bloque 01.
- **Salarios en Bloque 02:** Nuevo sub-apartado con registro y tabla separada. Usa categoría "Salario" en la tabla `egresos`. Los salarios se excluyen de la tabla de Gastos Operativos para no duplicarse.
- **Fondos de Reemplazo:** Movido de Bloque 03 independiente a sub-apartado dentro de Bloque 02. Se eliminó la sección "Aportar/Retirar" y se agregó un campo de aportación directa en cada tarjeta de fondo. El balance total se muestra en la cabecera de la sección.
- **Algoritmo SOMA filtro:** Ahora muestra proyectos de todos los estados del pipeline (lead→terminado), no solo Momento 2.
- **Estación 1 del Algoritmo simplificada:** Reducida a 2 tarjetas (1.1 Contacto con el candidato, 1.2 Llenado de programa). Los datos reales se inyectan en un grid informativo debajo.

### 88. CAMBIOS EN ARCHIVOS

| Archivo | Cambio |
|---------|--------|
| `web/js/ui.js` | **Modificado** — Restaura scroll al cerrar modales |
| `web/js/egresos.js` | **Modificado** — Filtra por período y excluye salarios de gastos operativos; nuevas funciones `loadSalarios`, `registrarSalario`, `eliminarSalario` |
| `web/js/fondos.js` | **Modificado** — Eliminadas funciones `apartar`/`retirar`; agregada `aportar` directa por tarjeta |
| `web/js/app.js` | **Modificado** — `cambiarPeriodo()` llama `App.refresh()`; carga `loadSalarios()` |
| `web/dashboard.html` | **Modificado** — Salarios y Fondos como sub-apartados dentro de Bloque 02; eliminado Bloque 03 |
| `web/css/dashboard.css` | **Modificado** — Estilos para `.block-divider` y `.fund-aportar` |
| `backend/server.py` | **Modificado** — Fondo acumulado agregado a métricas (opcional) |
| `web/algoritmo_soma.html` | **Modificado** — Filtro incluye todos los estados; Estación 1 simplificada a 2 tarjetas |
| `AGENTS.md` | **Modificado** — Sesión registrada |

### 89. PENDIENTES (PRÓXIMA SESIÓN)

1. **[Alta] Revisar inconsistencias en el flujo de trabajo del Algoritmo SOMA**.
2. Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD.
3. Lead magnet — decidir ubicación en página web.

---

## Sesión: 2026-06-25 — Algoritmo SOMA: Estación 2-3, Guía de Visita, Programa Arquitectónico

### 90. LOGROS DE LA SESIÓN

- **2.2.1 Datos del Cliente reorganizado** en dos tarjetas: 2.2.1.1 Datos de Inmersión (expediente) + 2.2.1.2 Datos de Entrevista (síntesis cliente → `datos_cliente_sintetico.txt`). Eliminada tarjeta dinámica "Respuestas de Inmersión Web".
- **Guía de Entrevista → Guía de Visita**: `guia_visita.html` unifica checklists de sitio (2.2.2: terreno, elementos interiores, exteriores) y ambientales (2.2.4: ruido, olores) con los 6 tópicos de entrevista.
- **Análisis Procesado eliminado** de Estación 3 (`renderAnalisisReal()` removida).
- **Programa Real dentro de tarjeta 3.3** (`renderProgramaReal()` inyecta en el detalle de 3.3, no como tarjeta independiente).
- **Programa Arquitectónico editable**: Nueva ruta `GET /programa/<id>/html` con tabla de 9 columnas (CLAVE, ZONA, ESPACIO, M², TIPO, AFORO, MOBILIARIO, INSTALACIONES, ADYACENCIAS). Formato SOMA dark. Campos editables: aforo (number), mobiliario, instalaciones. Adyacencias readonly (solo desde Diagrama 3.4). Botón EXPORTAR PDF.
- **Batch-update**: `POST /programa/<id>/batch-update` guarda todos los campos editables. Columna `instalaciones` agregada a `programa_arquitectonico` con migración automática en `init_db()`.
- **Heurísticas de sugerencia eliminadas**: Ya no se intenta adivinar aforo/mobiliario por nombre de espacio — el arquitecto llena manualmente.
- **Zona/TIPO legibles**: texto oscuro sobre fondos pastel en ZONA; labels completos ("✔ Deseado", "+ Comp.", "★ Lujo") en TIPO.
- **Deploy a Render**: commit 93c389e → push a main.

### 91. ARCHIVOS CREADOS/MODIFICADOS

| Archivo | Cambio |
|---------|--------|
| `web/js/algoritmo.js` | **Creado** — Lógica del Algoritmo SOMA (tarjetas, diagrama, programa) |
| `web/css/algoritmo.css` | **Creado** — Estilos del Algoritmo SOMA |
| `web/guia_visita.html` | **Creado** — Guía unificada de visita (checklist sitio + ambientales + 6 tópicos) |
| `web/algoritmo_soma.html` | **Modificado** — Reorganización de tarjetas, botones a expediente/guía/programa |
| `backend/server.py` | **Modificado** — Nuevas rutas programa/html y programa/batch-update; migración instalaciones; init_db actualizado |
| `metodologia/…/PROCESO DE DISEÑO 2.0` | **Modificado** — 1.2 renombrado "Visita en Campo", referencias actualizadas |
| `metodologia/…/protocolo_2.2.1.2_entrevista_inmersion.md` | **Modificado** — Renombrado como protocolo de Visita con checklists sitio + ambientales |
| `AGENTS.md` | **Modificado** — Sesión registrada |
| `SOLOJUAN.md` | **Modificado** — Instrucciones literales de la sesión |
| `SOMA_SNAPSHOT.md` | **Modificado** — Nueva sesión registrada |
| `BITACORA_SOMA.md` | **Modificado** — Esta entrada de sesión |

### 92. PENDIENTES (PRÓXIMA SESIÓN)

1. Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
2. Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación
3. Lead magnet — decidir ubicación en página web

---

## Sesión: 2026-06-27 — Cloudflare Worker Keep-Warm + Token Workers Deploy

### 93. LOGROS DE LA SESIÓN

- **Cloudflare Worker keep-warm desplegado:** `soma-keep-warm` en `https://soma-keep-warm.habitarq85.workers.dev` con cron `*/5 * * * *` (cada 5 minutos) que pinguea `soma-853c.onrender.com` para evitar que Render se duerma por inactividad.
- **Token Cloudflare creado:** `SOMA Workers Deploy` con permisos `Workers Scripts -> Edit` + `User Details -> Read`.
- **Estructura:** `workers/keep-warm/wrangler.toml` + `src/index.js` en el repo.
- **Verificación:** Endpoint `GET /__ping` responde `Render status: 200`.
- **Documentos actualizados:** AGENTS.md, SOMA_SNAPSHOT.md, SOMA_CORE_INDEX.md, BITACORA_SOMA.md.

### 94. ARCHIVOS CREADOS/MODIFICADOS

| Archivo | Cambio |
|---------|--------|
| `workers/keep-warm/wrangler.toml` | **Creado** — Configuración Wrangler con account_id + cron cada 5 min |
| `workers/keep-warm/src/index.js` | **Creado** — Worker que pinguea Render (cron + fetch handler) |
| `AGENTS.md` | **Modificado** — Sesión 27 Jun registrada |
| `SOMA_SNAPSHOT.md` | **Modificado** — Nueva sesión + última actualización 27/06/2026 |
| `SOMA_CORE_INDEX.md` | **Modificado** — Bloque 7 (Infraestructura) agregado |
| `BITACORA_SOMA.md` | **Modificado** — Esta entrada de sesión |

### 95. PENDIENTES (PRÓXIMA SESIÓN)

1. Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
2. Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación
3. Lead magnet — decidir ubicación en página web

---

## SESIÓN 03/07/2026 — MIGRACIÓN A SUPABASE (IPv6 → POOLER IPv4)

### 96. CONTEXTO

Render PostgreSQL inyectaba `DATABASE_URL` con valor malformado (`DATABASE_URL=postgresql://...`). Se decide migrar a Supabase. Primer intento falla porque Supabase free tier solo expone IPv6 y Render no puede enrutar a `2600:1f18::`.

### 97. PROBLEMAS ENCONTRADOS

| # | Problema | Síntoma | Solución |
|---|----------|---------|----------|
| 1 | `DATABASE_URL` malformada por Render | `invalid dsn: invalid connection option "DATABASE_URL"` | Eliminar DB de Render + stripping de `KEY=` prefix en `_get_db_url()` |
| 2 | Supabase solo IPv6 | `connection to server at ... failed: Network is unreachable` | Usar **connection pooler** `aws-0-us-east-1.pooler.supabase.com:6543` (tiene IPv4) |
| 3 | `pgbouncer=true` no válido | `invalid URI query parameter: "pgbouncer"` | Quitar `pgbouncer=true`, psycopg2 no lo reconoce |
| 4 | Render no lee `render.yaml` | `SUPABASE_URL` no aparecía en logs | Variables de Dashboard sobreescriben `render.yaml` — se fija valor exacto en Dashboard |

### 98. CAMBIOS REALIZADOS

| Archivo | Cambio |
|---------|--------|
| `backend/db.py` | `_get_db_url()` prueba SUPABASE_URL primero, luego DATABASE_URL. Si el valor empieza con `KEY=`, lo limpia. Debug logging de env vars. |
| `backend/server.py` | `use_pg` verifica `SUPABASE_URL or DATABASE_URL` |
| `render.yaml` | `SUPABASE_URL` apunta al pooler: `postgresql://postgres.dejojumyyydrlqoegqnf:...@aws-0-us-east-1.pooler.supabase.com:6543/postgres?sslmode=require` |
| `workers/keep-warm/src/index.js` | Agregado ping a `https://dejojumyyydrlqoegqnf.supabase.co` para evitar pausa por inactividad |
| `.env` | URL pooler + `CLOUDFLARE_API_TOKEN` guardado |
| `start.sh` | WhatsApp Baileys eliminado |

### 99. CONEXIÓN FINAL (Pooler IPv4)

```
Host: aws-0-us-east-1.pooler.supabase.com
Port: 6543
User: postgres.dejojumyyydrlqoegqnf
SSL: require
Database: postgres
```

### 100. LOGROS DE LA SESIÓN

- **Render DB eliminada** — ya no inyecta `DATABASE_URL` malformada
- **Supabase pooler con IPv4** — Render conecta sin problema
- **Deploy exitoso** — clientes visibles en dashboard, datos accesibles
- **Cloudflare Worker actualizado** — pinguea Supabase cada 5 min
- **Token guardado** en `.env` para futuros deploys

### 101. ARCHIVOS CREADOS/MODIFICADOS

| Archivo | Cambio |
|---------|--------|
| `backend/db.py` | **Modificado** — KEY= stripping + debug |
| `backend/server.py` | **Modificado** — use_pg con SUPABASE_URL |
| `render.yaml` | **Modificado** — URL pooler IPv4 |
| `.env` | **Modificado** — Token + URL pooler |
| `workers/keep-warm/src/index.js` | **Modificado** — Ping a Supabase |
| `AGENTS.md` | **Modificado** — Sesión 03 Jul |
| `SOMA_SNAPSHOT.md` | **Modificado** — Nueva sesión |
| `SOMA_CORE_INDEX.md` | **Modificado** — Bloque infraestructura |

### 102. PENDIENTES (PRÓXIMA SESIÓN)

1. Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
2. Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación
3. Lead magnet — decidir ubicación en página web
