import random

names = ["Saksham", "CS Dojo", "Carl Lewis",  "Pewdiepie", "Dominic", "Dan the Man"]

i = 0




print("Guess the Word: Saksham= 1, CS Dojo= 2, Carl Lewis 3,  Pewdiepie= 4, Dominic= 5, Dan the Man= 6")

while i<5:
    word = random.choice(names)
    ques = input()



    if ques == "1":
        ques = names[0]
        print(names[0])
        if ques == word:
            print("You were Right! :)")

        else:
            print(f"You were Wrong! {word} is the right answer.")

    if ques == "2":
        ques = names[1]
        print(names[1])
        if ques == word:
            print("You were Right! :)")

        else:
            print(f"You were Wrong! {word} is the right answer.")

    if ques == "3":
        ques = names[2]
        print(names[2])
        if ques == word:
            print("You were Right! :)")

        else:
            print(f"You were Wrong! {word} is the right answer.")

    if ques == "4":
        ques = names[3]
        print(names[3])
        if ques == word:
            print("You were Right! :)")

        else:
            print(f"You were Wrong! {word} is the right answer.")

    if ques == "5":
        ques = names[4]
        print(names[4])
        if ques == word:
            print("You were Right! :)")

        else:
            print(f"You were Wrong! {word} is the right answer.")

    if ques == "6":
        ques = names[5]
        print(names[5])
        if ques == word:
            print(f"You were Right! :)")

        else:
            print(f"You were Wrong! {word} is the right answer.")


    i+=1










# index