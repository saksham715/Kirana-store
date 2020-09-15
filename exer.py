
def fiboiter(n):

    prevnum = 0
    currentnum = 1

    for i in range(1, n):
        prevprev = prevnum
        prevnum = currentnum
        currentnum = prevnum + prevprev
    return currentnum

if __name__ == '__main__':
    print(fiboiter(5))


def facto(n):
    factorial = 1
    # factorail_2 = factorial
    if n<0:
        print("Error")
    elif n==0:
        print("1")

    else:
        for i in range(factorial, n+1):
            factorial *= i
        print(factorial)

        # if factorial > 1:
        #     print(factorial//factorail_2)
        #
        # else:
        #     print(factorial)

if __name__ == '__main__':
    facto(7)


def itera(n):
    for i in range(n):
        yield i

vals = itera(12)

print(vals.__iter__())
print(vals.__next__())
print(vals.__next__())
print(vals.__next__())

def findDuplicate():
    lst = [23, 34, 34, 11, 67, 54, 90, 17]

    for i in range(len(lst)):
        if lst[i] == lst[i + 1]:
            return lst[i], lst[i+1]

print(findDuplicate())

num = 153
copy_n = num
sum = 0
convert_str = len(str(num))

while num > 0:

    dipo = num % 10

    sum += dipo ** convert_str

    num = num // 10


if sum == copy_n:
    print('armstrong')

else:
    print('buzz')





# import requests
# import json
#
# url = requests.get('https://api.github.com')
# jason = url.json()
#
# dd = json.dumps(jason)
#
# dd2 = json.loads(dd)
# print(dd)
# print(dd2)




# print(json.loads(dd))
# print(json.dumps(dd))