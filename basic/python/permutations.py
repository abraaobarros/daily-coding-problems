# backtracking


nums = [1,2,3,4,5,6,7]
output = []
# number of permutations of one array
def backtrack(start=0):
    # decline case
    # acceptance case

    # iteration
    #   recursion
    #   backtracking
    if start == len(nums):
        output.append(nums[:]) 

    for i in range(start, len(nums)):
        
        #swap
        nums[i], nums[start] = nums[start], nums[i]
        
        backtrack(start+1)
        
        #reverse
        nums[i], nums[start] = nums[start], nums[i]


print(nums)
backtrack()
print(output)




      



