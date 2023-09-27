def solution(arr, delete_list):
    
    orderList = []
    
    for i in range(0, len(delete_list)):
        if delete_list[i] in arr:
            orderList.append(arr.index(delete_list[i]))
            
    orderList = sorted(orderList, reverse=True)
    
    for i in orderList:
        del arr[i]
        
    return arr