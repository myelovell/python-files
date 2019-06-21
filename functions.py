# My E. Lovell 2019-03-02, lära mig funktioner, med hjälp av peter
def greet(name):
    print("hello " + name)

# greet("peter")
def plus20(var):
    var += 20
    return var

# print (float(plus20(20)))

def minus40(var):
    var -= plus20(20)

    return var

#print (minus40(300))

def greatest_dog(name):
    print ("the greatest dog is "+ name +"!!!!!")

greatest_dog("phoebe")
