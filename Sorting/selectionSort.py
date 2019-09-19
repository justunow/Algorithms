nums = []
number = int(input("Total number of elements: "))
for i in range(number):
    value = int(input("%d element of list nums: " % i))
    nums.append(value)


def selectionSort(nums):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if (nums[i] > nums[j]):
                nums[i], nums[j] = nums[j], nums[i]


selectionSort(nums)
print(nums)