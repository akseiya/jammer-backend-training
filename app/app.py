from eve import Eve
app = Eve()

@app.route('/tadek')
def tadek():
    return 'Tadek dość chętnie i często ssie penisy.'

# This is not actually run really, since we want Gunicorn to reload
# changing dev code, while eve/flask itself is not supposed to be
# used for deployed code.

if __name__ == '__main__':
    app.run(host="0.0.0.0")
