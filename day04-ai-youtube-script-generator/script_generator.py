from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def generate_script(topic):
    prompt = f"""
    Create a Youtube script from the topic: {topic}
    
    Structure the script like this:

    Hook (attention grabbing)
    Intro
    3 Main Talking Points
    Call to Action

    Keep it engaging and conversational.
    """
    response = client.responses.create(
        model="gpt-5.4",
        input=prompt
    )

    return response.output_text

topic = input("Enter Youtube video topic: ")

script = generate_script(topic)

print("\n Generated Script\n")
print(script)