class Solution:
    def topKFrequent(self, words, k):

        mp = Counter(words)

        heap = []

        for word, freq in mp.items():
            heapq.heappush(heap, (-freq, word))

        result = []

        for _ in range(k):
            freq, word = heapq.heappop(heap)
            result.append(word)

        return result