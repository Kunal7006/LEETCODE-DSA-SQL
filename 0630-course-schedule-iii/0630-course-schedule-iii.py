class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        n = len(courses)
        courses.sort(key = lambda x:x[1])

        heap =[]
        total =0

        for course in courses:
            duration = course[0]
            lastDay = course[1]

            total += duration
            heapq.heappush(heap,-duration)

            if total>lastDay:
                total -= -heapq.heappop(heap)
            
        return len(heap)