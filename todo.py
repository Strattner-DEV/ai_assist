from datetime import date
from enum import Enum
from uuid import uuid4


class Status(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    COMPLETED = 2

class Priority(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2

class Item():
    __creation_date = date.today()
    __title = "empty"
    __status =  Status.NOT_STARTED
    __priority = Priority.LOW
    __flag = False
    __url = ""
    __due_date = date
    __state = False
    __notes = ""
    __icon = ""

    def __init__(self, title:str=None):
        if title is not None:
            self.__title = title
        self.__id = str(uuid4())
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.__current < len(self.__todos) - 1:
            self.__current += 1
            print(self.__todos[self.__current].title)
            return self.__todos[self.__current]
        else:
            self.__current = -1
        raise StopIteration
    
    def __len__(self):
        return len(self.__todos)
    
    @property
    def title(self):
        """ Return the title of the item """
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def priority(self):
        """ Return the priority of the item """
        return self.__priority

    @priority.setter
    def priority(self, value):
        self.__priority = value

    @property
    def creation_date(self):
        """ Return the creation_date of the item """
        return self.__creation_date

    @creation_date.setter
    def creation_date(self, value):
        self.__creation_date = value

    @property
    def age(self):
        return self.__creation_date - date.today()

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        self.__status = value
    
    @property
    def notes(self):
        return self.__notes
    
    @notes.setter
    def notes(self, value):
        self.__notes = value

class Todo():
    __todos = []

    def __init__(self):
        print("New todo list created")
        self.__current = -1
    
    def new_item(self, item:Item):
        self.__todos.append(item)

    @property
    def items(self) -> list:
        return self.__todos

    def show(self):
        print("*"*80)
        for item in self.__todos:
            print(item.title, item.status, item.priority, item.age)

    def remove_item(self, uuid:str=None, title:str=None) -> bool:
        if title is None and uuid is None:
            print("You need to provide some details for me to remove it, either UUID or title")
        
        if uuid is None and title:
            for item in self.__todos:
                if item.title == title:
                    self.__todos.remove(item)
                    return True
            
            print("Item with title", title, "not found")
            return False
        if uuid:
            self.__todos.remote(uuid)
            return True

# i = Item("Get Shopping")
# l = Todo()
# l.new_item(i)
# l.show()
# l.remove_item(title="Get Shopping")
# l.show()
    

    
    