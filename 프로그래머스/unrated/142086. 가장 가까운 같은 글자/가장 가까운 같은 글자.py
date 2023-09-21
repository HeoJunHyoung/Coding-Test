def solution(s):
    answer = []
    alphabet = "abcdefghijklmnopqrstuwvxyz"
    alphabet_list = [-1 for i in range(0,26)]

    for index, value in enumerate(s):
        # print(index, value)

        # 만약 읽은 숫자가 처음 등장하는거라면,
        if alphabet_list[alphabet.index(value)] == -1:
            #print(alphabet.index(value))
            # 알파벳 숫자의 수만큼 만들어진 리스트에 value에 해당하는 index를 찾아서,
            # (만약 읽는 숫자가 b라면 b에 해당하는 index인 1이 0으로 만들어진 리스트에
            # 처음 등장하는 인덱스를 넣는다.
            alphabet_list[alphabet.index(value)] = index
            answer.append(-1)
            #print(alphabet_list[alphabet.index(value)])

        #만약 읽은 숫자가 이전에 등장했다면,
        else:
            diff_index = index - alphabet_list[alphabet.index(value)]
            answer.append(diff_index)
            alphabet_list[alphabet.index(value)] = index
    return answer