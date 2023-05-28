from src import create_app


app = create_app()


@app.route("/")
def hello_world():
    return "hello world"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
