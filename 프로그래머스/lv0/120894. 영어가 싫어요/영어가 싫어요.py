def solution(numbers):
    
    word_list = ['one','two','three','four','five','six','seven','eight','nine','zero']
    list_num = list(range(1, 10))
    list_num.append(0)
    num_list = []
    
    word_dict = dict(zip(word_list, list_num))
    answer = ''
    cur = 0
    
    
    while cur < len(numbers):
    
    
        if numbers[cur] == 'o':
            temp = numbers[cur:cur+3]
            cur += 3
            num_list.append(word_dict[temp])
        elif numbers[cur] == 'e':
            temp = numbers[cur:cur+5]
            cur += 5
            num_list.append(word_dict[temp])
        elif numbers[cur] == 'n':
            temp = numbers[cur:cur+4]
            cur += 4
            num_list.append(word_dict[temp])
        elif numbers[cur] == 'z':
            temp = numbers[cur:cur+4]
            cur += 4
            num_list.append(word_dict[temp])
        elif numbers[cur] == 't':
            if numbers[cur+1] == 'w':
                temp = numbers[cur:cur+3]
                cur += 3
                num_list.append(word_dict[temp])
            else:
                temp = numbers[cur:cur+5]
                cur += 5
                num_list.append(word_dict[temp])
        elif numbers[cur] == 'f':
            if numbers[cur+1] == 'o':
                temp = numbers[cur:cur+4]
                cur += 4
                num_list.append(word_dict[temp])
            else:
                temp = numbers[cur:cur+4]
                cur += 4
                num_list.append(word_dict[temp])
        else:
            if numbers[cur+1] == 'i':
                temp = numbers[cur:cur+3]
                cur += 3
                num_list.append(word_dict[temp])
            else:
                temp = numbers[cur:cur+5]
                cur += 5
                num_list.append(word_dict[temp])
    
    return int(''.join(map(str, num_list)))
    
    
            
            
            
            
            
            
            