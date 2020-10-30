# 68 Python Tutorial for Beginners | Linear Search using Python

pos = 0
arr = [4, 6, 7, 9, 10, 0]
#n = int(input("Enter number to search"))
n = 6

def search1(arr,n):
    for i in range(len(arr)):
        if arr[i] == n:
            globals()['pos'] = i
            return True
    return False


if search1(arr, n):
    print('search1 found at postion ', pos + 1)
else:
    print('search1  not found')



print('------------------------------------------------')
print('------------------------------------------------')


pos1 = 0
arr1 = [4, 6, 7, 9, 10, 0]
#n = int(input("Enter number to search"))
n1 = 6


def search(arr1,n1):
    i = 0
    while i < len(arr1):
        if arr[i] == n1:
            globals()['pos'] = i
            return True
        i +=1
    return False




if search(arr1,n1):
    print('found at postion ', pos +1)
else:
    print('not found')

