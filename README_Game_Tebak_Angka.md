# Game Tebak Angka

Program ini adalah permainan sederhana di mana pemain diminta untuk menebak sebuah angka rahasia antara 1 hingga 100 yang telah dipilih secara acak oleh komputer.

## Fitur
- Angka rahasia diacak setiap kali program dijalankan.
- Pemain diberi petunjuk apakah tebakan terlalu besar atau terlalu kecil.
- Validasi input untuk memastikan pengguna hanya memasukkan angka.
- Menampilkan jumlah percobaan setelah berhasil menebak dengan benar.

## Cara Menjalankan
1. Pastikan Python telah terinstall di komputer Anda.
2. Buka terminal atau command prompt.
3. Jalankan program dengan perintah:

```bash
python "Game Tebak Angka.py"
```

4. Masukkan tebakan angka sesuai instruksi di layar.

## Contoh Output
```
=========================================
            Game Tebak Angka
=========================================
Saya Mempunyai Angka 1-100 
Tebak Angka Rahasia: 50
Tebakan Terlalu Kecil
Tebak Angka Rahasia: 75
Tebakan Terlalu Besar
Tebak Angka Rahasia: 63
Tebakan Anda Benar, Anda Menebak 3 kali
```

## Catatan
- Program ini menggunakan `try-except` untuk menangani input yang tidak valid.
- Jumlah percobaan dicatat dan ditampilkan setelah berhasil menebak.