# PROTOCOLO: ANTEPROYECTO
## Bloque 2 — Taller SOMA (Operación) | Secciones 6 y 8 del PROCESO DE DISEÑO 2.0
## Referencia: Items 6.1-6.2 (Básico), 8.1-8.6 (Integral)

**Qué es:** Formalización del diseño en planos arquitectónicos presentables.
El cliente puede entenderlos y un constructor puede cotizar.

**Entrada:** Modelo 3D evaluado y corregido (de Evaluación 4.14-4.15).

**Salida:** Juego de planos de anteproyecto para aprobación del cliente.

---

## 6. Planimetría — Etapa Básica (SOMA Esencial)

```
[HUMANO→AI] 6.1 Plantas Arquitectónicas (P2.0 ref: 6.1)
─────────────────────────────────
INPUT:  4.15 Diseño final + Modelo 3D (desde 5.2 o CAD/BIM)
OPERA:  Generar láminas: planta de conjunto, plantas de distribución
        por nivel, cotas, ejes, nombres de espacios, norte, escala
OUTPUT: Lámina(s) de plantas arquitectónicas (PDF)
PROC:   HUMANO (prepara) → AI (genera lámina base desde modelo)
```

```
[HUMANO→AI] 6.2 Alzados Arquitectónicos (P2.0 ref: 6.2)
─────────────────────────────────
INPUT:  4.15 Diseño final + Modelo 3D
        4.11.5 Fachadas + 4.8.5 Materiales
OPERA:  Generar alzados de todas las fachadas con cotas verticales,
        materiales anotados y escala gráfica
OUTPUT: Lámina(s) de alzados arquitectónicos (PDF)
PROC:   HUMANO (prepara) → AI (genera lámina base desde modelo)
```

### Lámina de presentación
- [ ] Nombre del proyecto y cliente
- [ ] Ubicación y dirección del predio
- [ ] Área de terreno y área construida
- [ ] Cuadro de áreas por nivel
- [ ] Escala gráfica + flecha de norte
- [ ] "SOMA Taller Virtual de Arquitectura · MM. Arq. Juan José Piña May"

### Planta de Conjunto (1:100 o 1:75)
- [ ] Polígono del predio con dimensiones y colindancias
- [ ] Proyección de cubiertas con pendientes
- [ ] Áreas exteriores, vegetación, accesos
- [ ] Restricciones marcadas (línea punteada)

### Planta(s) Arquitectónica(s) por nivel (1:75 o 1:50)
- [ ] Muros con espesor real
- [ ] Vanos con identificación y dimensiones
- [ ] Cotas de todos los espacios
- [ ] Nombres de cada espacio + área en m²
- [ ] NPT en cada espacio
- [ ] Escalera: número de escalones, huella, contrahuella

### Cortes Arquitectónicos (1:75)
- [ ] Mínimo 2 cortes (longitudinal y transversal)
- [ ] Niveles de piso terminado y banqueta
- [ ] Alturas libres acotadas
- [ ] Composición de cubierta esquemática

### Alzados (1:75)
- [ ] Las 4 fachadas con cotas verticales
- [ ] Materiales anotados (texto)
- [ ] Vegetación y contexto (siluetas)

---

## 8. Anteproyecto — Etapa Integral (SOMA Integral)

```
[DEC] 8.1 Selección Real de Acabados (P2.0 ref: 8.1)
─────────────────────────────────
INPUT:  4.8.5 Paleta de materiales (conceptual)
        Presupuesto + disponibilidad local
OPERA:  Convertir paleta conceptual en acabados reales: productos
        específicos (marca, modelo), proveedores locales, costo/m²
OUTPUT: Tabla de acabados reales con proveedores y costos
PROC:   HUMANO
```

```
[GUI] 8.2 Criterio de Instalaciones Hidrosanitarias (P2.0 ref: 8.2)
─────────────────────────────────
INPUT:  4.15 Diseño final + 2.2.2.1 Acometidas existentes
OPERA:  Definir bajantes, registros, diámetros tentativos, captación
        pluvial, cisterna, tinaco, calentador, bombeo
OUTPUT: Diagrama de criterio hidrosanitario sobre planta
PROC:   HUMANO (criterio) → AI (verificación dimensional)
```

```
[GUI] 8.3 Criterio de Estructura (P2.0 ref: 8.3)
─────────────────────────────────
INPUT:  4.8.6 Sistema estructural propuesto
        2.2.2.1 Mecánica de suelos (si existe)
        3.7 Restricciones normativas
OPERA:  Definir sistema, claros máximos, secciones tentativas,
        cimentación, material
OUTPUT: Esquema estructural con ejes y secciones tentativas
PROC:   HUMANO (decisión) → AI (cálculos preliminares)
```

```
[HUMANO→AI] 8.4 Planos de Permiso (P2.0 ref: 8.4)
─────────────────────────────────
INPUT:  6.1-6.2 Plantas y alzados actualizados
        8.2-8.3 Criterios de ingeniería
        3.7 Restricciones normativas
OPERA:  Generar planos para trámite municipal: plantas, alzados,
        cortes, cimentación, estructura, instalaciones, fachadas
OUTPUT: Juego de planos de permiso (PDF, para firma y sello)
PROC:   HUMANO (prepara) → AI (genera formato) → HUMANO (revisa y sella)
```

```
[ACC] 8.5 Perspectivas Adicionales (P2.0 ref: 8.5)
─────────────────────────────────
INPUT:  8.4 Planos de permiso + 5.1 Vistas seleccionadas
OPERA:  Generar perspectivas adicionales: fachada con contexto,
        interiores adicionales, vistas aéreas, esquemas
OUTPUT: Juego adicional de renders y diagramas
PROC:   HUMANO→AI→HUMANO
```

```
[OUT] 8.6 Documento de Entrega Integral (P2.0 ref: 8.6)
─────────────────────────────────
INPUT:  6.1-6.2 Planos + 8.4 Planos de permiso
        8.1 Tabla de acabados + 8.5 Perspectivas
        7.1 HTML actualizado
OPERA:  Compilar todo en carpeta de entrega organizada
OUTPUT: Carpeta de entrega Integral (digital, por secciones)
PROC:   AI (compilación)
```

---

## Salida del Anteproyecto

### Esencial ($250/m²)
- [ ] Lámina de presentación
- [ ] Planta de conjunto
- [ ] Plantas arquitectónicas por nivel
- [ ] 2 cortes
- [ ] 4 alzados

### Integral ($350/m²) — todo lo anterior más:
- [ ] Tabla de acabados reales con proveedores
- [ ] Criterio hidrosanitario
- [ ] Criterio estructural
- [ ] Planos de permiso municipal
- [ ] Perspectivas adicionales
- [ ] Dossier HTML de entrega

---

## FUENTES

- Ching, F. (2015). *Architectural Graphics.*
- Ching, F. (2020). *Building Construction Illustrated.*
- NOM-008-SCFI — Sistema General de Unidades de Medida.
- Reglamento de Construcción del Municipio de Mérida.
- ISO 13567 — Organization and naming of layers.
