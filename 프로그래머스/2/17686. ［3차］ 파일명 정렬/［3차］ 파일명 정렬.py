import re

def split_filename(files):
    # 정규 표현식을 사용하여 파일명을 분리
    match = re.match(r'([^0-9]+)([0-9]+)(.*)', files)
    if match:
        head, number, tail = match.groups()
        splited_files = [head, number, tail]
        return splited_files

def solution(files):
    splited_files = []
    result = []
    for file in files:
        splited_files.append(split_filename(str(file)))
        
    splited_files = sorted(splited_files, key = lambda x : (x[0].lower(),int(x[1])))
    
    for splited_file in splited_files:
        result.append(''.join(splited_file))
    
    return result
    
    