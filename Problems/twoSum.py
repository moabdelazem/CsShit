# Brute Force
# O(n^2)
# def twoSum(array, target):
#     for i in range(len(array)):
#         for j in range(i + 1, len(array)):
#             if array[i] + array[j] == target:
#                 return [i, j]
#     return None

# O(n)
# One Pass Hash
def twoSum(array, target):
    numMap, n = {}, len(array)

    for i in range(n):
        complement = target - array[i]

        if complement in numMap:
            return [numMap[complement], i]

        numMap[array[i]] = i
    
    
print(twoSum([2,7,11,5], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))