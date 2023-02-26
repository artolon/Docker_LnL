from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_beluga():
    url = "https://greenglobaltravel.com/wp-content/uploads/2021/01/beluga-whale-1.jpg"
    return render_template("index.html", url=url)

if __name__ == "__main__":
    app.run()