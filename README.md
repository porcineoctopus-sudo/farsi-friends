# Farsi Friends

A little Farsi (Persian) learning app for kids, starring **Koochooloo** the hamster
and her friend the Cat. Built as a single static page — no build step, no framework.

## Play it

**<https://porcineoctopus-sudo.github.io/farsi-friends/>**

On an iPad, open that link in Safari and choose *Share → Add to Home Screen* to run
it full-screen like a real app.

## What's in it

Four vocabulary themes, each with a **Learn** grid (tap a card to hear the word) and a
**Play** quiz (tap the picture you heard):

| Theme | Words |
|---|---|
| 👋 Greetings | hello, goodbye, how are you, thank you, I love you … |
| 🍎 Food | fruit, vegetables, grains, dairy, drinks, "I'm hungry" … |
| 🌳 Nature | trees, sky and weather, water and land, little creatures |
| 🏙️ Places | house, school, hospital, library, park, zoo … |

Plus:

- **🎬 Stories** — short illustrated conversations with a branch point where the
  child picks Koochooloo's reply. Two so far: *Meet the Cat* and *At the Park*.
- **🥕 Feed Me! / 🥜 Nuts!** — listen to what Koochooloo asks for and feed her;
  her tummy meter fills and she visibly rounds out.

Every word and line is a pre-generated neural Persian recording, so it sounds like a
person rather than a robot. If a recording can't load, the app falls back to the
device voice.

## Running it locally

Serve the folder over HTTP — opening `index.html` straight off disk stops the
browser loading the mp3s:

```sh
python3 -m http.server 8777
open http://127.0.0.1:8777/index.html
```

## Regenerating the audio

The recordings are made with [edge-tts](https://github.com/rany2/edge-tts)
(`fa-IR-DilaraNeural`, and `fa-IR-FaridNeural` for the Cat):

```sh
python3 -m venv .venv
./.venv/bin/pip install edge-tts
./.venv/bin/python gen_audio.py    # vocabulary words  -> audio/
./.venv/bin/python gen_convo.py    # story + game lines -> audio/
```

`gen_audio.py` holds the word lists; `gen_convo.py` holds the story and game lines
with a per-character voice and pitch.

### A note on spelling

Persian script leaves out short vowels, and the voice sometimes guesses wrong. Where
that happened, the **generator scripts** carry a respelled version while `index.html`
keeps the standard spelling that children see on the card:

| Word | Shown on the card | Fed to the voice | Why |
|---|---|---|---|
| banana | موز | مَوز | fatha pins the vowel |
| forest | جنگل | جَنگَل | otherwise not "jan-gal" |
| rainbow | رنگین‌کمان | رنگین کمان | the zero-width non-joiner tripped it |
| zoo | باغ‌وحش | باغِ وحش | kasra spells out the ezâfe, "bâgh-**e** vahsh" |
