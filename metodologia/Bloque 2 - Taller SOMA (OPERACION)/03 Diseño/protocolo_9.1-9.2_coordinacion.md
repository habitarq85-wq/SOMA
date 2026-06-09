# PROTOCOLO: COORDINACIÓN DE INGENIERÍAS
## Bloque 2 — Taller SOMA (Operación) | Etapa 11 del Ciclo

### ¿Qué es la Coordinación?

Es la gestión de los especialistas externos (ingenieros) que complementan el diseño arquitectónico. SOMA no realiza los cálculos de ingeniería — los coordina, los integra y verifica que sean coherentes con el proyecto.

**Entrada:** Anteproyecto aprobado + Memorias de cálculo de especialistas.
**Salida:** Juego de planos de ingenierías coordinados + memorias técnicas.

### Principio rector

SOMA diseña, los ingenieros calculan, SOMA coordina. El arquitecto es el **director de orquesta** — no toca todos los instrumentos, pero se asegura de que todos suenen juntos.

---

## 1. PERFILES DE ESPECIALISTAS REQUERIDOS

| Especialidad | ¿Cuándo se necesita? | ¿Incluido en qué paquete? |
|-------------|----------------------|--------------------------|
| Ingeniero estructural | Proyectos de más de 1 nivel, o claros >6m | Ejecutivo (+ Integral opcional) |
| Ingeniero hidrosanitario | Todo proyecto con baños y cocina | Integral y Ejecutivo |
| Ingeniero eléctrico | Todo proyecto | Integral y Ejecutivo |
| Ingeniero de climatización | Proyectos que requieran AC central | Ejecutivo |
| Perito en construcción municipal | Para firmar planos de permiso de construcción | Integral y Ejecutivo |
| Topógrafo | Antes de empezar el diseño (Fase 5) | Esencial+ (se contrata por separado) |
| Mecánica de suelos | Proyectos de más de 1 nivel | Ejecutivo |

(Fuente: Reglamento de Construcción del Municipio de Mérida — requisitos de peritos y especialistas)

---

## 2. FLUJO DE COORDINACIÓN

### 2.1 Antes de contratar especialistas
- [ ] Preparar **paquete base** para cada especialista:
  - Planos arquitectónicos del anteproyecto (plantas, cortes, alzados)
  - Nota de diseño (intenciones, restricciones, decisiones clave)
  - Lista de preguntas específicas que el especialista debe resolver
- [ ] Definir **alcance de cada especialista** por escrito (memoria de cálculo, planos, firmas)

### 2.2 Durante el desarrollo de las ingenierías
(Fuente: Project Management Institute, PMBOK Guide — gestión de interesados y comunicaciones)

- [ ] **Punto de control 1 (20% del avance):** Revisar criterios generales y proposed solution
  - ¿El especialista entendió el proyecto?
  - ¿Las soluciones propuestas son compatibles con la arquitectura?
- [ ] **Punto de control 2 (60% del avance):** Revisar planos preliminares
  - ¿Las trayectorias de instalaciones no cruzan zonas nobes?
  - ¿Los ductos y shafts están donde se previeron?
  - ¿Las cargas estructurales son consistentes con la arquitectura?
- [ ] **Punto de control 3 (100%):** Recepción de memorias y planos finales
  - ¿Los planos están en formato compatible (PDF + DWG o RVT)?
  - ¿Las memorias de cálculo están completas y firmadas?

### 2.3 Resolución de conflictos
(Fuente: Schein, Organizational Culture and Leadership — gestión de conflictos en equipos multidisciplinarios)

Cuando un especialista propone algo que afecta la arquitectura:
1. **Identificar el conflicto:** ¿qué elemento arquitectónico se ve afectado? (vista, espacio libre, material, geometría)
2. **Evaluar jerarquía:** ¿es una restricción normativa (no negociable) o una preferencia técnica (negociable)?
3. **Proponer alternativa:** dar al especialista 2 opciones que respeten la intención arquitectónica
4. **Documentar la decisión:** registrar en bitácora qué se decidió, por qué y quién autorizó

---

## 3. CRITERIOS DE VERIFICACIÓN POR ESPECIALIDAD

### 3.1 Estructural
- [ ] ¿La cimentación corresponde al tipo de suelo (roca calcárea Yucatán — losa de cimentación típica)?
- [ ] ¿Las columnas y trabes no obstruyen espacios arquitectónicos críticos?
- [ ] ¿Los claros estructurales corresponden a la modulación arquitectónica?
- [ ] ¿Las losas tienen el espesor adecuado para los claros propuestos?
- [ ] ¿Se consideró la carga de acabados (peso de pisos, muros divisorios)?
- [ ] ¿La estructura de cubierta permite la pendiente de drenaje pluvial?
- [ ] ¿Hay juntas de dilatación donde se requieran (≥30m lineales)?

### 3.2 Hidrosanitario
- [ ] ¿Las bajadas de aguas negras están en ductos verticales accesibles?
- [ ] ¿Los registros están en áreas de servicio (no en sala o recámara)?
- [ ] ¿La cisterna tiene capacidad suficiente (dotación ≥ 150 L/persona/día)?
- [ ] ¿El tinaco está a la altura suficiente para presión por gravedad (≥3m sobre el punto más alto)?
- [ ] ¿Las tuberías de agua caliente están aisladas térmicamente?
- [ ] ¿La pendiente de drenaje (mín 2%) es viable en toda la red?
- [ ] ¿El sistema de captación pluvial (si aplica) tiene filtro de hojas?

### 3.3 Eléctrico
(Fuente: NOM-001-SEDE — Instalaciones Eléctricas)
- [ ] ¿La carga total estimada es correcta (vivienda: ~100W/m²)?
- [ ] ¿El tablero principal está en lugar accesible pero no en área social?
- [ ] ¿Los circuitos están balanceados por fase?
- [ ] ¿Hay contactos cada 2.5m en muros perimetrales? (norma)
- [ ] ¿Hay contactos en exterior (jardín, terraza)? (IP66 mínimo)
- [ ] ¿La iluminación exterior tiene fotocontrol o timer?
- [ ] ¿Las canalizaciones prevén espacio para expansión futura?
- [ ] ¿La acometida cumple con el diámetro mínimo según CFE (10mm² calibre 6)?

### 3.4 Climatización (si aplica)
- [ ] ¿La carga térmica estimada considera: orientación, vanos, ocupación, equipos?
- [ ] ¿Las unidades condensadoras están en lugar ventilado y alejado de recámaras?
- [ ] ¿Las rutas de refrigerante son rectas y cortas (evitar pérdida de eficiencia)?
- [ ] ¿Se previeron drenajes para cada evaporadora?
- [ ] ¿Los difusores de aire no están sobre áreas de estar (evitar corriente directa)?

---

## 4. ENTREGABLES DE COORDINACIÓN

### 4.1 Por especialidad
Cada especialista entrega:
1. **Memoria de cálculo** (PDF firmado) — con criterios, cargas, cálculos
2. **Planos de la especialidad** (PDF + DWG/RVT) — consistentes con planos arquitectónicos
3. **Notas de coordinación** — conflictos detectados y soluciones

### 4.2 Integración final
- [ ] Fusión de planos de ingenierías con modelo arquitectónico (modelo federado)
- [ ] Verificación de interferencias (clash detection: estructura vs instalaciones)
- [ ] Actualización del modelo arquitectónico con shafts y ductos
- [ ] Generación de planos de obra: arquitectura + instalaciones sobrepuestas
- [ ] Documento de "Especificaciones Técnicas Generales" (unificado)
- [ ] Bitácora de coordinación (decisiones, fechas, responsables)

---

## 5. CHECKLIST FINAL DE COORDINACIÓN

- [ ] ¿Todos los especialistas entregaron memoria de cálculo firmada?
- [ ] ¿Los planos de ingeniería están en la misma base arquitectónica que el anteproyecto?
- [ ] ¿Se resolvieron todas las interferencias detectadas?
- [ ] ¿Los shafts y ductos están reflejados en los planos arquitectónicos finales?
- [ ] ¿El perito municipal (si aplica) firmó los planos para permiso?
- [ ] ¿La bitácora de coordinación está completa?
- [ ] ¿El cliente fue informado de los alcances de cada especialidad?

---

## 6. SALIDA DE LA COORDINACIÓN

1. **Juego completo de planos para construcción** (arquitectura + ingenierías)
2. **Memorias técnicas** de cada especialidad
3. **Modelo BIM federado** (todos los sistemas integrados, si se usó Revit)
4. **Bitácora de coordinación** archivada en `proyectos/SOMA-XXXX/coordinacion/`
5. **Planos de permiso listos** para firma de perito y gestión municipal

Este es el **entregable final del paquete Ejecutivo**. Con estos documentos, el cliente puede:
- Solicitar permiso de construcción
- Solicitar cotizaciones a contratistas
- Construir el proyecto

---

## FUENTES

- **Francis D.K. Ching**, *Building Construction Illustrated* (6th ed., 2020) — integración de sistemas constructivos, puntos de conflicto entre disciplinas.
- **Francis D.K. Ching**, *Architecture: Form, Space, & Order* (4th ed., 2014) — como las decisiones estructurales y de instalaciones afectan el espacio arquitectonico.
- **C. M. Deasy**, *Design Places for People* (1974) — coordinacion centrada en el usuario final, no en la eficiencia tecnica.
- **Jacques Paul Grillo**, *Form, Function and Design* (1960) — integracion de sistemas sin sacrificar la unidad formal del proyecto.
- **Project Management Institute**, *PMBOK Guide* (7th ed., 2021) — gestión de interesados, comunicaciones, integración.
- **Reglamento de Construcción del Municipio de Mérida** — requisitos de peritos, firmas responsivas, planos de permiso.
- **William Peña**, *Problem Seeking: An Architectural Programming Primer* (5th ed., 2012) — coordinación del programa arquitectónico como base de la coordinación interdisciplinaria.
- **NOM-001-SEDE** — Instalaciones Eléctricas (distancias de seguridad, especificaciones).

---

*"La coordinación es invisible cuando funciona. Cuando falla, está en todos los planos."*
