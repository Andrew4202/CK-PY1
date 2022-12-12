import random
import string
def get_random_password() -> str:
    a = string.digits + string.ascii_letters
    b = "".join(random.sample(a,8))
    return b


print(get_random_password())
