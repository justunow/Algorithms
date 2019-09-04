nums = []
number =  int(input("Total number of elements: "))
for i in range(number):
	value = int(input("%d element of list nums: " %i))
	nums.append(value)

def bubbleSort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if (nums[j] > nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
                
bubbleSort(nums)
print(nums)

