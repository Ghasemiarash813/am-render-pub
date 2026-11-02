"""5 vertical clip Shorts from Longyou-Caves.mp4 via bank/cloud/shorts_lib.py (hand-picked). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3, 9], hook="THE 'BOTTOMLESS' POND", title="Farmers pumped a 'bottomless' pond for 17 days and found a giant carved hall #Shorts"),
 2: dict(shots=[15, 22, 23, 25], hook="ALIEN DRILL MARKS?", title="The Longyou 'machine marks' vs the iron chisel found inside the caves #Shorts"),
 3: dict(shots=[29, 31, 32], hook="THEY READ THE ROCK", title="2,000-year-old cave builders cut roofs along the rock layers, and dug test tunnels #Shorts"),
 4: dict(shots=[16, 37, 41, 42], hook="WHERE DID 900,000 M³ GO?", title="Where did the Longyou Caves' missing stone go? Follow the river #Shorts"),
 5: dict(shots=[46, 48, 49], hook="HOW OLD ARE THEY?", title="Han pottery or Song jars? The real mystery of the Longyou Caves is the date #Shorts"),
}
TAGS = "#LongyouCaves #China #AncientMysteries #AncientAliens #Archaeology"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Longyou-Caves.mp4', "Longyou Caves: Alien Drill Marks or Ancient Chinese Quarry? (China's Hidden Giant Halls Tested)", CLIPS, TAGS, n)
