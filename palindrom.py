name=input("enter the number:")
length=len(name)
var=""
i=-1
while i>=-length:
    var+=name[i]
    i-=1
if name==var:
    print(var,"=","it is palindrom")
else:
    print(var,"=","it'not palindrom")