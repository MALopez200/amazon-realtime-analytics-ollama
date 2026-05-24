# 📦 Real-Time E-Commerce Analytics Engine with Local AI

This project simulates a live e-commerce production environment (Amazon style) that generates transactions in real time, stores them efficiently in a local relational database, and utilizes a local Large Language Model (LLM) to interpret data and instantly generate business executive reports.

## 🚀 System Architecture

The system consists of two parallel asynchronous components:
1. **Data Factory (`amazon_clon.py`):** A Python script that simulates non-stop second-by-second user transactions (generating products, prices, US states, and ratings) and injects them into an optimized SQLite database.
2. **Analytics & AI Engine (`analisis_en_vivo.py`):** A script that runs advanced unified SQL aggregate queries (calculating real-time revenue, transaction volume, and ticket averages) to feed **Llama 3.2** locally via **Ollama**, delivering strategic insights without internet dependency.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Database:** SQLite (Relational, optimized local storage)
* **Artificial Intelligence:** Ollama + Llama 3.2 (3B) executed locally
* **Automation:** Native Python Subprocess (direct OS terminal interaction)

## 💡 Key Insights & Data Optimization
* **Storage Efficiency:** The pipeline handles around 3,600 sales per hour. Thanks to SQLite binary storage optimization, an 8-hour continuous run consumes only ~1.8 MB of disk space, demonstrating massive efficiency compared to standard formats like Excel.
* **LLM Hallucination Mitigation:** LLMs are notoriously unreliable with arithmetic. To bulletproof the system, all mathematical processing (`SUM`, `COUNT`, and average division) is performed directly within the SQLite engine. The AI only receives fully computed KPIs, ensuring 100% accurate business analysis.
