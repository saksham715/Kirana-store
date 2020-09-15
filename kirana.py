import time

sum = 0
print("Enter the prices one by one")

while True:
    ques = input()
    if ques != 'q':
        sum += int(ques)
        print(f'Yet sum {sum}')



    else:
        print(f'Thanks for using our product \n')
        time.sleep(2)
        print(f'Sum of products is {sum}')
        break