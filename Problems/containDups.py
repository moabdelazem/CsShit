""" 
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


def containDups(array : list):
    # O(n)
    # Create Set
    # mySet = set()
    # for i in array:
    #     if i in mySet:
    #         return True
    #     else:
    #         mySet.add(i)
    # return False

    # O(1)
    mySet = set(array)
    if len(mySet) != len(array):
        return True
    return False



# Test Area
nums_1 = [1,2,3,1]
nums_2 = [1,2,3,4]
nums_3 = [1,1,1,3,3,4,3,2,4,2]

print(containDups(nums_1))
print(containDups(nums_2))
print(containDups(nums_3))