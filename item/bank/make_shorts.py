"""5 vertical clip Shorts from Saqqara-Bird.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 14, 33, 63], hook="A PLANE FROM 200 BC?", title="A 2,200-year-old Egyptian 'model plane'? We tested whether it can fly #Shorts"),
 2: dict(shots=[17, 18, 19, 20], hook="HOW A MYTH GREW", title="How the Saqqara Bird got a 'groove', landing gear and secret papyri it never had #Shorts"),
 3: dict(shots=[39, 40, 41, 42], hook="4x ITS WEIGHT IN LIFT?", title="The wind-tunnel test that 'proved' the Saqqara Bird flies, and the catch #Shorts"),
 4: dict(shots=[46, 48, 49, 51], hook="WE SCANNED THE REAL ONE", title="Engineers simulated the real Saqqara Bird from a 3D scan. It cannot fly straight #Shorts"),
 5: dict(shots=[34, 53, 54, 55], hook="WHAT THE FIN WAS FOR", title="Why does an ancient Egyptian bird have an aeroplane tail? The likely answer #Shorts"),
}
TAGS = "#SaqqaraBird #AncientEgypt #AncientMysteries #Archaeology #AncientAliens"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Saqqara-Bird.mp4', "The Saqqara Bird: A 2,200-Year-Old Model Glider? We Flight-Tested the Claim", CLIPS, TAGS, n)
