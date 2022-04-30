def MathChallenge(num):
  c = True
  if num == 0:
    c = False
  
  while(num !=1):
    if num %2 != 0:
      c = False
    num = num // 2

  return c

# keep this function call here 
print(MathChallenge(input()))