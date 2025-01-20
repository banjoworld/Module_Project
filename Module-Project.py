from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simple Webpage</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
            }
            h1 {
                color: #3498db;
            }
            p {
                color: #2c3e50;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to My Simple Webpage!</h1>
        <p>This is a simple webpage created using Python and Flask.</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)