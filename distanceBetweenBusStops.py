class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        clockwise = sum(distance[min(start, destination):max(start, destination)])
        s = sum(distance) - clockwise
        return min(s, clockwise)


if __name__ == '__main__':
    solu = Solution()
    print solu.distanceBetweenBusStops([7,10,1,12,11,14,5,0],7,2)
