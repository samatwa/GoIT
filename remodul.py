import re

text="Guido van Rossum began working on Python in the late 1980s, \
    as a successor to the ABC programming language, \
    and first released it in 1991 as Python 0.9.0."
word='python'

def find_word(text, word):
    d={}
    result=re.search(word,text)
    if result:
        d['result']=True
        d['first_index']=result.start()
        d['last_index']=result.end()
        d['search_string']=result[0]
        d['string']=result.string
    else:
        d['result']=False
        d['first_index']=None
        d['last_index']=None
        d['search_string']=word
        d['string']=text
    return d

print(find_word(text,word))
    