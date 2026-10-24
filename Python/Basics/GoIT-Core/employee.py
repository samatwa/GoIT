path=r'C:\Users\samat\.vscode\python\test.txt'
def get_employees_by_profession(path, profession):
    with open(path,'r') as file:
        lines=file.readlines()
        employee=[]
        for line in lines:
            if line.find(profession)>0:
                employee.append(line.strip())
        string="".join(employee).replace(profession,'').strip()

    return string

        

print(get_employees_by_profession(path,'cook'))