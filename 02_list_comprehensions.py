#una lista de los primeros 10 numeros natuarales al cuadrado

def run():
  # Creams una lista  de el cuadrado de los numeros entre el 1 y el 10

  # for i in range(1,11):
  #   squared_number = i**2
  #   squares.append(squared_number)
  
  #misma lista pero con list comprehension
  # squares = [i**2 for i in range(1, 101) if i % 3 != 0]
  # print(squares)
  # print(squares)


  # RETO
  # Crear con list comprehension una lista de todos los moultiplos de 4 que a la vez tambien sean multiplos de 6 y 8 hasta 5 digitos
  numbers = [number for number in range(1, 100000) if number % 4 == 0 and number % 6 == 0 and number % 9 == 0 ]
  print(numbers)

if __name__ == '__main__':
  run()