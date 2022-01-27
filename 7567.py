shape=input()
height =10
if shape.startswith(")")==True:
   before = ")"
else:
   before = "("
for i in range(len(shape)-1):
   if shape.startswith(before +"(")==True:
      before += "("
   else:
      before += ")"
   if before.endswith("((")==True:
      height +=5
   elif before.endswith("))")==True:
      height +=5
   else:
      height +=10
print(height)
