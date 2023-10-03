def solution(score):
    result = []
    
    arr = [sum(i)/2 for i in score]
    sorted_score = []
    sorted_score = sorted(arr, reverse=True)
    # print(sorted_score)
    for i in arr:
        # print(sorted_score.index(i))
        result.append(sorted_score.index(i)+1)
    
    return result