import pyjokes
from ai import AI

wanda = AI()

def joke():
    funny = pyjokes.get_joke()
    print(funny)
    wanda.say(funny)

command = ""
while True and command != "goodbye":
    command = wanda.listen()
    print("Command was:", command)

    if command == "tell me a joke":
        joke()

wanda.say("Goodbye, I'm going to sleep now")
