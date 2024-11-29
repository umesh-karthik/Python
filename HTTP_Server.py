from flask import Flask, render_template_string

app = Flask(__name__)

# pythonanywhere.com


@app.route('/')
def home():
    return render_template_string("""
        <html>
        <head>
            <title>Welcome to the Python Server</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #e0f7fa; }
                h1 { color: #333; }
                p { color: #555; }
                .container { max-width: 800px; margin: auto; background: white; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
                a { color: #1a73e8; text-decoration: none; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to the Python Server</h1>
                <p>Explore the pages to learn more about Python!</p>
                <ul>
                    <li><a href="/about">About Python</a></li>
                    <li><a href="/features">Key Features of Python</a></li>
                    <li><a href="/getting-started">Getting Started with Python</a></li>
                    <li><a href="/libraries">Popular Python Libraries</a></li>
                    <li><a href="/ides">Best IDEs for Python</a></li>
                    <li><a href="/tutorials">Python Tutorials</a></li>
                    <li><a href="/community">Python Community</a></li>
                    <li><a href="/projects">Python Project Ideas</a></li>
                </ul>
            </div>
        </body>
        </html>
    """)

@app.route('/about')
def about():
    return render_template_string("""
        <html>
        <head>
            <title>About Python</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #e0f7fa; }
                h1 { color: #333; }
                p { color: #555; }
                .container { max-width: 800px; margin: auto; background: white; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
                a { color: #1a73e8; text-decoration: none; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>About Python</h1>
                <p>Python is a high-level, interpreted programming language known for its clear syntax and readability. It was created by Guido van Rossum and first released in 1991. Python is popular for its versatility, and it is used for web development, data analysis, artificial intelligence, scientific computing, and more.</p>
                <a href="/">Back to Home</a>
            </div>
        </body>
        </html>
    """)

@app.route('/features')
def features():
    return render_template_string("""
        <html>
        <head>
            <title>Key Features of Python</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #e0f7fa; }
                h1 { color: #333; }
                ul { color: #555; }
                .container { max-width: 800px; margin: auto; background: white; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
                a { color: #1a73e8; text-decoration: none; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Key Features of Python</h1>
                <ul>
                    <li>Easy to learn and use</li>
                    <li>Extensive libraries and frameworks</li>
                    <li>Supports multiple programming paradigms (procedural, object-oriented, functional)</li>
                    <li>Cross-platform compatibility</li>
                    <li>Strong community support</li>
                </ul>
                <a href="/">Back to Home</a>
            </div>
        </body>
        </html>
    """)

@app.route('/getting-started')
def getting_started():
    return render_template_string("""
        <html>
        <head>
            <title>Getting Started with Python</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #e0f7fa; }
                h1 { color: #333; }
                pre { background: #eee; padding: 10px; border-radius: 5px; }
                .container { max-width: 800px; margin: auto; background: white; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
                a { color: #1a73e8; text-decoration: none; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Getting Started with Python</h1>
                <ol>
                    <li>Download Python from <a href="https://www.python.org/downloads/">python.org</a></li>
                    <li>Install Python on your machine</li>
                    <li>Write your first Python program:</li>
                    <pre><code>print("Hello, World!")</code></pre>
                    <li>Run your program in a terminal or command prompt</li>
                </ol>
                <a href="/">Back to Home</a>
            </div>
        </body>
        </html>
    """)

@app.route('/libraries')
def libraries():
    return render_template_string("""
        <html>
        <head>
            <title>Popular Python Libraries</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #e0f7fa; }
                h1 { color: #333; }
                ul { color: #555; }
                .container { max-width: 800px; margin: auto; background: white; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
                a { color: #1a73e8; text-decoration: none; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Popular Python Libraries</h1>
                <ul>
                    <li><strong>NumPy:</strong> Used for numerical and matrix operations</li>
                    <li><strong>Pandas:</strong> Data analysis and manipulation</li>
                    <li><strong>Matplotlib:</strong> Plotting and visualization</li>
                    <li><strong>Flask:</strong> Web development framework</li>
                    <li><strong>TensorFlow:</strong> Machine learning library</li>
                </ul>
                <a href="/">Back to Home</a>
            </div>
        </body>
        </html>
    """)

@app.route('/ides')
def ides():
    return render_template_string("""
        <html>
        <head>
            <title>Best IDEs for Python</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #e0f7fa; }
                h1 { color: #333; }
                ul { color: #555; }
                .container { max-width: 800px; margin: auto; background: white; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
                a { color: #1a73e8; text-decoration: none; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Best IDEs for Python</h1>
                <ul>
                    <li><strong>PyCharm:</strong> Full-featured IDE for Python</li>
                    <li><strong>VSCode:</strong> Lightweight, customizable editor</li>
                    <li><strong>Jupyter:</strong> Best for data science and notebooks</li>
                    <li><strong>Spyder:</strong> Great for scientific computing</li>
                </ul>
                <a href="/">Back to Home</a>
            </div>
        </body>
        </html>
    """)

@app.route('/tutorials')
def tutorials():
    return render_template_string("""
        <html>
        <head>
            <title>Python Tutorials</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #e0f7fa; }
                h1 { color: #333; }
                ul { color: #555; }
                .container { max-width: 800px; margin: auto; background: white; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
                a { color: #1a73e8; text-decoration: none; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Python Tutorials</h1>
                <ul>
                    <li><a href="https://www.w3schools.com/python/">W3Schools Python Tutorial</a></li>
                    <li><a href="https://www.learnpython.org/">LearnPython.org</a></li>
                    <li><a href="https://realpython.com/">Real Python</a></li>
                    <li><a href="https://www.codecademy.com/learn/learn-python-3">Codecademy Python Course</a></li>
                </ul>
                <a href="/">Back to Home</a>
            </div>
        </body>
        </html>
    """)

@app.route('/community')
def community():
    return render_template_string("""
        <html>
        <head>
            <title>Python Community</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #e0f7fa; }
                h1 { color: #333; }
                ul { color: #555; }
                .container { max-width: 800px; margin: auto; background: white; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
                a { color: #1a73e8; text-decoration: none; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Python Community</h1>
                <ul>
                    <li><a href="https://www.python.org/community/">Official Python Community</a></li>
                    <li><a href="https://www.reddit.com/r/Python/">Python on Reddit</a></li>
                    <li><a href="https://www.python.org/psf/">Python Software Foundation</a></li>
                </ul>
                <a href="/">Back to Home</a>
            </div>
        </body>
        </html>
    """)

@app.route('/projects')
def projects():
    return render_template_string("""
        <html>
        <head>
            <title>Python Project Ideas</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #e0f7fa; }
                h1 { color: #333; }
                ul { color: #555; }
                .container { max-width: 800px; margin: auto; background: white; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
                a { color: #1a73e8; text-decoration: none; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Python Project Ideas</h1>
                <ul>
                    <li>Build a simple calculator</li>
                    <li>Create a to-do list application</li>
                    <li>Develop a weather application using an API</li>
                    <li>Build a personal website using Flask</li>
                    <li>Develop a simple game (like Tic-Tac-Toe)</li>
                </ul>
                <a href="/">Back to Home</a>
            </div>
        </body>
        </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
