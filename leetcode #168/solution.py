
nums = [2,5,8,11,15,19]
target_no = 19

def two_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return left, right
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []

print(two_sum(nums,target_no))
