phone="   (050)123-32-34"

def format_phone_number(func):
    def inner(phone):
        new_phone=func(phone)
        if new_phone.startswith('3'):
            new_phone = '+' + new_phone
        elif new_phone.startswith('0'):
            new_phone = '+38' + new_phone
        return new_phone  
    return inner 
        
        
@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone

print(sanitize_phone_number(phone))