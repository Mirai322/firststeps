def stroki(one,two):
    if isinstance(one,str) and isinstance(two,str):
        if one == two:
            result=1
        elif len(one.lower()) > len(two.lower()):
            result=2
        elif (one.lower() != two.lower()) and (two == "learn"):
            result=3
        else :
            result = "Vtoraya dlinee, no eto ne tochno"
    else :
        result=0
    return(result)
#str1 = input ("str1: ")
#str2 = input ("str2: ")
#a = stroki(str1,str2)
#print(a)
print(stroki(5,"pro"))
print(stroki("vas","learn"))
print(stroki("vas","ssslearn"))