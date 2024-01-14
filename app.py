from flask import Flask, send_file

app = Flask(__name__)

# Funkcja do obsługi przesyłania plików
@app.route('/upload', methods=['POST'])
def upload_file():
    # Obsługa przesyłanego pliku
    # ...
    return 'Plik został przesłany pomyślnie'

# Funkcja do obsługi pobierania plików
@app.route('/download/<file_code>', methods=['GET'])
def download_file(file_code):
    # Logika pobierania pliku na podstawie kodu pliku (file_code)
    # Przykład: file_path = znajdź_sciezke_pliku_na_podstawie_kodu(file_code)

    # Wysłanie pliku do klienta
    # W przykładzie załóżmy, że file_path wskazuje na plik do pobrania
    return send_file(file_path, as_attachment=True)

# Funkcja do obsługi strony głównej
@app.route('/')
def index():
    return open('index.html').read()

if __name__ == '__main__':
    app.run()
