def divisors(num):
  # divisors = [divisor for divisor in range(1, num + 1) if num % divisor == 0]
  divisors = []
  for i in range(1, num+1):
    if num % i == 1:
      divisors.append(i)
  return divisors

def main():
  number = int(input("Porfavor ingresa un numero: "))
  number_divisors = divisors(number)
  print(number_divisors)


if __name__ == "__main__":
  main()