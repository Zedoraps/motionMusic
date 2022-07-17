from flask import Flask

from manager import Manager

app = Flask(__name__)
manager = Manager()
manager.start_player()


@app.route('/stop')
def stop():
    return manager.stop()


@app.route('/star')
def start():
    return manager.stop()


def main():
    app.run()


if __name__ == "__main__":
    main()
