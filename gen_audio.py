import asyncio, edge_tts
VOICE = "fa-IR-DilaraNeural"   # Iranian (Tehran) female; male = fa-IR-FaridNeural

THEMES = {
    "greetings": [
        ("سلام",        "salam.mp3"),
        ("درود",        "dorood.mp3"),
        ("خداحافظ",     "khodahafez.mp3"),
        ("شب بخیر",     "shab_bekheyr.mp3"),
        ("چطوری؟",      "chetori.mp3"),
        ("خوبی؟",       "khoobi.mp3"),
        ("خوبم",        "khoobam.mp3"),
        ("مرسی",        "mersi.mp3"),
        ("بله",         "bale.mp3"),
        ("نه",          "na.mp3"),
        ("دوستت دارم",  "dooset_daram.mp3"),
    ],
    "food": [
        # Fruit
        ("سیب",          "sib.mp3"),
        ("مَوز",         "moz.mp3"),        # diacritic spelling -> "moaz"
        ("انگور",        "angoor.mp3"),
        ("پرتقال",       "porteghal.mp3"),
        ("هندوانه",      "hendevane.mp3"),
        ("گیلاس",        "gilas.mp3"),
        ("هلو",          "holoo.mp3"),
        # Vegetables
        ("هویج",         "havij.mp3"),
        ("گوجه فرنگی",    "gojefarangi.mp3"),
        ("خیار",         "khiyar.mp3"),
        ("سیب زمینی",     "sibzamini.mp3"),
        ("پیاز",         "piyaz.mp3"),
        ("ذرت",          "zorrat.mp3"),
        # Grains
        ("نان",          "nan.mp3"),
        ("برنج",         "berenj.mp3"),
        # Dairy
        ("شیر",          "shir.mp3"),
        ("پنیر",         "panir.mp3"),
        # Drinks
        ("آب",           "ab.mp3"),
        # Useful phrases
        ("گرسنه هستم",   "gorosname.mp3"),
        ("تشنه هستم",    "teshname.mp3"),
        ("خوشمزه است",   "khoshmaze.mp3"),
        ("نوش جان",      "nooshe_jan.mp3"),
    ],
    "nature": [
        # Trees & plants
        ("درخت",         "derakht.mp3"),
        ("گل",           "gol.mp3"),
        ("برگ",          "barg.mp3"),
        ("چمن",          "chaman.mp3"),
        ("جَنگَل",        "jangal.mp3"),    # fat-ha pins "jan-gal"
        ("گیاه",         "giyah.mp3"),
        # Sky & weather
        ("خورشید",       "khorshid.mp3"),
        ("ماه",          "mah.mp3"),
        ("ستاره",        "setare.mp3"),
        ("آسمان",        "aseman.mp3"),
        ("ابر",          "abr.mp3"),
        ("باران",        "baran.mp3"),
        ("برف",          "barf.mp3"),
        ("باد",          "bad.mp3"),
        ("رنگین کمان",   "ranginkaman.mp3"),  # plain space; the ZWNJ tripped the voice
        # Water & land
        ("دریا",         "darya.mp3"),
        ("رودخانه",      "rudkhane.mp3"),
        ("کوه",          "kuh.mp3"),
        ("سنگ",          "sang.mp3"),
        # Little creatures
        ("پروانه",       "parvane.mp3"),
        ("پرنده",        "parande.mp3"),
        ("زنبور",        "zanbur.mp3"),
        ("ماهی",         "mahi.mp3"),
    ],
    "places": [
        # Home & town
        ("خانه",         "khane.mp3"),
        ("ساختمان",      "sakhteman.mp3"),
        ("برج",          "borj.mp3"),
        ("قلعه",         "ghale.mp3"),
        ("کارخانه",      "karkhane.mp3"),
        # Around town
        ("مدرسه",        "madrese.mp3"),
        ("دانشگاه",      "daneshgah.mp3"),
        ("بیمارستان",    "bimarestan.mp3"),
        ("کتابخانه",     "ketabkhane.mp3"),
        ("موزه",         "muze.mp3"),
        ("مسجد",         "masjed.mp3"),
        ("بانک",         "bank.mp3"),
        # Shops & food
        ("مغازه",        "maghaze.mp3"),
        ("نانوایی",      "nanvayi.mp3"),
        ("رستوران",      "restoran.mp3"),
        # Going places
        ("فرودگاه",      "forudgah.mp3"),
        ("ایستگاه",      "istgah.mp3"),
        ("سینما",        "sinema.mp3"),
        ("ورزشگاه",      "varzeshgah.mp3"),
        ("پارک",         "park.mp3"),
        ("باغِ وحش",     "baghevahsh.mp3"),  # kasra spells out the ezâfe: "bâgh-e vahsh"
    ],
    "extras": [
        ("آفرین",       "afarin.mp3"),   # mascot celebration
    ],
}
async def main():
    for theme, items in THEMES.items():
        for text, fname in items:
            await edge_tts.Communicate(text, VOICE, rate="-10%").save("audio/" + fname)
            print("saved", fname)
asyncio.run(main())
