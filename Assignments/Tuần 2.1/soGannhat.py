n= int(input())
a=list(map(int,input().split()))
k,x=map(int,input().split())
def binary_search(arr,k,x):
  low=0
  high= len(arr)-k
  while low<high:
    mid =low+(high-low)//2
    if x-arr[mid]>arr[mid+k]-x:
      low=mid+1
    else:
      high=mid
  return arr[low: low+k]
b=binary_search(a,k,x)
for i in range (k):
  print(b[i],end=' ')