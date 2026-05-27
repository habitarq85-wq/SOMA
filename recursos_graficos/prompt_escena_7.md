# ESCENA 7 — CIERRE
*Duración: ~3 segundos*

## Concepto
Identidad visual de SOMA. El nombre y el lema como conclusión de todo lo visto. La síntesis del mensaje: lo protocolario se programa, lo creativo se libera.

## Textos en pantalla (timing exacto)

| # | Texto | Timing | Posición | Animación |
|---|-------|--------|----------|-----------|
| 1 | `"SOMA"` | t=0.0s aparece | Centrado (x=50%, y=38%) | Fundido 0.6s in. Tamaño grande (60pt). Sin animación adicional |
| 2 | `"TALLER VIRTUAL DE ARQUITECTURA"` | t=0.6s aparece | Centrado debajo de SOMA (x=50%, y=48%) | Fundido 0.5s in. Tamaño medio (24pt). Tracking (letter-spacing) amplio |
| 3 | `"LO PROTOCOLARIO SE PROGRAMA"` | t=1.5s aparece | Centrado (x=50%, y=65%) | Fundido 0.5s in. Tamaño pequeño (16pt). Tipografía más delgada (peso Light) |
| 4 | `"LO CREATIVO SE LIBERA"` | t=2.0s aparece | Centrado debajo del anterior (x=50%, y=72%) | Fundido 0.5s in. Mismo estilo que el anterior |

**Todos los textos se mantienen visibles juntos desde t=2.5s hasta t=3.0s.** Luego fundido a negro de 0.8s.

**Tipografía:**
- "SOMA": Sans-serif, peso Bold o SemiBold, color #bc4b21, tracking normal
- "TALLER VIRTUAL DE ARQUITECTURA": Sans-serif, peso Light, color #bc4b21 al 80%, tracking amplio (+0.2em)
- Lemas: Sans-serif, peso Light, color #bc4b21 al 70%, tamaño más pequeño

## Especificaciones de cámara
No aplica — no hay cámara. Fondo negro absoluto sin textura, sin gradiente, sin elemento visual alguno.

## Iluminación
No aplica.

## Paleta de colores

- **Fondo:** #000000 (negro absoluto)
- **"SOMA":** #bc4b21 (terracota pleno)
- **"TALLER VIRTUAL DE ARQUITECTURA":** #bc4b21 con opacidad 80%
- **Lemas:** #bc4b21 con opacidad 70%

## Composición

Todo el texto está centrado horizontalmente. El eje vertical está equilibrado:

```
                    (35% del alto)
        S O M A     (grande, bold)
  TALLER VIRTUAL DE ARQUITECTURA  (medio, light, tracking amplio)
                    (espacio)
  lo protocolario se programa      (pequeño, light)
  lo creativo se libera            (pequeño, light)
                    (resto del espacio)
```

No hay logotipo, no hay ícono, no hay línea separadora. Solo tipografía sobre negro. El diseño debe recordar a un crédito final de cine minimalista.

## Elementos visuales clave

- Ninguno — solo texto sobre negro
- Sin sombras, sin brillos, sin partículas, sin texturas
- Sin animación adicional más allá de los fundidos de entrada

## Secuencia

| Tiempo | Evento |
|--------|--------|
| t=0.0s - 0.6s | Fundido de entrada de "SOMA" |
| t=0.6s - 1.1s | Fundido de entrada de "TALLER VIRTUAL DE ARQUITECTURA" |
| t=1.1s - 1.5s | Pausa — solo los dos textos visibles |
| t=1.5s - 2.0s | Fundido de entrada de "lo protocolario se programa" |
| t=2.0s - 2.5s | Fundido de entrada de "lo creativo se libera" |
| t=2.5s - 3.0s | Todos los textos visibles — pausa de 0.5s para lectura |
| t=3.0s - 3.8s | Fundido lento a negro de 0.8s |

## Nota para producción
Esta escena no requiere generación de video por IA — puede componerse directamente en cualquier software de edición (Premiere, After Effects, DaVinci Resolve). Si el flujo de trabajo requiere que Gemini genere también esta escena, solicitar: fondo negro de 4 segundos, sin elementos visuales, para superponer tipografía en postproducción.

**Fin del video.**
