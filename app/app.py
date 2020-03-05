# import class library logging
import logging
# import class Eve from library eve
from eve import Eve
# create object app - instance of Eve
app = Eve()
# decorator

# dekorator - czyli opakowanie funkcji w cos dodatkowego
# .route - jest to metoda klasy Flask - która jest nadrzędną dla klasy Eve
# czyli Eve dziedziczy po Flask (inherits)
# wywoluje metode chuj z parametrem test
# app.chuj('test')
# wywoluje metode chuj z wynikiem funkcji tadek jako parametr
# app.chuj(tadek())

# !!! DEKORATOR !!!
# @ oznacza dekorator - czyli metoda chuj obiektu app staje sie wrapperem dla funkcji zdefiniowanej bezposrednio za nia
#@app.chuj('/tadek')
# Function tadek - simple function that return string
#def tadek():
#    return 'Tadek dość chętnie i często ssie penisy.'

# zebys mogl uzyc @ przed wywolaniem metody, metoda musi byc specjalnie napisana - jako dekorator/wrapper 
@app.route('/cokolwiek')

# Function tadek - simple function that return string
def tadek(a as string):
#   return 'Tadek dość chętnie i często ssie penisy.'
    return a

# wrapper - funkcja, ktora robi cos z wynikami innej funkcji
print(tadek())

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
