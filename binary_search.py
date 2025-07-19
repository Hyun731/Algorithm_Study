def binary_search(arr,s_data):
    low = 0
    high = len(arr) - 1
    mid = len(arr) // 2
    while(low <= high):
        mid = (low + high) // 2
        if(arr[mid] < s_data):
            low = mid + 1
        elif(arr[mid] > s_data):
            high = mid - 1
        else:
            return mid
    return -1
