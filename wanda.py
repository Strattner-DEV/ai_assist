import pyjokes
from ai import AI

wanda = AI()

def joke():
    funny = pyjokes.get_joke()
    print(funny)
    wanda.say(funny)

def master():
    sentence = "The great master Bruno!"
    print(sentence)
    wanda.say(sentence)

command = ""
while True and command != "goodbye":
    command = wanda.listen()
    print("Command was:", command)

    if command == "tell me a joke":
        joke()
    if command == "who is your master?"
        master()

wanda.say("Goodbye, I'm going to sleep now")
