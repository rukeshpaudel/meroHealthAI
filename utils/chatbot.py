from  openai import OpenAI
import gradio as gr
import os

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def chat_response(prompt, history=[]):
    """
    Provides a chatbot response based on the given prompt and history.

    Args:
        prompt (str): The user's input prompt.
        history (list, optional): List of previous interactions (user and assistant messages). Defaults to [].

    Returns:
        str: The assistant's response.
    """

    # Update history with the user's prompt
    history.append({"role": "user", "content": prompt})

    # Generate response using OpenAI's chat completion API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=None,
        n=1
    )
    assistant_response = response.choices[0].message.content

    # Update history with the assistant's response
    history.append({"role": "assistant", "content": assistant_response})

    return assistant_response, history

# Create the Gradio interface
interface = gr.Interface(
    fn=chat_response,
    inputs=gr.Textbox(lines=3, label="Enter your prompt:"),
    outputs="text",
    title="OpenAI Chatbot: Ask Me Anything!",
    #theme="dark",
    #use_legacy_return=True,  # Ensure all outputs are returned to Gradio
)

# Launch the interface
interface.launch()
