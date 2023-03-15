import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thank you.", "I'm good, thanks for asking.", "I'm fine, thanks."],
    "what's up": ["Not much, how about you?", "Just chatting with you.", "Nothing much, what's up with you?"],
    "bye": ["Goodbye!", "See you later!", "Have a nice day!"]
}

def chat_bot():
    print("Hello, I'm a chatbot. What can I help you with today?")

    # loop to handle user input and generate bot response
    while True:
        user_input = input("> ")
        user_input = user_input.lower()

        if user_input in responses:
            bot_response = random.choice(responses[user_input])
            print(bot_response)
        else:
            print("I'm sorry, I didn't understand what you said. Could you please rephrase your question or statement?")

        # check if user wants to exit the chat
        if user_input == "bye":
            break

chat_bot()
