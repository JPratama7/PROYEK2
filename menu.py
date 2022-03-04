import telebot
import mysql.connector
from telebot import types
from dataclasses import dataclass
import re
from mysql.connector import Error

from lib import cekpass, cekuser, buat_koneksi, cekdata, cekdataadmin, user_ke_utc, convert_utc_to_usertz, buat_id
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    database='databasekita')


dict_global = {}

sql = mydb.cursor()
api = '2132984370:AAEkaWP1x0kOWO3x6r3d6j0555szKPBGU7A'
bot = telebot.TeleBot(api)


@dataclass
class ID:
    id: int = None
    username: str = None
    password: str = None


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id

    custom = types.ReplyKeyboardMarkup()
    a = types.KeyboardButton('/Berita')
    b = types.KeyboardButton('/Informasi')
    c = types.KeyboardButton('/PengumpulanDraf')
    d = types.KeyboardButton('/MenuUtama')
    e = types.KeyboardButton('/MenuAdmin')

    custom.row(a, b)
    custom.row(c,)
    custom.row(d)
    custom.row(e)

    bot.send_message(
        chat_id, 'Selamat Datang Di SMA XAVERIUS BATURAJA\n\n'
        'Untuk melihat berita tebaru mengenai SMA XAVERIUS BATURAJA silakan ketika atau tekan /Berita\n\n'
        'Untuk melihat informasi ketik atau tekan /informasi\n\n'
        'Untuk pengumpulan draf dokumen silakan ketik atau tekan \n/pengumpulanDraf', reply_markup=custom)


@bot.message_handler(commands=['MenuUtama'])
def send_welcome(message):
    chat_id = message.chat.id

    custom = types.ReplyKeyboardMarkup()
    a = types.KeyboardButton('/Berita')
    b = types.KeyboardButton('/Informasi')
    c = types.KeyboardButton('/PengumpulanDraf')
    d = types.KeyboardButton('/MenuUtama')
    e = types.KeyboardButton('/MenuAdmin')

    custom.row(a, b)
    custom.row(c)
    custom.row(d)
    custom.row(e)

    bot.send_message(
        chat_id, 'Anda berada di Menu Utama\n\n'
        'Untuk melihat berita tebaru mengenai SMA XAVERIUS BATURAJA silakan ketika atau tekan /Berita\n\n'
        'Untuk melihat informasi ketik atau tekan /informasi\n\n'
        'Untuk pengumpulan draf dokumen silakan ketik atau tekan \n/pengumpulanDraf', reply_markup=custom)


@bot.message_handler(commands=['Berita'])
def send_welcome(message):
    chat_id = message.chat.id

    custom = types.ReplyKeyboardMarkup()
    a = types.KeyboardButton('/News')
    b = types.KeyboardButton('/KalenderAkademik')
    c = types.KeyboardButton('/MenuUtama')

    custom.row(a, b)
    custom.row(c)
    bot.send_message(
        chat_id, 'Selamat Datang di Menu Berita \n\n'
        'Untuk melihat berita terkini silakan ketika atau tekan /News\n\n'
        'Untuk melihat informasi ketik atau tekan /KalenderAkademik\n\n', reply_markup=custom)


@bot.message_handler(commands=['News'])
def text(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('C:\PROYEK 2\\kegiatan1.jpeg',
                   'rb'))
    bot.send_photo(chatid, open('C:\PROYEK 2\\kegiatan4.jpeg', 'rb'),
                   'Kegiatan Rutin Sabtu Pramuka SMA Xaverius Baturaja  13 November 2021 penyelenggara team Pramuka xaveba ')
    bot.send_photo(chatid, open('C:\PROYEK 2\\kegiatan2.jpeg', 'rb'),
                   'Kegiatan Adiwiyata untuk mempercantik lingkungan Pada tanggal 16 November 2021 ')
    bot.send_photo(chatid, open('C:\PROYEK 2\\kegiatan3.jpeg', 'rb'),
                   'Kegiatan belajar diluar sekolah ditaman Baturaja Kemiling 3 November 2021 ')


@bot.message_handler(commands=['KalenderAkademik'])
def text(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('C:\PROYEK 2\\kalenderpendidikan.png', 'rb'))


@bot.message_handler(commands=['Informasi'])
def send_welcome(message):
    chat_id = message.chat.id

    custom = types.ReplyKeyboardMarkup()
    a = types.KeyboardButton('/MenuUtama')

    custom.row(a)
    bot.send_message(
        chat_id, 'Berikut Informasi Terkini :\n\n'
        '>>> PENGUMUNAN!!! <<<\n\n'
        '1. Khusus Kelas XII, dimohon dengan sangat untuk bisa menyelesaikan administrasi foto bersama dari Adi Warna sebesar Rp. 50.000,-\n\n'
        '2. Dalam penyelesaian administrasi keuangan (SPP atau DPP atau Keuangan lainnya) dapat datang langsung ke sekolah setiap tanggal 10 pada jam kerja (pukul 07.00 - 12.00 WIB) atau dapat melalui Tranfer Rekening Bank BRI ke nomor rekening : 0008-01-011101-53-8 atas nama Marissa\n\n'
        '>> 01 Maret 2022, Kegiatan : PTM Terbatas berjalan seperti biasa (SISWA WAJIB MASUK SEKOLAH)\n\n'
        '>> 02 Maret 2022, Kegiatan : RABU ABU (SISWA BELAJAR DI RUMAH)\n\n'
        '>> 03 Maret 2022, Kegiatan : Hari Raya NYEPI Tahun Baru SAKA 1944 (SISWA BELAJAR DI RUMAH\n\n'
        '>> 04-05 Maret 2022, Kegiatan : PTM Terbatas berjalan seperti biasa (SISWA WAJIB MASUK SEKOLAH)\n\n'
        '>> 07-15 Maret 2022, Kegiatan : Ujian Tengah Semester Genap (SISWA WAJIB MASUK SEKOLAH\n\n'
        '>> 17-21 Maret 2022, Kegiatan : Ujian Praktek Kelas XII\n\n'
        '>> 22 Maret 2022, Kegiatan : PTM Terbatas khusus kelas X dan XI\n\n'
        '>> 23-31 Maret 2022, Kegiatan : Ujian Satuan Pendidikan Kelas XII dan Pengolahan Nilai Tangah Semester Genap\n\n'
        '>> 01 April 2022, Kegiatan : Pembagian Rapor Tengah Semester Genal\n\n http://smaxavbta.test/')


@bot.message_handler(commands=['PengumpulanDraf'])
def send_welcome(message):
    chat_id = message.chat.id
    msg = bot.send_message(
        chat_id, 'Silakan masukan username anda! \n\n'
    )
    bot.register_next_step_handler(msg, namapengumpul)


def namapengumpul(message):
    chat_id = message.chat.id
    username = message.text
    user = ID()
    user.username = username
    dict_global[chat_id] = user
    if cekuser(username):
        msg = bot.send_message(chat_id, "Masukkan password!")
        bot.register_next_step_handler(msg, tespassword)
    else:
        msg = bot.reply_to(message, "Username salah!")
        bot.register_next_step_handler(msg, namapengumpul)


def tespassword(message):
    chat_id = message.chat.id
    password = message.text
    user = dict_global[chat_id]
    user.password = password
    data = cekdata(user.username, user.password)
    if data[0]:
        user.id = data[1]
        msg = bot.send_message(chat_id, "Silakan Upload Berkas Anda...")
        bot.register_next_step_handler(msg, berkas)
    else:
        msg = bot.reply_to(message, "Password salah!")
        bot.register_next_step_handler(msg, tespassword)
        del dict_global[chat_id]


def berkas(message):
    chat_id = message.chat.id
    user = dict_global[chat_id]
    try:
        fileID = message.document.file_id
        fileInfo = bot.get_file(fileID)
        downloaded_file = bot.download_file(fileInfo.file_path)
        with buat_koneksi() as koneksi:
            cursor = koneksi.cursor()
            query = "UPDATE tabel_pendaftaran SET dokumen = %s WHERE id_pendaftar = %s "
            val = (downloaded_file, user.id)
            cursor.execute(query, val)
            koneksi.commit()
            bot.reply_to(
                message, "Berkas berhasil di upload! \n\n http://smaxavbta.test/")
    except AttributeError as attrb:
        msg = bot.send_message(
            chat_id, "Type Berkas Tidak Sesuai Silakan Upload Ulang!")
        bot.register_next_step_handler(msg, berkas)
    except Exception as e:
        print(e)
        bot.send_message(chat_id, "Berkas gagal di upload!")


@bot.message_handler(commands=['MenuAdmin'])
def send_welcome(message):
    chat_id = message.chat.id
    msg = bot.send_message(
        chat_id, 'Silakan masukan username admin! \n\n'
    )
    bot.register_next_step_handler(msg, namaadmin)


def namaadmin(message):
    chat_id = message.chat.id
    username = message.text
    user = ID()
    user.username = username
    dict_global[chat_id] = user
    msg = bot.send_message(chat_id, "Masukkan password admin!")
    bot.register_next_step_handler(msg, passwordadmin)


def passwordadmin(message):
    chat_id = message.chat.id
    text = message.text
    user = dict_global[chat_id]
    user.password = text
    data = cekdataadmin(user.username, user.password)
    if data[0]:
        user.id = data[1]
        msg = bot.send_message(chat_id, "Silakan masukan username siswa")
        bot.register_next_step_handler(msg, userdelete)
    else:
        bot.reply_to(
            message, "Username Salah, Silahkan Mengulangi!")
        del dict_global[chat_id]


def userdelete(message):
    chat_id = message.chat.id
    user = dict_global[chat_id]
    text = message.text
    try:
        with buat_koneksi() as koneksi:
            cursor = koneksi.cursor()
            query = "UPDATE tabel_pendaftaran SET dokumen = %s WHERE username = %s"
            val = (None, text)
            cursor.execute(query, val)
            koneksi.commit()
            bot.reply_to(message, "Berkas berhasil di hapus!")
    except Exception as e:
        print(e)
        bot.send_message(chat_id, "Berkas gagal di hapus!")


@bot.message_handler(commands=['ListSiswa'])
def send_welcome(message):
    chat_id = message.chat.id

    custom = types.ReplyKeyboardMarkup()
    a = types.KeyboardButton('/MenuUtama')

    custom.row(a)
    bot.send_message(
        chat_id, '>>> Daftar Nama Siswa Yang Sudah Mengumpulkan Persyaratan dokumen!!! <<<\n\n'
        '1. Hanan\n 2. Yuda\n 3. Desti')


@bot.message_handler(commands=['agenda'])
def router(msg):
    chat_id = msg.chat.id
    text = msg.text.lower().split()
    if len(text) > 1:
        if text[1] == 'tambah':
            tambah_agenda(msg)
        elif text[1] == 'hapus':
            remove_agenda(msg)
        elif text[1] == 'list':
            list_agenda(msg)
        else:
            bot.send_message(chat_id, "Perintah tidak dikenali")
    else:
        bot.send_message(chat_id, "WHY PERINTAHNYA KURANG")

def tambah_agenda(msg):
    chat_id = msg.chat.id
    text = msg.text.split(' ')
    text = text[2:]
    text = ' '.join(text)
    result = re.split('agendanya', text)
    if len(result) > 1:
        try:
            list = [s.strip() for s in result]
            agenda = list[1]
            waktu = user_ke_utc(list[0])
            with buat_koneksi() as conn:
                cursor = conn.cursor()
                query = "INSERT INTO reminder_user VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (buat_id(), chat_id, agenda, waktu))
                conn.commit()
                bot.send_message(chat_id, "Agenda telah ditambahkan")
        except Exception as e:
            print(e)
            bot.send_message(chat_id, "Format agenda tidak sesuai\n"
                                          "Silahkan mengikuti contoh dibawah ini\n"
                                          "/agenda 6 jan 21 17:21 agendanya Mabar Valorant")
    else:
        bot.send_message(chat_id, "Format agenda tidak sesuai\n"
                                      "Silahkan mengikuti contoh dibawah ini\n"
                                      "/agenda 6 jan 21 17:21 agendanya Mabar Valorant")

def list_agenda(msg):
    chat_id = int(msg.chat.id)
    with buat_koneksi() as conn:
        cursor = conn.cursor()
        query = f"SELECT isi_reminder, waktu, id_reminder FROM reminder_user WHERE id_telegram = {chat_id}"
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) > 0:
            for i in result:
                bot.send_message(chat_id, f"ID Reminder: {i[2]}\nWaktu: {convert_utc_to_usertz(i[1], 'WIB')}\nAgenda: {i[0]}")
        else:
            bot.send_message(chat_id, "Anda belum memiliki agenda")

def remove_agenda(msg):
    chat_id = msg.chat.id
    text = msg.text.split(' ')
    text = text[2:]
    if len(text) != 0:
        if text[0].isdigit():
            agenda = int(text[0])
            with buat_koneksi() as conn:
                cursor = conn.cursor()
                query = "DELETE FROM reminder_user WHERE id_reminder = %s AND id_telegram = %s"
                try:
                    cursor.execute(query, (agenda, chat_id))
                    bot.send_message(chat_id, "Agenda telah Dihapus")
                except Error:
                    bot.send_message(chat_id, "Agenda tidak ditemukan")
        else:
            bot.send_message(chat_id, "WHY U ISI SELAIN ANGKA")
    else:
        bot.send_message(chat_id, "Format agenda tidak sesuai\n"
                                      "Silahkan mengikuti contoh dibawah ini\n"
                                      "/agenda hapus 123456")

print('bot start running')
bot.polling()