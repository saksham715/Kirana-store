def ask(ques, age, weight, height):
    while True:
        if age <=0:
            print("Please enter the valid age")
            break

        else:
            pass


        if weight <=0:
            print('Please enter the valid weight')
            break

        else:
            pass

        if height <= 0:
            print('Please enter the valid height')
            break

        else:
            pass

        bmi = weight / height **2
        print('BMI: ')
        print(bmi)

        if bmi < 25:
            print(f'{ques}, you are underweight.')

        else:
            print(f'{ques}, you are overweight.')

        break

ques = input("Please enter your name: ")
age = int(input("Please enter your age: "))
weight = float(input("Please enter your weight (in m): "))
height = int(input("Please enter your height (in kg): "))


ask(ques, age, weight, height)