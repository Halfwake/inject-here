import hashlib
from pprint import pprint

with open('words.txt') as f_obj:
    HASH_DICT = {}
    for word in f_obj.readlines():
        word = word.strip()
        HASH_DICT[word] = hashlib.sha512(word).hexdigest()

pprint(HASH_DICT)
