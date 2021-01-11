# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoin
from view.view_nilai import *

while True:
    c = input("\n(T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar: ")

    if (c.lower() == 't'):
        tambah_data()

    elif (c.lower() == 'u'):
        ubah_data()

    elif (c.lower() == 'h'):
        hapus_data()

    elif (c.lower() == 'c'):
        cetak_hasil_pencarian()

    elif (c.lower() == 'l'):
        cetak_daftar_nilai()

    elif (c.lower() == 'k'):
        break

    else:
        print("=== Pilih Sesuai Menu Yang Tersedia ===")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
