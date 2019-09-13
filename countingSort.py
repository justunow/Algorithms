nums = []
number = int(input("Total number of elements: "))
for i in range(number):
    value = int(input("%d element of list nums: " % i))
    nums.append(value)


def countingSort(nums):
    n = len(nums)
    output = [0] * n
    count = [0] * 10
    for i in range(0, n):
        count[nums[i]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        output[count[nums[i]] - 1] = nums[i]
        count[nums[i]] -= 1
        i -= 1
    for i in range(0, n):
        nums[i] = output[i]


countingSort(nums)
print(nums)