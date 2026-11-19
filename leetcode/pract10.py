
def longestSubarray(arr, k):
    left = even = ans = 0

    for right in range(len(arr)):
        if arr[right] % 2 == 0:
            even += 1

        while even > k:
            if arr[left] % 2 == 0:
                even -= 1
            left += 1

        ans = max(ans, right - left + 1)

    return ans


n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(longestSubarray(arr, k))

