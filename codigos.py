# Abre el archivo rockyou.txt y procesa las contraseñas
with open("rockyou.txt", "r", errors="ignore") as f:
    passwords = f.read().splitlines()

# Filtra y modifica las contraseñas
filtered_passwords = []
for password in passwords:
    if password and password[0].isalpha():
        modified_password = password[0].upper() + password[1:] + "0"
        filtered_passwords.append(modified_password)

# Guarda las contraseñas filtradas y modificadas en un nuevo archivo
with open("passwords_filtered_and_modified.txt", "w") as f:
    for password in filtered_passwords:
        f.write(password + "\n")

print("Proceso completado. Las contraseñas que comienzan con letras han sido modificadas y guardadas en passwords_filtered_and_modified.txt")