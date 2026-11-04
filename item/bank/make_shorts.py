"""5 vertical clip Shorts from Tiwanaku-Gate-of-the-Sun.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=55 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 12, 63], hook="A GATE NO HUMANS COULD CARVE?", title="Is the Gate of the Sun at Tiwanaku alien? We dug into the claims #Shorts"),
 2: dict(shots=[20, 22, 23], hook="15,000 YEARS OLD?", title="The 15,000 BC date for Tiwanaku, and why it was debunked #Shorts"),
 3: dict(shots=[38, 39, 40, 42], hook="MACHINE-CUT H-BLOCKS?", title="Pumapunku's H-blocks: machine-cut by aliens, or a kit of repeating parts? #Shorts"),
 4: dict(shots=[32, 33, 35], hook="HOW DID THEY CUT IT?", title="How Tiwanaku's masons cut andesite with stone tools and rope, tested #Shorts"),
 5: dict(shots=[55, 56, 57, 58], hook="WHAT KILLED TIWANAKU?", title="No fire from the sky: how drought ended the city of Tiwanaku #Shorts"),
}
TAGS = "#Tiwanaku #GateOfTheSun #AncientMysteries #Archaeology #AncientAliens"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Tiwanaku-Gate-of-the-Sun.mp4', "Tiwanaku & the Gate of the Sun: Lost High-Tech City or Andean Masterpiece?", CLIPS, TAGS, n)
