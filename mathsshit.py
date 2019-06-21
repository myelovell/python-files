# My E. Lovell 2019-03-13, just maths

def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print "%d squared is %d." % (n, squared)
  return squared

#-----

  def power(base, exponent):
    result = base ** exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

#-----

    def cube(number):
  return number * number * number

#-----

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False

#-----
