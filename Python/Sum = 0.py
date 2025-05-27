def sol_1(arr):
    l,r = 0 , len(arr) - 1
    sorted (arr)



    while(l<r):
        sum=arr[l] + arr[r]
        if sum<0:
            l += 1
        elif sum>0:
            r -= 1
        else:
            return (l,r)
        

