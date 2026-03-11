from openai import OpenAI

client = OpenAI()

def ask_ai(question):
    response = client.responses.create(
        model="gpt-5.4",
        input=question
    )

    return response.output_text

print("AI chat started (type 'exit' to quit, 'help' for help)\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    if user_input.lower() == "help":
        print("You can ask me anything about AI, coding, or business.\nType 'exit' to quit.")

    answer = ask_ai(user_input)

    print(f"\nAI: {answer}\n")