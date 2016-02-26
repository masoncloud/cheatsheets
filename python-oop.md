# Python Object Oriented Programming

### Simple Python inheritance and polymorphism example 

The below shows a simple inheritance (name attribute) and polymorphism (speak method) example in Python 3. 

    class Animal:

        def __init__(self, name):
    
            self.name = name
    
        def speak(self):
    
            raise NotImplementedError("I don't know how to speak!")
    
    
    class Cat(Animal):
    
        def __init__(self, name, is_tabby):
    
            super().__init__(name=name)
            self.is_tabby = is_tabby
    
        def speak(self):
    
            return "Meeeow"
    
    
    class Elephant(Animal):
    
        def speak(self):
    
            return "eRowwwwrrrh"
    
    
    frank = Cat(name="Frank", is_tabby=False)
    print(frank.name, frank.speak())
    
    roger = Elephant(name="Roger")
    print(roger.name, roger.speak())
    
    generic_animal = Animal(name="Kurt")
    print(generic_animal.name, end=" ")
    try:
        print(generic_animal.speak())
    except NotImplementedError as e:
        print(e)

Running this would output:

    Frank Meeeow
    Roger eRowwwwrrrh
    Kurt I don't know how to speak!
