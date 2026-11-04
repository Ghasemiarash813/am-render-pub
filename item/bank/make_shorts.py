"""5 vertical clip Shorts from Gunung-Padang.mp4 via bank/cloud/shorts_lib.py. usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3], hook="WORLD'S OLDEST PYRAMID?", title="Gunung Padang: is this Indonesian hill the world's oldest pyramid? #Shorts"),
 2: dict(shots=[11, 12, 13], hook="RADAR SAW CHAMBERS?", title="Gunung Padang radar claims: hidden chambers under a Java hill #Shorts"),
 3: dict(shots=[22, 23, 24], hook="NATURE MADE THESE?", title="Gunung Padang's stone columns: natural volcanic rock, say geologists #Shorts"),
 4: dict(shots=[32, 33, 34], hook="PAPER RETRACTED", title="The 27,000-year-old pyramid paper that was retracted in 2024 #Shorts"),
 5: dict(shots=[50, 51, 52], hook="THE VERDICT", title="Gunung Padang verdict: temple on a volcano, not a lost pyramid #Shorts"),
}
TAGS = "#GunungPadang #Pyramid #Indonesia #UnsolvedMysteries #Archaeology"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Gunung-Padang.mp4', "Gunung Padang: The World's Oldest Pyramid, or a Volcano With a Temple?", CLIPS, TAGS, n)
