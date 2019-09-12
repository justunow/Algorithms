nums = []
number = int(input("Total elements of nums: "))
for i in range(number):
    value = int(input("%d element of list nums: " % i))
    nums.append(value)


def shellSort(nums):
    n = len(nums)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            t = nums[i]
            j = i
            while j >= gap and nums[j - gap] > t:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = t
        gap //= 2


shellSort(nums)
print(nums)