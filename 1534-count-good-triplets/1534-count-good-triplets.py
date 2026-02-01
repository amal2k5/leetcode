class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):

        nums = len(arr)
        count = 0

        for i in range(nums):
            for j in range(i + 1, nums):
                for k in range(j + 1, nums):

                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:

                        count += 1
        return count           

        