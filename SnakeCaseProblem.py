def SnakeCase(strParam):

  a = ["~","|","}","{","`","^","]","[","@","?",">","=","<",";",":","."," ","#","$","&","'",",", "*","/","-","+","%","&","!"]


  for i in a:
    strParam = strParam.replace(i,"_")
  
  strParam = strParam.lower()

  return strParam

# keep this function call here 
print SnakeCase(raw_input())