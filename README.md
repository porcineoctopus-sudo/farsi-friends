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
  child picks a reply. Three so far: *Meet the Cat*, *At the Park*, and
  *The Golden Rooster*.
- **🥕 Feed Me! / 🥜 Nuts!** — listen to what Koochooloo asks for and feed her;
  her tummy meter fills and she visibly rounds out.

Every word and line is a pre-generated neural Persian recording, so it sounds like a
person rather than a robot. If a recording can't load, the app falls back to the
device voice.

### The Golden Rooster

*The Golden Rooster* retells Ahmad Shamlou's **«خروس زری پیرهن پری»** at beginner
level — the plot and characters are his, the wording is ours, kept to words the app
teaches elsewhere. The fox flatters the rooster to lure him close and the cat saves him.

Shamlou's own recording (with Babak Bayat's music) is **not part of this repo**. It is
copyrighted, and publishing it here would be redistribution. If you keep a personal
copy at `audio/original/kz_part1.mp3` and `kz_part2.mp3`, a *"🎧 Hear the real story"*
button appears on that story and plays it as continuous story-time audio, separate from
the tap-through learning lines. Without those files the button stays hidden, which is
why the public site never shows it. `audio/original/` is gitignored — keep it that way.

Story time also shows **English subtitles** and a **picture that changes with the
scene**, both driven by `audio/original/kz_story.json` (also local-only):

```jsonc
{ "kz_part1": {
    "subs":   [[54, "Once upon a time, there was no one — but God."], ...],
    "scenes": [[0, "cabin"], [174, "warning"], ...] } }
```

`subs` is `[second, english]`; `scenes` is `[second, sceneName]` naming an entry in the
`SCENES` object in `index.html`. Both lists must be sorted by time. The English is a
translation made for this app, working from YouTube's Persian auto-captions for the
timings — it is not Shamlou's text and makes no claim to be. The thirteen scene
illustrations are drawn in `index.html` from a shared set of pieces (`sCabin`, `sFox`,
`sRooster`, `sCat`, `sLark`, `sTree`…), all on a `0 0 400 240` viewBox; they are
original drawings, not the book's — Farshid Mesghali's illustrations are copyrighted,
and the recording's video track is only a still of the cover in any case.

Both recordings are trimmed to where the story actually ends. The source uploads carry
a publisher's jingle and several unrelated stories after it, which is why part 2 stops
at 21:55.

## Running it locally

Serve the folder over HTTP — opening `index.html` straight off disk stops the
browser loading the mp3s:

```sh
python3 -m http.server 8777
open http://127.0.0.1:8777/index.html
```

To reach it from an iPad on the same wifi — which is how you get the story-time audio,
since that never goes to the public site — serve on all interfaces and use this Mac's
LAN address:

```sh
python3 -m http.server 8777 --bind 0.0.0.0
ipconfig getifaddr en0          # e.g. 192.168.1.24 -> http://192.168.1.24:8777
```

### Running that server automatically

A LaunchAgent keeps it up so nothing has to be started by hand. It is **not** in this
repo — it lives in the home directory and points at this checkout by absolute path:

```sh
~/Library/LaunchAgents/com.farsi-friends.server.plist
```

It runs the same `http.server` on port 8777 bound to `0.0.0.0`, starts at login, and
restarts if the process dies. Useful commands:

```sh
launchctl print gui/$UID/com.farsi-friends.server     # status and pid
launchctl kickstart -k gui/$UID/com.farsi-friends.server   # restart it
launchctl bootout gui/$UID/com.farsi-friends.server        # stop and disable
launchctl bootstrap gui/$UID ~/Library/LaunchAgents/com.farsi-friends.server.plist
```

Requests are logged to `.server.log` (gitignored). Because it binds `0.0.0.0`, anyone
on the same wifi can reach the folder — including `audio/original/`. That is the point
(it is how the iPad gets the recording), but if you'd rather it were reachable only
from this Mac, change `--bind 0.0.0.0` to `127.0.0.1` in the plist and kickstart it.

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
with a per-character voice and pitch. Persian edge-tts offers only two voices, so the
four characters are pitch-separated pairs:

| Character | Voice | Pitch |
|---|---|---|
| Koochooloo the hamster | Dilara | +60Hz |
| Khoroos Zari the rooster | Dilara | +15Hz |
| the Cat | Farid | +25Hz |
| the Fox | Farid | −30Hz |

Both scripts rewrite every file they know about. To add just a few lines without
re-downloading the rest, exec the source up to `async def main` to borrow the voice
constants and generate only your new entries.

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
