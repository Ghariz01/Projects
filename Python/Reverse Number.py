def sol_3(num):
    n = 1
    temp = num

    while (temp>10):
        temp = temp//10
        n += 1

    arr=[]

    for i in range(n):
        arr.append(0)

    for i in range(n):
        arr[n-1-i] = n%10
        num = num//10

    return arr