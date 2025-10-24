# v1.0
def insertion_sort1(arr): 
    for i in range(1,len(arr)):
        current = i 
    while ((current >= 2) and (arr[current-1] > arr[current])):
        # Exchange 
        arr[current],arr[current-1] = arr[current-1] ,arr[current]   
        current = current - 1 
        
# v2.0
def insertion_sort2(arr): 
    for i in range(1, len(arr)):
        current = arr[i] 
        j = i - 1 
        
        while ((j >= 0) and (arr[j] > current)):
            # shift element to the right
            arr[j + 1] = arr[j]      
            j = j - 1 
        
        arr[j + 1] = current
    

              
    

a = [10,20,30,40,50,80,90,110,70]
b = [1,3,5,7,9,4,2,6,8,10]

# test v1.0
print(a)
insertion_sort1(a)        
print(a)

# test v2.0
print(b)
insertion_sort2(b)        
print(b)