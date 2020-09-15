import time
import random
#
# for i in range(20):
#
#     if i%2 != 0:
#         print("""                 clap
#                  clap
#                  clap""")
#
#     elif i%2 ==0:
#         print("Sachin!! Sachin!!")
#
#     time.sleep(2)

names = ["Dumb", "Hippo", "Genius", "Billionaire"]
nameslist = random.choice(names)

s = input("Enter Name: ")
print(s)

print(f"{s} is {nameslist}")