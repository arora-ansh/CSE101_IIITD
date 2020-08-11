print("""
def insertionSort(arr): 
  
    
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j = j-1
        arr[j + 1] = key 


def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        if   arr[j] <= pivot: 
          
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  

def quickSort(arr,low,high): 
    if low < high: 
  
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) """)
