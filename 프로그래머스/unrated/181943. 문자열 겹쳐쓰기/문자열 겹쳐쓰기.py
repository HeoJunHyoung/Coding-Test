def solution(my_string, overwrite_string, s):
    answer = ''
    
    str1 = my_string[0:s]
    str2 = overwrite_string[0:len(overwrite_string)]
    str3 = my_string[s + len(overwrite_string): len(my_string)]
    return str1+str2+str3