# 📋 Tareas — Amazon Real-Time Analytics + IA Local

> Proyecto multi-agente con IA local. Cada tarea = 1 rama de Git.
> Se hace commit antes de pasar a la siguiente (regla #19).

---

## ✅ Completadas

- [x] Auto-refresh del dashboard
- [x] Alertas por correo SMTP
- [x] Agente de pricing con IA local

---

## 🚀 Próximas tareas (en orden sugerido)

### 1️⃣ Resumen Ejecutivo — `feature/resumen-ia`

Un agente `resumen.py` que cada vez que lo corres:
1. Saca 5 métricas de la BD: total ventas, producto top, ingresos totales, % de devoluciones, categoría líder
2. Le pasa todo a la IA local para que escriba un **resumen ejecutivo de 1 párrafo**
3. Lo imprime bonito en terminal

**Qué aprenderás:**
- Pasar múltiples datos estructurados a la IA en un solo prompt
- La IA como analista de negocio (no solo contestadora)
- Dar contexto completo para que la IA razone mejor

---

### 2️⃣ Analizador de Horas Pico — `feature/picos-ia`

Un agente `picos.py` que:
1. Agrupa ventas por hora del día con `strftime('%H', TIMESTAMP)`
2. Pregunta a la IA: *"estas son las ventas por hora, ¿cuáles son las horas pico y qué recomiendas?"*
3. La IA sugiere estrategia de personal, inventario o marketing

**Qué aprenderás:**
- SQL con formato de fechas (`strftime`)
- La IA reconociendo patrones en números
- Prompt engineering para recomendaciones accionables

---

### 3️⃣ Diagnóstico de Devoluciones — `feature/devoluciones-ia`

Un agente `devoluciones.py` que:
1. Busca los 5 productos con más devoluciones
2. Pregunta a la IA: *"¿por qué crees que estos productos se devuelven más?"*
3. La IA diagnostica causas probables y sugiere soluciones

**Qué aprenderás:**
- Consultas SQL con filtros (`WHERE RETURN_STATUS = 'Devuelto'`)
- La IA haciendo análisis de causa raíz
- Prompt de "diagnóstico" vs prompt de "resumen"

---

### 4️⃣ Recomendador de Inventario — `feature/recomendar-ia`

Un agente `recomendar.py` que:
1. Compara top 5 más vendidos vs top 5 menos vendidos
2. La IA recomienda qué mantener en stock y qué descontinuar
3. Imprime la recomendación con nivel de confianza

**Qué aprenderás:**
- Consultas SQL con `ORDER BY ASC` y `DESC` en el mismo script
- La IA como consejera de inventario
- Comparar extremos opuestos en un mismo análisis

---

### 5️⃣ Descubridor de Insights — `feature/insights-ia`

Un agente `insights.py` que:
1. Cada vez que lo corres, agarra 3 métricas aleatorias (de una lista)
2. La IA devuelve un "dato curioso" o insight inesperado
3. Imprime: 💡 *"¿Sabías que...?"*

**Qué aprenderás:**
- Aleatoriedad controlada con `random.choice()`
- La IA descubriendo cosas no obvias en datos simples
- Hacer que un programa siempre sorprenda

---

## 🏭 Mini Proyecto: Sistema de Inventario

> Después de las 5 tareas pequeñas, este mini-proyecto agrega el ciclo completo:
> **Compras → Inventario → Ventas → Alertas de stock**

### 6️⃣ Tabla de Inventario — `feature/inventario-tabla`

Crear la tabla `inventario` en SQLite con:
| Columna | Qué guarda |
|---|---|
| `PRODUCT_NAME` | Nombre del producto |
| `CATEGORY` / `SUB_CATEGORY` | Clasificación |
| `CANTIDAD_RECIBIDA` | Unidades que entraron |
| `CANTIDAD_ACTUAL` | Unidades que quedan |
| `COSTO_UNITARIO` | Lo que costó comprarlo |
| `PROVEEDOR` | Quién lo trajo |
| `FECHA_INGRESO` | Cuándo llegó |

Se agrega dentro de `database.py` junto a la tabla `ventas`.

**Qué aprenderás:**
- Que una BD puede tener múltiples tablas relacionadas
- Diseñar una tabla desde cero pensando en cómo se usará

---

### 7️⃣ Simulador de Compras — `feature/compras-simulador`

Un agente `compras.py` que cada cierto tiempo:
1. Escoge productos aleatorios del catálogo
2. Decide cantidades (20-100 unidades)
3. Asigna costo (precio_venta × 0.6)
4. Los mete a la tabla `inventario`
5. Imprime: 🚚 *"Llegaron 50 iPads a la bodega"*

**Qué aprenderás:**
- Poblar una segunda tabla con datos realistas
- Coordinar dos simuladores (compras + ventas)
- Pensar en costos, no solo en precios

---

### 8️⃣ Descontar Stock al Vender — `feature/ventas-con-stock`

Modificar `amazon_clon.py` para que:
1. Antes de insertar una venta, verifique stock en `inventario`
2. Si hay stock → descuenta 1 y vende normal
3. Si no hay stock → salta ese producto o elige otro
4. Avise en terminal: *"⚠️ Sin stock de X, eligiendo otro..."*

**Qué aprenderás:**
- Lógica condicional con estado real de la BD
- Hacer que dos tablas trabajen juntas
- Manejo de casos borde (falta de inventario)

---

### 9️⃣ Alertas de Stock Bajo — `feature/alertas-stock`

Un agente `stock_alerts.py` que:
1. Busca productos con `CANTIDAD_ACTUAL < 5`
2. Le pasa la lista a la IA local
3. La IA recomienda órden de reabastecimiento (urgencia)
4. Envía alerta por correo con las recomendaciones

**Qué aprenderás:**
- Umbrales dinámicos con IA (no solo if/else)
- Integrar inventario con el sistema de alertas que ya tienes
- La IA priorizando bajo presión (poco stock, muchos productos)

---

## 🔟 Bonus: Dashboard de Inventario — `feature/dashboard-inventario`

Agregar una pestaña en `dashboard.py` (o un segundo dashboard) que muestre:
- Productos con bajo stock (rojo)
- Nivel de inventario general (verde/amarillo/rojo)
- Últimas compras realizadas
- Consulta a la IA: *"¿Cómo está mi inventario?"*

**Qué aprenderás:**
- Múltiples vistas en Streamlit con `st.sidebar`
- Visualizar datos de inventario en tablas y colores
- La IA al servicio del monitoreo visual

---

## 📌 Notas

- Cada tarea empieza con `git checkout -b feature/<nombre>`
- Varios commits locales antes de un solo push (regla #25)
- Pistas primero, código solo si me atoro (regla #7)
- Las 5 tareas pequeñas primero, el inventario después
