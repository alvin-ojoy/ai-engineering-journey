from openai import OpenAI

client = OpenAI()

def summarizer_text(text):
    response = client.responses.create(
        model="gpt-5.4",
        input=f"Summarize this text in 3 bullet points:\n\n{text}" 
    )
    return response.output_text

user_text = input("Paste text to summarize: ")
summary = summarizer_text(user_text)

print("\nAI Summary:\n")
print(summary)