def Consecutive(arr):
  a = 0
  arr = sorted(arr)

  for i in range(min(arr),max(arr)):

    a = a+1

  arr.remove(min(arr))
  arr.remove(max(arr))

  return (a-1)-len(arr)

# keep this function call here 
print(Consecutive(input())) 