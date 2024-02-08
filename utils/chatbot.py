import gradio as gr

class Doctor():
    
    doctor_professions = {
        "neurologist": "Dr. Ram Hari",
        "psychiatrist": "Dr. Sita",
        "cardiologist": "Dr. Deals",
        "dermatologist": "Dr. Hari",
    }
    
    def display_profession(profession_key):
        # Handle invalid key (same as previous example)
        if profession_key not in Doctor.doctor_professions:
            return "Invalid profession. Please choose from available options."

        doctor_data = Doctor.doctor_professions[profession_key]
        # Build desired output format (adjust to your preference)
        output = f"\n**Doctor details:**\n - Name: {doctor_data}\n - Profession: {profession_key}"

        return output


with gr.Blocks() as block:
    profession_key = gr.Textbox(label="Profession", interactive=True)
    doc_info = gr.Textbox(label="Doctor Information")  # Define textbox globally

    gr.Button("display_profession").click(
        # Pass textbox element directly
        Doctor.display_profession, inputs=[profession_key], outputs=doc_info
    )

block.launch()
