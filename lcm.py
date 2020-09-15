# mult_by = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# fac = []
#
# num_1 = int(input('Enter the number: '))
#
# for i in mult_by:
#     print(num_1 * i)
#

num_1 = int(input('Enter the first number: '))
num_2 = int(input('Enter the second number: '))

maxx = max(num_1, num_2)


while True:
    if maxx % num_1 == 0 and maxx % num_2 == 0:
        print(f'LCM is {maxx}')
        break

    maxx +=1


mult = 2

user_input = int(input('Enter the number: '))

if mult < user_input:
    if