def generate_password (length):
  charecters = numerals + letters + Capital_letters + signs
  numerals = [1,2,3,4,5,6,7,8,9]
  letters = ["a","b","c","d","e","f","g","h","i","j"]
  Capital_letters = ["A","B","C","D","E","F","G","H","I","J"]
  signs = ["!","@","#","$","%","^","&","*","_","+","="]
  password = ''.join(random.choice(charecters) for _ in range (length))
  return password
  password_length = int(input("Введите желаемую длину пароля: "))
  generated_password = generate_password(password_length)
  print("Ваш сгенерированный пароль:",generated_password)
