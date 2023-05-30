#list chooser 

def person_intro(name, age, height):
    a =str(name)
    b = str(age)
    c = str(height)
    print("Welcome back", a, "\nYour ",b, " years old\nYour ",c, " cm Tall")

a = input("Your name: ")
b = input("your age: ")
c = input("your height: ")

person_intro(a,b,c)