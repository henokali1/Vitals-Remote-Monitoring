from flask import Flask, render_template, request


app = Flask(__name__)
app.secret_key = b'somelongrandomstring'

@app.route('/t')
def t():
    temp = request.args.get('temp', default = '', type = str)
    hb = request.args.get('hb', default = '', type = str)
    print(f'temp: {temp}\thb={hb}')
    return {"temp": temp, "hb": hb}
    # return render_template('logs.html')

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=9999)
