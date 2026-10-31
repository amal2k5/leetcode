class Solution(object):
    def topKFrequent(self, words, k):

        freq = {}

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        min_heap = []

        for word, count in freq.items():
            heapq.heappush(min_heap, (-count, word))

        result = []    

        for _ in range(k):
            count, word = heapq.heappop(min_heap)
            result.append(word)
        return result        

