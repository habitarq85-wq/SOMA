# PROTOCOLO 02: ENTREVISTA DE INMERSION PROFUNDA
## Bloque 2 — Taller SOMA (Operacion)

Esta entrevista es la primera reunion presencial con el cliente. Se realiza
apoyandose en la **App de Entrevista** (`aplicaciones_python/app_inmersion/`,
puerto 5050) que graba la conversacion y estructura los datos.

La dinamica es conversacional en 6 topicos. El arquitecto lleva el hilo;
la app registra audio, tiempo por topico y el formulario post-entrevista.

---

## Flujo de la Entrevista (6 Topicos)

### Topico 1: La razon de estar aqui
*Objetivo: Entender el encargo, el sitio y las reglas del juego.*

- Describa el proyecto: que quiere construir, donde, para que.
- Terreno: dimensiones, ubicacion, si ya es propietario.
- Reglas: manual de construccion del fraccionamiento, restricciones conocidas.
- Tomador de decisiones: quien tiene la ultima palabra en lo estetico y economico.
- Presupuesto: el presupuesto incluye el terreno? o es solo construccion +
  honorarios?

### Topico 2: Los habitantes
*Objetivo: Construir la UserEntity de cada habitante.*

- Quienes van a habitar el edificio? (cantidad, edades, salud/movilidad).
- Tipos de usuarios: residentes fijos, visitas frecuentes, personal de servicio.
- Capacidad de usuarios: accesibilidad, necesidades especiales.
- Quien pasa mas tiempo en casa? Quien trabaja desde casa?
- Mascotas.

### Topico 3: El programa arquitectonico
*Objetivo: Registrar los espacios solicitados para analizar despues que
espacios complementarios necesita.*

- Recamaras: cantidad, todas con bano y closet? recamara en PB?
- Banos: banjo de visitas, medios banos.
- Zonas de trabajo/hobby: oficina, estudio, taller, gimnasio, cava, cuarto de TV.
- Servicios: cuarto de servicio con bano, lavado, bodega, cochera (autos).
- Extras: alberca, terraza, jardin, roof garden.
- Colecciones o equipamiento especial que requiera espacio dedicado.
- NO se complementa en el momento — se registra para analisis posterior.

### Topico 4: Dinamicas y rutinas
*Objetivo: Poblar la ActivityMatrix de 24 slots.*

- Como es un dia entre semana en la familia? (despertar, comidas, trabajo,
  llegada a casa, dormir).
- Como son los fines de semana?
- Quien cocina? Se come junto o separado?
- Reciben visitas seguido? Fiestas? Familia que se queda a dormir?
- Rutinas de mascotas.
- Clima: prefieren ventilacion natural o A/C? Que tanto uso de aire esperan?
- Materiales: busqueda de materiales "eternos" o aprecian la patina y la nobleza
  de la madera/piedra?
- Orden: espacios que deban ser faciles de limpiar vs. espacios que puedan tener
  "desorden creativo".

### Topico 5: Inversion
*Objetivo: Validar la viabilidad economica y definir prioridades.*

- Presupuesto realista: cuanto pueden invertir en el proyecto completo?
- El proyecto se construira de una sola vez o por etapas?
- Prioridad: prefieren mas metros cuadrados con acabados sencillos, o menos
  metros con acabados de lujo?
- Honorarios de diseno incluidos en el presupuesto?
- Rango de obra esperado (terceros): $14k–$16.5k (Esencial), $18.5k–$23k
  (Integral), $28k–$40k (Ejecutivo) por m2.

### Topico 6: La cereza del pastel (Poetica)
*Objetivo: Extraer el CreativeCore y el Mensaje Creativo.*

- Si al entrar a tu casa pudieras sentir un solo adjetivo (paz, poder, orden,
  libertad), cual seria?
- Cual es tu recuerdo mas feliz relacionado con un espacio?
- Hay algun mueble, cuadro u objeto que deba dictar el diseno de un espacio?
- Que es lo que NO quieres que pase en este proceso o en el resultado final?
- Como te imaginas viviendo en este espacio en 10 anos?
- Cierre breve de la filosofia SOMA: automatizamos lo tecnico, liberamos el
  diseno. Explicar como trabajamos (disenamos, no construimos; tenemos
  coadyuvantes externos) y proceso de anticipos/cobros.

---

## Post-Entrevista (Formulario en App)

Al finalizar la grabacion, el arquitecto llena en la app:

- Cliente: nombre completo, correo, telefono.
- Habitantes: resumen de UserEntity.
- Programa: lista de espacios solicitados.
- Rutinas: notas sobre ActivityMatrix.
- Inversion: presupuesto confirmado, etapas.
- Notas adicionales del arquitecto.
- Checkbox: "Analizar con IA" (procesar con DeepSeek Flash cuando este
  configurado).

---

## Procesamiento (IA)

1. **Transcripcion:** `faster-whisper` (local) convierte el audio a texto.
2. **Analisis:** `DeepSeek Flash API` recibe la transcripcion + base de
   conocimiento SOMA (Psicologia Ambiental, Patrones Alexander, Space Syntax,
   Environmental Behavior, POE, Proxemica).
3. **Salida:**
   - `guia_de_diseno.md` — documento para el equipo de diseno.
   - `datos_estructurados.json` — Activity Matrix, ejes, CreativeCore.

---

## Estructura de proyecto generada

```
backend/proyectos/SOMA-YYYYMMDD-XXXX/
  info.json                ← metadatos (estado, cliente, fechas)
  entrevista.webm          ← grabacion de audio
  transcripcion.txt        ← salida de Whisper
  guia_de_diseno.md        ← documento para disenadores
  datos_estructurados.json ← Activity Matrix, ejes, etc.
```

---

## Complementariedad Web + Entrevista

| Fuente | Que captura | Como se usa |
|--------|-------------|-------------|
| Inmersion Web (10 ejes) | Preferencias visuales A/B | Parametros de fachada, planta, materialidad |
| Entrevista (6 topicos) | Contexto profundo: habitantes, rutinas, poetica | Guia de diseno unificada |

Ambas fuentes se fusionan en la `guia_de_diseno.md` de cada proyecto.
