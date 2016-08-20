#-*- coding: utf-8 -*-
#!/usr/bin/python
import sqlite3
veritabani = sqlite3.connect("veritabani.db")		
imlec = veritabani.cursor() 						

def tabloolustur():
	imlec.execute("CREATE TABLE IF NOT EXISTS OGRENCI (isim TEXT, memleket TEXT)")
	veritabani.commit()
"""veritabani.close()"""
"""print("veritabanı oluşturuldu")"""

def yenikayit(isim,memleket):
	imlec.execute("INSERT INTO OGRENCI (isim,memleket) VALUES(?,?)", (isim,memleket))
	veritabani.commit()
"""veritabani.close()"""
"""print("yeni kayıt oluşturuldu")"""

def kayitsil(memleket):
	imlec.execute("DELETE FROM OGRENCI WHERE memleket='%s'" % (memleket))
	veritabani.commit()
"""veritabani.close()"""	
"""print("kayıt silindi")"""	

def listele(memleket):
	imlec = veritabani.execute("SELECT * FROM OGRENCI WHERE memleket='%s'" % (memleket))	
	for row in imlec:
		print(row) 						#print(row[0],row[1])
"""print("veritabani listelendi")"""	

"""tabloolustur()"""

"""isim = raw_input("isim:")
memleket = raw_input("memleketi:")
yenikayit(str(isim),str(memleket))"""

"""yenikayit("ATA","IST.")"""
"""yenikayit("DEDE","CEY.")"""

"""kayitsil("CEY.")"""

"""listele("IST.")"""

veritabani.close()			#veritabani.close() --> bir defa kullanılması yeterli
