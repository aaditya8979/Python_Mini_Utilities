import random
import string

def generate_password():
    l = string.ascii_lowercase
    u= string.ascii_uppercase
    d = string.digits
    s = "!@#$%^&*()_-+="

    random_chars = random.choices(l, k=random.randint(3,5)) + random.choices(u,k=random.randint(3,5)) + random.choices(d,k=random.randint(3,5)) + random.choices(s,k=random.randint(3,5))
    random.shuffle(random_chars)
    password = ''.join(random_chars)
    return password

if __name__ == "__main__":
    print("Generated Password:", generate_password())