import os
from openai import OpenAI

#  API key s
client = OpenAI(api_key="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")  # ← Replace with your actual key

print("🟢 Ticum Chatbot is running!")
print("Type 'exit' to quit.\n")


chat_history = [
    {"role": "system", "content": "You are a friendly chatbot named Ticum."}
]

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break

    chat_history.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if your key supports it
            messages=chat_history
        )
        reply = response.choices[0].message.content
        print(f"Bot: {reply}")
        chat_history.append({"role": "assistant", "content": reply})

    except Exception as e:
        print("⚠️ Error:", e)
