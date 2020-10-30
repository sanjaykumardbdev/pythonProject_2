def sort(list):
    #for i in range(0,5,1):
    for i in range(5):
        minval = i;
        for j in range(i, 6):
            if list[j] < list[minval]:
                minval = j

        temp = list[i]
        list[i] = list[minval]
        list[minval] = temp;

        #print(list)

list = [5, 3, 8, 6, 7, 2]
sort(list)

print(list)

# Search: Linear Binary
# Sorting: Selection sort, Bubble Sort,
print('*********************************************')
# Selection  Sort:
print('*********************************************')

def sort(lst):
    # max val: go from high index to low index
    # min val: go from low index(0) to high index(5), want to reach till 4
    for i in range(5):
        minval = i
        for j in range(i,6):
            if lst[j] < lst[minval]:
                print(lst[minval], lst[j] )
                print(minval,j)
                minval = j

        temp = lst[i]
        lst[i] = lst[minval]
        lst[minval] = temp
        print('---------------------')
        print(lst)
        print('---------------------')


# pos   1   2   3   4   5   6   7   8   9

#lst = [42, 14, 34, 89, 35, 45, 12, 99, 11]
lst = [60, 50, 40, 30, 20, 10]

sort(lst)

print(lst)