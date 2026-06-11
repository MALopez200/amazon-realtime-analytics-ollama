import ollama
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# ──────────────────────────────────────────────
# Cliente compartido (se crea UNA SOLA VEZ)
# ──────────────────────────────────────────────
_cliente_deepseek = OpenAI(
    api_key=os.getenv('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com"
)

def consultar_local(prompt):

    respuesta = ollama.chat(
    model= 'llama3.2:latest', 
    messages=[
        {'role':'user','content':prompt}
    ])

    return respuesta['message']['content']

def auditar_respuesta(respuesta_local, datos_reales, prompt_contexto,):

    prompt = (
        f"Actúas como un auditor de datos. "
        f"Contexto: {prompt_contexto}.\n"
        f"Datos reales de la base: {datos_reales}.\n"
        f"Respuesta generada por IA local: {respuesta_local}.\n"
        f"Tarea: Verifica si la respuesta coincide con los datos reales. "
        f"Si hay errores, señálalos. Si es correcta, indícalo."
    )    

    respuesta = _cliente_deepseek.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": prompt}
    ])

    return (respuesta.choices[0].message.content)

