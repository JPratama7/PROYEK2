from mysql import connector
import hashlib


def buat_koneksi():
    try:
        mydb = connector.connect(
            host='localhost',
            user='root',
            database='databasekita')
        return mydb
    except:
        print("DB ERRROR ")


def logfunc(type, e):
    type = str(type).upper()
    with open("logbot.txt", "a") as log:
        log.write(f"{type} ERROR : {e}\n")


def cekuser(username):
    with buat_koneksi() as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT username FROM tabel_pendaftaran WHERE username ='{username}'")
        data = cursor.fetchone()
        if data != None:
            return True
        return False


def cekpass(password):
    with buat_koneksi() as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT password FROM tabel_pendaftaran WHERE password ='{password}'")
        data = cursor.fetchone()
        if data != None:
            return True
        return False


def cekdata(username: str, password: str) -> bool:
    with buat_koneksi() as conn:
        cursor = conn.cursor()
        query = "SELECT id_pendaftar FROM tabel_pendaftaran WHERE username = %s AND password = %s"
        val = (username, password)
        cursor.execute(query, val)
        data = cursor.fetchone()
        if data != None:
            return [True, data[0]]
        return False


def upload(file):
    with buat_koneksi() as conn:
        cursor = conn.cursor()
        cursor.execute(
            f" UPDATE tabel_pendaftaran SET dokumen = {file} WHERE id_telegram = %s")
        data = cursor.fetchone()
        if data != None:
            return True
        return False


def cekdataadmin(username: str, password: str) -> bool:
    with buat_koneksi() as conn:
        cursor = conn.cursor()
        query = "SELECT id_admin FROM tabel_admin WHERE usernameadmin = %s AND passwordadmin = %s"
        val = (username, password)
        cursor.execute(query, val)
        data = cursor.fetchone()
        if data != None:
            return [True, data[0]]
        return False


def cekemailsiswa(username: str, password: str) -> bool:
    with buat_koneksi() as conn:
        cursor = conn.cursor()
        query = "SELECT id_admin FROM tabel_admin WHERE usernameadmin = %s AND passwordadmin = %s"
        val = (username, password)
        cursor.execute(query, val)
        data = cursor.fetchone()
        if data != None:
            return [True, data[0]]
        return False
