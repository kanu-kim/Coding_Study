def solution(nums):
    return len(nums)//2 if len(set(nums)) > len(nums)//2 else len(set(nums))

# return min(len(set(nums)),len(nums)//2)
