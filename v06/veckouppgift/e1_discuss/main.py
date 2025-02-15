"""
1 Läsa och förstå kod - diskutera i grupp
Skriv ner vad du tror kommer skrivas ut. Skriv sedan in koden i din IDE, exakt som den står, och kör den. Fick du samma resultat som du trodde? Om inte, varför?
"""

# 1 Vad gör följande kod?
class SafeStorage:
    __data = None
    
    def get(self):
        return self.__data
    
    def put(self, data):
        self.__data = data

safe = SafeStorage() # instans
safe.put("Anakonda") # SafeStorage.__data = Anakonda
x = safe.get() # x <- Anakonda
safe.put("Boaorm") # SafeStorage.__data = Boaorm
y = safe.get() # y <- Boaorm
print(x, y) # => "Anakonda Boaorm"

# 2a Vad gör följande kod? Fixa eventuella fel.

class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")

class Dog(Animal):
    def make_noise(self):
        print("Voff!")

class Cat(Animal):
    def make_noise(self):
        super().make_noise()
        print("Mjau!")
        
class Rooster(Animal):
    pass

def sound_off(animal):
    for item in animal:
        item.make_noise()

c = Cat() # c blir instans av Cat class med basclass Animal
d = Dog() # d blir instans av Dog class med basclass Animal
h = Rooster() # h blir instans av Rooster med basclass Animal

sound_off([c, d, h])
 # 1. "Detta djur har vi inget ljud för."
 # 2. "Mjau!"
 # 3. "Voff!"
 # 4. "Detta djur har vi inget ljud för."


# 2b Lägg till en klass för ett annat djur, till exempel en guldfisk.

class Fish():
    def make_noise(self):
        print("Fishes makes no sound")
        
f = Fish()
# Som ovan plus
# 5. "Fishes makes no sound"

sound_off([c, d, h, f])