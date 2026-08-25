# Contexto de Sesión — Algoritmo SOMA

## Sesión: 25 Ago 2026 ✅ — Menú de navegación minimalista en la web pública (hamburguesa arriba-derecha + panel desplegable sutil)

### Bitácora del día
1. **Servidor local levantado** con el comando de siempre (`systemd-run --user --unit=soma-flask ...` en `localhost:8080`).
2. **Menú de navegación para las 5 secciones** de `web/Pagina Web 6.html`:
   - **Ids ancla agregados**: `#inicio` (hero), `#portafolio`, `#trayectoria`, `#filosofia`, `#servicios`.
   - **Logo minimalista sin fondo circular**: solo 3 líneas finas (1.5px, 20px). Sobre fondos oscuros se ven claras y sobre claras se invierten solas vía `mix-blend-mode: difference`. Al abrirse se transforman en **X terracota** (`var(--accent)` con `mix-blend-mode: normal`) — visible sobre cualquier sección.
   - **Panel desplegable pequeño y sutil** (~125×170px) anclado bajo el botón: fondo `rgba(10,10,10,0.18)` (18% opacidad, ajustado por Juan desde 0.45→0.5→0.25→0.18) + `blur(10px)`, esquinas redondeadas, textos JetBrains Mono 0.62rem uppercase alineados a la derecha. Aparición escalonada de los enlaces.
   - **Posición final**: fijo arriba-derecha (`top: 22px; right: 32px`), con su eje vertical **alineado exactamente con el centro del botón circular Cotizador SOMA** inferior (verificado: diff = 0px). Juan primero lo pidió a la izquierda y luego lo regresó a la derecha.
   - **Enlaces**: Inicio, Proyectos, Evolución, Filosofía, Servicios (Juan pidió quitar "Inicio", lo vio como "logo dinámico" y pidió restaurarlo).
   - **JS**: toggle con `aria-expanded`, scroll suave con `scrollIntoView({behavior:'smooth'})` dentro del contenedor scroll-snap, cierre con Esc / clic fuera / selección. El panel queda bajo los modales (z-index 1550/1600 vs modales 2000+).
3. **Duda sobre Supabase pausada**: Juan recibió correo de advertencia de inactividad. Verificado en vivo que el keep-warm sigue funcionando (`__health` → db ok/postgres, `/keepwarm` → OK). Explicación: huecos cuando Render suspende el servicio al agotar 750 h/mes — no hace falta meter cotizaciones de prueba, el `SELECT 1` cada 5 min ya cuenta como actividad. Pendiente raíz: revisar Usage en Render.
4. **Push a GitHub** (commit `d054c08`, solo `web/Pagina Web 6.html`; los no rastreados quedaron fuera por decisión de Juan).

### Archivos creados/modificados
- `web/Pagina Web 6.html` — CSS del menú (toggle + panel), HTML del botón/nav con ids en secciones, JS de toggle/navegación.

### Próxima sesión
- Verificar el menú en el celular de Juan (A12) y en vivo tras deploy de Render.
- Investigar el límite de horas de Render Free (panel → Usage); decidir plan de pago (~$7 USD/mes) o mover estáticos a Cloudflare Pages.
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD.
- Lead magnet — decidir ubicación en página web.

---

## Sesión: 14 Ago 2026 ✅ — Fix carrusel en landscape verificado en celular, efecto imagen+título completado, y servicios/contacto compactos en celular horizontal (incluye push de cotizadores a GitHub y diagnóstico de cold start)

### Bitácora del día
1. **Push a GitHub del trabajo acumulado de cotizadores** (commit `ce7b91d`, solo los 6 archivos modificados — el resto quedó sin rastrear por decisión de Juan). El push falló una vez con `gnutls_handshake() failed: The TLS connection was non-properly terminated` y se resolvió reintentando con `sleep 2`.
2. **Diagnóstico del "constructor" matutino de Render**: la página tardó en cargar mostrando el spinner de Render. Verificado en vivo: worker `soma-keep-warm` (`__health`) → `{status: ok}` con server/db/brevo OK; Render `/health` → HTTP 200 en ~1.5s; wrangler autenticado y cron `*/5 * * * *` configurado. **Los workers de Cloudflare NO están fallando.** Causa más probable: Render Free tier (750 h/mes) — el keep-warm 24/7 consume ~744 h/mes y al agotarse el cupo Render suspende el servicio hasta el siguiente ciclo, produciendo cold start al entrar por la mañana. Sin token de API de Render en `.env` no se puede consultar el uso de horas por CLI.
3. **Fix: carrusel de proyectos cortado en celular horizontal** (reporte de Juan: el carrusel quedaba muy abajo y lo cortaba la parte inferior). Causa: en landscape el slide vertical (150×267) definía la altura del carrusel (~287-307px) que sumada al título (`padding-top: 6vh` inline) excedía el alto del viewport (360-430px). Fix en `@media (max-height: 520px)`:
   - Slide vertical de la sección 2: `150×267` → **`120×200px`**.
   - Sección 2: `justify-content: center !important; padding-top/bottom: 0 !important`.
   - Título: `> div:nth-of-type(2) { padding-top: 0 !important }` (anula el 6vh inline).
   - Verificado con Puppeteer (scroll real en `#main-viewport`, no `scrollIntoView` que se engaña con el scroll-snap): 667×375, 740×360, 844×390, 932×430 → carrusel visible completo (`fits: true`). Desktop/tablet y vertical sin cambios.
   - Commit `bef0557` pusheado a `origin/main`.
4. **Fix carrusel landscape verificado en el celular de Juan (Samsung Galaxy A12)** y pulido del efecto:
   - **Títulos enormes/solapados en landscape ancho** (844/932px): la regla `max-width: 768px` no aplica a anchos mayores, así que el `.slide-title` base (0.65rem) se veía grande. Se añadieron reglas compactas en `@media (max-height: 520px)`: `.slide-title` 0.5rem con fondo oscuro redondeado abajo-izquierda, y el **efecto naranja** `background: var(--accent)` + `opacity: 1` en `.slide.revealed .slide-title`.
   - **Imagen "estática" en landscape ancho**: causa raíz = `@media (hover: none)` dejaba la imagen no-revelada en `grayscale(0.4)/opacity(0.8)`, haciendo imperceptible el cambio al revelar. Fix: en el bloque landscape, `section:nth-of-type(2) .slide img` ahora parte de `grayscale(0.8)/opacity(0.6)` con `transform: scale(0.9)` y `transition` completa (filter+opacity+transform) — el efecto queda idéntico al vertical y laptop. Verificado con estilos computados iguales en 844×390, 667×375 y 390×844.
   - Commit `05c57c9` pusheado a `origin/main`.
5. **Servicios/Contacto compactos en celular horizontal** (reporte de Juan: la sección no cabía completa en su A12 en landscape). Root cause: el contenido apilado (menú 40px + visual 230px + contacto) excedía el alto efectivo del viewport cuando la barra del navegador Android está visible (~300px). Fix en `@media (max-height: 520px)`:
   - `.services-row` en **2 columnas** (`minmax(150px,1fr) 2fr`) con menú a la izquierda y visual a la derecha (antes 1 columna apilada) → ahorra ~44px de alto.
   - **Cotizadores compactos**: `.services-visual` 210px, imagen 150px, `.render-cotizador` padding 6px/10px y `min-height` 200px, h3/rc-sub/rc-opt/rc-mini/rc-total/rc-btn-quote/rc-input reducidos para que el panel quepa dentro del visual sin montarse (BIM 200px, Planos 203px).
   - Verificado con Puppeteer en 800×360, 800×300, 667×375 y 568×320 con los **4 cotizadores abiertos**: contacto cabe (fits), cotizador dentro del visual (`cotEnVisual OK`, sin scroll interno `scrollH < clientH`), sin solapamientos entre h3/rc-sub/rc-grid/rc-block/rc-total/rc-term-hint, sin scroll horizontal, secciones de 360px exactos.
   - Commit `d077a87` pusheado a `origin/main`.

### Archivos creados/modificados
- `web/Pagina Web 6.html` — fix carrusel landscape (3 líneas CSS en `@media (max-height: 520px)`), efecto completo imagen+título, servicios 2 columnas + cotizadores compactos en landscape.
- `AGENTS.md` — Esta entrada.
- `BITACORA_SOMA.md`, `SOMA_SNAPSHOT.md`, `SOMA_CORE_INDEX.md` — Actualizados.

### Próxima sesión
- Revisar en el celular de Juan el fix de servicios/contacto en landscape (A12) tras recargar con Ctrl+Shift+R.
- Investigar el límite de horas de Render Free: revisar en el panel de Render → Usage; si está al tope, evaluar plan de pago de Render (~$7 USD/mes) o mover la parte estática a Cloudflare Pages.
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD.
- Lead magnet — decidir ubicación en página web.

---

## Sesión: 13 Ago 2026 ✅ — Cotizadores BIM y Planos alineados en grid (mismo criterio que el de renders) y botón COTIZADOR SOMA robusto en móvil

### Bitácora del día
1. **BIM y Planos convertidos a grid de botones uniformes** (mismo criterio que el cotizador de renders): ambos ahora usan `.rc-grid` con botones del mismo ancho/altura (30px), alineados y dentro del borde.
   - BIM: `.rc-grid-4` (4 columnas) — Tipo de proyecto (4 btns), luego "Disciplina" (span-2) + "Superficie" (span-2) con campo `rc-field rc-span-2` (input+m²).
   - Planos: `.rc-grid` (3 columnas) con `.plano-grid` (gap 6px) — "Tipo de proyecto" (span-2) + campo Superficie (span-1, `rc-cell` input 62×22px), luego 3 btns tipo, luego "Complejidad del proyecto" (span-3), luego 3 btns complejidad.
   - Se corrigió un bug en planos: el primer armado perdió el botón COMERCIAL y excedía el borde (337px). Ahora con "Superficie" en la fila 1 y el campo compacto el panel mide **289px desktop** (dentro de 290) y **292px tablet/móvil** (dentro de 320).
   - `bimSelect` y `planoSelect` ahora usan `data-grp` (como `rcSelect`) para agrupar botones independientemente del contenedor.
   - Verificado en 4 viewports (1366/768/390/480): los 3 cotizadores caben en el contenedor y los botones son uniformes por grupo.
2. **Botón COTIZADOR SOMA robusto en móvil** (reporte de Juan: se veía más ancho que la imagen y tardaba en desaparecer al cambiar de servicio):
   - `.sv-caption` ahora tiene `max-width: 150px; overflow: hidden; box-sizing: border-box; transition: none` + `opacity: 0` + `pointer-events: none` cuando está oculto (`.show` los activa).
   - `.sv-btn` con `max-width: 150px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap` para que el texto nunca desborde los 150px de la imagen (incluso si JetBrains Mono no carga).
   - Regla de refuerzo `.services-visual.cotizador-on .sv-caption { visibility: hidden !important }` — el botón se oculta al instante al entrar a cualquier cotizador, sin depender del JS.
   - `backdrop-filter` eliminado en los breakpoints móviles (768px, 480px y max-height 520px) por lentitud de render en Android.
   - En 480px se redujo el botón a `font-size: 0.45rem; letter-spacing: 1.5px; padding: 7px 8px`.
   - Verificado en 320/360/375/390px: botón 150px = imagen 150px, `scrollWidth=150` (sin desborde), desaparición instantánea (60ms, transición none).

### Archivos creados/modificados
- `web/Pagina Web 6.html` — grids de BIM/Planos, `data-grp` en bimSelect/planoSelect, botón COTIZADOR SOMA robusto, backdrop-filter off en móvil.
- `AGENTS.md` — Esta entrada.
- Scripts de prueba temporales en `recursos_graficos/material_instagram/` eliminados.

### Próxima sesión
- Verificar en el celular de Juan (reporte original: botón ancho y desaparición tardía).
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD.
- Lead magnet — decidir ubicación en página web.

---

## Sesión: 13 Ago 2026 ✅ — Cotizador de renders rediseñado (sin Aéreo, "Nivel de ambientación", tooltips), sección Servicios estática y contacto visible en pantalla

### Bitácora del día
1. **Imagen de servicios recuperó su proporción**: en lugar de estirarse a 420×290 (tamaño de los cotizadores), la imagen ahora se centra en su proporción original (150×210) dentro del contenedor transparente 420×290 (desktop) / 320px alto (móvil). El layout no cambia al alternar servicios.
2. **Contacto visible al final del scroll**: ajustados `section:last-of-type` padding de `8vh 10% 6vh` → `5vh 10% 4vh` y `.contacto-block` margin-top de `clamp(5vh,8vh,12vh)` → `clamp(2vh,4vh,6vh)`. Verificado: con scroll al máximo el contacto queda dentro de pantalla con espacio abajo — desktop 126px, móvil 161px (antes quedaba ~68px fuera de la pantalla porque el scroll-snap dejaba la sección a 194px del top).
3. **Botón "COTIZADOR SOMA" justo debajo de la imagen**: `.sv-caption` se movió DENTRO de `#services-visual` y ahora es `position: absolute; top: calc(50% + 105px)` (borde inferior de la imagen 210px centrada), centrado con `left: 50%; translateX(-50%)`. En los breakpoints móviles la imagen pasa de `height: 100%` (se estiraba a 318px) a `height: 210px` fija para mantener la proporción y dejar el hueco del botón. Solo se muestra en Diseño (índice 0, `toggle('show', index===0)`); en cotizadores queda oculto y no interfiere con el panel (que sobresale ~9px por `overflow: visible`). Verificado: `gapImgBtn = 0px` en desktop y móvil, contacto sigue cabiendo.
4. **Bloque de servicios subido y borde del contenedor transparente**: `section:last-of-type` padding `5vh 10% 4vh` → `1vh 10% 1vh` (desktop) y el breakpoint `max-width: 768px` de `6vh 4% 6vh` → `1vh 4% 2vh`; margen del `.contacto-block` reducido (`clamp(2vh,4vh,6vh)` → `clamp(1vh,2vh,3vh)` desktop; 8vh→4vh, 6vh→3vh, 4vh→2vh en breakpoints móviles). Contacto queda con ~162px de espacio abajo en desktop y ~190px en móvil. El borde de `.services-visual` cambió de `rgba(255,255,255,0.05)` a `transparent` — en Diseño ya no se ve la rejilla; en cotizadores sigue el borde terracota (`border-color: var(--accent)`).
5. **Label bajado, título pegado al menú y contacto con más aire**: `section:last-of-type` padding-top `1vh` → `3vh` (label a 23px del borde, antes 8px). Se eliminó el `<p>` vacío que separaba título y menú, y se corrigieron los selectores `.services-wrapper > div > div:last-child` → `.contacto-block` (la regla daba `margin-top: 45px` y `padding-left: 25px` al `.services-row`, empujando todo el grid hacia abajo). `.services-row` ahora `align-items: start` (antes center) para que el menú quede arriba alineado con el cotizador. Resultado: hueco título→menú 170px→15px, contacto con **242px** de aire abajo (desktop) y **291px** (móvil). Verificado en D5/BIM/Planos/Diseño y viewports 1366/1024/390.
6. **Sección de servicios centrada verticalmente**: `section:last-of-type` cambia de `justify-content: flex-start` → `center` (desktop y breakpoint móvil `padding: 2vh 4%`), logrando espacios superior e inferior **iguales** en los viewports normales: 132px=132px (desktop 768 y tablet 1024), 149px=150px (móvil 390×844), 123px=124px (móvil 480). En landscape (390px de alto) el contenido excede la pantalla y el label queda parcialmente cortado arriba (caso límite preexistente), contacto siempre visible.
1. **Cotizador de renders rediseñado** (petición de Juan): botón AÉREO eliminado (solo INTERIOR/EXTERIOR), "Complejidad" → "Nivel de ambientación" (BÁSICO/MEDIO/ALTO ×0.8/1.0/2.5), botones uniformes estilo calculadora (tipo 2 cols, nivel 3 cols). `RENDER_PRECIOS = { interior: 2500, exterior: 3000 }`.
2. **Tooltips por tipo** (`RENDER_TIPS` + `actualizarTipsRender()`): los tooltips de BÁSICO/MEDIO/ALTO cambian según interior/exterior al hacer clic.
3. **Alturas de cotizadores igualadas**: eliminado `#render-cotizador .rc-block { flex-direction: column }` que hacía el panel de renders 60px más alto. Los 3 paneles miden 290px (desktop) / 292px (móvil).
4. **Contenedor visual de tamaño fijo**: `.services-visual` siempre 420×290 (desktop) / 320px alto (móvil). `.sv-caption` usa `visibility` para reservar espacio sin salto.
5. **Menú y contacto estáticos** al alternar los 4 servicios: verificado en 7 viewports (1366, 1024, 834, 768, 390×844, 844×390, 667×375), sin errores JS ni overflow.
6. **Móvil**: `.rc-opts.four` fijo en `repeat(4, 1fr)` (el wrap a 2 cols hacía el BIM 320px vs 282px), min-height panel 292px.

### Archivos creados/modificados
- `web/Pagina Web 6.html` — rediseño cotizador de renders (HTML+JS+CSS), contenedor visual fijo, breakpoints móvil/landscape.
- `BITACORA_SOMA.md` — Entrada de sesión.

### Próxima sesión
- Revisar el cambio en vivo tras deploy a Render.
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Lead magnet — decidir ubicación en página web

---

## Sesión: 13 Ago 2026 ✅ — Ajustes de cotizadores a medio camino: regla BIM alineada a m², copy D5 a "renders", limpieza de imágenes de servicios

---

## Sesión: 11 Ago 2026 ✅ — Cotizadores D5 + BIM LOD 300 + Planos Ejecutivos: actividades y precios definidos

### Bitácora del día
1. **Cotizador D5 (Visualización) terminado**: botón "VER COTIZACIÓN" con validación de contacto real (correo válido o teléfono ≥10 dígitos), total oculto hasta presionar, POST `/cotizar_perspectivas` → correo a `habitarq85@gmail.com` vía Brevo.
2. **Cotizador BIM LOD 300 (nuevo)** en sección Servicios (index 2 en `changeService`):
   - Precios base por m² (rango bajo del mercado): Vivienda **$90**, Residencial **$110**, Comercial **$130**, Industrial **$150**.
   - Disciplinas: **solo Arquitectura y Estructura, mismo precio, sin MEP**.
   - Descuentos por volumen: >500 m² −5%, >1,000 m² −10%. Tarifa mínima **$12,000 MXN**.
   - Entregable: **solo archivo Revit (RVT)** (se quitó DWG/PDF).
   - Backend: endpoint público **`POST /cotizar_bim`** (espejo de `/cotizar_perspectivas`), correo confirmado (`email: sent`).
3. **Análisis crítico de los cotizadores** (formas de pago y tiempos) + investigación de mercado 2026 (Budgeto MX, Carnet 3D, myarchitectai, ENGINYRING, Arrival 3D, GCC).
4. **Tiempos de entrega actualizados** a referencia de mercado (el compromiso real se cierra en la entrevista de alcance):
   - D5: 3–5 días hábiles/vista · 3–5 vistas 1–2 semanas · 6+ vistas 2–3 semanas.
   - BIM: 2–3 semanas ≤1,000 m² · 3–4 semanas 1,000–3,000 m² · 4–6 semanas >3,000 m².
5. **Esquema de pago dinámico**: **50/50** si total < $15,000; **30/40/30** si ≥ $15,000 (umbral definido por Juan). Solo transferencia.
6. **IVA explícito**: los totales ahora muestran **"+ IVA"** (antes "no incluye IVA" ambiguo).
7. **Verificación**: `/cotizar_bim` probado localmente → `email: sent`, reporte correcto en `backend/reportes/`.
8. **Cotizador PLANOS EJECUTIVOS (nuevo, sin industrial)** en sección Servicios (index 3 en `changeService`; reemplaza a "PLANOS DE ANTEPROYECTO", que se eliminó de la lista):
   - Precios base por m² (validados contra mercado 2026: Arqbeat, Resendiz, Arqzon, PE BIM, Cronoshare Mérida): Vivienda **$130**, Residencia **$160**, Comercial **$190**. **Sin industrial/naves industriales** (decisión de Juan).
   - Complejidad del proyecto: Simple ×0.85 · Estándar ×1.0 · Complejo ×1.6.
   - Descuentos por volumen: >300 m² −5%, >600 m² −10%. Tarifa mínima **$10,000 MXN**.
   - Entregables: planos en **PDF y DWG** (plantas, cortes, fachadas, acabados, carpinterías/cancelería, detalles, especificaciones).
   - Tiempos (referencia): 3–4 semanas ≤300 m² · 4–6 semanas 300–600 m² · 6–8 semanas >600 m².
   - Backend: endpoint público **`POST /cotizar_planos`** (espejo de `/cotizar_bim`).
9. **Estilo visual de los 3 cotizadores (D5, BIM, Planos)**: fondo pasa de negro `#1a1a1a` a **panel semitransparente** `rgba(168,62,24,0.35)` con `backdrop-filter: blur(4px)` (igual que el botón de cotizador del servicio Diseño), con `#services-visual.cotizador-on` transparente para que el blur tome el fondo terracota. Textos que usaban `--accent` (h3, total, botón, hint) reescritos a tono claro `#ffd2bd` para contraste.

### Archivos creados/modificados
- `web/Pagina Web 6.html` — cotizador BIM LOD 300 (HTML+JS), `changeService` index 2, tiempos de mercado, esquema de pago dinámico, "+ IVA", entregable solo RVT.
- `backend/server.py` — endpoint `POST /cotizar_bim` + `public_paths` actualizado.
- `web/Pagina Web 6.html` — cotizador Planos Ejecutivos (HTML+JS), `changeService` index 3, reemplaza a "PLANOS DE ANTEPROYECTO" (eliminado), tiempos de mercado, pago dinámico, + IVA.
- `backend/server.py` — endpoint `POST /cotizar_planos` + `public_paths` actualizado.
- `AGENTS.md`, `BITACORA_SOMA.md`, `SOMA_SNAPSHOT.md`, `SOMA_CORE_INDEX.md` — Actualizados.

### Próxima sesión
- Continuar con la web: revisar los cotizadores en vivo y pulir copy de Servicios.
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Lead magnet — decidir ubicación en página web

---

## Sesión: 07 Ago 2026 ✅ — Rediseño de Servicios e Integración de Mini-Cotizador D5 en Web Local

### Bitácora del día
1. **Reordenamiento**: Mover "VISUALIZACIÓN ARQUITECTÓNICA D5 RENDER" a la posición 2 en la lista de servicios (después de Diseño Arquitectónico).
2. **Mini-Cotizador D5**: Implementado en la zona visual de servicios cuando se selecciona Visualización. Los demás servicios siguen mostrando su imagen correspondiente de forma instantánea.
3. **Precios y Reglas (Ajuste Mérida)**:
   - Base por vista: Interior $2,500, Exterior $3,000, Aéreo $4,500.
   - Complejidad renombrada a tipo de proyecto para mayor claridad: Vivienda (×1.0), Residencia (×1.5), Comercial (×2.0).
   - Paquete de vistas: 3-5 vistas (-10%), 6+ vistas (-15%).
   - Animación opcional: $700/segundo (mínimo 10s).
   - Se removió la distinción por calidad (Estándar/Premium) y el botón directo de WhatsApp a petición del usuario.
4. **Desborde Solucionado**: Corregido bug donde la transición del contenedor `max-width` en desktop provocaba un desborde temporal hacia el borde derecho de la pantalla (ahora la expansión del contenedor es instantánea al hacer clic y la animación del cotizador es únicamente por opacidad fade sin desplazamiento físico).
5. **Términos y condiciones**: Agregada la leyenda legal indicando que la cotización final se confirmará tras la entrevista de alcance.
6. **Validación responsive**: Verificada la maquetación y el cálculo en PC (340px derecha), tablet (baja y ajusta), móvil vertical y horizontal sin scroll horizontal.

### Archivos creados/modificados
- `web/Pagina Web 6.html` — servicios ordenados, HTML/JS/CSS del mini-cotizador D5, fixes responsive.

## Estado del Proyecto
- ✅ **DASHBOARD funcional**: Pipeline completo (3 momentos), expediente, PDFs, métricas, auth.
- ✅ **Cotizadores en web (D5 + BIM LOD 300 + Planos Ejecutivos)**: Servicios muestran mini-cotizadores interactivos con validación de contacto, precio oculto hasta presionar y correo a `habitarq85@gmail.com` vía Brevo.
  - **D5 (Visualización)**: Interior $2,500 · Exterior $3,000 · Aéreo $4,500 por render. Complejidad ×0.8 (Básico)/×1.0 (Medio)/×2.5 (Cargado). Paquete 3-5 renders −10%, 6+ −15%. Endpoint `/cotizar_perspectivas`.
  - **BIM LOD 300**: Vivienda $90 · Residencial $110 · Comercial $130 · Industrial $150/m². Solo Arq/Est (sin MEP), mismo precio. >500 m² −5%, >1,000 m² −10%, mínimo $12,000. Entregable: Revit (RVT). Endpoint `/cotizar_bim`.
  - **Planos Ejecutivos**: Vivienda $130 · Residencia $160 · Comercial $190/m² (**sin industrial**). Complejidad del proyecto ×0.85 (Simple)/×1.0 (Estándar)/×1.6 (Complejo). >300 m² −5%, >600 m² −10%, mínimo $10,000. Entregable: PDF + DWG. Endpoint `/cotizar_planos`.
  - **Tiempos (referencia de mercado)**: D5 3-5 días/render, paquetes 1-3 semanas; BIM 2-6 semanas según m². Compromiso real en entrevista de alcance.
  - **Pago dinámico**: 50/50 si total < $15,000; 30/40/30 si ≥ $15,000. Precios + IVA explícito. Solo transferencia.
- ✅ **Base de datos en Supabase (Pooler IPv4)**: PostgreSQL vía `aws-0-us-east-1.pooler.supabase.com:6543`. Keep-warm cada 5 min con query SQL real (`/keepwarm`).
- ✅ **Fallback local SQLite**: Si Supabase falla, `db.py` usa automáticamente el backup local (`web/EjemploBD/proyectos_arquitectonicos.db`).
- ✅ **Backup diario**: Cron a las 12pm ejecuta `backup_pg_to_sqlite.py` para mantener el SQLite local sincronizado.
- ✅ **Cloudflare Cache**: 3 Page Rules activas (Cache Everything + Edge TTL 2h) para carga instantánea de la web.
- ✅ **Correo del cotizador vía Brevo API**: HTTPS 443 (Render no alcanza SMTP). `BREVO_API_KEY` en `.env` y Render. Free 300 correos/día. Remitente `info@soma-arquitectura.com` verificado.

## ⚠️ LECCIÓN CRÍTICA DE RED (no repetir)
**Render free NO alcanza ciertos servicios externos.** Ya pasó 2 veces:
1. **Supabase IPv6**: Render no enruta IPv6 → `Network is unreachable` (se resolvió con pooler IPv4).
2. **Gmail SMTP (puertos 587/465)**: desde Render dan `timed out` (Gmail bloquea/ralentiza IPs de datacenter).

**Regla:** servicios externos desde Render SIEMPRE por **HTTPS (puerto 443)** — es lo único garantizado. Nunca usar SMTP directo (Gmail) desde Render; usar API de correo por HTTPS (Brevo/Resend).

## Sesión: 05 Ago 2026 ✅ — Monitoreo de salud: /health + alertas automáticas por correo

### Bitácora del día
1. **Motivación**: varias sorpresas del free tier (Supabase pausada, Render, SendGrid, sender no verificado). Se quiso detectar fallas en minutos, no en días.
2. **`GET /health`** (público): chequea servidor + BD (`SELECT 1`, indica postgres/sqlite) + Brevo (`/v3/account`). Devuelve `status: ok` o `degraded`.
3. **`POST /health/alert`** (público, rate-limit 30 min/componente): envía correo de alerta a `habitarq85@gmail.com` vía Brevo.
4. **Worker keep-warm actualizado**: cada 5 min consulta `/health`; si falla algo → alerta por correo (1 vez/30 min vía Cache API); al recuperarse limpia estado. Endpoints manuales `__ping` y `__health`.
5. **Verificado online**: Render `/health` → ok; worker `__health` → ok; alerta de prueba `delivered`.

### Archivos creados/modificados
- `backend/server.py` — endpoints `/health` y `/health/alert`
- `workers/keep-warm/src/index.js` — health check + alertas
- `AGENTS.md`, `BITACORA_SOMA.md` — Actualizados

### ⚠️ LECCIÓN: probar la integración completa, no solo "sin error"
- El flujo completo quedó: **worker (Cloudflare) → /health (Render) → /health/alert (Render) → Brevo → correo**. Cualquier eslabón roto se detecta ahora por el propio sistema.

### Próxima sesión
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación
- Lead magnet — decidir ubicación en página web

---

## Sesión: 05 Ago 2026 ✅ — Correo Brevo arreglado: sender `info@` no estaba verificado

### Bitácora del día
1. **Diagnóstico**: tras la migración a Brevo (04/08), la web respondía sin error (`email: sent`) pero el correo no llegaba.
2. **Causa raíz**: el sender `info@soma-arquitectura.com` **no estaba verificado** en Brevo. Brevo acepta el POST (201) y **descarta el correo silenciosamente** (`event: error`). Por eso nunca había error en pantalla.
3. **Cómo se detectó**: `GET /v3/smtp/statistics/events` muestra `event: error` con reason *"sender not valid"*. El único sender activo era `habitarq85@gmail.com` (`GET /v3/senders`).
4. **Solución**: dominio autenticado en Brevo (4 registros DNS en Cloudflare: DKIM×2, brevo-code, DMARC + SPF `include:spf.brevo.com`) + sender `info@` creado y validado con **código OTP** (`PUT /v3/senders/2/validate`).
5. **Verificado online**: envío real desde Render (`SOMA-05082026-0352`) → `event: delivered`. Lead de prueba eliminado.

### ⚠️ LECCIÓN (nueva): Brevo no rechaza remitentes no verificados, los descarta
- Brevo devuelve **201 aunque el sender no sea válido** — el correo se pierde en silencio. **Nunca confiar en `status 201` ni en `email: sent` para dar por bueno un envío.**
- Siempre verificar en `GET /v3/senders` que el remitente esté `active: true`, y mirar `GET /v3/smtp/statistics/events` para confirmar `delivered` (no `error`).
- Para crear/verificar un sender por API: `POST /v3/senders` → Brevo envía OTP por email → `PUT /v3/senders/{id}/validate` con `{"otp": 123456}`.

### Archivos creados/modificados
- `AGENTS.md`, `BITACORA_SOMA.md` — Actualizados
- `render.yaml` — Pendiente limpiar SMTP/SendGrid obsoletos

### Próxima sesión
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación
- Lead magnet — decidir ubicación en página web

---

## Sesión: 04 Ago 2026 ✅ — Correo del cotizador: SendGrid → Brevo

### Bitácora del día
1. **Diagnóstico**: correo del cotizador fallaba online. SendGrid (cuenta free) sin créditos → `401 Maximum credits exceeded`. El lead sí se guarda en BD.
2. **Migración a SMTP Gmail**: `enviar_correo()` reescrito a `smtplib`. Probado localmente OK.
3. **Nuevo fallo online**: Gmail SMTP (587/465) da `timed out` desde Render (Gmail bloquea IPs de datacenter). Documentado en sección LECCIÓN CRÍTICA arriba.
4. **Email público `info@`**: intacto, gestionado por Cloudflare Email Routing → reenvía a `habitarq85@gmail.com`. Independiente del sistema de notificaciones.
5. **Solución final — Brevo API**: `enviar_correo()` usa `POST https://api.brevo.com/v3/smtp/email` (HTTPS 443, `urllib`, sin dependencias). Cuenta free 300 correos/día. Remitente `info@soma-arquitectura.com` verificado.
6. **Verificado online**: `/notificaciones/status` → `conectado: true`. Envío real desde Render → `email: sent`. Lead de prueba eliminado de Supabase (se conservaron los leads reales `Pimay12@hotmail.com`).

### Archivos creados/modificados
- `backend/server.py` — `enviar_correo()` vía Brevo API + `/notificaciones/status` con GET `/v3/account`. Eliminados `_smtp_connect()`, SMTP y SendGrid.
- `.env`, `.env.example` — `BREVO_API_KEY` configurada; SMTP/SendGrid eliminadas
- `AGENTS.md`, `BITACORA_SOMA.md` — Actualizados con lección de red y resolución

### Próxima sesión
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación
- Lead magnet — decidir ubicación en página web

---

## Sesión: 21 Jul 2026 ✅

### Bitácora del día
1. **Diagnóstico de caída**: Supabase pausó el proyecto gratuito por inactividad. Worker keep-warm no contaba como actividad de BD porque solo pingueaba el API REST.
2. **Reactivación**: Juan resumió el proyecto desde app.supabase.com. Datos intactos.
3. **Keep-warm real**: Endpoint `/keepwarm` con `SELECT 1` agregado a `server.py`. Worker actualizado para pinguear este endpoint.
4. **Backup Supabase→SQLite**: Script `backup_pg_to_sqlite.py` exporta 8 tablas (60 registros) a SQLite local.
5. **Fallback automático**: `db.py` ahora atrapa errores de conexión PostgreSQL y cae a SQLite sin intervención.
6. **Cron diario**: Backup automático cada 12pm.
7. **Push a GitHub**: Render desplegando cambios.

### Archivos creados/modificados
- `backend/backup_pg_to_sqlite.py` — Nuevo
- `backend/db.py` — Fallback PG→SQLite
- `backend/server.py` — Endpoint `/keepwarm`
- `workers/keep-warm/src/index.js` — Ping a `/keepwarm`
- `.env` — DATABASE_URL reactivado
- `AGENTS.md`, `BITACORA_SOMA.md`, `SOMA_CORE_INDEX.md`, `SOMA_SNAPSHOT.md` — Actualizados

### Próxima sesión
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación
- Lead magnet — decidir ubicación en página web

---

## Sesión: 24 Jul 2026 ✅

### Bitácora del día
1. **10 posts Instagram creados** sobre "Errores comunes en diseño arquitectónico" (serie educativa 1/10 a 10/10).
2. **Formato Editorial Split** (50/50 imagen + texto, barra acento terracota) usado para temas conceptuales.
3. **Imágenes de proyectos propios** reutilizadas (Casa Alina, Casona Cristi, Casa-Taller Roma) + img_tendencias.
4. **PNGs generados**: 10 nuevas imágenes en `publicaciones/` (post_11 a post_20).
5. **Tooling permanente**: `npm run generate` funcionando sin reinstalar Puppeteer.

### Archivos creados/modificados
- `recursos_graficos/material_instagram/post_11_error_contexto.html` — Nuevo
- `recursos_graficos/material_instagram/post_12_error_orientacion.html` — Nuevo
- `recursos_graficos/material_instagram/post_13_error_jerarquia.html` — Nuevo
- `recursos_graficos/material_instagram/post_14_error_iluminacion.html` — Nuevo
- `recursos_graficos/material_instagram/post_15_error_escala.html` — Nuevo
- `recursos_graficos/material_instagram/post_16_error_flexibilidad.html` — Nuevo
- `recursos_graficos/material_instagram/post_17_error_conectividad.html` — Nuevo
- `recursos_graficos/material_instagram/post_18_error_forma_funcion.html` — Nuevo
- `recursos_graficos/material_instagram/post_19_error_instalaciones.html` — Nuevo
- `recursos_graficos/material_instagram/post_20_error_presupuesto.html` — Nuevo
- `recursos_graficos/material_instagram/screenshot.js` — Actualizado (10 nuevos posts)
- `recursos_graficos/material_instagram/publicaciones/` — 10 PNGs nuevos generados

### Próxima sesión
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación
- Lead magnet — decidir ubicación en página web
- Programar publicación de serie "10 errores de diseño arquitectónico" en Instagram

---

## Sesión: 06 Jul 2026 ✅

### Bitácora del día
1. **Investigación de tendencias**: Tiny Houses, Cohousing, Coliving, Conversión casa→deptos, Vivienda sustentable. Documentadas tendencias en México/LATAM 2026.
2. **6 posts Instagram creados** con nueva composición "Editorial Split" (50/50 imagen + texto, barra acento terracota) para diferenciar temas conceptuales de posts de proyectos.
3. **Imágenes libres descargadas**: 5 fotos de Unsplash/Pexels para temas conceptuales en `recursos_graficos/img_tendencias/`.
4. **Tooling permanente**: `package.json` + `screenshot.js` instalados en `material_instagram/`. Comando: `npm run generate`. Ya no requiere instalar puppeteer cada vez.
5. **PNGs generados**: 6 imágenes en `publicaciones/` (post_06a a post_10).
6. **CONTENIDO_INSTAGRAM.md actualizado**: Semanas 7-8 agregadas con captions completos.

### Archivos creados/modificados
- `recursos_graficos/material_instagram/post_06a_tiny_houses.html` — Nuevo
- `recursos_graficos/material_instagram/post_06b_tiny_houses.html` — Nuevo
- `recursos_graficos/material_instagram/post_07_cohousing.html` — Nuevo
- `recursos_graficos/material_instagram/post_08_coliving.html` — Nuevo
- `recursos_graficos/material_instagram/post_09_conversion.html` — Nuevo
- `recursos_graficos/material_instagram/post_10_5_formas.html` — Nuevo
- `recursos_graficos/material_instagram/package.json` — Nuevo (tooling)
- `recursos_graficos/material_instagram/screenshot.js` — Nuevo (script)
- `recursos_graficos/img_tendencias/` — 5 imágenes libres
- `Bloque 4/CONTENIDO_INSTAGRAM.md` — Semanas 7-8 + captions
- `AGENTS.md` — Comando actualizado para generar PNGs

### Próxima sesión
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación
- Lead magnet — decidir ubicación en página web

## Sesión: 03 Jul 2026 ✅

### Bitácora del día
1. **Migración de Render PostgreSQL a Supabase**: Eliminada DB de Render que inyectaba `DATABASE_URL` malformada (`DATABASE_URL=postgresql://...` con key+value concatenado). Código actualizado para hacer stripping del prefijo `KEY=` en `_get_db_url()`.
2. **Problema IPv6**: Supabase free tier solo tiene IPv6 (`2600:1f18:...`). Render no puede enrutar → `Network is unreachable`. Solucionado usando **Supabase Connection Pooler** con IPv4: `aws-0-us-east-1.pooler.supabase.com:6543` con usuario `postgres.dejojumyyydrlqoegqnf`.
3. **render.yaml**: URL actualizada al pooler, quitado `pgbouncer=true` (no válido para psycopg2).
4. **db.py**: `_get_db_url()` ahora prueba `SUPABASE_URL` primero, luego `DATABASE_URL`. Hace stripping automático de `KEY=` prefix. Debug logging de env vars.
5. **server.py**: `init_db()` verifica `SUPABASE_URL` y `DATABASE_URL` para `use_pg`.
6. **Cloudflare Worker keep-warm**: Actualizado para pinguear también `https://dejojumyyydrlqoegqnf.supabase.co` cada 5 min y evitar que Supabase se pause por inactividad.
7. **Token Cloudflare**: Guardado en `.env` (gitignored). Comando deploy: `cd workers/keep-warm && source ../../.env && wrangler deploy`.
8. **Deploy exitoso**: Clientes visibles en dashboard, datos accesibles vía pooler.

### Archivos modificados
- `backend/db.py` — KEY= stripping, debug logging, SUPABASE_URL priority
- `backend/server.py` — use_pg verifica SUPABASE_URL + DATABASE_URL
- `render.yaml` — Pooler URL (IPv4), removed `pgbouncer=true`
- `workers/keep-warm/src/index.js` — Agregado ping a Supabase
- `.env` — URL pooler + Cloudflare token
- `start.sh`, `start_local.sh` — WhatsApp Baileys eliminado (sesiones anteriores)

### Próxima sesión
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación
- Lead magnet — decidir ubicación en página web

## Sesión: 26 Jun 2026 ✅

### Bitácora del día
1. **Botón Cotizador SOMA en portada**: texto naranja "Cotizador SOMA" debajo de "Taller Virtual de Arquitectura", con fondo negro 40% opacity, padding ajustado, cursor pointer. Llama a `openImmersion()`.
2. **Cache de Cloudflare**: 3 Page Rules configuradas (`/`, `/recursos_graficos/*`, `/web/*`) con Cache Everything + Edge Cache TTL 2h. La web se sirve desde el edge de Cloudflare, eliminando cold start de Render.
3. **`_redirects` creado** (para futura migración a Cloudflare Pages): mapea rutas estáticas directo y APIs proxy a `soma-853c.onrender.com`.

## Sesión: 27 Jun 2026 ✅

### Bitácora del día
1. **Cloudflare Worker keep-warm desplegado**: `soma-keep-warm` con cron `*/5 * * * *` (cada 5 min) que pinguea `soma-853c.onrender.com` para evitar que Render se duerma por inactividad. URL: `https://soma-keep-warm.habitarq85.workers.dev`.
2. **Token Cloudflare creado**: `SOMA Workers Deploy` con permisos `Workers Scripts -> Edit` + `User Details -> Read`. Almacenado localmente para deploy via Wrangler.
3. **Estructura creada**: `workers/keep-warm/wrangler.toml` + `src/index.js`.

### Próxima sesión
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación
- Lead magnet — decidir ubicación en página web

## Sesión: 26 Jun 2026 ✅

### Bitácora del día
1. **Estación 4 corregida contra PROCESO DE DISEÑO 2.0**: reestructuración completa de 15 cards en `algoritmo_soma.html`:
   - Eliminado: 4.3 "Documento de Intenciones" y 4.15 "Documento de Concepto" (no existen en 2.0)
   - Separado en 2 pasos c/u: Volumetrización+Zonificación → 4.3+4.4, y Ubicación+Accesos → 4.5+4.6
   - Agregados sub-items: 4.8.1-6 (Espacialidad), 4.9.1-8 (Evaluación I), 4.11.1-6 (Configuración), 4.14.1 (Evaluación II)
   - Renombrado: 4.1, 4.2, 4.7, 4.15 según nomenclatura de 2.0
2. **CSS para sub-items**: clases `.stag.sh/sa/sm` con colores de procesador (naranja/azul/morado) para tags en sub-items.
3. **Limpiados rangos numéricos redundantes** en textos OPERA de cards 4.8, 4.9, 4.11, 4.14 para evitar que "4.8.1" apareciera dos veces (en texto y en listado).

### Próxima sesión
- Afinar detalles visuales de Estación 4
- Vincular estaciones 5+ (Modelado, Visualización, Anteproyecto) con datos de la BD
- Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación

## Sesión: 24 Jun 2026 ✅

### Bitácora del día
1. **Estación 1 simplificada**: Solo tarjeta 1.1 Contacto (eliminada 1.2 Programa y datos reales inyectados).
2. **Mensaje placeholder**: Cambiado "Sin proyectos activos en Momento 2" → "Sin proyectos registrados."
3. **Lección**: No mezclar cambios visuales con cambios de infraestructura (server.py / fetch). Mantener server.py intacto para evitar romper auth.

## Sesión: 22 Jun 2026 (p.m.) ✅

### Bitácora del día
1. **Barra de progreso global eliminada**: removido marcador de avance por estación (HTML+CSS+JS). Se conserva solo Estación 10 como Control.
2. **Barra de avance en tarjeta de proyecto**: cada proyecto en el selector ahora muestra una barra que se llena de izquierda a derecha (0–100%) con el progreso real del algoritmo. Se actualiza al cargar/guardar progreso vía `calcularProgresoGlobal()` + `actualizarProgresoTarjeta()`.

## Sesión: 22 Jun 2026 (noche) ✅

### Bitácora del día
1. **Diagrama SOMA integrado en Algoritmo (3.4)**: 
   - Botón "ABRIR DIAGRAMA DE RELACIONES" en la tarjeta 3.4 de Station 3 (Análisis).
   - Sección colapsable debajo del step-grid con vis-network (force-directed graph).
   - Carga datos reales desde `/api/diagrama/grafo/<proyecto_id>` (espacios + relaciones).
   - Filtro por zona (Social/Operativa/Descanso/Soporte/Transición).
   - Posiciones guardadas en localStorage, botón Reset, export PNG.
   - Leyenda cromática por zona.
2. **Cambio de proyecto re-renderiza estación activa**: al seleccionar otra tarjeta, la estación visible se actualiza con los datos del nuevo proyecto (incluyendo diagrama si está abierto).

### Próxima sesión
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación
- Lead magnet — decidir ubicación en página web

## Sesión: 23 Jun 2026 ✅

### Bitácora del día
1. **Corrección doble-codificación JSON en ubicación**: `programa.js` y `server.py` ahora usan columnas directas (`calle_numero`, `colonia`, `ciudad`, `estado_ubic`) en vez de `ubicacion` JSON, eliminando el bug de datos que se perdían al reabrir el modal.
2. **PDFs de expediente y cierre con respuestas A/B descriptivas**: mapeo completo de los 10 pasos de inmersión (step1…step10) con sus opciones (p.ej. `Pregunta 1: B. Cerrada`) tanto en el expediente modal, PDF de expediente y PDF de cierre.
3. **Protección de Momento 2**: el modal PROGRAMA se vuelve de solo lectura en fases `contratado`, `primera_entrega`, `entrega_final` (botones de agregar/eliminar espacios y guardar ocultos).
4. **Botón ELIMINAR en Momento 1**: todas las tarjetas de Candidatos ahora muestran botón ELIMINAR para borrar leads sin inmersión completa o erróneos (p.ej. "Casa del sol").
5. **Refresh robusto**: timeouts de 10s en cada `fetch` y 15s en `App.refresh()` + guard de modal solo en auto-refresh (30s), nunca en manual.
6. **Datos de ubicación como columnas simples**: migración automática en `init_db()` crea `calle_numero`, `colonia`, `ciudad`, `estado_ubic` en `captura_web`; PDFs y expediente leen directo.
7. **Auth básica en Render**: protección HTTP Basic Auth en `/dashboard`, `/algoritmo`, APIs y PDFs. Credenciales por defecto `admin` / `Yucata85` (configurables vía `DASHBOARD_USER` / `DASHBOARD_PASS` en Render). Página pública (`/`, `/web/*`, `/css/*`, `/recursos_graficos/*`, `/backend/*`) sin protección.

### Próxima sesión
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación
- Lead magnet — decidir ubicación en página web

## Sesión: 22 Jun 2026 (madrugada) ✅

### Bitácora del día
1. **Expediente simplificado (v1)**: removidos cobros del modal expediente. Orden exacto v1: datos de inmersión → análisis multidimensional → respuestas A/B línea por línea → programa arquitectónico → PDF de expediente.
2. **Respuestas A/B en español**: formato "Pregunta 1: a Fachada abierta", "Pregunta 2: b Privacidad cerrada", etc. con labels descriptivos desde BD.
3. **Ruta PDF expediente**: `/lead/<id>/expediente-pdf` genera HTML imprimible del expediente completo (datos, análisis, respuestas, programa).
4. **DB limpia**: eliminados proyectos 7 (María Torres), 9 (Juan Pérez), 11 (Casa Alina). Único proyecto demo `SOMA-20260622-DEMO` con inmersión completa.
5. **Fix métricas Bloque 01**: `cargarMetrics()` llamado directamente antes de `App.refresh()` en `pagarCobroDirecto` y `avanzar` para evitar que el guard de modal activo bloquee la actualización de KPIs.

### Próxima sesión
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación
- Lead magnet — decidir ubicación en página web
- Revisar deploy en Render (soma.onrender.com responde 404 no-server)

### Comandos
```bash
# Servidor
systemctl --user stop soma-flask.service
systemd-run --user --unit=soma-flask --setenv=DATABASE_URL=postgresql://soma_user:soma_pass@localhost:5432/soma_db /home/juan/Documentos/PROYECTO\ SOMA/backend/venv/bin/python /home/juan/Documentos/PROYECTO\ SOMA/backend/server.py

# Logs
journalctl --user -u soma-flask.service -f

# Dashboard
http://localhost:8080/dashboard

# Algoritmo
http://localhost:8080/algoritmo

# PostgreSQL
PGPASSWORD=soma_pass psql -h localhost -U soma_user -d soma_db

# Métricas
curl -s "http://127.0.0.1:8080/metrics/bloque01?year=2026&month=6" | python3 -m json.tool

# Expediente PDF
curl -s "http://127.0.0.1:8080/lead/12/expediente-pdf"
```

### Archivos clave
```
web/
├── dashboard.html          # Dashboard 2.0
├── css/
│   ├── dashboard.css       # Estilos oscuros (dark editorial)
│   └── algoritmo.css       # Estilos del Algoritmo SOMA
├── js/
│   ├── api.js              # API calls
│   ├── ui.js               # UI utilities
│   ├── leads.js            # Leads, pipeline, expediente, pagos
│   ├── egresos.js          # Gastos de operación
│   ├── fondos.js           # Fondos de provisión
│   ├── programa.js         # Programa arquitectónico + cotización
│   ├── app.js              # App shell, refresh loop, metrics
│   └── algoritmo.js        # Algoritmo SOMA (tarjetas, diagrama, programa)
├── algoritmo_soma.html     # Algoritmo con tarjetas de proyecto
├── guia_visita.html        # Guía de visita (checklist sitio + ambientales + 6 tópicos)
└── guia_entrevista.html    # (obsoleto, reemplazado por guia_visita)

backend/server.py           # Flask (rutas: leads, cobros, metrics, expediente-pdf, programa/html)
antecedentes/dashboard_v1/  # Dashboard original (referencia)
```

## Flujo de trabajo — Contenido Instagram

### Proceso para crear posts
1. El usuario pide contenido para Instagram (tema, cantidad)
2. Crear cards HTML (800×800px) con identidad visual SOMA:
   - Fondo oscuro `#0a0a0a`, acento terracota `#d45e2c`
   - Tipografía: Georgia (serif) + Courier New (monospace)
   - Imágenes de fondo desde `recursos_graficos/Carrusel_por_proyecto/`
   - Pie con `info@soma-arquitectura.com · soma-arquitectura.com`
3. Guardar en `recursos_graficos/material_instagram/post_XX_tema.html`
4. Generar PNG con Puppeteer (herramienta instalada permanente):
   ```bash
   cd "/home/juan/Documentos/PROYECTO SOMA/recursos_graficos/material_instagram" && npm run generate
   ```
5. Las imágenes quedan en `recursos_graficos/material_instagram/publicaciones/`
6. Entregar captions listos para copiar/pegar

### Para carruseles (varias slides)
- Nombrar: `post_01a_tema.html` (slide 1), `post_01b_tema.html` (slide 2)
- Incluir indicador "1/2", "2/2" y "Desliza →"

### Captions
- Incluir siempre: texto del post + llamada a la acción (pregunta en comentarios)
- Hashtags: #ArquitecturaMérida #ConstruirEnMérida #PrimeraCasa #SOMATallerVirtual + específicos
```
