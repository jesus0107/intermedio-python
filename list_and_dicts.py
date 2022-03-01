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
  print("Imprimiendo superlista")
  for key in super_list:
    print(key)
if __name__ == "__main__":
  main()