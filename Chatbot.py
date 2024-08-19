def chatbot_respose(user_input):
      user_input = user_input.lower()

      if "hello" in user_input or "hi" in user_input:
            return "Hello Sir, How can i assist you today sir"
      elif "who" in user_input:
            return "I am a chatbot, I am here to assist you with any questions or tasks"
      elif "how" in user_input:
            return "I am chatbot made using python."
      elif "weather" in user_input:
            return "sorry sir, i couldn't the given request for you sir."
      elif "goodbye" in  user_input or "bye" in user_input:
            return "It was nice chatting with you, have a great day sir"
      else:
            return "sir could please re-type sir"
#if this possibility is true
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        break
    response = chatbot_respose(user_input)
    print("Chatbot :",response)
     
     
