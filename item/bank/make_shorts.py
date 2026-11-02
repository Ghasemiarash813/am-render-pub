"""5 vertical clip Shorts from Ark-of-the-Covenant-Machine.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[28, 29, 51, 52], hook="ELECTROCUTED BY THE ARK?", title="Did the Ark of the Covenant kill Uzzah with electricity? We ran the numbers #Shorts"),
 2: dict(shots=[11, 12, 13], hook="OLDER THAN THE LIGHT BULB", title="The 'electric Ark' theory is older than the light bulb #Shorts"),
 3: dict(shots=[34, 35, 36], hook="THE HIGH PRIEST'S ROPE?", title="The rope tied to the high priest's ankle? No ancient source mentions it #Shorts"),
 4: dict(shots=[37, 38, 39], hook="TUTANKHAMUN'S 'ARK'", title="Tutankhamun was buried with a gold chest on carrying poles #Shorts"),
 5: dict(shots=[42, 43, 44, 46], hook="WHERE IS THE ARK?", title="Where is the Ark of the Covenant today? Babylon, Mount Nebo or Axum #Shorts"),
}
TAGS = "#ArkOfTheCovenant #AncientMysteries #BiblicalArchaeology #AncientAliens #History"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Ark-of-the-Covenant-Machine.mp4', 'The Ark of the Covenant: Ancient Machine or Sacred Shrine?', CLIPS, TAGS, n)
