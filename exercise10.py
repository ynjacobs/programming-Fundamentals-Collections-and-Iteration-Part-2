students = {
    'cohort1': 34,
    'cohort2': 42,
    'cohort3': 22
}

for key, val in students.items():
  print("{}: {} students".format(key, val))

students['cohort4'] = 43