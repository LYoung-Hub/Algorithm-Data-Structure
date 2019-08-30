# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd_array = []
        even_array = []
        for i in range(0, len(array)):
            if array[i] % 2 == 0:
                even_array.append(array[i])
            else:
                odd_array.append(array[i])

        odd_array.extend(even_array)
        return odd_array


if __name__ == '__main__':
    solu = Solution()
    print solu.reOrderArray([1, 2, 3, 4, 5, 6, 7])
