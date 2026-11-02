"""5 vertical clip Shorts from Kailasa-Temple.mp4 via bank/cloud/shorts_lib.py (hand-picked). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[3, 37, 39], hook="400,000 TONS IN 18 YEARS?", title="'Impossible without aliens'? Do the maths on Kailasa's 400,000 tons #Shorts"),
 2: dict(shots=[23, 24, 25, 26], hook="LASERS? LOOK AT THE WALLS", title="Alien lasers at Ellora? The walls of Kailasa are covered in chisel marks #Shorts"),
 3: dict(shots=[29, 30, 32, 33], hook="A TEMPLE FROZEN HALFWAY", title="This unfinished temple shows exactly how Kailasa was carved top-down #Shorts"),
 4: dict(shots=[42, 43, 44, 45], hook="WHERE DID THE ROCK GO?", title="Kailasa's missing rubble: the one real mystery at Ellora #Shorts"),
 5: dict(shots=[14, 15, 16, 64], hook="EVEN THE ARCHITECT WAS AMAZED", title="A 1,200-year-old copper plate says even Kailasa's architect was amazed #Shorts"),
}
TAGS = "#Kailasa #Ellora #AncientAliens #India #Archaeology"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Kailasa-Temple.mp4', "Kailasa Temple: Carved From One Rock by Aliens? The 400,000-Ton Claim Tested (Ellora Cave 16)", CLIPS, TAGS, n)
