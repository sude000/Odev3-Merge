import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """
    Belirtilen kriterlere göre rastgele bir şifre oluşturur.
    
    Parametreler:
    - length: Şifre uzunluğu (varsayılan 12)
    - use_upper: Büyük harf kullanımı (varsayılan True)
    - use_lower: Küçük harf kullanımı (varsayılan True)
    - use_digits: Rakam kullanımı (varsayılan True)
    - use_special: Özel karakter kullanımı (varsayılan True)
    """
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("En az bir karakter türü seçmelisiniz!")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
