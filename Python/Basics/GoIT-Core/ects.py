grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

def formatted_grades(students):
    new_list=[]
    number=1
    for i,j in students.items():
        for k,l in grades.items():
            if j==k:
                new_list.append(f"{number:>4}|{i:<10}|{k:^5}|{l:^5}")
        number+=1
    return new_list
for el in formatted_grades(students):
    print(el)
    
