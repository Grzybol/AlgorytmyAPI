from flask import Flask, request, send_file
from cryptography.fernet import Fernet
import os

app = Flask(__name__)

# Ścieżka do folderu przechowującego przesłane pliki
UPLOAD_FOLDER = '/AlgorytmyAPI/upload'
# Ścieżka do folderu, z którego będziemy pobierać pliki
DOWNLOAD_FOLDER = '/AlgorytmyAPI/download'
# Ścieżka do pliku z kluczem szyfrującym
KEY_FILE = '/AlgorytmyAPI/key.key'

# Wygenerowanie klucza szyfrującego, jeśli nie istnieje
def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as key_file:
            key_file.write(key)

# Wczytanie klucza szyfrującego
def load_key():
    return open(KEY_FILE, 'rb').read()

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        generate_key()
        key = load_key()
        file = request.files['file']
        
        if file:
            # Szyfrowanie przesłanego pliku
            f = Fernet(key)
            encrypted_data = f.encrypt(file.read())
            
            # Zapisanie zaszyfrowanego pliku
            encrypted_filename = os.path.join(UPLOAD_FOLDER, file.filename + ".enc")
            with open(encrypted_filename, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)
            
            return 'Plik został przesłany i zaszyfrowany.'
        return 'Nie wybrano pliku.'
    except Exception as e:
        return 'Wystąpił błąd podczas przesyłania i zapisywania pliku: ' + str(e)

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        generate_key()
        key = load_key()
        
        # Odszyfrowanie pliku
        encrypted_filename = os.path.join(UPLOAD_FOLDER, filename)
        with open(encrypted_filename, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
            f = Fernet(key)
            decrypted_data = f.decrypt(encrypted_data)
        
        # Zapisanie odszyfrowanego pliku
        decrypted_filename = os.path.join(DOWNLOAD_FOLDER, filename[:-4])
        with open(decrypted_filename, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)
        
        return send_file(decrypted_filename, as_attachment=True)
    except Exception as e:
        return 'Wystąpił błąd podczas pobierania i odszyfrowywania pliku: ' + str(e)

if __name__ == '__main__':
    app.run(debug=True)
