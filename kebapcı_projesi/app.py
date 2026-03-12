from flask import Flask, render_template

app = Flask(__name__)

# Daha geniş bir menü verisi
menu_verisi = {
    "kebaplar": {
        "baslik": "🔥 Kebap Çeşitleri",
        "urunler": [
            {"ad": "Adana Kebap", "fiyat": 280},
            {"ad": "Urfa Kebap", "fiyat": 270},
            {"ad": "Beyti Sarma", "fiyat": 310}
        ]
    },
    "icecekler": {
        "baslik": "🥤 Soğuk İçecekler",
        "urunler": [
            {"ad": "Şalgam (Acılı)", "fiyat": 40},
            {"ad": "Yayık Ayran", "fiyat": 35}
        ]
    },
    "lahmacunlar": {
        "baslik": "🌮 Çıtır Lahmacunlar",
        "urunler": [
            {"ad": "Antep Lahmacun", "fiyat": 90},
            {"ad": "Kıymalı Lahmacun", "fiyat": 80}
        ]
    }
}

@app.route('/')
def ana_sayfa():
    # Ana sayfada sadece kategori isimlerini gösteriyoruz
    return render_template('index.html', kategoriler=menu_verisi.keys())

@app.route('/kategori/<kategori_adi>')
def kategori_detay(kategori_adi):
    # Tıklanan kategorinin ürünlerini gösteriyoruz
    secilen = menu_verisi.get(kategori_adi)
    return render_template('urunler.html', kategori=secilen)

if __name__ == '__main__':
    app.run(debug=True)