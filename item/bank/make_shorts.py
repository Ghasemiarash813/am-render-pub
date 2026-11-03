"""5 vertical clip Shorts from Gold-Flyers.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3, 63], hook="A JET FROM 1,000 YEARS AGO?", title="Gold 'fighter jets' from ancient Colombia? We identified the species #Shorts"),
 2: dict(shots=[25, 26, 31, 32], hook="THE FISH THAT LOOKS LIKE A JET", title="Why these ancient gold 'airplanes' are almost certainly fish #Shorts"),
 3: dict(shots=[37, 38, 40, 41], hook="THE 'GOLDFLYER' THAT FLEW", title="The 1994 model of the Quimbaya 'jet' flew. Here is what they added #Shorts"),
 4: dict(shots=[46, 47, 48, 50], hook="WIND TUNNEL VS GOLD JET", title="Engineers scanned an ancient gold 'airplane' and put it in a wind tunnel #Shorts"),
 5: dict(shots=[12, 14, 15, 17], hook="THE LINE THAT SOLD THE MYTH", title="'No insect has wings at the bottom, so it's a plane' and the logic gap #Shorts"),
}
TAGS = "#Quimbaya #TolimaJets #AncientMysteries #AncientAliens #Colombia"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Gold-Flyers.mp4', "Ancient Colombian Gold 'Jets': Aircraft or Fish? We Identified the Species", CLIPS, TAGS, n)
