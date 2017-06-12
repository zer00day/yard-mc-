#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import time
import sys
import os
import platform

class renkler:
    PEMBE = '\033[95m'
    MAVİ = '\033[94m'
    YESİL = '\033[92m'
    SARI = '\033[93m'
    KIRMIZI = '\033[91m'

print(renkler.YESİL + "[ ... ] Sistem Yardımcısı Başlatılıyor...")
time.sleep(3)
print()

print(renkler.MAVİ + """

	$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	$                                               $
	$               SİSTEM YARDIMCISI               $
	$                blinkcursor.org                $
	$                                               $
	$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

	""")

print(renkler.YESİL + "[ + ] Sistem Tarihi : ")
print(renkler.KIRMIZI + "[ ! ]", time.ctime())
print("")
print(renkler.YESİL + "[ + ] Çalıştırılan Ortam : ")
print(renkler.KIRMIZI + "[ ! ]", sys.platform)
print("")
print(renkler.YESİL + "[ + ] Çalışan Sistem Mimarisi : ")
print(renkler.KIRMIZI + "[ ! ]", platform.architecture())
print("")
print(renkler.YESİL + "[ + ] Ayrıntılı Sistem Bilgisi : ")
print(renkler.KIRMIZI + "[ ! ]", os.uname())
print("")
print(renkler.SARI + "[ ! ] Yardımcı Kapatıldı!")
time.sleep(1)
print("")
sys.exit()