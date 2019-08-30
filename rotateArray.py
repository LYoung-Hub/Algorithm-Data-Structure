# -*- coding:utf-8 -*-
class Solution:

    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        else:
            left = 0
            right = len(rotateArray) - 1
            while left < right:
                mid = left + (right - left) / 2
                if rotateArray[left] > rotateArray[left + 1]:
                    return rotateArray[left + 1]
                else:
                    if rotateArray[right] < rotateArray[mid]:
                        left = mid
                    else:
                        right = mid


if __name__ == '__main__':
    solu = Solution()
    solu.minNumberInRotateArray([3, 4, 5, 1, 2])
