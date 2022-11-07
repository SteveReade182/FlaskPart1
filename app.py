from flask import Flask, Response, request, url_for
# flask is the module that Flask class is coming from

app = Flask(__name__)


@app.route('/')
def hello_from_flask():
    return "Hello from Flask!"


@app.route('/get/text')
def get_text():
    return Response("Hello from Flask using an explicit Response object", mimetype='text/plain')


@app.route('/post/text', methods=['POST'])
def post_text():
    data_sent = request.data.decode('utf-8')
    return Response("You posted this data to the Flask app: " + data_sent, mimetype='text/plain')


@app.route('/dynamic/<word>')
def dynamic(word):
    return "You said..."+word


@app.route('/activity/<name>')
def activity(name):
    return "Hello: "+name


@app.route('/square/<int:number>')
def square(number):
    squared = number ** 2
    line = "Your number squared is " + str(squared)
    return line


@app.route('/sayhello/<name>')
def say_hello_page(name):
    return """
    <html>
    <head>
        <title>Sample Flask Webpage</title>
    </head>
    <body>
        <h1>Name Page</h1>
        <p>Hello {}!</p>
        <hr>
        <p>Goodbye!</p>
    </body>
    </html>
    """.format(name)


@app.route('/activity_two/<name>/<int:age>')
def activity_two(name, age):
    url = url_for('get_text')
    return """
    <html>
    <head>
        <title>Sample Flask Webpage</title>
    </head>
    <body>
        <h1>Name Page</h1>
        <p>Hello {}!</p>
        <p>You are {} year(s) old.</p>
        <hr>
        <a href="{}">Welcome</a>
        <hr>
        <p>Goodbye!</p>
    </body>
    </html>
    """.format(name, age, url)


if __name__ == "__main__":
    app.run(debug=True)

# git test to make sure thinks commit correctly - this should only be on dev branch!
