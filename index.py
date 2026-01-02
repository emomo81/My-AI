# pip install openai
import openai

from openai import OpenAI
#h
# 1. Setup the client
# Replace 'YOUR_API_KEY_HERE' with the key you copied in Step 1 I
client = OpenAI(api_key="YOUR_API_KEY_HERE")

# 2. Create the conversation history.
# This "system" message tells the bot how to behave.
messages = [
    {"role": "system", "content": "You are a sarcastic, funny, and helpful assistant."}
]

print("Bot is ready! Type 'quit' to exit.")

while True:
    # 3. Get user input
    user_input = input("You: ")
    
    # Check if user wants to quit
    if user_input.lower() == "quit":
        break

    # 4. Add user message to history
    messages.append({"role": "user", "content": user_input})

    # 5. Send the conversation to OpenAI
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", # You can use "gpt-3.5-turbo" or "gpt-4o"
            messages=messages
        )

        # 6. Get the AI's reply
        bot_reply = response.choices[0].message.content
        print(f"Bot: {bot_reply}")

        # 7. Add bot reply to history (so it remembers context)
        messages.append({"role": "assistant", "content": bot_reply})

    except Exception as e:
        print(f"An error occurred: {e}")
