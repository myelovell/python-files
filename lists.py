# My E. Lovell 2019-03-07, övar på att skriva listor

numbers = [1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ,10]
strings = ["no one", "everyone", "anyone", "enemy"]

print (numbers[::2])
print (strings)

x = object()
y = object()

x_list = [x, x, x, x, x, x, x, x, x, x]
y_list = [y, y, y, y, y, y, y, y, y, y]
big_list = x_list + y_list

print ("x list contains ", len(x_list), " objects")
print ("y list contains ", len(x_list), " objects")
print ("big list contains ", len(big_list), " objects")

#-----

my_list = [1,9,3,8,5,7]

for number in my_list:
  print 2 * number

#-------

start_list = [5, 3, 1, 2, 4]
square_list = []

for x in start_list:
  square_list.append(x**2)
square_list.sort()

print square_list

#-----

shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

def compute_bill(food):
  total = 0
  for item in food:
    total = total + prices[item]
  return total

#-----
