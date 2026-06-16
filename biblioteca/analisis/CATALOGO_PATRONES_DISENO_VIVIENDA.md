# Catálogo de Patrones de Diseño — Biblioteca SOMA

> Item 2.1.3.3 — Construir el catálogo de patrones de diseño
> AI→HUMANO: AI compila primer catálogo, humano cura

## Estructura del Patrón

Cada patrón incluye:
- **ID**: Código único en el catálogo
- **Nombre**: Título del patrón
- **Tipo**: Acontecimiento / Espacial / De uso / Tectónico / Bioclimático
- **Descripción**: Qué resuelve y cuándo aplica
- **Relaciones**: Patrones relacionados
- **Referencia**: Fuente (Alexander, SOMA, otro)

---

## PATRONES SOMA

### SP-01 | Patio Central
- **Tipo**: Espacial
- **Descripción**: Espacio abierto central que organiza las habitaciones a su alrededor. Provee luz, ventilación y conexión visual.
- **Relaciones**: SP-02 (Galería Perimetral), BC-01 (Ventilación Cruzada)
- **Referencia**: Casa colonial yucateca, Alexander 106 (+Positive Outdoor Space)

### SP-02 | Galería Perimetral (Corredor/Zaguán)
- **Tipo**: Espacial
- **Descripción**: Espacio de transición techado entre el interior y el exterior. Protege del sol y la lluvia mientras permite ventilación.
- **Relaciones**: SP-01 (Patio Central), BC-01 (Ventilación Cruzada)
- **Referencia**: Arquitectura colonial y porfiriana yucateca

### SP-03 | Solar (Traspatio Productivo)
- **Tipo**: De uso / Acontecimiento
- **Descripción**: Área trasera no construida destinada a servicios, vegetación, animales o huerto. Es parte integral de la vivienda maya.
- **Relaciones**: SP-01 (Patio Central)
- **Referencia**: Casa maya contemporánea, tradición yucateca

### SP-04 | Zaguán / Vestíbulo de Transición
- **Tipo**: Espacial
- **Descripción**: Espacio cubierto en la entrada que filtra la vista desde la calle hacia el interior. Sirve como sala de espera, recibidor y control de privacidad.
- **Relaciones**: SP-02 (Galería Perimetral)
- **Referencia**: Casa colonial y porfiriana

### SP-05 | Habitaciones en Batería (Ala Lineal)
- **Tipo**: Espacial
- **Descripción**: Habitaciones alineadas una tras otra con acceso directo a la galería o patio. Cada una tiene puerta al exterior sin pasillo interior.
- **Relaciones**: SP-01 (Patio Central), SP-02 (Galería Perimetral)
- **Referencia**: Casa maya, vivienda popular yucateca

### SP-06 | Doble Altura / Espacio Vertical Continuo
- **Tipo**: Espacial
- **Descripción**: Altura libre de 4-6 m en el espacio principal para estratificación térmica (calor sube, zona ocupada fresca).
- **Relaciones**: BC-01 (Ventilación Cruzada), BC-02 (Chimenea Térmica)
- **Referencia**: Alexander 190 (+Ceiling Height Variety), Givoni (1969)

### SP-07 | Vacío Interior Conectado Visualmente
- **Tipo**: Espacial
- **Descripción**: Hueco vertical que conecta dos niveles visual pero no funcionalmente. Genera sensación de amplitud y conexión.
- **Relaciones**: SP-06 (Doble Altura)
- **Referencia**: Alexander 191 (+The Shape of Indoor Space)

---

### US-01 | Cocina Abierta al Comedor
- **Tipo**: De uso
- **Descripción**: Cocina visualmente conectada al comedor, pero con posibilidad de cerrarse mediante celosías o cancelería.
- **Relaciones**: SP-02 (Galería Perimetral), AC-01 (Celosía / Filtro)
- **Referencia**: Vivienda contemporánea mexicana

### US-02 | Baño con Ventilación Natural Directa
- **Tipo**: De uso / Bioclimático
- **Descripción**: Baño con ventana al exterior para evacuación de humedad y olores sin extractor mecánico.
- **Relaciones**: BC-01 (Ventilación Cruzada)
- **Referencia**: NTC Proyecto Arquitectónico, habitabilidad e higiene

### US-03 | Cuarto de Lavado / Servicio con Acceso Exterior
- **Tipo**: De uso
- **Descripción**: Área de lavado y tendedero con acceso directo al solar o azotea, separado pero cercano a la cocina.
- **Relaciones**: SP-03 (Solar), SP-04 (Zaguán)
- **Referencia**: Vivienda popular mexicana

### US-04 | Estancia Multifuncional (Sala-Comedor-Estancia)
- **Tipo**: De uso
- **Descripción**: Espacio principal sin divisiones fijas que alberga sala, comedor y estar. Muebles definen zonas.
- **Relaciones**: SP-01 (Patio Central), SP-06 (Doble Altura)
- **Referencia**: Casa maya, vivienda minimalista contemporánea

---

### AC-01 | Celosía / Filtro Visual
- **Tipo**: Tectónico
- **Descripción**: Elemento perforado (tabique, madera, concreto, block de vidrio) que filtra luz, vista y ventilación.
- **Relaciones**: BC-02 (Control Solar), SP-02 (Galería Perimetral)
- **Referencia**: Arquitectura moderna mexicana (Barragán, Legorreta)

### AC-02 | Pérgola / Estructura de Sombreado
- **Tipo**: Tectónico
- **Descripción**: Estructura ligera con travesaños que genera sombra rayada. Puede ser de madera, acero o concreto.
- **Relaciones**: BC-02 (Control Solar), SP-02 (Galería Perimetral)
- **Referencia**: Arquitectura tropical, climatización pasiva

### AC-03 | Muro de Mampostería / Piedra / Chukum
- **Tipo**: Tectónico
- **Descripción**: Muro macizo de piedra, block o recubrimiento de chukum que aporta inercia térmica y textura local.
- **Relaciones**: BC-03 (Inercia Térmica), AC-01 (Celosía)
- **Referencia**: Arquitectura yucateca tradicional y contemporánea

### AC-04 | Cubierta Ligera / Palapa
- **Tipo**: Tectónico
- **Descripción**: Techo de material vegetal (guano, palapa) o lámina con cámara de aire. Bajo peso, alta reflectividad, aislante natural.
- **Relaciones**: BC-01 (Ventilación Cruzada), BC-02 (Control Solar)
- **Referencia**: Casa maya, arquitectura de playa

### AC-05 | Entortado / Bóveda Catalana
- **Tipo**: Tectónico
- **Descripción**: Sistema de techo de ladrillo y mortero de origen colonial. Inercia térmica, acústica, durabilidad.
- **Relaciones**: BC-03 (Inercia Térmica)
- **Referencia**: Arquitectura colonial yucateca

---

### BC-01 | Ventilación Cruzada
- **Tipo**: Bioclimático
- **Descripción**: Aperturas en fachadas opuestas o adyacentes que permiten flujo de aire continuo. Ventanas altas para extracción.
- **Relaciones**: SP-01 (Patio Central), SP-06 (Doble Altura)
- **Referencia**: Givoni (1969, 1998), Olgyay (1963)

### BC-02 | Control Solar Pasivo (Aleros / Volados / Parasoles)
- **Tipo**: Bioclimático
- **Descripción**: Elementos horizontales o verticales que bloquean la radiación solar directa según orientación y latitud.
- **Relaciones**: AC-01 (Celosía), AC-02 (Pérgola)
- **Referencia**: Olgyay (1963), NOM-020-ENER (2011)

### BC-03 | Inercia Térmica en Muros y Losas
- **Tipo**: Bioclimático
- **Descripción**: Masa térmica (concreto, piedra, ladrillo) que absorbe calor de día y lo libera de noche, amortiguando picos.
- **Relaciones**: AC-03 (Muro de Mampostería)
- **Referencia**: Givoni (1998)

### BC-04 | Estratificación Térmica (Doble Altura + Ventilación Alta)
- **Tipo**: Bioclimático
- **Descripción**: El aire caliente sube y se extrae por aperturas altas; el fresco permanece a nivel de uso.
- **Relaciones**: SP-06 (Doble Altura), BC-01 (Ventilación Cruzada)
- **Referencia**: Clima cálido-húmedo, Givoni

### BC-05 | Cubierta Reflectiva / Ajardinada
- **Tipo**: Bioclimático
- **Descripción**: Cubierta clara, con recubrimiento reflectivo o vegetación para reducir ganancia de calor por radiación.
- **Relaciones**: BC-03 (Inercia Térmica)
- **Referencia**: NOM-020-ENER, techos verdes tropicales

### BC-06 | Captación de Agua Pluvial
- **Tipo**: Bioclimático
- **Descripción**: Sistema de recolección de agua de lluvia desde cubiertas hacia cisterna. Para riego y usos no potables.
- **Relaciones**: SP-03 (Solar)
- **Referencia**: Estrategias sustentables Yucatán (acuífero único, sin drenaje pluvial municipal)

### BC-07 | Protección de Lluvias Torrenciales (Aleros Anchos / Canales)
- **Tipo**: Bioclimático
- **Descripción**: Aleros de más de 60 cm para proteger muros y vanos de la lluvia horizontal. Canales y bajadas pluviales sobredimensionadas.
- **Relaciones**: BC-02 (Control Solar), SP-02 (Galería Perimetral)
- **Referencia**: Clima cálido-húmedo con tormentas tropicales

---

### EC-01 | Integración al Contexto Urbano / Patrimonial
- **Tipo**: Acontecimiento / Guía
- **Descripción**: El proyecto debe dialogar con su entorno construido: alturas, materiales, ritmo de vanos, colores, alineamiento.
- **Relaciones**: SP-04 (Zaguán), AC-03 (Mampostería)
- **Referencia**: Reglamento de Construcción de Mérida, Plan de Desarrollo Urbano

### EC-02 | Privacidad Progresiva (Calle → Semipúblico → Privado → Íntimo)
- **Tipo**: Acontecimiento
- **Descripción**: Gradiente de privacidad desde el zaguán hasta los dormitorios. El patio como filtro.
- **Relaciones**: SP-01 (Patio Central), SP-04 (Zaguán), AC-01 (Celosía)
- **Referencia**: Alexander 127 (+Intimacy Gradient)

### EC-03 | Umbral de Entrada / Bienvenida
- **Tipo**: Acontecimiento
- **Descripción**: La entrada debe tener un espacio de transición que invite: banco, vegetación, luz indirecta, cambio de material.
- **Relaciones**: SP-04 (Zaguán), EC-02 (Privacidad Progresiva)
- **Referencia**: Alexander 112 (+Entrance Transition)

---

## Cómo Usar Este Catálogo

1. AI selecciona patrones aplicables al proyecto (según clima, programa, tipología, cultura)
2. Humano revisa y ajusta la selección
3. Los patrones seleccionados guían el diseño conceptual
4. Se documentan en la memoria de diseño qué patrones se usaron y por qué
5. El catálogo se enriquece con cada proyecto

> Este es un documento vivo. Los patrones se añaden, refinan o eliminan según la experiencia de cada proyecto.
