# PROTOCOLO: VISUALIZACIÓN
## Bloque 2 — Taller SOMA (Operación) | Etapa 6 del Ciclo

### ¿Qué es la Visualización?

Es la traducción del modelo 3D a imágenes que comunican el proyecto con la calidad estética de SOMA. No es "hacer renders bonitos" — es producir las vistas necesarias para que el cliente entienda el proyecto y para el portafolio del taller.

**Entrada:** Modelo 3D verificado (del Modelado, Etapa 5).
**Salida:** Set de imágenes fijas y/o animaciones listas para presentación y portafolio.

### Principio rector

La visualización en SOMA es **sistemática, no artística**. El estilo es consistente: fondos oscuros, acento naranja (#bc4b21), vegetación regional, cielo al atardecer/amanecer. La creatividad está en el diseño, no en la postproducción.

---

## 1. FLUJO DE TRABAJO (Revit → D5 → Photoshop)

### 1.1 Desde Revit / Blender / SketchUp
(Fuente: D5 Render Official Workflow — d5render.com/learn)

- [ ] Exportar modelo en formato compatible:
  - Revit → .rvt (D5 LiveSync) o .fbx
  - Blender → .fbx o .glb
  - SketchUp → .skp (D5 LiveSync)
- [ ] Configurar unidad de exportación: milímetros (coincidir con D5).
- [ ] Limpiar el modelo antes de exportar:
  - Ocultar geometría no visible (interiores de muros, estructura no relevante)
  - Colapsar componentes repetitivos en instancias
  - Verificar que las normales de las caras apunten hacia afuera
- [ ] Usar LiveSync cuando sea posible para cambios en tiempo real
  (Fuente: D5 Render LiveSync Tutorial — D5 Creative Team)

### 1.2 Configuración en D5 Render
(Fuente: D5 Render Beginner Tutorial EP.01-05 — D5 Official)

- [ ] **Entorno:**
  - HDR de atardecer o amanecer (golden hour) para exteriores
  - HDR nublado suave para interiores (luz difusa)
  - Rotar HDR para que la luz principal coincida con la orientación real del proyecto
- [ ] **Clima:**
  - Cielo despejado ligeramente nublado (Mérida: atmósfera con humedad ligera)
  - Altitud solar: 15°–30° sobre el horizonte (sombras largas que definan la forma)
- [ ] **Cámara (Section 2 detalla las vistas obligatorias):**
  - Relación de aspecto: 16:9 (horizontal), 9:16 (vertical para Instagram/Web)
  - Lentes: 35mm–50mm para exteriores (visión humana natural)
  - Lentes: 24mm–28mm para interiores (sin distorsión excesiva)
  - DOF (profundidad de campo): desactivado para vistas generales, activo para detalles
  - Altura de cámara: 1.60 m (altura de ojos del habitante)

### 1.3 Materiales
(Fuente: D5 Material System — d5render.com)

- [ ] Usar el **catálogo de materiales SOMA** (ver sección 4):
  - Materiales base guardados como .d5mat para reutilización
  - Cada material debe tener: color base, roughness, normal map, metalness
- [ ] Ajustes generales:
  - Concreto: roughness 0.6–0.8, color gris cálido (#B5B0A8)
  - Madera: roughness 0.4–0.6, color según especie (regional: caoba, cedro, tzalam)
  - Vidrio: roughness 0.0–0.1, transmisión 0.95, color ligeramente verdoso/neutro
  - Agua: roughness 0.0, altura de olas 0.2–0.5m
  - Vegetación: usar D5 Asset Library — vegetación regional (ceiba, flamboyán, palma)
- [ ] Evitar materiales hiperrealistas que compitan con la arquitectura
  (Fuente: Fran Silvestre Arquitectos — estilo de visualización, referenced en D5 Instructor tutorials)

### 1.4 Postproducción en D5 (integrada)
(Fuente: D5 Post-Processing Panel — D5 Official)

- [ ] **Exposición:** Ajustar para que las fachadas iluminadas estén en rango correcto (sin quemados)
- [ ] **Contraste:** S-curve suave (estilo SOMA: sombras profundas, luces controladas)
- [ ] **Color:**
  - Temperatura: 5500K–6500K (neutro-ligeramente cálido para exteriores)
  - Tinte: +5 a +10 (verde apenas perceptible — vegetación regional)
  - Saturación: −5 a −10 (estilo sobrio, no saturado)
- [ ] **Bloom:** 0.2–0.3 (sutil, para fuentes de luz)
- [ ] **Vignete:** 0.1–0.2 (oscurecer bordes, enfocar centro)
- [ ] **Sharpening:** 0.3–0.5 (nitidez sin artefactos)
- [ ] **Fog:** Desactivado (clima de Mérida: atmósfera limpia en golden hour)

### 1.5 Postproducción en Photoshop (mínima)
(Fuente: prácticas de visualización arquitectónica — D5 Community)

- [ ] Corrección de color global (curvas, niveles) — solo si D5 no logró el tono exacto
- [ ] Inserción de cielo si el HDR no funcionó (usar fotos propias de Mérida)
- [ ] Inserción de vegetación en primer plano (siluetas para profundidad)
- [ ] Corrección de distorsión de lente si aplica
- [ ] Exportación final: PNG (pérdida cero) → escalar a resolución final

---

## 2. VISTAS OBLIGATORIAS POR PAQUETE
(Fuente: Francis D.K. Ching, Architecture: Form, Space, and Order — principios de representación arquitectónica; SOMA Brand Guidelines — estilo visual)

### 2.1 SOMA Esencial (4 vistas)
- [ ] **Vista aérea isométrica:** El proyecto en su contexto (muestra implantación, cubiertas, relación con el predio). Ángulo 45°, altura suficiente para ver todo el conjunto.
- [ ] **Vista peatonal desde acceso principal:** Fachada principal desde la calle. La primera impresión del proyecto.
- [ ] **Vista interior del espacio social principal:** Sala-comedor o espacio central. Muestra la relación interior-exterior, luz natural, materialidad.
- [ ] **Corte perspectivado (opcional):** Sección volumétrica que muestre la relación de alturas y espacios interiores.

### 2.2 SOMA Integral (8 vistas — incluye las 4 anteriores)
- [ ] + **Vista posterior/jardín:** Fachada posterior, relación con el exterior, terraza, alberca (si aplica).
- [ ] + **Vista interior de recámara principal:** Confort visual, luz natural, vista al exterior.
- [ ] + **Vista de cocina / espacio operativo:** Funcionalidad del espacio de trabajo.
- [ ] + **Vista nocturna:** Iluminación artificial, ambiente, temperatura de color cálida.

### 2.3 SOMA Ejecutivo (12 vistas — incluye las 8 anteriores)
- [ ] + **2 vistas de detalle constructivo:** Encuentros material-fachada, celosías, voladizos, escaleras.
- [ ] + **Recorrido animado (video 30–60s):** Cámara lenta que recorre el proyecto a velocidad peatonal.
- [ ] + **Exploded axonometric:** Explosión de capas del proyecto (estructura, arquitectura, instalaciones).
- [ ] + **Vista de baño principal:** Detalle de materiales, iluminación, espejos, vanitorio.

### 2.4 Resolución mínima de exportación
| Uso | Resolución mínima | Formato |
|-----|-------------------|---------|
| Presentación / PDF | 3840 × 2160 (4K) | PNG |
| Web (Portafolio SOMA) | 1920 × 1080 | WebP o JPG calidad 90% |
| Instagram (cuadrado) | 1080 × 1080 | JPG calidad 90% |
| Instagram (vertical) | 1080 × 1350 | JPG calidad 90% |

---

## 3. SETUP DE CÁMARAS (Plantillas D5)

Guardar como escenas dentro del archivo de D5 para reutilización entre proyectos:

| Escena | Cámara | Altura | Lente | Iluminación |
|--------|--------|--------|-------|-------------|
| Aérea | Isométrica / Perspectiva | 50–100m | 35mm | Golden hour |
| Fachada | Peatonal frontal | 1.60m | 50mm | Golden hour |
| Interior día | Gran angular | 1.50m | 24mm | Luz natural difusa |
| Interior noche | Gran angular | 1.50m | 24mm | Luz artificial cálida |
| Detalle | Close-up | Según objeto | 85mm | Luz suave lateral |
| Nocturna exterior | Peatonal | 1.60m | 35mm | Blue hour + luz artificial |
| Video recorrido | Tracking | 1.60m | 35mm | Golden hour |

(Fuente: D5 Camera System — d5render.com/learn; principios de cinematografía arquitectónica)

---

## 4. CATÁLOGO DE MATERIALES SOMA (para D5)

Materiales base que deben estar preconfigurados para arrastrar y soltar:

| Material | Roughness | Metalness | Color Base | Uso típico |
|----------|-----------|-----------|------------|------------|
| Concreto SOMA | 0.7 | 0.0 | #B5B0A8 | Muros, losas, columnas |
| Concreto pulido | 0.3 | 0.0 | #C4BFB4 | Pisos interiores |
| Madera regional clara | 0.5 | 0.0 | #C4956A | Pisos, acabados |
| Madera regional oscura | 0.5 | 0.0 | #5C3A21 | Mobiliario, celosías |
| Piedra caliza | 0.6 | 0.0 | #D4C9B8 | Fachadas, muros |
| Acero Corten | 0.6 | 0.8 | #8B4513 | Detalles, fachada |
| Vidrio limpio | 0.05 | 0.0 | Transparente | Ventanas |
| Vidrio esmerilado | 0.3 | 0.0 | Translúcido | Baños, privacidad |
| Agua alberca | 0.0 | 0.0 | #1A8B9E | Alberca, espejo agua |
| Calle/asfalto | 0.8 | 0.0 | #3D3D3D | Contexto urbano |

- [ ] Crear carpeta `materiales_soma/` en la biblioteca local de D5
- [ ] Cada material debe tener: mapa de color base, roughness, normal map (si aplica)
- [ ] Incluir mapa de desplazamiento para texturas de piedra y concreto

(Fuente: D5 Material Creation — d5render.com/learn; experiencia de Juan en Duarte Aznar)

---

## 5. NAMING Y ARCHIVO

### 5.1 Convención de nombres

```
SOMA-{CLIENTE}-{VISTA}-{NUMERO}.{formato}
```

Ejemplos:
- `SOMA-LOPEZ-AEREA-01.png`
- `SOMA-LOPEZ-FACHADA-01.png`
- `SOMA-LOPEZ-INTERIOR_SALA-01.png`
- `SOMA-LOPEZ-NOCTURNA-01.png`
- `SOMA-LOPEZ-RECORRIDO.mp4`

### 5.2 Estructura de carpeta del proyecto

```
backend/proyectos/SOMA-YYYYMMDD-XXXX/
├── renders/
│   ├── 01_aerea/
│   ├── 02_fachada/
│   ├── 03_interiores/
│   ├── 04_nocturna/
│   ├── 05_detalles/
│   └── 06_video/
└── dossier_editorial/
    └── imagenes/  ← copias optimizadas para el dossier
```

---

## 6. CHECKLIST DE ENTREGA

- [ ] ¿Todas las vistas obligatorias del paquete están renderizadas?
- [ ] ¿El cielo y la vegetación corresponden a la región del proyecto?
- [ ] ¿La iluminación respeta la orientación real del proyecto (N-S real)?
- [ ] ¿Los materiales coinciden con el moodboard aprobado por el cliente?
- [ ] ¿La escala humana es correcta en todas las vistas?
- [ ] ¿Las imágenes no tienen artefactos (ruido, aliasing, reflejos falsos)?
- [ ] ¿Los nombres de archivo siguen la convención SOMA?
- [ ] ¿Se exportó una copia en resolución web para portafolio?

---

## 7. SALIDA DE LA VISUALIZACIÓN

Al completar esta etapa:

1. **Set de renders** en `proyectos/SOMA-XXXX/renders/` con naming estándar.
2. **Archivo fuente de D5** guardado (`.d5`) con todas las escenas configuradas.
3. **Copia en resolución web** para portafolio y redes.
4. **Selección de mejores vistas** para el dossier editorial (si aplica, el protocolo de Representación Integral las usará).

Este set de imágenes es la entrada directa a:
- **Representación Integral** (Etapa 7) — dossier editorial.
- **Portafolio SOMA** — actualización del carrusel web.
- **Redes sociales** — Instagram, LinkedIn.

---

## FUENTES

- **Francis D.K. Ching**, *Architecture: Form, Space, & Order* (4th ed., 2014) — principios de composición de vistas, jerarquía visual, proporción en encuadres arquitectónicos.
- **Francis D.K. Ching**, *Architectural Graphics* (6th ed., 2015) — convenciones de representación, técnicas de presentación, sistemas de dibujo.
- **C. M. Deasy**, *Design Places for People* (1974) — cómo la visualización debe comunicar la experiencia humana del espacio, no solo la forma.
- **Jacques Paul Grillo**, *Form, Function and Design* (1960) — relación entre la representación visual y la claridad del mensaje funcional.
- **D5 Render Official Documentation** (d5render.com/learn) — flujo LiveSync, configuración de materiales, postproducción, cámaras.
- **Rudolf Arnheim**, *Visual Thinking* (1969) — percepción visual aplicada a la composición de vistas, encuadres y jerarquía de imágenes arquitectónicas.
- **D5 Render AI Capabilities** — AI Agent for landscape, AI Inpainting, AI atmosphere matching. (d5render.com)

---

*"El render perfecto no es el que más parece una foto, sino el que mejor comunica la idea arquitectónica."*
