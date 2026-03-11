from openai import OpenAI

client = OpenAI()

def summarize_text(text):
    response = client.responses.create(
        model="gpt-5.4",
        input=f"Explain this text like I'm 10 years old:\n\n{text}" 
    )
    return response.output_text

user_text = input("Paste text to explain like you're a 10 years old: ")
summary = summarize_text(user_text)

print("\nAI Summary:\n")
print(summary)