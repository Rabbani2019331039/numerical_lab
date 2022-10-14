import numpy as np

def input_for_sle():
    n = int(input('Number of Unknowns?\n'))
    x = 'x'
    a = 'a'
    s = str('')
    for i in range(1,n+1):
        s += (str(a)+str(i)+str(x)+str(i)+' ')
        if i !=n: s+='+ '
    s+='= b'

    print("input the coefficients of unknowns: ")
    print(s)

    b = []
    arr = []
    for i in range(n):
        temp = np.array([float(x) for x in input().split()])
        b.append(temp[-1])
        temp = temp[:-1]
        arr.append(temp)
    
    arr = np.array(arr)
    b = np.array(b)

    return arr,b


def take_input():
    print('System Of Linear Equation\n\n')

    a,b = input_for_sle()
    
    print("What do you want?")
    print('1. naive Gauss elimination method')
    print('2. Gauss elimination method with partial pivoting')
    print('3. Find Inverse Matrix')
    print('4. Exit\n')

    op = int(input('Select an Option: '))

    if op >4: print('invalid')

    return op,a,b


