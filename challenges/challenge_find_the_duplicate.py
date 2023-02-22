def find_duplicate(nums):
    if not nums or type(nums) == str or len(nums) == 1:
        return False
    sorted_nums = sorted(nums)
    for index, num in enumerate(sorted_nums):
        if type(num) == str or num < 0:
            return False
        if num == sorted_nums[index - 1]:
            return num
    return False
