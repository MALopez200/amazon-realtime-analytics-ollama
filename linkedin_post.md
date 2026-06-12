# LinkedIn Post — Amazon Real-Time Analytics + Local AI

---

## 🇬🇧 English

🚀 **I built a real-time analytics engine with 100% local AI — no GPU, no cloud, zero cost.**

🧪 **The latest challenge:** Can a 3B local model suggest smart pricing strategies better than gut feeling?

I built an AI **Pricing Agent** that:
📊 Queries the database — grabs top 10 products by sales volume + average price
🤖 Feeds the raw numbers to Llama 3.2 locally (no data leaves my laptop)
💡 Gets back: "Raise this one 12%, discount that one 25% — here's why"

Then I added **automated email alerts** — when the system detects anomalies or completes an analysis cycle, it sends a summary straight to my inbox. No dashboards to refresh, no logs to check.

The architecture is dead simple:
• **Simulator** → Python + SQLite (3,600 tx/hour)
• **Local AI** → Llama 3.2 via Ollama (zero API cost)
• **Cloud auditor** → DeepSeek checks for hallucinations
• **Alerts** → SMTP email on every key event

Tech stack: #Python #Ollama #Llama3 #SQLite #LocalAI #DataEngineering #Analytics

Have you tried running AI agents locally for data analysis? 👇

---

## 🇪🇸 Español

🚀 **Construí un motor de analytics en tiempo real con IA 100% local — sin GPU, sin cloud, sin gastar un dólar.**

🧪 **El último reto:** ¿Puede un modelo local de 3B sugerir estrategias de pricing mejores que el instinto?

Construí un **Agente de Pricing** con IA que:
📊 Consulta la base de datos — top 10 productos por volumen de ventas + precio promedio
🤖 Alimenta los números crudos a Llama 3.2 local (sin que los datos salgan de mi laptop)
💡 Devuelve: "Sube este 12%, descuenta este 25% — aquí está el por qué"

Después añadí **alertas automáticas por correo** — cuando el sistema detecta anomalías o completa un ciclo de análisis, envía un resumen directo a mi bandeja de entrada. Sin necesidad de mirar dashboards ni revisar logs.

La arquitectura es muy simple:
• **Simulador** → Python + SQLite (3,600 tx/hora)
• **IA local** → Llama 3.2 vía Ollama (costo CERO en API)
• **Auditor cloud** → DeepSeek verifica que no haya alucinaciones
• **Alertas** → Correo SMTP en cada evento clave

Tech stack: #Python #Ollama #Llama3 #SQLite #LocalAI #DataEngineering #Analytics

¿Has probado ejecutar agentes de IA local para análisis de datos? 👇
