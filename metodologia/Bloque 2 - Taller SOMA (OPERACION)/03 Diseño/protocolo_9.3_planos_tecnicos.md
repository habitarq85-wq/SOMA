# PROTOCOLO: PLANOS TÉCNICOS
## Bloque 2 — Taller SOMA (Operación) | Sección 9 del PROCESO DE DISEÑO 2.0
## Referencia: Items 9.3-9.4

**Qué es:** Documentación constructiva detallada que un contratista necesita
para construir el proyecto. Solo se produce para el paquete **SOMA Ejecutivo**.

**Entrada:** Anteproyecto aprobado por el cliente (Sección 8).

**Salida:** Juego completo de planos técnicos + detalles constructivos.

**Principio rector:** Un buen plano técnico no tiene instrucciones escritas —
las cotas y detalles deben ser tan claros que un constructor competente pueda
ejecutar sin preguntar.

---

## 9.3 Complementos Arquitectónicos

```
[OUT] 9.3 Complementos Arquitectónicos (P2.0 ref: 9.3)
─────────────────────────────────
INPUT:  9.2 Proyecto actualizado + Modelo BIM
OPERA:  Desarrollar planos complementarios de detalle
OUTPUT: Juego de planos complementarios (5 sub-items 9.3.1-5)
PROC:   HUMANO
```

### 9.3.1 Plano de Acabados
- [ ] Acabados piso por piso y espacio por espacio
- [ ] Piso, muros, plafones, cubiertas con especificaciones
- [ ] Cuadro de especificaciones en la misma lámina

```
[OUT] 9.3.1 Plano de Acabados (P2.0 ref: 9.3.1)
PROC:   HUMANO (determinar) → AI (generar lámina)
```

### 9.3.2 Plano de Despieces
- [ ] Modulación y cuantificación de piezas
- [ ] Piso, muro, plafón y recubrimientos

```
[OUT] 9.3.2 Plano de Despieces (P2.0 ref: 9.3.2)
PROC:   HUMANO (diseño) → AI (cuantificación)
```

### 9.3.3 Planos de Cancelería, Herreros, Carpintería
- [ ] Vistas, cortes, detalles de unión, materiales y acabados
- [ ] Barandales y pérgolas

```
[OUT] 9.3.3 Planos de Elementos Fabricados (P2.0 ref: 9.3.3)
PROC:   HUMANO
```

### 9.3.4 Planos de Detalles de Baño, Cocina, Escalera
- [ ] Escala 1:20 o 1:10
- [ ] Cotas, cortes, detalles de colocación y unión

```
[OUT] 9.3.4 Planos de Detalle (P2.0 ref: 9.3.4)
PROC:   HUMANO
```

### 9.3.5 Planos de Detalles Generales
- [ ] Goteros, juntas, uniones, impermeabilización
- [ ] Anclajes, encuentros de materiales

```
[OUT] 9.3.5 Planos de Detalles Constructivos (P2.0 ref: 9.3.5)
PROC:   HUMANO
```

---

## Planos Ejecutivos Arquitectónicos (Escala 1:50)

### Plantas Ejecutivas
- [ ] Muros con espesor exacto y capas (block + repellado + pintura / block + cámara + tablaroca)
- [ ] Vanos con identificación y dimensiones de paño y derrame
- [ ] Puertas con especificación (madera sólida, tambor, herrajes)
- [ ] Acabados: símbolo de piso en cada espacio
- [ ] Muebles de baño y cocina acotados
- [ ] Equipos: calentador, tinaco, cisterna, minisplit
- [ ] Cadena de cotas completa (ejes, paños, vanos)
- [ ] NPT de cada espacio (±0.5 cm)
- [ ] Indicadores de cortes de detalle (DET-01, etc.)
- [ ] Cuadro de vanos en la misma lámina

### Cortes Ejecutivos (1:25 o 1:20)
- [ ] Composición de cubierta capa por capa
- [ ] Composición de muro exterior capa por capa
- [ ] Cimentación: tipo, profundidad, armado esquemático
- [ ] Encuentro muro-cubierta: junta, impermeabilización, goterón
- [ ] Losa de entrepiso: espesor, capas, acabado
- [ ] Benchmarks (NPT + banqueta + terreno natural)

### Detalles Constructivos (1:10, 1:5)
- [ ] Encuentro muro-cubierta (impermeabilización)
- [ ] Encuentro muro-piso (zócalo, junta)
- [ ] Vanos (derrame, marco, burlete)
- [ ] Cambio de material (concreto-madera)
- [ ] Escaleras (arranque, descanso, llegada)
- [ ] Barandal (fijación a piso/muro, perfil)
- [ ] Celosías y protecciones solares
- [ ] Cubierta (lámina, teja, losa verde)

---

## 9.4 Elaboración de Documentos Ejecutivos

```
[OUT] 9.4 Documentos Ejecutivos (P2.0 ref: 9.4)
─────────────────────────────────
INPUT:  9.2 Proyecto actualizado + 9.3 Complementos
        9.1 Ingenierías definitivas + 8.5 Perspectivas
OPERA:  Compilar todo en la entrega final: planos de todos los
        ingenieros + planos arquitectónicos + complementos +
        perspectivas. Crear presentación HTML navegable
OUTPUT: • Carpeta de Proyecto Ejecutivo completa (digital)
        • Documento HTML de entrega final (navegable)
        • PDF compilado para impresión
PROC:   AI (compilación y generación de documentos)
```

---

## Salida de Planos Técnicos

### Estructura de carpeta de entrega:
```
SOMA-XXXX_Ejecutivo/
├── 00_Presentacion/
├── 01_Planos_Arquitectonicos/
│   ├── 01_Plantas/
│   ├── 02_Cortes/
│   ├── 03_Alzados/
│   └── 04_Detalles/
├── 02_Ingenierias/
│   ├── 01_Estructural/
│   ├── 02_Hidrosanitaria/
│   ├── 03_Electrica/
│   └── 04_Climatizacion/
├── 03_Complementarios/
│   ├── 01_Acabados/
│   ├── 02_Despieces/
│   ├── 03_Canceleria/
│   ├── 04_Detalles_Baño_Cocina/
│   └── 05_Detalles_Generales/
├── 04_Renders/
├── 05_Dossier/
└── 06_Memorias/
```

---

## FUENTES

- ISO 13567 — Technical product documentation, layer naming.
- NOM-008-SCFI — Sistema General de Unidades de Medida.
- Ching, F. (2020). *Building Construction Illustrated.*
- Ching, F. (2015). *Architectural Graphics.*
- Deplazes, A. (2005). *Constructing Architecture.*
- Allen, E. (2019). *Fundamentals of Building Construction.*
- IMCA — Instituto Mexicano de la Construcción.
- Reglamento de Construcción del Municipio de Mérida.
