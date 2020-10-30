nums = [7, 8, 9, 2]

print(nums[0])
print(nums[3])

# IndexError: list index out of range
# print(nums[8])

for i in nums:
    print(i)

print('-----------------')
it = iter(nums)
print(it.__next__())            # will continue after this next.

print(next(it))

for i in it:
    print(i)