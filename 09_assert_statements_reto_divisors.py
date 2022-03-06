def divisors(num):
  assert num > 0, "Los numeros negativos no son validos"
  divisors = [divisor for divisor in range(1, num + 1) if num % divisor == 0]
  return divisors
  # try:
  #   if num < 0:
  #     raise ValueError("Los numeros negativos no son validos")
  #   divisors = [divisor for divisor in range(1, num + 1) if num % divisor == 0]
  #   return divisors
  # except ValueError as ve:
  #   print(ve)
  #   return False

def main():
  # Para poder ejecutar la funcion isnumeric() eliminamos del input la funcion int
  # Convertimos a numero la variable input_number despues de haber sido validada dentro del assert para poder enviar el valor a la funcion
  input_number = input("Porfavor ingresa un numero: ")
  assert input_number.isnumeric(), "Porfavor ingresa un numero"
  input_number = int(input_number)
  number_divisors = divisors(input_number)
  return print(number_divisors)

  # try:
  #   input_number = int(input("Porfavor ingresa un numero: ")) 
  #   number_divisors = divisors(input_number)
  #   return print(number_divisors)
  # except ValueError:
  #   print("Porfavor ingresa un numero.")
  #   return False


if __name__ == "__main__":
  main()