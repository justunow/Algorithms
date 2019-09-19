nums = []
number = int(input("Total number of elements: "))
for i in range(number):
    value = int(input("%d element of list nums: " % i))
    nums.append(value)


def partition(nums, l, h):
    pivot = nums[h]
    i = l - 1
    for j in range(l, h):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[h] = nums[h], nums[i + 1]
    return i + 1


def quickSork(nums):
    def _quickSort(nums, l, h):
        if l < h:
            pi = partition(nums, l, h)
            _quickSort(nums, l, pi - 1)
            _quickSort(nums, pi + 1, h)

    _quickSort(nums, 0, len(nums) - 1)


quickSork(nums)
print(nums)