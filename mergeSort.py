nums = []
number = int(input("Total number of elements: "))
for i in range(number):
    value = int(input("%d element of list nums: " % i))
    nums.append(value)


def merge(l, r):
    sortednums = []
    i = j = 0
    for _ in range(len(l) + len(r)):
        if i < len(l) and j < len(r):
            if l[i] <= r[j]:
                sortednums.append(l[i])
                i += 1
            else:
                sortednums.append(r[j])
                j += 1
        elif i == len(l):
            sortednums.append(r[j])
            j += 1
        elif j == len(r):
            sortednums.append(l[i])
            i += 1
    return sortednums


def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    l = mergeSort(nums[:mid])
    r = mergeSort(nums[mid:])
    return merge(l, r)


nums = mergeSort(nums)
print(nums)

