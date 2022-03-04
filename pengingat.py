import os

from datetime import datetime
from lib import timezone_dict, convert_to_utc, buat_koneksi
from time import sleep
from telebot import TeleBot
from pytz import timezone

api = '2132984370:AAEkaWP1x0kOWO3x6r3d6j0555szKPBGU7A'
bot = TeleBot(api)
tz = timezone_dict.get('WIB')


if __name__ == "__main__":
    print(f"Current TimeZone : {tz}")
    print("Starting Reminder User")
    while 1:
        noow = convert_to_utc(datetime.now(timezone(tz)))
        with buat_koneksi() as conn:
            cursor = conn.cursor()
            query = "SELECT id_telegram, isi_reminder FROM reminder_user WHERE waktu = %s"
            cursor.execute(query, (noow,))
            result_set = cursor.fetchall()
            if len(result_set) != 0:
                for data in result_set:
                    try:
                        bot.send_message(data[0], data[1])
                        print(f"Sending to {data[0]}")
                    except:
                        print(f"Failed to send to {data[0]}")

            sleep(60)