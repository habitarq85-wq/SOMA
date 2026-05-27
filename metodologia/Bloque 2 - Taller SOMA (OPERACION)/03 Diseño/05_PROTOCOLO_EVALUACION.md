# PROTOCOLO: EVALUACIÓN DE HABITABILIDAD
## Bloque 2 — Taller SOMA (Operación) | Etapa 8 del Ciclo

### ¿Qué es la Evaluación?

Es la auditoría sistemática del proyecto contra indicadores de habitabilidad antes de liberar la documentación final. No es opcional — es el control de calidad del taller SOMA.

**Entrada:** Modelo 3D + Planos de anteproyecto (de Etapas 5, 6, 7).
**Salida:** Tabla de indicadores evaluados ✅/⚠️/❌ con ajustes documentados.

### Principio rector

La evaluación no juzga la estética — verifica que el proyecto **funciona** para el ser humano que lo va a habitar.

---

## 1. INDICADORES TÉRMICOS
(Fuentes: ISO 7730:2005 / ISO 7730:2025 — PMV/PPD para confort térmico, iso.org/standard/39155.html; ASHRAE Standard 55 — Thermal Environmental Conditions for Human Occupancy, ashrae.org; NOM-020-ENER-2011 — Eficiencia energética en edificaciones, México)

### 1.1 Criterios de evaluación

| Indicador | Rango aceptable | Herramienta de verificación |
|-----------|-----------------|---------------------------|
| Temperatura operativa | 22°C – 26°C (Mérida, clima cálido) | Carta psicrométrica / Climate Consultant |
| Humedad relativa | 40% – 70% | Carta psicrométrica |
| Velocidad de aire | 0.2 – 1.0 m/s (ventilación natural) | CFD básico / cálculo manual |
| PMV (voto medio estimado) | −0.5 a +0.5 | ISO 7730 cálculo (herramienta online) |
| PPD (porcentaje insatisfechos) | < 10% | ISO 7730 cálculo |
| Diferencia de temperatura radiante | < 5°C entre muros opuestos | Simulación solar |

### 1.2 Checklist
- [ ] **Radiación solar directa en vanos:** Verificar que vanos E/O tengan protección solar (alero, celosía, volado). Vanos N-S pueden tener menor protección.
- [ ] **Ventilación cruzada:** ¿Cada espacio habitable tiene dos muros opuestos con vanos? Si no, ¿hay ventilación inducida (efecto chimenea)?
- [ ] **Cubierta:** Reflectancia solar ≥ 0.7 (cool roof) para clima cálido. ¿La cubierta está aislada térmicamente?
- [ ] **Muros exteriores:** ¿La composición del muro (block + repellado + aislamiento) cumple la transmitancia térmica recomendada para Mérida (U ≤ 1.5 W/m²K)?
- [ ] **Zonificación térmica:** ¿Las zonas A (confort natural) están correctamente ubicadas (Social + Descanso)? ¿Zonas C (asistido) en Soporte?

---

## 2. INDICADORES DE ILUMINACIÓN
(Fuentes: NOM-025-STPS-2008 — Iluminación en centros de trabajo; Christopher Alexander, A Pattern Language — patrones 135, 161 sobre luz natural; 01_PROTOCOLO_ANALISIS.md — % de ventana por espacio)

### 2.1 Criterios

| Espacio | Iluminancia recomendada (lux) | % ventana-piso | Temperatura color |
|---------|------------------------------|----------------|-------------------|
| Sala / Social | 200–300 lux | 15–25% | 3000K–3500K (cálida) |
| Recámara / Descanso | 100–200 lux | 10–20% | 2700K–3000K (cálida) |
| Cocina / Operativa | 300–500 lux | 15–25% | 4000K (neutra) |
| Baño | 200–300 lux | 5–10% (privacidad) | 4000K (neutra) |
| Circulaciones / Transición | 100–150 lux | 5–10% | 3000K (cálida) |
| Estudio / Trabajo | 300–500 lux | 20–30% | 4000K–5000K |

### 2.2 Checklist
- [ ] **% ventana-piso:** Cada espacio cumple el % mínimo para su zona? (del análisis de iluminación en Protocolo de Análisis)
- [ ] **Protección solar:** Vanos E/O tienen protección? Vanos N-S sin protección directa?
- [ ] **Deslumbramiento:** ¿Ningún plano de trabajo (mesa, escritorio, cocina) tiene luz solar directa?
- [ ] **Balance de luz natural:** ¿La profundidad del espacio permite que la luz natural llegue al fondo? (regla: prof. máxima = 2× altura de ventana)
- [ ] **Iluminación artificial:** ¿Hay circuitos separados por zonas de uso? ¿Luces regulables en espacios sociales?

---

## 3. INDICADORES ACÚSTICOS
(Fuentes: NOM-081-SEMARNAT-1994 — Ruido en exteriores; ISO 140 / ISO 717 — Aislamiento acústico; Christopher Alexander, Pattern Language — patrón 155 "floor surface", 159 "light on two sides" como atenuación) 

### 3.1 Criterios

| Situación | Nivel sonoro máx. | Aislamiento mín. fachada | Aislamiento mín. entre espacios |
|-----------|-------------------|------------------------|-------------------------------|
| Recámaras (descanso) | 35 dB(A) nocturno | Rw ≥ 45 dB (vía ruidosa) / Rw ≥ 35 dB (vía tranquila) | Rw ≥ 40 dB entre recámaras |
| Sala / Social | 45 dB(A) | Rw ≥ 40 dB | Rw ≥ 35 dB |
| Cocina / Operativa | 50 dB(A) | Rw ≥ 35 dB | Rw ≥ 30 dB |
| Baño | 45 dB(A) | Rw ≥ 35 dB | Rw ≥ 30 dB |

### 3.2 Checklist
- [ ] **Separación de zonas ruidosas y silenciosas:** Cocina y cuarto de máquinas NO contiguos a recámaras? (verificar zonificación SOMA)
- [ ] **Muros entre recámaras:** ¿Tienen aislamiento acústico? (block macizo + cámara de aire + tablaroca sobre perfilería)
- [ ] **Instalaciones ruidosas:** ¿El calentador, bomba de agua y minisplit están alejados de recámaras o con envolvente acústica?
- [ ] **Pisos:** ¿Hay cambio de material en zonas de alto tránsito? (reducir ruido de impacto)
- [ ] **Fachada:** Si el predio está en avenida, ¿la fachada tiene doble acristalamiento o muro macizo?

---

## 4. INDICADORES DEL PROGRAMA
(Fuente: 01_PROTOCOLO_ANALISIS.md — verificación de programa; 02_PROTOCOLO_MODELADO.md — checklist de áreas)

### 4.1 Checklist
- [ ] **Área total construida:** ¿No excede el CUS del predio? (verificar contra normativa municipal)
- [ ] **Área por espacio:** ¿Cada espacio cumple el área mínima funcional? (recámara ≥ 12m², baño ≥ 3m², sala-comedor ≥ 25m²)
- [ ] **Dimensiones mínimas:** Ancho de circulaciones ≥ 0.90m, puertas ≥ 0.80m, altura libre ≥ 2.60m (2.40m baños)
- [ ] **Relaciones espaciales:** ¿Las conexiones del Diagrama Espacial SOMA se reflejan en la planta? (los espacios con relación directa deben ser contiguos)
- [ ] **Accesibilidad:** ¿Hay acceso sin escalón a nivel de calle? ¿Rampas donde hay desniveles? ¿Baño accesible en planta baja?

---

## 5. INDICADORES PROXÉMICOS
(Fuentes: Edward T. Hall, The Hidden Dimension (1966) — teoría proxémica, distancias interpersonales; Christopher Alexander, A Pattern Language — patrones 127 "intimacy gradient", 129 "common areas at the heart")

### 5.1 Distancias interpersonales por contexto (Hall, 1966)

| Relación | Distancia | Se aplica en |
|----------|-----------|-------------|
| Íntima | 0–0.45 m | Recámara, baño, espacios personales |
| Personal | 0.45–1.20 m | Sala, comedor, cocina (familia cercana) |
| Social | 1.20–3.60 m | Sala (visitas), comedor formal, estudio |
| Pública | 3.60m+ | Acceso, recibidor, espacios públicos |

### 5.2 Checklist
- [ ] **Gradiente de intimidad (Alexander, patrón 127):** ¿La secuencia acceso → social → descanso es progresiva en privacidad? (verificar contra recorrido principal)
- [ ] **Dimensiones de espacios sociales:** Sala-comedor: ¿la distancia entre asientos permite conversación social (1.20–2.50m)? No debe ser tan grande que se pierda la intimidad.
- [ ] **Recámaras:** ¿La cama tiene distancia personal (>0.45m) a cada muro?
- [ ] **Baño:** ¿Los elementos (wc, lavabo, regadera) respetan distancia íntima (>0.30m entre sí)?
- [ ] **Cocina:** ¿El triángulo de trabajo (estufa-fregadero-refrigerador) tiene distancias entre 1.20–2.70m? (Alexander, patrón 139)

---

## 6. INDICADORES NORMATIVOS
(Fuentes: Reglamento de Construcción del Municipio de Mérida; NOM-001-SEDE — Instalaciones eléctricas; Normativa de protección civil; COS/CUS del plan director)

### 6.1 Checklist por municipio (Mérida como base)
- [ ] **COS (Coeficiente de Ocupación del Suelo):** No excedido. Verificar contra escrituras.
- [ ] **CUS (Coeficiente de Utilización del Suelo):** No excedido. Verificar contra escrituras.
- [ ] **Altura máxima:** No excedida. (generalmente 8–10m en zonas residenciales)
- [ ] **Restricciones frontales:** Respetadas (generalmente 3–5m de retiro frontal)
- [ ] **Restricciones laterales y posteriores:** Respetadas
- [ ] **Cajones de estacionamiento:** Número mínimo según uso (1 cajón cada 50m² construidos en vivienda)
- [ ] **Rampas de acceso:** Pendiente máxima 12% (interior) o 8% (exterior) para accesibilidad
- [ ] **Área verde / jardín:** Porcentaje mínimo de terreno permeable según reglamento
- [ ] **Normativa de gas:** Ubicación del calentador a ≥ 1.5m de ventanas y colindancias
- [ ] **Protección civil:** Extintor visible y accesible en cocina, ruta de evacuación marcada

---

## 7. TABLA DE RESULTADOS

| Indicador | Estado | Ajuste requerido |
|-----------|--------|------------------|
| Confort térmico (PMV) | ✅ / ⚠️ / ❌ | _ |
| Protección solar vanos E/O | ✅ / ⚠️ / ❌ | _ |
| Ventilación cruzada | ✅ / ⚠️ / ❌ | _ |
| Iluminación natural (% V/P) | ✅ / ⚠️ / ❌ | _ |
| Iluminación artificial | ✅ / ⚠️ / ❌ | _ |
| Aislamiento acústico fachada | ✅ / ⚠️ / ❌ | _ |
| Separación zonas ruidosas | ✅ / ⚠️ / ❌ | _ |
| Programa (áreas vs normativa) | ✅ / ⚠️ / ❌ | _ |
| Accesibilidad | ✅ / ⚠️ / ❌ | _ |
| Gradiente de intimidad (proxémica) | ✅ / ⚠️ / ❌ | _ |
| Dimensiones proxémicas | ✅ / ⚠️ / ❌ | _ |
| COS / CUS / Altura máx. | ✅ / ⚠️ / ❌ | _ |
| Estacionamiento | ✅ / ⚠️ / ❌ | _ |
| Normativa de gas / eléctrica | ✅ / ⚠️ / ❌ | _ |

**Leyenda:**
- ✅ = Cumple (no requiere ajuste)
- ⚠️ = Requiere ajuste menor (documentar cambio)
- ❌ = No cumple (requiere rediseño parcial)

---

## 8. PROCESO DE EVALUACIÓN

1. **Evaluación inicial** (arquitecto, 1 día): llenar tabla completa contra modelo y planos
2. **Documentación de hallazgos** (arquitecto, 0.5 día): para cada ⚠️/❌, escribir:
   - ¿Cuál es el problema?
   - ¿Qué ajuste se propone?
   - ¿Impacta en otras áreas del diseño?
3. **Ajustes** (arquitecto, 0.5–1 día): implementar correcciones en el modelo
4. **Re-evaluación** (arquitecto, 0.5 día): verificar que los ajustes resolvieron los ⚠️/❌
5. **Firma de liberación:** el protocolo se archiva con el proyecto

---

## 9. SALIDA DE LA EVALUACIÓN

1. **Tabla de indicadores** completada y firmada, archivada en `proyectos/SOMA-XXXX/evaluacion/`
2. **Modelo 3D corregido** con los ajustes implementados
3. **Notas de diseño** documentando cada corrección

Esta evaluación es el requisito para liberar el **Anteproyecto** (Etapa 9) y detonar el segundo pago (40%).

---

## FUENTES

- **Francis D.K. Ching**, *Building Construction Illustrated* (6th ed., 2020) — composición de cerramientos, criterios de confort, dimensiones mínimas normativas.
- **Francis D.K. Ching**, *Architecture: Form, Space, & Order* (4th ed., 2014) — proporciones espaciales, jerarquía de espacios, relación luz-forma.
- **C. M. Deasy**, *Design Places for People* (1974) — evaluación de cómo los espacios funcionan para el comportamiento humano, criterios de éxito habitacional.
- **Jacques Paul Grillo**, *Form, Function and Design* (1960) — verificación de que la forma cumple su función, método de auditoría funcional.
- **Edward T. Hall**, *The Hidden Dimension* (1966) — teoría proxémica: distancias interpersonales y su aplicación al diseño de espacios. (edwardthall.com)
- **Christopher Alexander**, *A Pattern Language* (1977) — patrones 127 (intimacy gradient), 129 (common areas), 135 (light on two sides), 155 (floor surface), 161 (sunny place). (patternlanguage.com)
- **ISO 7730:2005 / ISO 7730:2025** — PMV/PPD para confort térmico. (iso.org/standard/39155.html)
- **ASHRAE Standard 55-2023** — Thermal Environmental Conditions for Human Occupancy. (ashrae.org)
- **NOM-020-ENER-2011** — Eficiencia energética en edificaciones, México.
- **NOM-025-STPS-2008** — Iluminación en centros de trabajo.
- **NOM-081-SEMARNAT-1994** — Ruido en exteriores.
- **Reglamento de Construcción del Municipio de Mérida** — COS, CUS, alturas, estacionamiento, restricciones.
- **Ernst Neufert**, *Arte de Proyectar en Arquitectura* (17ª ed. española, 2014 / original alemán 1936) — estándares dimensionales universales, verificación de espacios habitables.
- **Julius Panero & Martin Zelnik**, *Human Dimension & Interior Space: A Source Book of Design Reference Standards* (1979) — antropometría detallada por actividad, verificación de mobiliario y circulaciones.
- **Charles J. Holahan**, *Psicología Ambiental: Un Enfoque General* (1982) — evaluación psicoambiental del espacio, confort perceptual, bienestar psicológico.
- **NMX-R-001-SCFI-2015** — Dibujo técnico, nomenclatura oficial de planos.
- **NOM-001-SEDE** — Instalaciones Eléctricas.

---

*"Un proyecto no está terminado hasta que pasa su propia auditoría."*
