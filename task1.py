# Function to process user input and provide a response
def chatbot_response(user_input):
    user_input = user_input.lower()  # Make input case-insensitive
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm functioning as expected! How about you?"
    elif "your name" in user_input:
        return "I'm your friendly rule-based chatbot. What can I help you with?"
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime('%H:%M:%S')
        return f"The current time is {current_time}."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Start a conversation loop
print("Chatbot: Hello! You can start chatting with me.")
while True:
    user_input = input("You: ")
    
    # Exit if the user says 'bye'
    if "bye" in user_input.lower():
        print("Chatbot: Goodbye! Have a great day!")
        break
    
    # Get chatbot response
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
