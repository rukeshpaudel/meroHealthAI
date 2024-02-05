import openai
from openai import OpenAI
import gradio as gr

client = OpenAI(
        api_key = "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"  # Set your API key securely
        )
class SpecializedDoctor:
    def __init__(self, specialty):
        self.specialty = specialty
        self.load_prompts()

    def load_prompts(self):
        try:
            with open(f"utils/prompts.txt", "r") as f:
                self.prompts = f.read().splitlines()
        except FileNotFoundError:
            print(f"Error: Prompts file for '{self.specialty}' not found.")
            self.prompts = []

    def provide_medical_advice(self, patient_query):
        prompt = f"{self.specialty}: {patient_query}\n{self.prompts[0]}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.4,
        )
        return response.choices[0].message.content.strip()

def chat_response(message, history):
    # Assuming you have only one doctor instance:
    doctor = SpecializedDoctor("Cardiology")  # Change here if you have more
    doctor_response = doctor.provide_medical_advice(message)

    # Update history and return
    history = [{"role": "user", "content": ""}]  # Start with an empty user message
    if isinstance(history, dict):
        history = [history]
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": doctor_response})
    return "", history

# Create the Gradio interface
iface = gr.ChatInterface(
    chat_response, title="Cardiologist Assistant", theme="dark"
)

# Launch the interface
iface.launch()
