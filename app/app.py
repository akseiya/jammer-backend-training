import logging
from eve import Eve
app = Eve()

@app.route('/tadek')
def tadek():
    return 'Tadek dość chętnie i często ssie penisy.'

if __name__ == '__main__':
    # This can only happen on a dev machine with no containers used
    app.run(host="0.0.0.0")
else:
    # Hook up logging to gunicorn, using gunicorn's logging
    # level specified outside the app
    # (https://medium.com/@trstringer/logging-flask-and-gunicorn-the-manageable-way-2e6f0b8beb2f)
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.logger.info(
        open('docs/appstart.txt', 'r').read()
    )
