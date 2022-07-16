from flask import Flask

from manager import Manager

app = Flask(__name__)
manager = Manager()


@app.route('/start')
def index():
    return manager.start_player()


def main():
    app.run()


if __name__ == "__main__":
    main()
