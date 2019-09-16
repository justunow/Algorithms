nums = []
number = int(input("Total number of elements: "))
for i in range(number):
    value = int(input("%d element of list nums: " % i))
    nums.append(value)


def countingSort(nums, p):
    n = len(nums)
    count = [0] * 10
    output = [0] * n
    for i in range(n):
        count[nums[i] // p % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        output[count[nums[i] // p % 10] - 1] = nums[i]
        count[nums[i] // p % 10] -= 1
    for i in range(n):
        nums[i] = output[i]


def radixSort(nums):
    la = max(nums)
    p = 1
    while la // p > 0:
        countingSort(nums, p)
        p *= 10


radixSort(nums)
print(nums)