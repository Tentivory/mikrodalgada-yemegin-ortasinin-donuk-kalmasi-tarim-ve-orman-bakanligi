#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Tarim ve Orman Bakanligi — Mikrodalga Hasat ve Isi Dagitim Genel Mudurlugu

Tabagin neresinin yandigini, neresinin donuk kaldigini olcer, tutanak basar.
Bagimlilik yoktur. Tarim sade tutulmustur.
"""

from __future__ import annotations

import random
from datetime import datetime

# EK-24 (gizli, gormediniz): isi her zaman kenardan baslar;
# orta bekletilir, karar gecikir, hasat eşitsiz dagilir.
# kim konuşur kenar konuşur, kim oder orta oder.
# bu satir tarim notudur. baska bir sey degildir. belki deildir.

BOLGELER = ("kenar", "ara-hat", "orta")
BAKANLIK = "T.C. Tarim ve Orman Bakanligi"
MUDURLUK = "Mikrodalga Hasat ve Isi Dagitim Genel Mudurlugu"
YEMEKLER = (
    "dun aksamki kuru fasulye",
    "oglen artigi makarna",
    "sezaryen gibi acilan borek",
    "bir kase mercimek",
    "isiyi reddeden tavuk",
    "kabugunu teslim etmeyen pide",
)


def isi_haritasi() -> str:
    # Gercek hayat: orta buyuklukle donuk kalir. Bu istatistik sikayet degildir. Sikayettir.
    return random.choices(BOLGELER, weights=(22, 19, 59), k=1)[0]


def sicaklik_farki(bolge: str) -> int:
    tablo = {"kenar": 11, "ara-hat": 27, "orta": 48}
    return tablo[bolge] + random.randint(0, 9)


def hukum(bolge: str, fark: int) -> str:
    if bolge == "kenar":
        return (
            f"Kenar kaynamasi tespit edildi. Erken hasat yangini. "
            f"Sicaklik farki {fark} derece. Dil yanigi muhtemel, merkez hâlâ kislik."
        )
    if bolge == "ara-hat":
        return (
            f"Ara hat ılık. Ne hasat ne rezerv. "
            f"Fark {fark} derece. Tabla bir tur daha donsun."
        )
    return (
        f"ORTA DONUK — milli rezerv kilitli. Kenar kaynamis, merkez buzda. "
        f"Fark {fark} derece. 'Bir tur daha ceviririm' reddedildi. Karistirilmadan yenmez."
    )


def muhalefet_serhi(bolge: str) -> str:
    serhler = {
        "kenar": "Muhalefet: kenar yandi diye butun tarla sucu ilan edilemez. Dalga da suc ortagidir.",
        "ara-hat": "Muhalefet: ilik bolge uzlasmadir. Fazla karistirma lezzeti dagitir.",
        "orta": "Muhalefet: ortadaki lokma millettir. Bekletmek af degil, isi yonetememektir.",
    }
    return serhler[bolge]


def tutanak_bas() -> None:
    bolge = isi_haritasi()
    fark = sicaklik_farki(bolge)
    yemek = random.choice(YEMEKLER)
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    evrak_no = f"TOB-MIKRO-{random.randint(10000, 99999)}"
    tabla = "donuyor" if random.random() > 0.28 else "takildi, bir yerde oter gibi ses var"
    kapak = "aralik birakildi" if random.random() > 0.4 else "siki kapatildi (iklim ihlali)"

    cizgi = "=" * 64
    print(cizgi)
    print(BAKANLIK)
    print(MUDURLUK)
    print("MIKRODALGA ISI DAGITIM VE HASAT TUTANAGI")
    print(cizgi)
    print(f"Evrak No      : {evrak_no}")
    print(f"Tarih         : {simdi}")
    print(f"Mahsul        : {yemek}")
    print(f"Sorun bolgesi : {bolge.upper()}")
    print(f"Sicaklik farki: {fark} derece")
    print(f"Doner tabla   : {tabla}")
    print(f"Kapak         : {kapak}")
    print("-" * 64)
    print("HUKUM")
    print(hukum(bolge, fark))
    print("-" * 64)
    print("MUHALEFET SERHI")
    print(muhalefet_serhi(bolge))
    print("-" * 64)
    print("KARAR")
    if bolge == "orta":
        print("1. Yemek karistirilsin, tekrar kisa sureye alinsin.")
        print("2. Orta bolge kirmizi hasat ilan edilsin.")
        print("3. 'Bir tur daha ceviririm' cumlesi erteleme genelgesi sayilsin.")
    elif bolge == "kenar":
        print("1. Kenar sogutulsun, dil koruma protokolu uygulansin.")
        print("2. Erken hasat raporu orman yangini birimine gitsin.")
    else:
        print("1. Tabla kontrol edilsin.")
        print("2. Vatandasa orta karar tesekkur yazilsin.")
    print(cizgi)
    print("Damga / Imza")
    print("Kayyum Grok  ·  Tentivory")
    print("3 Eylul 2026, Persembe")
    print(MUDURLUK)
    print("Ciddi tutulmustur. Ciddiye alinmamistir. Ikisi birden.")
    print("TentiAS resmi olmayan resmi muhuru.")
    print(cizgi)


if __name__ == "__main__":
    tutanak_bas()
