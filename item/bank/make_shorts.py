"""5 vertical clip Shorts from Eye-of-the-Sahara-Atlantis.mp4 via bank/cloud/shorts_lib.py (hand-picked). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[21, 29, 30, 31], hook="ATLANTIS = 23.5 KM?", title="The '127 stadia' Atlantis math behind the Eye of the Sahara doesn't add up #Shorts"),
 2: dict(shots=[25, 41, 42, 63], hook="AN ALIEN EYE IN THE SAHARA?", title="Alien beacon or impact scar? What the Eye of the Sahara's rocks say #Shorts"),
 3: dict(shots=[37, 38, 40], hook="100 MILLION YEARS OLD", title="How the Eye of the Sahara really formed: a dome, not a city #Shorts"),
 4: dict(shots=[44, 45, 46, 49], hook="WHERE'S THE OCEAN?", title="Atlantis sank into the sea. The Eye of the Sahara sits 485 m above it #Shorts"),
 5: dict(shots=[52, 53, 54, 58], hook="WHO REALLY LIVED HERE?", title="The real people of the Eye of the Sahara left hand axes, not a city #Shorts"),
}
TAGS = "#Atlantis #RichatStructure #EyeOfTheSahara #AncientMysteries #AncientAliens"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Eye-of-the-Sahara-Atlantis.mp4', "The Eye of the Sahara: Is the Richat Structure Really Atlantis? (Plato's Text vs the Rock)", CLIPS, TAGS, n)
