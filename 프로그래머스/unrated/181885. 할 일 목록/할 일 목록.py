def solution(todo_list, finished):
    
    todo_dict = dict(zip(todo_list, finished))
    
    return [key for key, value in todo_dict.items() if value is False]