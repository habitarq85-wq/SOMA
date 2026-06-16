# PROTOCOLO: MODELADO SOMA
## Bloque 2 — Taller SOMA (Operación) | Sección 5 del PROCESO DE DISEÑO 2.0
## Referencia: Items 4.3–4.8 (volumetría), 5.1–5.2 (vistas + detallado)

**Qué es:** Traducción del concepto arquitectónico a un modelo digital tridimensional
que sirve como herramienta de diseño, verificación y base para las etapas siguientes.

**Entrada:** Documento de Concepto (de la Conceptualización, Sección 4).

**Salida:** Modelo 3D verificado y listo para extraer vistas.

**Principio rector:** El modelo es herramienta de decisión, no un dibujo bonito.

---

## Estrategia de Modelado

### Niveles de Desarrollo (LOD)

| Paquete | LOD | Herramienta | Qué se modela |
|---------|-----|-------------|--------------|
| Esencial | LOD 200 | SketchUp/Blender | Masas, vanos, cubierta, topografía |
| Integral | LOD 300 | Revit/Blender | Muros, losas, estructura, instalaciones esquemáticas |
| Ejecutivo | LOD 350+ | Revit | Todos los elementos constructivos + detalles |

### Organización del Modelo

- [ ] **Capas por sistema:** Estructura, Arquitectura, Mobiliario, Contexto, Instalaciones
- [ ] **Nomenclatura:** `MURO_EXTERIOR_PB_NORTE`, `LOSA_PB_COCINA`
- [ ] **Componentes:** todo elemento repetible como componente
- [ ] **Colores por zona SOMA:** Social (naranja), Descanso (azul), Operativa (gris), Soporte (oscuro), Transición (claro)

### Iteración y Verificación Continua

Modelar por ciclos cortos: volumen → vanos → circulación → revisión → ajuste. Cada ciclo verificar contra:
- [ ] Intenciones de Diseño (4.1)
- [ ] Área construida ≤ CUS
- [ ] Áreas por espacio ≥ dimensiones mínimas
- [ ] Alturas libres ≥ 2.60 m (2.40 m baños)
- [ ] Circulaciones ≥ 0.90 m

---

## Modelado por Sistemas

### Sistema Estructural (Esquemático)
- [ ] Trama estructural (ejes, claros, dirección de losas)
- [ ] Cimentación: según mecánica de suelos
- [ ] Columnas / muros de carga cada 4-6 m
- [ ] Losas: espesor según claro (maciza ~12-15 cm)
- [ ] Cubierta: pendiente mín 2%, tipo según estrategia bioclimática

### Sistema Arquitectónico
- [ ] Muros exteriores según estrategia bioclimática
- [ ] Muros interiores: block partido o tablaroca
- [ ] Vanos: % ventana/piso del análisis de iluminación
- [ ] Cubierta: plana o inclinada, material de acabado

### Circulaciones y Accesos
- [ ] Modelar recorrido principal como elemento continuo
- [ ] Verificar alturas y anchuras libres
- [ ] Marcar umbrales (cambios de nivel, material, altura)
- [ ] Acceso principal con énfasis

### Instalaciones (Diagramático — Integral+)
- [ ] Ductos verticales y horizontales (solo shafts)
- [ ] Baños agrupados para compartir instalaciones
- [ ] Prever salida campana, ducto gas, punto agua
- [ ] Cuarto de instalaciones (calentador, cisterna, tinacos)

---

```

[ACC] 5.1 Selección de Vistas (P2.0 ref: 5.1)
─────────────────────────────────
INPUT:  4.15 Diseño final + 4.2 Idea rectora
        2.2.1.1 Inmersión (ejes de diseño del cliente)
OPERA:  Seleccionar las vistas que mejor comuniquen la intención
        del proyecto según el paquete contratado
OUTPUT: Lista de vistas seleccionadas con ángulo y propósito
PROC:   HUMANO
```

| Paquete | Vistas obligatorias |
|---------|-------------------|
| Esencial | Exterior general, fachada principal, espacio interior principal |
| Integral | Esencial + espacio clave (cocina/baño), zona exterior, corte perspectivado |
| Ejecutivo | Integral + vistas de detalle constructivo, recorridos |

- [ ] ¿La vista captura la Idea Matriz?
- [ ] ¿Muestra la relación del proyecto con el contexto?
- [ ] ¿Comunica la experiencia del usuario al habitar el espacio?

---

```
[ACC] 5.2 Detallado de Modelado en Vista (P2.0 ref: 5.2)
─────────────────────────────────
INPUT:  4.15 Diseño final + 5.1 Vistas seleccionadas
OPERA:  Modelar en 3D los elementos visibles en cada vista con el
        nivel de detalle según paquete (LOD 200/300/350)
OUTPUT: Modelo 3D listo para renderizar
PROC:   HUMANO
```

- [ ] Geometría arquitectónica completa para las vistas seleccionadas
- [ ] Vanos y cancelería
- [ ] Mobiliario fijo y móvil visible
- [ ] Texturas y materiales asignados

---

## Verificación del Modelo

### Checklist
- [ ] **Programa:** cada espacio con su área correcta
- [ ] **Zonificación SOMA:** cada espacio en la zona correcta
- [ ] **Circulaciones:** recorrido fluido, anchos correctos
- [ ] **Orientación:** modelo orientado al norte real
- [ ] **Accesibilidad:** sin desniveles sin rampa
- [ ] **Estructura:** columnas sin estorbar en espacios
- [ ] **Alturas:** todas ≥ mínimo normativo
- [ ] **Áreas:** total construido ≤ CUS

### Pruebas Visuales Mínimas
- [ ] Vista aérea — ¿la forma se lee claramente?
- [ ] Vista peatonal desde calle — ¿se integra al contexto?
- [ ] Vista interior del espacio principal — ¿la luz entra como se planeó?
- [ ] Corte por espacio principal — ¿relación alturas/vanos funciona?

---

## Salida del Modelado

1. Modelo 3D organizado por capas con nomenclatura definida
2. Vistas seleccionadas con ángulo y propósito
3. Checklist de verificación marcado
4. Notas de diseño — decisiones tomadas durante el modelado
5. Archivo de intercambio (.ifc, .fbx, .obj)

Entrada directa a: Visualización (5.3), Representación (7), Evaluación (4.9), Planos Técnicos (9).

---

## FUENTES

- BIM Forum, *LOD Specification* (2023). bimforum.org
- ISO 19650-1:2018 — BIM.
- Ching, F. (2020). *Building Construction Illustrated.*
- Deplazes, A. (2005). *Constructing Architecture.*
- Allen, E. (2019). *Fundamentals of Building Construction.*
- Reglamento de Construcción del Municipio de Mérida.
