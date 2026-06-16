# PROTOCOLO: EVALUACIÓN DE HABITABILIDAD
## Bloque 2 — Taller SOMA (Operación) | Sección 4 del PROCESO DE DISEÑO 2.0
## Referencia: Items 4.9 a 4.15

**Qué es:** Auditoría sistemática del proyecto contra indicadores de habitabilidad.
Control de calidad del taller SOMA.

**Entrada:** Modelo 3D + Planos de anteproyecto (de Etapas 5, 6, 7).

**Salida:** Tabla de indicadores evaluados ✅/⚠️/❌ con ajustes documentados.

---

## 4.9 Evaluación Ambiental I

```
[EVA] 4.9 Evaluación Ambiental I (P2.0 ref: 4.9)
─────────────────────────────────
INPUT:  4.8 Espacialidad (propuesta de diseño)
        3.1-3.2 Análisis del sitio
        3.9.3 Estrategias bioclimáticas
OPERA:  Evaluar diseño propuesto contra 8 criterios ambientales
        (4.9.1 a 4.9.8). Si algún criterio es ❌, se ejecuta 4.10
OUTPUT: Tabla de evaluación con 8 criterios + decisión de ajuste
PROC:   AI→HUMANO
```

### 4.9.1 Asoleamiento
- [ ] Radiación solar directa en vanos: vanos E/O con protección solar
- [ ] Verificar sombras arrojadas en fechas críticas (solsticios, equinoccios)
- [ ] Horas de sol por fachada: ¿las críticas tienen protección?

### 4.9.2 Ventilación
- [ ] Cada espacio habitable tiene dos muros opuestos con vanos
- [ ] Cruce de viento en espacios principales
- [ ] Obstrucciones al flujo de viento

### 4.9.3 Accesibilidad
- [ ] Anchos de circulación ≥ 0.90 m
- [ ] Pendientes de rampa ≤ 10%
- [ ] Puertas ≥ 0.80 m
- [ ] Espacios de giro en baños ≥ 1.50 m

### 4.9.4 Seguridad y Privacidad
- [ ] Gradiente público-privado (Alexander, patrón 127)
- [ ] Visuales desde calle y colindancias
- [ ] Iluminación nocturna de accesos

### 4.9.5 Comportamiento en Lluvia
- [ ] Pendientes de cubierta ≥ 2%
- [ ] Canalización pluvial
- [ ] Áreas de inundación potencial
- [ ] Pozos de absorción (1 c/350 m²)

### 4.9.6 Elementos Simbólicos
- [ ] Legibilidad y ubicación jerárquica
- [ ] No competencia entre elementos
- [ ] Funcionamiento a escala humana y urbana

### 4.9.7 Ergonomía y Proxémica

| Relación | Distancia (Hall, 1966) | Se aplica en |
|----------|----------------------|-------------|
| Íntima | 0-0.45 m | Recámara, baño |
| Personal | 0.45-1.20 m | Sala, comedor, cocina |
| Social | 1.20-3.60 m | Sala (visitas), comedor formal |
| Pública | 3.60 m+ | Acceso, recibidor |

- [ ] Gradiente de intimidad: acceso → social → descanso progresivo
- [ ] Distancias entre asientos en sala-comedor: 1.20-2.50 m
- [ ] Triángulo de trabajo cocina: 1.20-2.70 m

### 4.9.8 Eficiencia del Programa
- [ ] Área total ≤ CUS
- [ ] Área por espacio ≥ mínimos normativos
- [ ] Relación útil/construido: objetivo >80%
- [ ] Área de circulación: objetivo <12%

---

```
[ACC] 4.10 Ajustes Evaluación Ambiental I (P2.0 ref: 4.10)
─────────────────────────────────
INPUT:  4.9 Resultados (items ❌ y ⚠️)
OPERA:  Corregir items ❌ (obligatorio). Evaluar ⚠️ (opcional).
        Repetir hasta que todos sean ✅ o ⚠️
OUTPUT: Diseño ajustado (nueva iteración de 4.4-4.8)
PROC:   HUMANO (ajuste) → AI (re-evaluación)
```

---

## 4.11 Proceso Avanzado de Configuración (Integral+)

```
[ACC] 4.11 Proceso Avanzado (P2.0 ref: 4.11)
─────────────────────────────────
INPUT:  4.8 Espacialidad ajustada + 4.10 Ajustes
OPERA:  Configuración detallada de elementos específicos.
        Solo si el paquete lo requiere (Integral o Ejecutivo)
OUTPUT: Configuración detallada (6 sub-items 4.11.1 a 4.11.6)
PROC:   HUMANO
```

- [ ] **4.11.1 Diseño General de Baños** — mobiliario, circulaciones, ventilación
- [ ] **4.11.2 Diseño General de Cocina** — triángulo de trabajo, zonificación
- [ ] **4.11.3 Diseño General de Escalera** — huella/contrahuella, ancho, barandales
- [ ] **4.11.4 Diseño de Vanos** — dimensión, tipo, material de cada vano
- [ ] **4.11.5 Diseño de Fachadas** — composición, materialidad, protecciones
- [ ] **4.11.6 Diseño de Terrazas** — orientación, protección solar, vegetación

---

## 4.12 Criterio de Iluminación Artificial

```
[GUI] 4.12 Criterio Iluminación Artificial (P2.0 ref: 4.12)
─────────────────────────────────
INPUT:  4.8 Espacialidad + 4.9.1 Asoleamiento
        3.10.4 Perfil de diseño (eje iluminación)
OPERA:  Definir por espacio: tipo de iluminación, temperatura de
        color, altura de luminarias, controles, eficiencia
OUTPUT: Criterio de iluminación artificial por espacio
PROC:   HUMANO
```

| Espacio | Iluminancia | Temp. color | % ventana-piso |
|---------|------------|-------------|----------------|
| Sala | 200-300 lux | 3000-3500K | 15-25% |
| Recámara | 100-200 lux | 2700-3000K | 10-20% |
| Cocina | 300-500 lux | 4000K | 15-25% |
| Baño | 200-300 lux | 4000K | 5-10% |
| Circulación | 100-150 lux | 3000K | 5-10% |
| Estudio | 300-500 lux | 4000-5000K | 20-30% |

---

## 4.13 Criterio de Diseño de Paisaje

```
[GUI] 4.13 Criterio de Paisaje (P2.0 ref: 4.13)
─────────────────────────────────
INPUT:  4.4 Zonificación (áreas exteriores)
        2.2.2.1-2 Vegetación existente
        3.9.4 Integración urbana
OPERA:  Definir vegetación a conservar, especies propuestas (locales,
        bajo consumo de agua), zonificación del jardín, mobiliario
        exterior, riego e iluminación exterior
OUTPUT: Criterio de paisaje + propuesta de especies
PROC:   HUMANO
```

---

## 4.14 Evaluación Ambiental II (Cualitativa)

```
[EVA] 4.14 Evaluación Ambiental II (P2.0 ref: 4.14)
─────────────────────────────────
INPUT:  4.11 Configuración avanzada + 4.12-4.13 Criterios
        3.10.4 Perfil de diseño (datos cualitativos)
OPERA:  Segunda evaluación cualitativa centrada en la experiencia
        del usuario: 5 dimensiones humanas
OUTPUT: Evaluación cualitativa (4.14.1)
PROC:   HUMANO
```

### 4.14.1 Evaluación: Fisiológica, Psicológica, Funcional, Social, Cultural

| Dimensión | Criterio | ✅/⚠️/❌ |
|-----------|----------|---------|
| Fisiológica | Confort térmico, lumínico, acústico | |
| Psicológica | Seguridad, pertenencia, privacidad | |
| Funcional | Eficiencia recorridos, mantenimiento | |
| Social | Espacios de reunión, integración familiar | |
| Cultural | Pertinencia tipológica, materialidad local | |

---

```
[ACC] 4.15 Ajustes II Evaluación Ambiental (P2.0 ref: 4.15)
─────────────────────────────────
INPUT:  4.14 Resultados (items ❌ y ⚠️)
OPERA:  Corregir configuración avanzada. Repetir hasta que todos
        los criterios sean al menos ⚠️
OUTPUT: Diseño final ajustado → listo para Visualización (Sección 5)
PROC:   HUMANO
```

---

## Tabla de Resultados Final

| Indicador | Estado | Ajuste |
|-----------|--------|--------|
| Asoleamiento | ✅/⚠️/❌ | |
| Ventilación | ✅/⚠️/❌ | |
| Accesibilidad | ✅/⚠️/❌ | |
| Seguridad y privacidad | ✅/⚠️/❌ | |
| Lluvia | ✅/⚠️/❌ | |
| Elementos simbólicos | ✅/⚠️/❌ | |
| Ergonomía y proxémica | ✅/⚠️/❌ | |
| Eficiencia programa | ✅/⚠️/❌ | |
| Iluminación artificial | ✅/⚠️/❌ | |
| Paisaje | ✅/⚠️/❌ | |
| Cualitativa (5 dim.) | ✅/⚠️/❌ | |
| COS / CUS / Altura | ✅/⚠️/❌ | |

---

## Salida de la Evaluación

1. Tabla de indicadores completada y archivada en `proyectos/SOMA-XXXX/evaluacion/`
2. Modelo 3D corregido con ajustes implementados
3. Notas de diseño documentando cada corrección

---

## FUENTES

- ISO 7730:2005/2025 — PMV/PPD confort térmico.
- ASHRAE Standard 55-2023 — Thermal Environmental Conditions.
- NOM-020-ENER-2011 — Eficiencia energética.
- NOM-025-STPS-2008 — Iluminación.
- NOM-081-SEMARNAT-1994 — Ruido.
- Hall, E. T. (1966). *The Hidden Dimension.*
- Alexander, C. (1977). *A Pattern Language.*
- Neufert, E. *El Arte de Proyectar.*
- Panero, J. & Zelnik, M. (1979). *Human Dimension.*
- Holahan, C. (1982). *Psicología Ambiental.*
- Reglamento de Construcción del Municipio de Mérida.
