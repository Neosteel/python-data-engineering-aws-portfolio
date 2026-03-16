#  find subsrting in list of strings fin

print("hello world")

stringlist = ["hello", "i love you fatty", "cutie pie", "hotty", "beauty"]


userinput = input("enter substring needed : ")
def findsubstring(stringlist) : 
    res = []
    for r in stringlist:
      if userinput in r:
         res.append(r)
    return res                




result = findsubstring(stringlist)
print(result)
    
            

                
            