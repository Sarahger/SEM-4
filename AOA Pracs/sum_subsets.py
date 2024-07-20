# sum of subsets
def subset_sum(nums, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(nums)):
            backtrack(i + 1, target - nums[i], path + [nums[i]])

    result = []
    backtrack(0, target, [])
    return result

# Example usage:
nums = [2, 3, 7, 8, 10]
target = 10
print("Subsets with sum equal to", target, ":")
print(subset_sum(nums, target))