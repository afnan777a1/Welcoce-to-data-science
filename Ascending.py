import numpy as np

data_type = [
    ('name', 'S15'),
    ('class', int),
    ('height', float)
    
]
students_details = [
    ('James', 5, 48.5),
    ('Nail', 5, 52.5),
    ('Paul', 5, 42.10),
    ('pit', 5, 40.11)
    
]

students = np.array(students_details, dtype=data_type)

print("Original array:")
print(students)

print()

print("Sort by height")
print(np.sort(students, order='height'))