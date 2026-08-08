import asyncio, edge_tts
H, HP = "fa-IR-DilaraNeural", "+60Hz"   # Koochooloo the hamster (cute, high)
C, CP = "fa-IR-FaridNeural",  "+25Hz"   # the Cat (cute cartoon)
# (text, voice, pitch, filename)
LINES = [
    ("سلام!",                  H, HP, "cc01.mp3"),
    ("سلام!",                  C, CP, "cc02.mp3"),
    ("چطوری؟",                 H, HP, "cc03.mp3"),
    ("خوبم، مرسی. تو چطوری؟",  C, CP, "cc04.mp3"),
    ("گرسنه هستم!",            H, HP, "cc05.mp3"),
    ("سیب می‌خوای؟",           C, CP, "cc06.mp3"),
    ("بله، مرسی!",             H, HP, "cc07a.mp3"),
    ("نه، مرسی.",              H, HP, "cc07b.mp3"),
    ("بفرما، نوش جان!",        C, CP, "cc08.mp3"),
    ("خوشمزه است!",            H, HP, "cc09.mp3"),
    ("خداحافظ!",               H, HP, "cc10.mp3"),
    ("خداحافظ!",               C, CP, "cc11.mp3"),
    ("آفرین!",                 H, HP, "cc_afarin.mp3"),  # cute celebration for story end
    # Story 2 — a day at the park (reuses the Nature + Places words)
    ("بریم پارک؟",              H, HP, "pk01.mp3"),
    ("بله، بریم!",              C, CP, "pk02.mp3"),
    ("نگاه کن! یک درخت بزرگ!",   H, HP, "pk03.mp3"),
    ("یک پرنده روی درخت است.",   C, CP, "pk04.mp3"),
    ("یک پروانه هم هست!",        H, HP, "pk05.mp3"),
    ("خیلی قشنگ است!",          H, HP, "pk06a.mp3"),
    ("بیا بازی کنیم!",           H, HP, "pk06b.mp3"),
    ("باران می‌آید!",            C, CP, "pk07.mp3"),
    ("بریم خانه!",              H, HP, "pk08.mp3"),
    ("خداحافظ پارک!",           C, CP, "pk09.mp3"),
    ("امروز خیلی خوب بود!",      H, HP, "pk10.mp3"),
    ("بله! خداحافظ!",           C, CP, "pk11.mp3"),
    # Koochooloo's personality catchphrases (always hungry / loves her wheel)
    ("گرسنه هستم!",            H, HP, "k_hungry.mp3"),
    ("یه چیزی بخوریم؟",         H, HP, "k_eat.mp3"),
    ("دلم سیب می‌خواد!",         H, HP, "k_apple.mp3"),
    ("بازی کنیم؟",              H, HP, "k_play.mp3"),
    ("چرخمو دوست دارم!",        H, HP, "k_wheel.mp3"),
    ("بریم بدوییم!",            H, HP, "k_run.mp3"),
    # Feed Koochooloo game — she asks for a food (k_apple reused for apple)
    ("دلم هویج می‌خواد!",        H, HP, "kf_carrot.mp3"),
    ("دلم ذرت می‌خواد!",         H, HP, "kf_corn.mp3"),
    ("دلم انگور می‌خواد!",       H, HP, "kf_grapes.mp3"),
    ("دلم خیار می‌خواد!",        H, HP, "kf_cucumber.mp3"),
    ("دلم مَوز می‌خواد!",         H, HP, "kf_banana.mp3"),
    ("دلم تخمه می‌خواد!",        H, HP, "kf_seeds.mp3"),
    ("دلم بادام‌زمینی می‌خواد!",  H, HP, "kf_peanut.mp3"),
    ("دلم گردو می‌خواد!",        H, HP, "kf_walnut.mp3"),
    ("دلم پسته می‌خواد!",        H, HP, "kf_pistachio.mp3"),
    ("دلم بادام می‌خواد!",       H, HP, "kf_almond.mp3"),
    ("سیر شدم، مرسی!",          H, HP, "kf_full.mp3"),
]
async def main():
    for text, voice, pitch, f in LINES:
        await edge_tts.Communicate(text, voice, rate="-10%", pitch=pitch).save("audio/" + f)
        print("saved", f)
asyncio.run(main())
