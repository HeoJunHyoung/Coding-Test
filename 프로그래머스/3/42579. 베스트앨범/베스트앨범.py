def findFreqGenre(genres, plays):
    genre_play = dict()
    for index, value in enumerate(genres):
        if value not in genre_play:
            genre_play[value] = (plays[index], [(plays[index], index)])
        else:
            old_tuple = genre_play[value]
            new_tuple = (old_tuple[0] + plays[index], old_tuple[1] + [(plays[index], index)])
            genre_play[value] = new_tuple
            
    return genre_play
    
def solution(genres, plays):
    result = []
    genre_play = findFreqGenre(genres, plays)
    sorted_plays = sorted(genre_play.items(), reverse=True, key=lambda x: x[1][0])

    for genre in sorted_plays:
        listA = genre_play[genre[0]]
        temp = sorted(listA[1], key=lambda x: (-x[0], x[1]))

        if len(temp) < 2:
            result.append(temp[0][1])
        else:
            result.append(temp[0][1])
            result.append(temp[1][1])

    return result
    
    