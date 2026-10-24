source='test.txt'
output='new_test.txt'

def sanitize_file(source, output):
    with open(source, 'r') as s_file, open(output, 'w') as o_file:
        for line in s_file:
            sanitized_line = ''.join(char for char in line if not char.isdigit())
            o_file.write(sanitized_line)

print(sanitize_file(source,output))
            
    
        
            
    
    
        
            
    
        
