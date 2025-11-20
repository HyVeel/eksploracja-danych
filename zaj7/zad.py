import streamlit as st
import pandas as pd
import sqlite3
import time

"""
Stwórz aplikację webową w Streamlit, która:
1. Łączy się z bazą sales.db (SQLite) i wyświetla dane z tabeli sales.
2. Pozwala dodać nowy rekord sprzedaży (produkt, ilość, cena, data).
3. Wyświetla dane w tabeli (st.dataframe) z możliwością filtrowania po produkcie.
4. Pokazuje dwa wykresy:

	a) sprzedaż dzienna (wartość: ilość × cena),

	b) suma sprzedanych produktów wg typu.

Dodaj elementy interaktywne (selectbox, input, button, checkbox) oraz np. st.balloons().
"""

st.title("Monitor sprzedaży")

# Połączenie z bazą danych
conn = sqlite3.connect("streamlit/sales.db")
cursor = conn.cursor()

# Pobranie danych z tabeli sales
def load_data():
	with st.spinner("Ładowanie danych..."):
		time.sleep(1) # Symulacja opóźnienia
		query = "SELECT * FROM sales"
		df = pd.read_sql_query(query, conn)

		return df

data = load_data()

# Dodawanie nowego rekordu sprzedaży
st.subheader("Nowy rekord sprzedaży")
with st.form("add_sale_form"):
	product = st.text_input("Produkt:")
	quantity = st.number_input("Ilość:", min_value=1, step=1)
	price = st.number_input("Cena za sztukę:", min_value=0.01, step=0.01, format="%.2f")
	date = st.date_input("Data sprzedaży:", value=pd.to_datetime("today"), max_value=pd.to_datetime("today"))

	submitted = st.form_submit_button("Dodaj rekord")

	if submitted:
		cursor.execute("""
		INSERT INTO sales (product, quantity, price, date)
		VALUES (?, ?, ?, ?)
		""", (product, quantity, price, date.strftime("%Y-%m-%d")))

		conn.commit()
		st.success("Rekord został dodany!")
		st.balloons()

		# Odświeżenie danych
		data = load_data()

# Filtr po produkcie
products = data["product"].unique().tolist()
selected_products = []

for product in products:
	if st.checkbox(product, value=True):
		selected_products.append(product)

filtered_data = data[data["product"].isin(selected_products)]

# Tabela z danymi
st.subheader("Dane sprzedaży")
st.dataframe(filtered_data)
st.write(f"Liczba rekordów: {len(filtered_data)}")

# Wykresy
# a) Sprzedaż dzienna
st.subheader("Sprzedaż dzienna")
daily_sales = filtered_data.copy()
daily_sales["total"] = daily_sales["quantity"] * daily_sales["price"]
daily_summary = daily_sales.groupby("date")["total"].sum().reset_index()
st.line_chart(daily_summary.set_index("date")["total"])

# b) Suma sprzedanych produktów wg typu
st.subheader("Suma sprzedanych produktów wg typu")
product_summary = filtered_data.groupby("product")["quantity"].sum().reset_index()
st.bar_chart(product_summary.set_index("product")["quantity"])

# Zamknięcie połączenia z bazą danych przy zakończeniu aplikacji
conn.close()