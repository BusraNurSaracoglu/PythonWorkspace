def Consecutive(arr):

  mx = max(arr) 
  mn = min(arr)

  arr.remove(mx)
  arr.remove(mn)

  uzunluk = len(arr) + 1
  sonuc = mx-mn-uzunluk



  return sonuc

# keep this function call here 
print Consecutive(raw_input())