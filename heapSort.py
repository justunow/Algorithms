nums = []
number = int(input("Total number of elements: "))
for i in range(number):
    value = int(input("%d element of list nums: " % i))
    nums.append(value)


def heapify(nums, n, i):
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2
    if left < n and nums[left] > nums[i]:
        largest = left
    if right < n and nums[right] > nums[largest]:
        largest = right
    if largest != i:
        nums[largest], nums[i] = nums[i], nums[largest]
        heapify(nums, n, largest)


def heapSort(nums):
    n = len(nums)
    for i in range(n // 2, -1, -1):
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


heapSort(nums)
print(nums)