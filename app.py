from utils.chatbot import Doctor
import time
import os
import gradio as gr

from openai import OpenAI

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

# Initialize the client
# Set your OpenAI API key

'''file = client.files.create(
    file=open("songs.txt", "rb"),
    purpose='assistants'
)'''

# Step 1: Create an Assistant
assistant = client.beta.assistants.create(
    name="MeroHealthAI",
    instructions="You are a highly qualified and skilled doctor who can ask all the right questions to the patient and create an engaging and interesting conversation and make patients let out all the diseases they are suffering from. Then you will create a medical report based on the symptoms. If you are 100% sure, you can also predict the disease else just report the symptoms in a formal formatted diagnosis report. Make sure to include all the vital informations by asking the patients. Ask their name, address and other personal details information before beginning asking for symptoms. Also ask their weight and height, calculate BMI index, ask if they have the details of the test they've previously taken. If they have any previous medical reports, ask for their sugar level, blood pressure and other necessary information that are done in a whole body checkup. Ask one question at a time so that the user doesn't feel overwhelmed. After completing asking the symptoms, automatically generate the symptoms in a medical report like format along with the patient's information.",
    model="gpt-3.5-turbo",
  #  file_ids=[file.id],
    tools=[{"type": "retrieval"}]
)

# Step 2: Create a Thread
thread = client.beta.threads.create()

def main(query, history):
    # Step 3: Add a Message to a Thread
    history=history,
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=query
    )

    # Step 4: Run the Assistant
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
        instructions="The user is a humanitarian worker who is going through digital transformation"
    )

    while True:
        # Wait for 5 seconds
        time.sleep(0.5)

        # Retrieve the run status
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )

        # If run is completed, get messages
        if run_status.status == 'completed':
            messages = client.beta.threads.messages.list(
                thread_id=thread.id
            )
            response = ""
            
            data = messages.data
            first_thread_message = data[0]
            content = first_thread_message.content
            response = content[0].text.value
            return response
        else:
            continue

# Create a Gradio Interface

iface = gr.ChatInterface(main, title="SAFe Specialist",\
                          description="SAFe Specialist guiding transitions with realistic and \
                            optimistic advice towards a product centric approach",\
                                examples=["How can I shift from project to product mode?",\
                                          "What are the key SAFe principles for my organization?",\
                                            "Can you provide options for agile practices in my setting?",\
                                                "How do I deal with cultural resistance in SAFe adoption?", \
                                                    "What's your advice for an org with many different digital solutions?",\
                                                        "Could you walk me through the step-by-step process of moving into SAFe?"]).queue()



profession_key = gr.Textbox(label="Profession", interactive=True)
doc_info = gr.Textbox(label="Doctor Information")  # Define textbox globally

gr.Button("display_profession").click(
    # Pass textbox element directly
    Doctor.display_profession, inputs=[profession_key], outputs=doc_info
)


if __name__ == "__main__":
    iface.launch()
    
