def write():
  names = ["jesus", "Martha", "Anahi"]
  with open("./archivo/names.txt", "w", encoding="utf-8") as file:
    for name in names:
      file.write(name + "\n")

def read():
  numbers = []
  with open("./archivos/numbers.txt", "r", encoding="utf-8") as file:
    for line in file:
      numbers.append(int(line))
  return print(numbers)

def run():
  write()  


if __name__ == "__main__":
  run()