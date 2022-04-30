def StringChallenge(strParam):

  c = False
  punc = ''' ! ()-[]{};:'"\,<>./?@#$%^&*_'''

  for a in strParam:
    if a in punc:
      strParam = strParam.replace(a,"")
  
  strParam = strParam.lower()
  
  if strParam == strParam[::-1]:
    c = True
  

  return c

# keep this function call here 
print(StringChallenge(input()))