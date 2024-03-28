import shutil

employee_residence={'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}
file_name='test.py'
#path 
def create_backup(path, file_name, employee_residence):
    full_path = f"{path}/{file_name}"
    with open(full_path, 'wb') as file_name:
        for i,j in employee_residence.items():
            s=f'{i} {j}\n'
            s=s.encode()
            file_name.write(s)

    arc=shutil.make_archive('backup_folder','zip','folder')  

    return arc       
