# PROTOCOLO: VISUALIZACIÓN
## Bloque 2 — Taller SOMA (Operación) | Sección 5 del PROCESO DE DISEÑO 2.0
## Referencia: Items 5.3 a 5.11

**Qué es:** Traducción del modelo 3D a imágenes que comunican el proyecto
con la calidad estética de SOMA.

**Entrada:** Modelo 3D verificado + Vistas seleccionadas (5.1-5.2).

**Salida:** Set de imágenes fijas listas para presentación y portafolio.

**Principio rector:** La visualización SOMA es **sistemática, no artística**.
Estilo consistente: fondos oscuros, acento #d45e2c, vegetación regional,
cielo al atardecer/amanecer.

---

## Flujo de Trabajo (Revit → D5 → Photoshop)

### Exportación
- [ ] Exportar modelo en formato compatible (.fbx, .glb, .skp)
- [ ] Configurar unidad: milímetros
- [ ] Limpiar: ocultar geometría no visible, colapsar repetitivos, verificar normales

### Configuración en D5
- [ ] HDR atardecer/amanecer (exteriores), nublado suave (interiores)
- [ ] Altitud solar 15°-30° para sombras que definan la forma
- [ ] Cámara: 16:9 horizontal, 9:16 vertical (web). 35-50mm exteriores, 24-28mm interiores
- [ ] Altura de cámara: 1.60 m (ojos del habitante)

---

```
[ACC] 5.3 Iluminación Natural (P2.0 ref: 5.3)
─────────────────────────────────
INPUT:  5.2 Modelo + 2.1.1.2 `carta_solar_merida.pdf`
        4.9.1 Datos de asoleamiento
OPERA:  Configurar iluminación natural: orientación del sol según hora
        y fecha, luz de cielo, penetración en interiores, sombras
OUTPUT: Render con iluminación natural configurada
PROC:   HUMANO
```

---

```
[ACC] 5.4 Iluminación Artificial (P2.0 ref: 5.4)
─────────────────────────────────
INPUT:  5.2 Modelo + 4.12 Criterio de iluminación artificial
OPERA:  Colocar luces artificiales: tipo, temperatura de color,
        intensidad, sombras, escena nocturna (si aplica)
OUTPUT: Render con iluminación artificial configurada
PROC:   HUMANO
```

---

```
[ACC] 5.5 Colocación y Mapeo de Materiales (P2.0 ref: 5.5)
─────────────────────────────────
INPUT:  5.2 Modelo + 4.8.5 Paleta de materiales
OPERA:  Asignar materiales a superficies: mapas de textura (diffuse,
        roughness, normal, displacement), escala, rotación, acabados
OUTPUT: Modelo con materiales asignados
PROC:   HUMANO
```

---

```
[ACC] 5.6 Colocación de Mobiliario (P2.0 ref: 5.6)
─────────────────────────────────
INPUT:  5.2 Modelo + 4.11.1-2 Diseño baños/cocina
        3.10.5 Necesidades no visibles
OPERA:  Colocar mobiliario fijo y móvil en las vistas seleccionadas
OUTPUT: Escena amueblada
PROC:   HUMANO
```

---

```
[ACC] 5.7 Colocación de Vegetación (P2.0 ref: 5.7)
─────────────────────────────────
INPUT:  5.2 Modelo + 4.13 Paisaje (especies)
        2.2.2.1-2 Vegetación existente a conservar
OPERA:  Colocar árboles existentes, vegetación propuesta, pasto
OUTPUT: Escena con paisajismo
PROC:   HUMANO
```

---

```
[ACC] 5.8 Colocación de Decoración (P2.0 ref: 5.8)
─────────────────────────────────
INPUT:  5.6-5.7 Escena + 4.2 Idea rectora (atmósfera deseada)
OPERA:  Colocar elementos decorativos: cojines, alfombras, cortinas,
        arte, vajilla, objetos, lámparas decorativas
OUTPUT: Escena decorada con atmósfera habitable
PROC:   HUMANO
```

---

```
[ACC] 5.9 Colocación de Personas (P2.0 ref: 5.9)
─────────────────────────────────
INPUT:  5.8 Escena + 3.10.1 Datos demográficos (habitantes reales)
OPERA:  Colocar figuras humanas realizando actividades del programa
        para dar escala y vida a la escena
OUTPUT: Escena con escala humana
PROC:   HUMANO
```

---

```
[ACC] 5.10 Refinamiento con IA (P2.0 ref: 5.10)
─────────────────────────────────
INPUT:  5.9 Escena renderizada (imagen base)
OPERA:  Usar IA generativa para refinar: mejorar iluminación y
        atmósfera, agregar detalle fino, variaciones de material/color.
        La IA refina — no crea desde cero
OUTPUT: Imagen base refinada (humano evalúa y acepta/rechaza)
PROC:   AI→HUMANO
```

---

```
[ACC] 5.11 Postproducción (P2.0 ref: 5.11)
─────────────────────────────────
INPUT:  5.10 Imagen refinada
OPERA:  Editar imagen final en Photoshop: niveles, curvas, color,
        exposición, viñeteado, retoque, cielo, formato final
OUTPUT: Render final listo para entrega
PROC:   HUMANO
```

---

## Checklist de Entrega

| Vistas por paquete | Esencial | Integral | Ejecutivo |
|-------------------|----------|----------|-----------|
| Exterior general (estilo SOMA) | ✅ | ✅ | ✅ |
| Fachada principal (contexto) | ✅ | ✅ | ✅ |
| Interior espacio principal | ✅ | ✅ | ✅ |
| Interior cocina/baño | ❌ | ✅ | ✅ |
| Zona exterior (jardín/terraza) | ❌ | ✅ | ✅ |
| Corte perspectivado | ❌ | ✅ | ✅ |
| Detalles constructivos | ❌ | ❌ | ✅ |
| Recorrido animado | ❌ | Opcional | Opcional |

Naming: `SOMA-XXXX_vista_tipo_01.jpg` (ej: `SOMA-0001_exterior_general_01.jpg`)

---

## FUENTES

- D5 Render Official Documentation. d5render.com/learn
- Ching, F. (2015). *Architectural Graphics.*
- Arnheim, R. (1969). *Visual Thinking.*
