print("Quiz")

score = 0
print("How old is Kevin?")
print("A: 16\nB: 17\nC: 19")
answer1 = input()

if answer1 == "B":
    score += 1 

print("In which country lives Kevin?")
print("A: Germany\nB: France\nC: America")
answer2 = input()

if answer2 == "A":
    score += 1

print("Who won the World Cup in 2014")
print("A: Spain\nB: France\nC: Germany")
answer3 = input()

if answer3 == "C":
    score += 1

if score > 0:
    print("you answerd " + str(score)+"/3 right!")
else:
    print("you answered no question correct! Try again")
