nums = []
numbers = int(input("Total number of elements: "))
for i in range(numbers):
	value = int(input("%d element of list nums: " %i))
	nums.append(value)

def shortBubbleSort(nums):
	for i in range(len(nums)-1,0,-1):
		flag = 1
		for j in range(i):
			if(nums[j] > nums[j+1]):
				nums[j], nums[j+1] = nums[j+1], nums[j]
				flag = 0
		if(flag == 1):
			break

shortBubbleSort(nums)
print(nums)			