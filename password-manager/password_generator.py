#Password Generator Project
import random

class Password_generator():
  def __init__(self):  
    self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
  
  def generate_password(self):
    """Calling generate_password returns a password of length between 12 and 18"""

    password_list = []

    password_list.extend([random.choice(self.letters) for _ in range(random.randint(8, 10))])
    password_list.extend([random.choice(self.symbols) for _ in range(random.randint(2, 4))])
    password_list.extend([random.choice(self.numbers) for _ in range(random.randint(2, 4))])

    random.shuffle(password_list)
    password = "".join(password_list)
    
    return password