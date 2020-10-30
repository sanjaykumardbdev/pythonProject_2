pos = 0

def bin_search(list,n):
    l = 0
    u = len(list) + 1

    while l <= u:
        mid = (l + u)//2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid
            else:
                u = mid
        return False


list = [12,23,33,34,45,56,67,78,82,93]


for i in range(10):
    n = list[i]
    print(n)
    if bin_search(list,n):
        print('found at postion ', pos+1)
    else:
        print('Not found at postion ')


n = 781
if bin_search(list,n):
    print('*** found at postion ', pos+1)
else:
    print('*** Not found at postion ')

