import pyodbc
from flask import Flask, request, render_template

app = Flask(__name__)

# Définissez les informations de connexion à la base de données
server = 'reservation-server.database.windows.net'
database = 'reservation-bd'
username = 'adminroot'
password = 'ReservationH3'
SQL_QUERY = """
INSERT INTO emails (email) VALUES (?)", email
"""

@app.route('/', methods=['GET', 'POST'])
def formulaire_reservation():
    if request.method == 'POST':
        email = request.form.get('email')
        connectionString = pyodbc.connect(f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
        conn = pyodbc.connect(conn)
        cursor = conn.cursor()
        cursor.execute(SQL_QUERY)

    return render_template('formulaire_reservation.html')

if __name__ == '__main__':
    app.run(debug=True)
