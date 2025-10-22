# this is simple and clear implementation to this algorithm 
# comments adapted by : ENG: Mohammed Hemed 
# Source : https://www.w3schools.com/python/python_dsa_mergesort.asp

# This function sorts a list using the "Divide and Conquer" strategy.
# 1. It recursively divides the list into two halves until it has
#    many lists containing only one element (the base case).
# 2. It then merges those sorted lists back together.
#
# args: arr (a list of elements)
# return: A new list containing all elements from 'arr' in sorted order.

def mergeSort(arr):
  # base case that stop the recursion   
  if len(arr) <= 1:
    return arr
  # "//" : floor division operator ex : 7//2 = 3 
  # ex : -7//2 = -4 note that in negative floor division : rounding down towards infinity 
  mid = len(arr) // 2
  # slicing rule [start:stop] including start and excluding stop 
  leftHalf = arr[:mid]          # exclude mid  
  rightHalf = arr[mid:]         # include mid
  
  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)

  return merge(sortedLeft, sortedRight)

# function that combine two sorted lists into a bigger sorted one 
# args : two sorted lists 
# return : one sorted list that merges the two lists 

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
mysortedlist = mergeSort(mylist)
print("Sorted array:", mysortedlist)