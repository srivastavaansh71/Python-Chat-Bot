import datetime
import time

name= input("Welcome Sir, enter your name : ")
presentHour= datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good Morning, ", name)
elif 11 <= presentHour <= 17:
    print("Good Afternoon, ", name)
elif 17 <= presentHour <=20:
    print("Good Evening, ", name)
else:
    print("Good night, ", name)


print("Hello sir! This is SPIDEY")
print("you can ask me questions, Type 'bye' to exit ")

# memory
responses = {
    "hello": "Hi welcome. What's up?",
    "how are you": "I am fine. Thanks for asking",
    "who are you": " I am smart Chatbot ",
    "motivate me": "Remember buddy. Rejction makes a man stronger. I belive you can not call yourself real man unless you can laugh off all the stuff that happened to you ",
    "happy": "Great to hear that",
    "good to see you": "same here friend"
}
# functions

def getResponseOfBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "Sorry I dont Know. But will try to look for it"    

while True:
    userInput= input("Please ask your question:")
    reply= getResponseOfBot(userInput)
    print("Bot Response : ", reply)

    if "bye" in userInput.lower():
        break
