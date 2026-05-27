# LOG MAESTRO: PROYECTO SOMA
*Registro Evolutivo de Ingeniería, Metodología y Decisiones de Diseño*

---

## 1. TESIS FUNDAMENTAL
**"Lo protocolario se programa, lo creativo se libera."**
SOMA no es un taller de arquitectura tradicional, es un sistema de **Arquitectura como Producto (AaaP)** que utiliza la **Ingeniería del Habitar** para democratizar el diseño de alta calidad.

---

## 2. OBSERVACIONES CRÍTICAS Y SESGOS DETECTADOS
*Registro de fallos en la implementación y críticas del Arquitecto (Juan).*

| Fecha | Observación / Crítica | Estado |
| :--- | :--- | :--- |
| 11/05/26 | **Pérdida de Integridad:** El dashboard se convirtió en una herramienta cosmética, ignorando procesos profundos del Bloque 02 (UserEntity, ActivityMatrix). | ⚠️ En Corrección |
| 11/05/26 | **Complacencia del Agente:** El asistente AI estaba aceptando decisiones sin análisis crítico, convirtiéndose en un riesgo para la precisión del sistema. | ✅ Mitigado |
| 11/05/26 | **Desconexión de Datos:** El esquema actual de SQLite no soporta la complejidad de los protocolos 01 y 02. | ✅ Corregido |
| 12/05/26 | **Estructura Relacional:** Se implementaron tablas para Habitantes, Actividades y Ejes de Diseño. | ✅ Finalizado |
| 13/05/26 | **Infraestructura de Inmersión:** Backend actualizado con 10 ejes de diseño y matriz de 24 slots. | ✅ Finalizado |

---

## 3. ACUERDOS METODOLÓGICOS (PENDIENTES DE CODIFICAR)
*Definiciones que deben pasar de papel a código.*

### A. Ingeniería del Habitar (Bloque 02)
- **UserEntity:** Debe incluir atributos estáticos (ergonomía), dinámicos (hobbies) y roles de poder.
- **Inmersión Visual (10 Ejes Detectados):**
    1. Fachada (Abierta/Cerrada)
    2. Recámaras (Juntas/Separadas)
    3. Planta (Abierta/Fraccionada)
    4. Iluminación (Directa/Tenue)
    5. Tacto (Textura/Liso)
    6. Niveles (Un nivel/Varios)
    7. Paisaje (Verde/Pétreo)
    8. Escala (Acogedor/Amplio)
    9. Perfil Social (Activo/Privado)
    10. Color (Neutral/Carácter)
- **ActivityMatrix (24 Slots):** Cada proyecto debe generar una matriz de 24 slots por habitante para determinar necesidades de aislamiento e iluminación.
- **CreativeCore (5 Ejes de Tensión):** Tensión/Calma, Brutalismo/Refinamiento, Privacidad/Transparencia, Ortogonalidad/Organicismo, Permanencia/Efimeridad.

### B. Gestión Financiera (Bloque 01)
- **Niveles de Surgimiento:** Esencial, Integral, Complejo.
- **Costo Estándar:** $18,500/m² (Alineado con el Cotizador Web V5).
- **Sincronización:** El backend ahora desglosa la inversión total en la `matriz_inversion` automáticamente al recibir un lead de la web.

---

## 4. ACCIONES PRIORITARIAS (BACKLOG)
1. [x] **Reestructuración de DB:** Crear tablas para `Habitantes`, `Actividades` y `EjesDiseno`.
2. [ ] **Script de Extracción:** Refinar el procesador `extractor.py` con más keywords y lógica de NLP básica.
3. [ ] **Lógica de Costos:** Implementar la fórmula de presupuesto basada en la Matriz de Inversión.
4. [ ] **Dashboard:** Crear la vista para visualizar la Matriz de Actividades de 24 slots.

---

## 5. HISTORIAL DE DECISIONES
- **2026-05-11:** Se decide priorizar la estructura de datos sobre la interfaz visual. Se crea este LOG para evitar la pérdida de información valiosa de conversaciones anteriores.
- **2026-05-18:** Se configura envío de correo vía SMTP Gmail (contraseña de aplicación) y notificación WhatsApp vía Twilio Sandbox +14155238886. Se acuerda migrar a Telegram cuando termine el crédito gratuito de Twilio.
