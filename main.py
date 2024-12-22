from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def beranda():
    return render_template('beranda.html')

@app.route('/daftar')
def daftar():
    return render_template('daftar.html')

@app.route('/masuk')
def masuk():
    return render_template('masuk.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/produk')
def produk():
    return render_template('produk.html')

@app.route('/produkml')
def produkml():
    return render_template('produkml.html')

@app.route('/produkff')
def produkff():
    return render_template('produkff.html')

@app.route('/produkpubg')
def produkpubg():
    return render_template('produkpubg.html')

if __name__ == '__main__':
    app.run(debug=True)
