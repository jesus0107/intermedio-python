DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def main():
  all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
  all_platzi_devs = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
  filter_all_adult_devs = list(filter(lambda worker: worker['age'] > 18, DATA))
  filter_all_adult_devs = list(map(lambda worker: worker["name"], filter_all_adult_devs))
#   add_old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))


  filter_all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
  filter_all_python_devs = list(map(lambda worker: worker["name"], filter_all_python_devs))

  filter_all_platzi_devs = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
  filter_all_platzi_devs = list(map(lambda worker: worker["name"], filter_all_platzi_devs))

  all_adult_devs = [dev["name"] for dev in DATA if dev["age"] > 18]

  for worker in all_adult_devs:
    print(worker)  

  # print(all_python_devs)


if __name__ == "__main__":
  main()