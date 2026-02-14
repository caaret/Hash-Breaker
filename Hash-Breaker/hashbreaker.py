import hashlib
import string
import itertools
from colorama import Fore, Style, init

init(autoreset=True)

def detect_hash_type(hash_value):
    hash_value = hash_value.strip().lower()
    length = len(hash_value)
    
    # Hash uzunluklarına göre tür haritası
    hash_map = {
        32: "md5",
        40: "sha1",
        56: "sha224",
        64: "sha256",
        96: "sha384",
        128: "sha512"
    }
    
    detected_type = hash_map.get(length)
    
    if detected_type:
        print(Fore.GREEN + f"[+] Tespit Edilen Tür: {detected_type.upper()}")
        return detected_type
    else:
        print(Fore.RED + "[!] Hash türü otomatik tespit edilemedi manuel biçimde girin.")
        return None

def crack_logic(target_hash, h_type, max_len):
    chars = string.ascii_lowercase + string.digits
    for length in range(1, max_len + 1):
        print(Fore.YELLOW + f"[*] {length} karakterli kombinasyonlar deneniyor...")
        for combo in itertools.product(chars, repeat=length):
            word = "".join(combo)
            hashed_try = hashlib.new(h_type, word.encode()).hexdigest()
            
            if hashed_try == target_hash:
                print(Fore.GREEN + Style.BRIGHT + f"\n[+!!] ŞİFRE BULDUN: {word}")
                return True
    return False

# --- ANA AKIŞ ---
print(Fore.CYAN + "--- HASH BREAKER ---")
user_hash = input("Kırılacak Hash'i girin: ").strip()

# Önce türü tahmin et
detected = detect_hash_type(user_hash)

if detected:
    confirm = input(f"Saldırı {detected.upper()} üzerinden başlatılsın mı? (E/H): ").lower()
    if confirm == 'e':
        max_l = int(input("Maksimum şifre uzunluğu: "))
        crack_logic(user_hash, detected, max_l)
    else:
        # Eğer kullanıcı "Hayır bu o değil" derse manuel seçtir
        manual_type = input("Lütfen türü manuel girin (md5, sha256 vb.): ").lower()
        max_l = int(input("Maksimum şifre uzunluğu: "))
        crack_logic(user_hash, manual_type, max_l)
else:
    print("Tür belirlenemediği için işleme devam edilemiyor.")