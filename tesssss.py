from lib import buat_koneksi, cekpass
from pyperclip import copy

# with buat_koneksi() as conn:
#     with conn.cursor() as cur:
#         with open('kegiatan1.jpeg', 'rb') as f:
#             byte = f.read().hex()
#             query = "UPDATE tabel_pendaftaran SET dokumen = %s WHERE id_pendaftar = 31 "
#             val = (None,)
#             cur.execute(query, val)
#             conn.commit()

print(cekpass('123'))
