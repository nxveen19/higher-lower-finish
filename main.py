import random
from art import logo
from game_data import data
from art import vs
print(logo)
a= random.choice(data)
def higher_lower():
 print(vs)
 b= random.choice(data)
 print(f"Comapre X: {a['name']}, a {a['description']}, from {a['country']}")
 print(f"Comapre Y: {b['name']}, a {b['description']}, from {b['country']}")
 higher_lower.X= int(a['follower_count'])
 higher_lower.Y= int(b['follower_count'])
 # print(a["name"])
 # b=random.choice(list(a.items()))
 # print(a)
 # print(b)
higher_lower()
c = input("Who has more followers type 'X' or 'Y': ")
sum = 0
if c==X:
 if higher_lower.X>higher_lower.Y:
  sum += 1
  print(f"Youre right. Current score: {sum}")
  higher_lower()
elif c==Y:
 if higher_lower.Y>higher_lower.X:
  b=a
  sum += 1
  print(f"Youre right. Current score: {sum}")
  higher_lower()
else:
 print(f"Sorry you are wrong, Score is: {sum}")

