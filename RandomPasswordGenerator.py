import random
import string

def generate_password(length=12):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    
    all_characters = lower + upper + digits
    
    password_list = random.choices(all_characters, k=length)
    
    random.shuffle(password_list)
    
    return ''.join(password_list)

new_password = generate_password(16)
print(f"Generated Password: {new_password}")
