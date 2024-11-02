import gradio as gr
from transformers import pipeline

# Lade das Chatbot-Modell
bot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

# Funktion für die Bot-Antwort
def respond(user_input):
    response = bot(user_input, max_length=50, num_return_sequences=1)
    return response[0]["generated_text"]

# Gradio Interface
interface = gr.Interface(
    fn=respond,
    inputs="text",
    outputs="text",
    title="Interaktiver Lehrplanungs-Bot",
    description="Stelle Fragen zur Lehrplanung, und der Bot gibt dir hilfreiche Antworten."
)

# Interface starten
interface.launch()
