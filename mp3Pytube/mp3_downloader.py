from tkinter import Tk, Label, Entry, Button, filedialog
from pytube import YouTube
import os

def indir():
    link = link_entry.get()
    try:
        yt_mp3 = YouTube(str(link))
        video_sesi = yt_mp3.streams.filter(only_audio=True).first()
        kayit_dizini = kayit_dizini_entry.get()
        mp3_dosyasi = video_sesi.download(output_path=kayit_dizini)

        base, ext = os.path.splitext(mp3_dosyasi)
        new_file = base + '.mp3'
        os.rename(mp3_dosyasi, new_file)
        info_label.config(text=yt_mp3.title + " Başarı ile indirildi ")
    except Exception as e:
        info_label.config(text="Hata: " + str(e))

def dizin_sec():
    dizin = filedialog.askdirectory()
    kayit_dizini_entry.delete(0, "end")
    kayit_dizini_entry.insert(0, dizin)

# Tkinter penceresini oluştur
root = Tk()
root.title("YouTube Mp3 İndirici")
root.geometry("400x200")

# Etiketler ve girdi alanları
link_label = Label(root, text="İndirilecek bağlantının linkini giriniz:")
link_label.pack()
link_entry = Entry(root, width=50)
link_entry.pack()

kayit_dizini_label = Label(root, text="Kaydedilecek dizini seçiniz:")
kayit_dizini_label.pack()
kayit_dizini_entry = Entry(root, width=50)
kayit_dizini_entry.pack()

dizin_sec_button = Button(root, text="Dizin Seç", command=dizin_sec)
dizin_sec_button.pack()

info_label = Label(root, text="", fg="green")
info_label.pack()

indir_button = Button(root, text="İndir", command=indir)
indir_button.pack()

root.mainloop()
