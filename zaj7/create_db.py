import sqlite3

# Połączenie z plikiem bazy danych (utworzy plik sales.db, jeśli nie istnieje)
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# Tworzenie tabeli (jeśli nie istnieje)
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    date TEXT NOT NULL
)
""")

# Przykładowe dane do wstawienia
sample_data = [
    ("Laptop", 2, 3200.50, "2025-05-01"),
    ("Monitor", 5, 800.00, "2025-05-02"),
    ("Mouse", 10, 50.00, "2025-05-02"),
    ("Keyboard", 7, 150.00, "2025-05-03"),
    ("Laptop", 1, 3100.00, "2025-05-03"),
    ("Monitor", 3, 850.00, "2025-05-04"),
    ("Mouse", 15, 55.00, "2025-05-04")
]

# Wstawianie danych do tabeli
cursor.executemany("""
INSERT INTO sales (product, quantity, price, date)
VALUES (?, ?, ?, ?)
""", sample_data)

# Zatwierdzenie zmian i zamknięcie połączenia
conn.commit()
conn.close()

print("Baza danych sales.db została utworzona i wypełniona przykładowymi danymi.")