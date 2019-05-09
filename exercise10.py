from collections import defaultdict
students = {
    'cohort1': 34,
    'cohort2': 42,
    'cohort3': 22
}

for key, val in students.items():
  print("{}: {} students".format(key, val))

students['cohort4'] = 43

for key, val in students.items():
  students[key] *= 1.05

print(students)


print(students.keys()) 



# students.pop('cohort2')
# print(students)



