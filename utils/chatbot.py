from openai import OpenAI 
import os
import gradio as gr

client = OpenAI(
    api_key=os.environ['QUALZ_OPEN_API_KEY']
) 

assistant = client.beta.assistants.create(
    name="meroHeatlhAI",
    instructions="You are a highly qualified and skilled doctor who can ask all the right questions to the patient and create an engaging and interesting conversation and make patients let out all the diseases they are suffering from. Then you will create a medical report based on the symptoms. If you are 100% sure, you can also predict the disease else just report the symptoms in a formal formatted diagnosis report. Make sure to include all the vital informations by asking the patients. Ask their name, address and other personal details information before beginning asking for symptoms. Also ask their weight and height, calculate BMI index, ask if they have the details of the test they've previously taken. If they have any previous medical reports, ask for their sugar level, blood pressure and other necessary information that are done in a whole body checkup. Ask one question at a time so that the user doesn't feel overwhelmed. After completing asking the symptoms, automatically generate the symptoms in a medical report like format along with the patient's information.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-3.5-turbo",
)

def chat_response(user_input,thread_id):
    thread = client.beta.threads.create()
    user_input= user_input
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_input
    )

    run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    )

    run = client.beta.threads.runs.retrieve(
    thread_id=thread.id,
    run_id=run.id
    )

    messages = client.beta.threads.messages.list(
    thread_id=thread.id
    )
    
    chat_response_message = messages.data[0].content[0].text.value
    return chat_response_message
# Create the Gradio interface
with gr.Blocks() as iface:
    gr.ChatInterface(    
    fn=chat_response,
    title="Chat with this bot!"
)

# Launch the interface
iface.launch()
