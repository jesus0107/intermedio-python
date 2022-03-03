
from functools import reduce

def main():

  my_first_list = [1,4,5,6,9,13,19,21]
  odd = list(filter(lambda x: x % 2 != 0,my_first_list))
  print(odd)

  my_list = [1,2,3,4,5]
  squares = list(map(lambda n: n**2, my_list))
  # squares = [i**2 for i in list]
  print(squares)

  my_list_2 = [2,2,2,2,2]
  reduce_my_list = reduce(lambda x,z: x*z, my_list_2)
  print(reduce_my_list)


if __name__ == "__main__":
  main()