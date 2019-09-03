# _*_ coding=utf-8 _*_

"""
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that
they add up to the target, where index1 must be less than index2.

Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and
you may not use the same element twice.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""


class Solution(object):

    def two_sum(self, nums: list, target: int) -> list:
        """
        :param nums:    List[int]
        :param target:  int
        :return:        List[int]
        """
        for i in range(len(nums)):
            a = nums[i]
            b = target - a

            if b >= a:  # nums为有序列表，b>=a，说明b的位置在i的右侧
                j = self.binary_search(nums, i + 1, len(nums) - 1, b)
            else:
                j = self.binary_search(nums, 0, i - 1, b)
            if j:
                break
            print(i,j)
        return sorted([i + 1, j + 1])

    def binary_search(self, li, left, right, val):

        while left <= right:
            mid = (left + right) // 2
            if li[mid] < val:
                left = mid + 1
            elif li[mid] > val:
                right = mid - 1
            else:
                return mid
        else:
            return None


arr = [2, 7, 11, 15]
s = Solution()
print(s.two_sum(arr, 9))
