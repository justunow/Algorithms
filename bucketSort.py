def bucketSort(nums):
    bucket = []
    n = len(nums)
    for i in range(n):
        bucket.append([])
    for i in nums:
        bucket[int(i * 10)].append(i)
    for i in range(n):
        bucket[i] = sorted(bucket[i])
    k = 0
    for i in range(n):
        for j in range(len(bucket[i])):
            nums[k] = bucket[i][j]
            k += 1


nums = [.42, .32, .33, .52, .37, .47, .51]
bucketSort(nums)
print(nums)