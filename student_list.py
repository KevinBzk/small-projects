#list of students


lists = []

def check_name(students):
    for spalte in lists:
        a = spalte
        print(a)
    

b = 0

while b == 0:
    stud0 = input("Your name: ")
    lists.append(stud0)
    c = input("Another Student?\n")
    if c == "yes":
        b= 0 
    elif c == "no":
        b +=1 
        
print(check_name(lists))