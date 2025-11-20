import sqlite3

# Połączenie z istniejącą bazą danych
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# Więcej przykładowych danych
sample_data = [
    ("Mouse", 20, 45.00, "2025-05-05"),
    ("Laptop", 1, 2999.00, "2025-05-05"),
    ("Keyboard", 10, 140.00, "2025-05-06"),
    ("Monitor", 2, 870.00, "2025-05-06"),
    ("Laptop", 3, 3300.00, "2025-05-07"),
    ("Mouse", 5, 49.99, "2025-05-07"),
    ("Keyboard", 1, 135.00, "2025-05-07"),
    ("Laptop", 4, 3150.00, "2025-05-08"),
    ("Monitor", 7, 820.00, "2025-05-08"),
    ("Mouse", 12, 48.00, "2025-05-08"),
    ("Laptop", 2, 3050.00, "2025-05-09"),
    ("Keyboard", 6, 145.00, "2025-05-09"),
    ("Monitor", 4, 810.00, "2025-05-09"),
    ("Mouse", 18, 50.00, "2025-05-09"),
    ("Laptop", 1, 2990.00, "2025-05-10"),
    ("Monitor", 3, 840.00, "2025-05-10")
]

# Wstawienie dodatkowych danych
cursor.executemany("""
INSERT INTO sales (product, quantity, price, date)
VALUES (?, ?, ?, ?)
""", sample_data)

# Zatwierdzenie i zamknięcie
conn.commit()
conn.close()

print("Dodatkowe dane zostały pomyślnie dodane do bazy sales.db.")