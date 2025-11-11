from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    conn = mysql.connector.connect(
        host="localhost",
        user="exampleuser",
        password="change_this_strong_password",
        database="exampledb"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT NOW()")  
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    return f"""
    <html>
        <head>
            <title>LEMP App</title>
            <style>
                body {{
                    background-color: black;
                    color: red;
                    font-family: 'Courier New', monospace;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }}
                .clock {{
                    font-size: 80px;
                }}
            </style>
        </head>
        <body>
            <div class="clock">{result[0]}</div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
