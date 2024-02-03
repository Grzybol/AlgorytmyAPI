# Dokumentacja techniczna projektu

## index.py - Plik serwera Flask

### Opis
Plik `index.py` jest głównym plikiem serwera stworzonego przy użyciu frameworku Flask. Serwer obsługuje przesyłanie, pobieranie i usuwanie zaszyfrowanych plików.

### Endpointy

1. `/` (Strona główna):
   - Endpoint odpowiada za wyświetlanie strony głównej, która zawiera interfejs użytkownika.

2. `/upload` (Metoda POST):
   - Endpoint obsługuje przesyłanie plików na serwer. Pliki są szyfrowane za pomocą klucza, a następnie zapisywane na serwerze.

3. `/download/<file_id>` (Metoda GET):
   - Endpoint pozwala na pobieranie zaszyfrowanych plików na podstawie ich identyfikatora. Pliki są deszyfrowane i zwracane jako odpowiedź HTTP.

4. `/delete/<file_id>` (Metoda POST):
   - Endpoint umożliwia usuwanie zaszyfrowanych i deszyfrowanych plików na podstawie ich identyfikatora.

### Funkcje pomocnicze:
- `load_key()`: Funkcja wczytuje klucz szyfrujący z pliku 'key.key' lub generuje go, jeśli nie istnieje.
- `generate_key()`: Funkcja generuje klucz szyfrujący i zapisuje go do pliku 'key.key'.
- `read_encrypted_file(file_id)`: Funkcja wczytuje zaszyfrowany plik na podstawie jego identyfikatora.
- `write_encrypted_file(file_id, data)`: Funkcja zapisuje zaszyfrowany plik na serwerze.
- `save_decrypted_file(file_id, data)`: Funkcja zapisuje zdeszyfrowany plik na serwerze.
- `delete_encrypted_file(file_id)`: Funkcja usuwa zaszyfrowany plik na podstawie jego identyfikatora.
- `delete_decrypted_file(file_id)`: Funkcja usuwa zdeszyfrowany plik na podstawie jego identyfikatora.

## index.html - Szablon strony internetowej

### Opis
Plik `index.html` to szablon strony internetowej, która stanowi interfejs użytkownika do przesyłania, pobierania i usuwania zaszyfrowanych plików na serwerze.

### Elementy interfejsu:

1. Przesyłanie pliku:
   - Pole wyboru pliku.
   - Przycisk "Wyślij plik".
   - Pole tekstowe do wyświetlania komunikatów.

2. Pobieranie pliku:
   - Pole tekstowe do wprowadzania kodu zaszyfrowanego pliku.
   - Przycisk "Pobierz plik".

3. Usuwanie pliku:
   - Pole tekstowe do wprowadzania kodu zaszyfrowanego pliku.
   - Przycisk "Usuń plik".

### Skrypty JavaScript:
- `uploadFile()`: Funkcja obsługuje przesyłanie pliku na serwer i wyświetla odpowiedzi od serwera.
- `downloadFile()`: Funkcja obsługuje pobieranie pliku z serwera na podstawie kodu zaszyfrowanego pliku.
