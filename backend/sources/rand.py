import random
import string

def id_generator(size, chars = string.digits):
    a = ''.join(random.choice(chars) for _ in range(size))
    a = '1' + a
    return a

def str_generator(size, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    a = ''.join(random.choice(chars) for _ in range(size))
    return a