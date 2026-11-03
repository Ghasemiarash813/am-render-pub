"""5 vertical clip Shorts from Abydos-Helicopter-Hieroglyphs.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 34, 63], hook="A HELICOPTER IN 1290 BC?", title="A helicopter carved in an Egyptian temple 3,300 years ago? What it really is #Shorts"),
 2: dict(shots=[15, 16, 17], hook="THE FAMOUS PHOTO WAS EDITED", title="The viral 'Abydos helicopter' photo was retouched. Here's the giveaway #Shorts"),
 3: dict(shots=[33, 34, 35], hook="TWO KINGS, ONE STONE", title="The Abydos helicopter is two pharaohs' names carved on top of each other #Shorts"),
 4: dict(shots=[39, 40, 42], hook="HIDDEN UNDER PLASTER", title="Ramesses II hid his father's words under plaster. 3,000 years later they came back #Shorts"),
 5: dict(shots=[49, 50, 53], hook="WHAT THE 'HELICOPTER' SAYS", title="We translated the Abydos 'helicopter' hieroglyphs. It's a royal boast #Shorts"),
}
TAGS = "#Abydos #AncientEgypt #AncientMysteries #Hieroglyphs #AncientAliens"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Abydos-Helicopter-Hieroglyphs.mp4', "The Abydos Helicopter Hieroglyphs: Ancient Aircraft or Re-Carved Titles? A Forensic Case File", CLIPS, TAGS, n)
