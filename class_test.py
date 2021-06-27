class Person:
    def __init__(self,name_input,age):
        self.name=name_input
        self.age=age

class student(Person):
    def __init__(self,name_input,age):
        Person.__init__(self,name_input,age)
        
    # def changename(self,input):
    #     Person.name=input

    def showname(self):
        print(self.name)

if __name__ == '__main__':
    ob=student("kim",18)
    ob.showname()