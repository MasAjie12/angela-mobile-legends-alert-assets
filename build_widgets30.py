# -*- coding: utf-8 -*-
"""Re-skin hardened theme 29 widgets for Angela Mobile Legends."""
from pathlib import Path
import re

BASE = Path(__file__).parent
SRC = BASE.parent / "29-blue-butterfly" / "widgets"
DST = BASE / "widgets"
DST.mkdir(exist_ok=True)
RAW_BG = "https://raw.githubusercontent.com/MasAjie12/angela-mobile-legends-alert-assets/main/bg.png"
RAW_TOP = "https://raw.githubusercontent.com/MasAjie12/angela-mobile-legends-alert-assets/main/hiasankananatas.png"
RAW_BOTTOM = "https://raw.githubusercontent.com/MasAjie12/angela-mobile-legends-alert-assets/main/hiasankananbawah.png"

SWAPS = [
    ("https://raw.githubusercontent.com/MasAjie12/blue-butterfly-alert-assets/main/bgkupu.jpg", RAW_BG),
    ("https://raw.githubusercontent.com/MasAjie12/blue-butterfly-alert-assets/main/kupu.png", RAW_TOP),
    ("#4FA8FF", "#F39BC8"), ("#2E7DFF", "#B86AD9"), ("#1E5FA8", "#70408D"),
    ("#9FD4FF", "#FFD0EA"), ("#BFE3FF", "#FFE6F5"), ("#EAF6FF", "#FFF8FD"),
    ("#0A2C52", "#5B4D9A"), ("#03101E", "#24184F"), ("#0B2E52", "#70408D"),
    ("#04182E", "#321A68"), ("#04101A", "#211145"), ("#061B33", "#3A2670"),
    ("79,168,255", "243,155,200"), ("79, 168, 255", "243, 155, 200"),
    ("46,125,255", "184,106,217"), ("46, 125, 255", "184, 106, 217"),
    ("30,95,168", "112,64,141"), ("30, 95, 168", "112, 64, 141"),
    ("11,46,82", "112,64,141"), ("11, 46, 82", "112, 64, 141"),
    ("4,24,48", "50,26,104"), ("4, 24, 48", "50, 26, 104"),
    ("🦋", "💗"), ("BLUE BUTTERFLY", "ANGELA SWEETHEART"),
    ("bf29-", "an30-"), ("t29", "t30"),
]
LEFTOVER = ["blue-butterfly", "bgkupu", "kupu.png", "bf29-", "t29", "BLUE BUTTERFLY", "#4FA8FF", "#2E7DFF"]

WIDGET_POLISH = '''
/* t30 Angela widget polish: keep artwork on alert card only */
.card,.subathon-container,#ms_container,#__next > div{position:relative!important;isolation:isolate!important;overflow:hidden!important}
.card .card-header,.sub_judul,.style-1.text-container{text-shadow:0 0 10px rgba(255,188,226,.62)!important}
'''

def transform(text):
    for old, new in SWAPS:
        text = text.replace(old, new)
    text = text.replace('inset:0 auto 0 -45%;', 'top:0;bottom:0;left:-45%;')
    return text + WIDGET_POLISH

files = sorted(SRC.glob("*.css"))
for src in files:
    text = transform(src.read_text(encoding="utf-8"))
    (DST / src.name).write_text(text, encoding="utf-8")
    bad = [word for word in LEFTOVER if word in text]
    assert not bad, f"{src.name}: leftover {bad}"
    assert "inset:" not in text, f"{src.name}: unsupported inset shorthand"
    assert text.count("{") == text.count("}"), f"{src.name}: brace imbalance"
    print("widget", src.name, len(text.encode()))

print("OK widgets", len(files))
assert len(files) >= 20
