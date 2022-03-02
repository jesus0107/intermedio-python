def main():
  my_list = ["Jesus", True, 28, 1.75]
  my_dict = {"name": "Jesus", "last_name": "Cruz"}

  super_list = [
    {"firstname": "Jesus", "lastname": "Cruz"},
    {"firstname": "martha", "lastname": "Estudillo"},
    {"firstname": "anahi", "lastname": "Cruz"},
  ]
  super_dict = {
    "naturalnums": [1,2,3,4,5],
    "floatnums": [1.1,2.1,3.87]
  }

  print("Imprimiendo super diccionario")
  for key, value in super_dict.items():
    print(f"Clave: {key}, Valor: {value}")

#Recorriendo una lista de diccionarios
#primero corremos un for sobre la lista aislando cada unos de los diccionarios dentro de la variable dicts
#Recorreremos cada dict(diccionario) de la manera comun con la se recorren los diccionarios, accediendo a llave, valor por medio de la funcion items()
  print("Imprimiendo superlista")
  for dicts in super_list:
    for name, value in dicts.items():
      print(name, value )


if __name__ == "__main__":
  main()