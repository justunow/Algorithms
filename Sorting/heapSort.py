nums = []
number = int(input("Total number of elements: "))
for i in range(number):
    value = int(input("%d element of list nums: " % i))
    nums.append(value)


def heapify(nums, n, i):
    la = i
    l = i * 2 + 1
    r = i * 2 + 2
    if l < n and nums[l] > nums[i]:
        la = l
    if r < n and nums[r] > nums[la]:
        la = r
    if la != i:
        nums[la], nums[i] = nums[i], nums[la]
        heapify(nums, n, la)


def heapSort(nums):
    n = len(nums)
    for i in range(n // 2, -1, -1):
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


heapSort(nums)
print(nums)