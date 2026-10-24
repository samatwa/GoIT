source_file=r'C:\Users\samat\.vscode\python\test.txt'
output_file=r'C:\Users\samat\.vscode\python\test1.txt'


def to_indexed(source_file, output_file):
    with open(source_file,'r') as source,open(output_file,'w') as output:
        text=source.readlines()
        for i,j in enumerate(text):
            k=f'{i}: {j}'
            output.write(k)

to_indexed(source_file,output_file)

