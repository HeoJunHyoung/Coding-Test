import heapq

def solution(scoville, K):
    blend_count = 0
    blend_scoville = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        first = heapq.heappop(scoville)
        if not scoville:
            if first < K:
                return -1
        second = heapq.heappop(scoville)
        blend_scoville = first + (second * 2)

        heapq.heappush(scoville, blend_scoville)
        blend_count += 1

    return blend_count