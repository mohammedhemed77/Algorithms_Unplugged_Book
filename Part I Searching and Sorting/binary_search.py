# v1.0
def binary_search(arr,key,left,right):
    left  = 0 
    right = len(arr) -1
    
    while (left <= right):
        mid = (left + right) // 2 
        
        if (arr[mid] == key): return f"element found at index : {mid}" 
        elif (arr[mid] < key ): left = mid+1 
        elif (arr[mid] > key ): right = mid -1
    
    return "Not found"      

# v2.0
def recursive_binary_search(arr,key,left,right):
  # base case 
  if (left > right) : return "Not found"
  mid = (left + right) // 2 
  
  if (arr[mid] == key): return f"element found at index : {mid}"
  elif (arr[mid] < key ): return recursive_binary_search (arr,key,mid+1,right)
  elif (arr[mid] > key ): return recursive_binary_search (arr,key,left,mid-1)
       


a = [10,20,30,40,50,60,70,80,90,100]
k1 = 90          
k2 = 5

#Test v1.0
print (binary_search(a,k1,0,len(a)-1))
print (binary_search(a,k2,0,len(a)-1))

#Test v2.0
print (recursive_binary_search(a,k1,0,len(a)-1))
print (recursive_binary_search(a,k2,0,len(a)-1))
