'''
swapping colors
0   0   0 0 1 1 1 2 2 2

                
0    1   1   2      2
    one 
            two
        three
'''

nums = list(map(int, input().split()))
n = len(nums)
one = 0
two = 0
three = n-1
# while(nums[three]==2):
#     three -= 1
while(two<=three):
    if(nums[two]==0):
        #if num[one]==0 
        # swap -> two+=1
        temp = nums[two]
        nums[two] = nums[one]
        nums[one] = temp
        two += 1
        one += 1
    elif(nums[two]==1):
        two+=1
    else:
        nums[two], nums[three] = nums[three], nums[two]
        three -= 1
print(nums)
        
        