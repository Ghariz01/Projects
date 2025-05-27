def sol_2(arr,x):
    l,r = 0, len(arr) - 1

    while(l<=r):
        mid = (l+r)//2

        if(arr[mid]<x):
               l = mid + 1
        elif (arr[mid]>x):
                r = mid - 1
        else:
            return True

    return False

