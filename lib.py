import string
from mysql import connector
from pytz import utc, timezone
from datetime import datetime
import random as rand

format_time = '%d/%m/%Y %H:%M'
date_format = '%d %b %y %H:%M'
timezone_dict = {"WIB": "Asia/Jakarta", "WITA": "Asia/Makassar", "WIT": "Asia/Jayapura"}

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

def user_ke_utc(date_time: string) -> datetime:
    date_time: string = date_time.lower()
    if not isinstance(date_time, datetime):
        date_time: datetime = datetime.strptime(date_time, date_format)
    date_time: datetime = date_time.astimezone(utc).strftime(date_format)
    date_time: datetime = datetime.strptime(date_time, date_format)
    return date_time

def buat_id(start: int = 0 , end: int = 9999)-> int:
    rand.seed(rand.randint(0,99999999))
    return rand.randint(start, end)

def convert_utc_to_usertz(date_time, user_timezone : string):
    tz_user = timezone(timezone_dict.get(user_timezone))
    if not isinstance(date_time, datetime):
        date_time = datetime.strptime(date_time, format_time)

    date_time = date_time.replace(tzinfo=utc)
    date_time = date_time.astimezone(tz_user).strftime(format_time)
    return date_time

def convert_to_utc(date_time) -> datetime:
    if not isinstance(date_time, datetime):
        date_time = datetime.strptime(date_time, format_time)

    date_time = date_time.astimezone(utc).strftime(format_time)
    date_time = datetime.strptime(date_time, format_time)
    return date_time