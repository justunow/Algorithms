nums = []
number = int(input("Total number of elements: "))
for i in range(number):
    value = int(input("%d element of list nums: " % i))
    nums.append(value)


def insertionSort(nums):
    for i in range(1, len(nums)):
        k = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > k:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = k


insertionSort(nums)
print(nums)