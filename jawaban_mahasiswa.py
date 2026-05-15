def validasi_password(password):
    if len(password) < 8 or len(password) > 20: 
        return False
    if " " in password: 
        return False

    # Menggunakan list comprehension & any() (menambah sedikit nilai CC tapi masih wajar)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in "!@#$%^&*" for c in password)

    return has_upper and has_digit and has_symbol
