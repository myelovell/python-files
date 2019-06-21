# My E. Lovell 2019-02-20, andragradsfunktionslösare med imaginära tal
print("WHEN")

# Testa om ert program kan lösa x^2+4x+5=0, förmodligen klarar den inte det. Kopiera din kod och utvidga den så den kan lösa ekvationer med komplexa rötter (med "i").
# Tips: Koden behöver kolla så att du inte försöker ta roten ur ett negativt tal. Använd if-sats. Se exempel ovan.

import math
print("du använder pq-formeln där x^2+px+q=0")
print("om p värdet är mindre än q värdet får man ett imaginärt tal\n")

p = float(input("vilket är ditt p värde?\n"))
q = float(input("vilket är ditt q värde?\n"))

print("detta är dina tal", p ,q)

print("\nnu räknar vi ut vad x är med denna formel x = -p/2 +/- math.sqrt((p/2)^2) - q")

if (p/2)**2>=q:
    x1= -(p/2) + math.sqrt((p/2)**2 - q)
    x2= -(p/2)- math.sqrt((p/2)**2 - q)
    print("x1 = ", x1)
    print("x2 = ", x2)

elif (p/2)**2<=q:
    reelt_tal= str(-(p/2))
    imaginärt_tal= math.sqrt(((p/2)**2 - q)*-1)

    print("x1 = ", reelt_tal, "+ ", imaginärt_tal, "i")
    print("x2 = ", reelt_tal, "- ", imaginärt_tal, "i")
