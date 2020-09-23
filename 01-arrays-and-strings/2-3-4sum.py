def fourSum(nums, target):

    def threeSum(nums, target):
        results = []
        nums.sort()
        for i in range(len(nums)-2):
            l = i + 1; r = len(nums) - 1
            t = target - nums[i]
            if i == 0 or nums[i] != nums[i-1]:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == t:
                        results.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]: l += 1
                        while l < r and nums[r] == nums[r-1]: r -= 1
                        l += 1; r -=1
                    elif s < t:
                        l += 1
                    else:
                        r -= 1

        return results


    results = []
    nums.sort()
    for i in range(len(nums)-3):
        if i == 0 or nums[i] != nums[i-1]:
            threeResult = threeSum(nums[i+1:], target-nums[i])
        for item in threeResult:
            results.append([nums[i]] + item)
    return results

if __name__ == "__main__":
    print(fourSum([0,1,2,4,7,9], 20))