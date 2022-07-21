import pyjokes
from ai import AI
from todo import Todo, Item
from weather import Weather
from randfacts import randfacts
# from datetime import datetime
import requests
import random
from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()


headers["Authorization"] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NDIsInVzZXJuYW1lIjoidGVzdDQ0IiwicGFzc3dvcmQiOiIkMmIkMTIkeWJpSXhjRGltMW1FazZMQUd1bm1BTzZJTnFkaFdjWHRXV3lmLmM2UEtwMElvQ21JSXJEaXEiLCJib2FyZCI6eyJ0YXNrcyI6eyJ0YXNrLTExMSI6eyJpZCI6InRhc2stMTExIiwiY29udGVudCI6InNkZ3NkZyIsInByaW9yaXR5IjoyfX0sImNvbHVtbnMiOnsiY29sdW1uLTEiOnsiaWQiOiJjb2x1bW4tMSIsInRpdGxlIjoiVG8gZG8iLCJ0YXNrSWRzIjpbInRhc2stMTExIl19LCJjb2x1bW4tMiI6eyJpZCI6ImNvbHVtbi0yIiwidGl0bGUiOiJEb25lIiwidGFza0lkcyI6W119LCJjb2x1bW4tMyI6eyJpZCI6ImNvbHVtbi0zIiwidGl0bGUiOiJJbiBwcm9ncmVzcyIsInRhc2tJZHMiOltdfX0sImNvbHVtbk9yZGVyIjpbImNvbHVtbi0xIiwiY29sdW1uLTIiLCJjb2x1bW4tMyJdfX0.7FhMOTYFzbMPXwiio54wD4W-tXL9VPgo7WUQEba8LTk"
headers["Content-Type"] = "application/json"
headers["Content-Length"] = "0"

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

def task():
    id_number = random.randint(0, 99999999999)
    content = "Test Wanda"
    priority = 1
    try:    
        url = f"http://192.168.232.183:8000/add_task?id_number={id_number}&content={content}&priority={priority}"
        resp = requests.post(url, headers=headers)
        print(resp)
    except:
        print("opps there was an error")
        pass

def sede():
    id_number = random.randint(0, 99999999999)
    content = "Necessiade de Agua"
    priority = 0
    try:    
        url = f"http://192.168.232.183:8000/add_task?id_number={id_number}&content={content}&priority={priority}"
        resp = requests.post(url, headers=headers)
        print(resp)
        wanda.say("A Equipe foi informada!")
    except:
        print("opps there was an error")
        pass

def dor():
    id_number = random.randint(0, 99999999999)
    content = "Necessiade de Apoio"
    priority = 1
    try:    
        url = f"http://192.168.232.183:8000/add_task?id_number={id_number}&content={content}&priority={priority}"
        resp = requests.post(url, headers=headers)
        print(resp)
        wanda.say("A Equipe foi informada!")
    except:
        print("opps there was an error")
        pass

def fome():
    id_number = random.randint(0, 99999999999)
    content = "Necessiade de Comida"
    priority = 0
    try:    
        url = f"http://192.168.232.183:8000/add_task?id_number={id_number}&content={content}&priority={priority}"
        resp = requests.post(url, headers=headers)
        print(resp)
        wanda.say("A Equipe foi informada!")
    except:
        print("opps there was an error")
        pass

def banheiro():
    id_number = random.randint(0, 99999999999)
    content = "Necessiade de Banheiro"
    priority = 1
    try:    
        url = f"http://192.168.232.183:8000/add_task?id_number={id_number}&content={content}&priority={priority}"
        resp = requests.post(url, headers=headers)
        print(resp)
        wanda.say("A Equipe foi informada!")
    except:
        print("opps there was an error")
        pass


command = ""
wanda.say("Olá! Como posso te ajudar?")
while True and command not in ["turn off", "goodbye", "thank you", "morra", "adeus"]:

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

    if command in ['tell me a fact','tell me something', "tell me more", 'conte um fato']:
        facts()
        command = ""

    if command in  ['tarefa']:
        task()
        command = ""
    
    if command in ['estou com sede', 'quero aquua', 'presciso de água', 'água']:
        sede()
        command = ""

    if command in ['estou com dor', 'sinto dor', 'presciso de ajuda', 'ajuda']:
        dor()
        command = ""
    
    if command in ['estou com fome', 'sinto fome', 'presciso de comida']:
        fome()
        command = ""

    if command in ['presciso ir ao banheiro', 'quero ir ao banheiro']:
        banheiro()
        command = ""
    
    # if command in ['good morning','good evening','good night','good afternoon']:
    #     now = datetime.now()
    #     hr = now.hour
    #     message = ""
    #     if hr <= 0 <=12:
    #         message = "Morning"
    #     if hr >=12 <= 17:
    #         message = "Afternoon"
    #     if hr >=17 <=21:
    #         message = "Evening"
    #     if hr > 21: message = "Night"

    #     greetings = "Good " + message + " Bruno"
    #     wanda.say(greetings)

wanda.say("Adeus, estou indo descansar")
