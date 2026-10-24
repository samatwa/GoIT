import re

def replace_spam_words(text, spam_words):
    new_text=text
    for spam_word in spam_words:
        long_spam='*'*len(spam_word)
        new_text = re.sub(re.escape(spam_word),long_spam,new_text,flags=re.IGNORECASE)
    return new_text

    
        