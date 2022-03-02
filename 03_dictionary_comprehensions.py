#Crear un diccionario cuyas llaves sean los priemros 100 numeros naturales y sus valores sean esos numeros elevados al cubo

def main():
  my_dict = {n:n**3 for n in range(1, 11) if n % 3 != 0}

  # for i in range(1, 11):
  #   if i % 3 != 0:
  #     my_dict[i] = i**3
  
  # print(my_dict)

  #RETO
  #Crear con un dictionary comprehension, un diccionario cuyas llaves sean los 1000 primeros numeros naturasles con sus raices cuadradas como valores
  numbers_sqrt = {i:round(i**0.5, 3) for i in range(1,101)}
  print(numbers_sqrt)

if __name__ == "__main__":
  main()