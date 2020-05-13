import aiml
import os

kernel = aiml.Kernel()
# kernel.learn("std-startup.xml")
# kernel.respond("load aiml b")

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

# kernel now ready for use

print("Bot : Hello Sir welcome to our eggshop")
print("Bot : How may I help you.(I want /I would like to buy some eggs /you cant help me )")

while True:
    message = raw_input("Enter your message >>> ")
    temp = kernel.respond(message)
    if message == "quit":
        exit()
    elif message == "save":
        kernel.saveBrain("bot_brain.brn")
    elif message == "bye":
        bot_response = kernel.respond(message)
        print(bot_response)
        exit()
    elif message == "you cant help me":
        bot_response = kernel.respond(message)
        print(bot_response)
        exit()
    elif temp == "Bot: Fuck Off :)":
        bot_response = kernel.respond(message)
        print(bot_response)
        exit()
    elif message == "here you go":
        bot_response = kernel.respond(message)
        print(bot_response)
        kernel.saveBrain("bot_brain.brn")
        exit()
    elif temp == "process":
        bot_response = kernel.respond("process")
        a = int(bot_response)
        price = a*7
        bot_response = kernel.respond("Calculated price " + str(price))
        print(bot_response)
    else:
        bot_response = kernel.respond(message)
        # Do something with bot_response
        print(bot_response)