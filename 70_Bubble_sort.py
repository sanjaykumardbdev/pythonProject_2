

def sort(list):
    # starting from 5[len = 6 but index starts with 0 so -1 ] till 0 , using step -1
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j + 1] = temp
            else:
                pass

list = [5, 3, 8, 6, 7, 2]
sort(list)

print(list)