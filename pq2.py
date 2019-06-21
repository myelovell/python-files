import math
print("du använder pq-formeln där x^2+px+q=0")

p = float(input("vilket är ditt p värde?"))
q = float(input("vilket är ditt q värde?"))

if (p/2)**2 < q:
  print("vafan du kan inte ha ett p värde som är mindre än q!!!!")
  
print("detta är dina tal", p ,q)

print("nu räknar vi ut vad x är med denna formel x = -p/2 +/- math.sqrt((p/2)^2) - q")

x1= -(p/2) + math.sqrt((p/2)**2 - q)
x2= -(p/2) - math.sqrt((p/2)**2 - q)

print("x1 = ", x1)
print("x2 = ", x2)