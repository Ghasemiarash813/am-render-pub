"""5 vertical clip Shorts from Nazca-Mummies.mp4 via bank/cloud/shorts_lib.py (hand-picked). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[16, 17, 18], hook="A FINGER GLUED BACKWARDS", title="The 'alien' three-fingered hand from Nazca: human bones, one glued in backwards #Shorts"),
 2: dict(shots=[21, 22, 23], hook="THE 'ALIEN' SKULL WAS A LLAMA", title="X-rays of the 'alien' Nazca figures: a llama skull and bird bones #Shorts"),
 3: dict(shots=[32, 33, 34, 35], hook="1,000 YEARS OLD = ALIEN?", title="The carbon date shown to Mexico's Congress, and what the lab actually said #Shorts"),
 4: dict(shots=[38, 40, 41], hook="'UNKNOWN DNA'?", title="The Nazca mummies' 'unknown DNA' was re-checked. It's modern human contamination #Shorts"),
 5: dict(shots=[1, 2, 3, 59], hook="ALIENS SHOWN TO CONGRESS?", title="Two 'alien bodies' were shown to Mexico's Congress. Here's what the scans show #Shorts"),
}
TAGS = "#NazcaMummies #Aliens #UFO #AncientMysteries #Peru"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Nazca-Mummies.mp4', "The 'Alien' Nazca Mummies: What the Scans Really Show", CLIPS, TAGS, n)
