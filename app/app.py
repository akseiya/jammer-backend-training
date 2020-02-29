from eve import Eve
app = Eve()

@app.route('/tadek')
def tadek():
    return 'Tadek chętnie i często ssie penisy.'

if __name__ == '__main__':
    app.run(host="0.0.0.0")
