# data.py

# Encabezado estándar para enviar solicitudes JSON
headers = {
    "Content-Type": "application/json"
}

# Cuerpo válido para crear un kit (se puede agregar el campo cardId si es necesario)
valid_kit_body = {
    "name": "Mi conjunto"
}

# Cuerpo inválido (falta 'name' y 'cardId' o token)
empty_body = {}

# Cuerpo con nombre inválido (para prueba de validación)
invalid_name_body = {
    "name": "123@#"
}

# Cuerpo con nombre demasiado corto
short_name_body = {
    "name": "A"
}

# Cuerpo con nombre demasiado largo
long_name_body = {
    "name": "NombreMuyLargoParaKit"
}

# Cuerpo con caracteres no permitidos
special_char_name_body = {
    "name": "Kit@Nombre!"
}

# Ejemplo con cardId explícito (cuando no se usa Authorization)
kit_with_card_id = {
    "name": "Kit para tarjeta",
    "cardId": 1
}
