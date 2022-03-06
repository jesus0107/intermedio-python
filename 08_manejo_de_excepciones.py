def divisors(num):
  try:
    if num < 0:
      raise ValueError("Los numeros negativos no son validos")
    divisors = [divisor for divisor in range(1, num + 1) if num % divisor == 0]
    return divisors
  except ValueError as ve:
    print(ve)
    return False

def main():
  try:
    input_number = int(input("Porfavor ingresa un numero: ")) 
    number_divisors = divisors(input_number)
    return print(number_divisors)
  except ValueError:
    print("Porfavor ingresa un numero.")
    return False


if __name__ == "__main__":
  main()