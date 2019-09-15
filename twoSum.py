class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        hash_set = {}
        for i in range(0, len(numbers)):
            if numbers[i] not in hash_set:
                hash_set[numbers[i]] = [i]
            else:
                hash_set[numbers[i]].append(i)

        for i in range(0, len(numbers)):
            temp = target - numbers[i]
            if temp != numbers[i] and temp in hash_set:
                return [i] + hash_set[temp]
            if temp == numbers[i] and len(hash_set[numbers[i]]) > 1:
                return hash_set[numbers[i]]


if __name__ == '__main__':
    solu = Solution()
    print solu.twoSum([2, 7, 11, 15], 9)
