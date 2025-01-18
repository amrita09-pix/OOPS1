class person:
    def __init__(self,name,age,weight,height):
        self.name = name
        self.age = age
        self.__weight = weight
        self.height = height
    
    def display(self):
        print(f"""person's info - 
        {name},
        {age},
        {weight},
        {height}""")

name = 'Amrita'
age = 25
weight = 50
height = "5'0"

per = person(name,age,weight,height)
#per.display()
print(per._person__weight)