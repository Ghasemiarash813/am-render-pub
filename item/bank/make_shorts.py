"""5 vertical clip Shorts from Anunnaki-Gods-Kings-Visitors.mp4 via bank/cloud/shorts_lib.py. usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[46, 51, 52], hook="THE '12TH PLANET' SEAL?", title="The '12th planet' seal actually says 'your servant' #Shorts"),
 2: dict(shots=[39, 48, 49], hook="IS NIBIRU REAL?", title="Nibiru was never a hidden planet. Here's what the word means #Shorts"),
 3: dict(shots=[17, 18, 19, 21], hook="THE GODS WENT ON STRIKE", title="Sumerian gods went on strike, so they made humans (Atrahasis) #Shorts"),
 4: dict(shots=[32, 33, 34], hook="A KING BECOMES A GOD", title="Naram-Sin: the first king who made himself a god #Shorts"),
 5: dict(shots=[45, 53, 54], hook="ALIEN HANDBAGS?", title="Alien handbags and 'blazing rockets'? Two Anunnaki clues decoded #Shorts"),
}
TAGS = "#Anunnaki #Sumerian #AncientAliens #Nibiru #AncientMysteries"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Anunnaki-Gods-Kings-Visitors.mp4', 'The Anunnaki: Gods, Kings, or Aliens? What the Sumerian Tablets Really Say', CLIPS, TAGS, n)
