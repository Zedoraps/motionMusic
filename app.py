from flask import Flask

from manager import Manager

app = Flask(__name__)
manager = Manager()
manager.start_player()


@app.route('/status')
def status():
    print("status called")
    return manager.status()


def main():
    app.run()


if __name__ == "__main__":
    main()
