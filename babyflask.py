from flask import Flask, render_template_string, url_for

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to the Coolest Website</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 0;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }
            button {
                background-color: #4caf50;
                border: none;
                color: white;
                padding: 1em 2em;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                transition-duration: 0.4s;
            }
            button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <a href="{{ url_for('hello_world') }}"><button>Enter the Coolest Website</button></a>
    </body>
    </html>
    """)

@app.route('/home')
def hello_world(): # HTML is from a ChatGPT prompt for the "coolest website".
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Coolest Website</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 0;
            }
            header {
                background-color: #1c1c1c;
                padding: 1em;
                text-align: center;
                font-size: 2em;
                color: white;
            }
            main {
                margin: 2em;
            }
            button {
                background-color: #4caf50;
                border: none;
                color: white;
                padding: 1em 2em;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                transition-duration: 0.4s;
            }
            button:hover {
                background-color: #45a049;
            }
        </style>
        <script>
            function toggleColor() {
                const body = document.querySelector('body');
                const currentColor = body.style.backgroundColor;
                body.style.backgroundColor = currentColor === 'white' ? '#f5f5f5' : 'white';
            }
        </script>
    </head>
    <body>
        <header>
            Coolest Website
        </header>
        <main>
            <p>Welcome to the coolest website you've ever seen! We have amazing content and features that will blow your mind.</p>
            <button onclick="toggleColor()">Toggle Background Color</button>
        </main>
    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run()
