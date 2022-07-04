import pyjokes
from ai import AI
from todo import Todo, Item
from weather import Weather
from randfacts import randfacts
from datetime import datetime

wanda = AI()
todo = Todo()

def facts():
    fact = randfacts.get_fact()
    print(fact)
    wanda.say(fact)

def joke():
    funny = pyjokes.get_joke()
    print(funny)
    wanda.say(funny)

def master():
    sentence = "The great master Bruno!"
    print(sentence)
    wanda.say(sentence)

def add_todo()->bool:
    item = Item()
    wanda.say("Tell me what to add to the list")

    item.title = ""
    try:
        item.title = wanda.listen()
        todo.new_item(item)
        message = "Added " + item.title
        wanda.say(message)
        return True
    except:
        print("oops there was an error")
        return False
    
def list_todos():
    if len(todo) > 0:
        wanda.say("Here are your to do's")
        for item in todo:
            wanda.say(item.title)
    else:
        wanda.say("The to do list is empty!")
    
def remove_todo()->bool:
    wanda.say("Tell me which item to remove")
    try:
        item_title = wanda.listen()
        todo.remove_item(title=item_title)
        message = "Removed " + item_title
        wanda.say(message)
        return True
    except:
        print("opps there was an error")
        return False

def weather():
    myweather = Weather()
    forecast = myweather.forecast
    print(forecast)
    wanda.say(forecast)

command = ""
wanda.say("hello")
while True and command not in ["turn off", "goodbye", "thank you"]:

    try:
        command = wanda.listen()
        command = command.lower()
    except:
        print("Oops there is a problem")
        command = ""
    
    print("Command was: ", command)

    if command in ["tell me a joke", "tell me another joke"]:
        joke()
        command = ""

    if command in ["who is your master", "who created you"]:
        master()
        command = ""

    if command in ["add to-do","add to do", "add item", "new item"]:
        add_todo()
        command = ""

    if command in ["list todos", "list todo", "list to do", "list to-do", "list to do's",'list items', "show to do", "show to-do", "show todo"]:
        list_todos()
        command = ""

    if command in ["remove todo", "remove item", "mark done", "remove todos", "remove to-do", "remove to do's"]:
        remove_todo()
        command = ""

    if command in ['what is the weather like', 'give me the forecast',"what's the weather"]:
        weather()
        command = ""

    if command in ['tell me a fact','tell me something', "tell me more"]:
        facts()
    
    if command in ['good morning','good evening','good night','good afternoon']:
        now = datetime.now()
        hr = now.hour
        message = ""
        if hr <= 0 <=12:
            message = "Morning"
        if hr >=12 <= 17:
            message = "Afternoon"
        if hr >=17 <=21:
            message = "Evening"
        if hr > 21: message = "Night"

        message = "Good " + message + " Bruno"
        wanda.say(message)

wanda.say("Goodbye, I'm going to sleep now")
