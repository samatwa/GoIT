names=[{
     'name': 'Kennedy Lane', 
     'email': 'mattis.Cras@nonenimMauris.net', 
     'phone': '(542) 451-7038', 
     'favorite': False}, 
     {'name': 'Cyrus Jackson', 
      'email': 'nibh@semsempererat.com', 
      'phone': '(501) 472-5218', 
      'favorite': True}]
def get_favorites(contacts):
     return [i for i in filter(lambda i: i['favorite'], contacts)]

print(get_favorites(names))