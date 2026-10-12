class MedianFinder:

    def __init__(self):
        self.l_max_heap =[]
        self.r_min_heap =[]

    def addNum(self, num: int) -> None:
        if not self.l_max_heap or num< -self.l_max_heap[0]:
            heapq.heappush(self.l_max_heap,-num)
        else:
            heapq.heappush(self.r_min_heap,num)

        if abs(len(self.l_max_heap) - len(self.r_min_heap))>1:
            heapq.heappush(self.r_min_heap,-heapq.heappop(self.l_max_heap))
        elif len(self.l_max_heap) < len(self.r_min_heap):
            heapq.heappush(self.l_max_heap,-heapq.heappop(self.r_min_heap))

    def findMedian(self) -> float:
        if len(self.l_max_heap) == len(self.r_min_heap):
            return (-self.l_max_heap[0] + self.r_min_heap[0])/2
        else:
            return -self.l_max_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()