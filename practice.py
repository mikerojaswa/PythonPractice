def main():
  n = input("Please enter a number")
  print(is_prime(n))

def is_prime(a):
  x = True
  for i in range(2,a):
    if(a%i == 0):
      x = False
      break
  return x



main()