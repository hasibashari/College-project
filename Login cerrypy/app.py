# Tambahkan library cherrypy
import cherrypy
import os


class Login(object):

    # method index akan menampilkan form login
    @cherrypy.expose
    def index(self):
        with open("templates/login.html", "r") as file:
            return file.read()

    # method login akan memproses data login dan memvalidasi username dan password
    @cherrypy.expose
    def login(self, username=None, password=None):
        if username == 'admin' and password == 'password':
            return "Login berhasil!"
        else:
            return "Username atau password salah!"


if __name__ == "__main__":
    # konfigurasi server untuk menyajikan file statis di direktori 'static'
    conf = {
        "/static": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": os.path.abspath("./static")
        }
    }
    # jalankan server dengan menginstansiasi objek Login() dan konfigurasi di atas
    cherrypy.quickstart(Login(), "/", conf)

# Penjelasan Kode:
# 0. pip3 install cherrypy
# 1. Import library cherrypy
# 2. Import library os
# 3. Buat class Login
# 4. Buat method index untuk menampilkan form login
# 5. Buat method login untuk memproses data login dan memvalidasi username dan password
# 6. Buat konfigurasi server untuk menyajikan file statis di direktori 'static'
# 7. Jalankan server dengan menginstansiasi objek Login() dan konfigurasi di atas
# 8. Jalankan dengan mengetikkan 'python app.py' di terminal
# 9. Buka browser dan ketikkan 'localhost:8080'
# 10. Coba login dengan username 'admin' dan password 'password'
# 11. Jika berhasil, maka akan muncul pesan 'Login berhasil!'
# 12. Jika gagal, maka akan muncul pesan 'Username atau password salah!'
# 13. Selesai
