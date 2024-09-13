"""

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""

# nums = [3,2,4]
# target = 6

# # nums = [2,7,11,15]
# # target = 9

# # nums = [3,3]
# # target = 6


# def twoSum(nums, target):
#     exclusion = {}

#     for i, num in enumerate(nums):
#         print("index 1: ", i)
#         print("number 1: ", num)
#         second_half = target - num
#         print("second half: ", second_half)
#         if second_half in nums:
#             print("second half index: ", nums.index(second_half))
#             if nums.index(second_half) != i:
#                 return [nums.index(second_half), i]



# print(twoSum(nums,target))


"""

Given an integer x, return true if x is a 
palindrome
, and false otherwise.

"""

x = -121

def isPalindrome(x):
    if x < 0:
        return False
    num_list = [str(x) for x in str(x)]              
    num_list.reverse()                                  
    single_integer = int(''.join(num_list))            
    if x == single_integer:                         
        return True
    else:
        return False

print(isPalindrome(x))

