d=[{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}]

def get_emails(list_contacts):
    return [i for i in map(lambda i:i["email"],list_contacts)]


print(get_emails(d))