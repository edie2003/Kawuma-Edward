class Dog:

    '''
    def bark(self):
        print('bark')

    
d = Dog()
d.bark()
print(type(d))
 
print('bark')'''
    '''def __init__ (self, name, age):
        self.name = name
        print(name, age, end='years old and has ')
        self.age = age
        
    def add_one(self, y):
        return y *2
        
    
    def bark(self):
        print('bark')
d = Dog("tim is", 55)
d2 = Dog('tom is', 66)
print(d.add_one(5), end = 'small dogs')
print(d2.name)'''
    
    def __init__ (self, name, age):
        self.name = name
        print(name, age, end='$$ ')
        self.age = age
    def getName(self):
        return self.name
    def getAge (self):
        return self.age
    def setAge (self):
        

d = Dog("tim is", 55)
d.setAge()
print(d.getAge(23))
d2 = Dog('tom is', 66)
dogsName = ['tim', 'tom']
dog