pos = -1

def bin_search(list,n):
    l = 0
    u = len(list) -1

    while l <= u:
        mid  = (l + u)//2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                #print(list[mid])
                l = mid+1
            else:
                u = mid-1
    return False


list = [12,23,33,34,45,56,67,78,82,93]


for i in range(9):
    n = list[i]
    print(n,i)
    if bin_search(list,n):
        print('found at postion ', pos+1)
    else:
        print('Not found at postion ')


n = 781
if bin_search(list,n):
    print('*** found at postion ', pos+1)
else:
    print('*** Not found at postion ')

