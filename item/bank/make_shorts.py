"""5 vertical clip Shorts from Costa-Rica-Stone-Spheres.mp4 via bank/cloud/shorts_lib.py (hand-picked). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[2, 22, 24, 26], hook="'PERFECT TO 2 MM'?", title="Costa Rica's 'perfect' stone spheres were measured with a tape and a fishing line #Shorts"),
 2: dict(shots=[45, 46, 47, 48], hook="DYNAMITED FOR GOLD", title="Banana workers blew up ancient stone spheres looking for gold. There was none #Shorts"),
 3: dict(shots=[13, 14, 15, 16], hook="NO METAL. NO LASERS.", title="How do you carve a giant stone sphere with fire, water and river stones? #Shorts"),
 4: dict(shots=[34, 35, 36, 37], hook="POINTING TO ATLANTIS?", title="Do Costa Rica's stone spheres point to Atlantis, Easter Island and Stonehenge? #Shorts"),
 5: dict(shots=[41, 42, 43, 44], hook="THE THUNDER GOD'S CANNONBALLS", title="Buried by floods, saved by silt: the Bribri story of Tara's cannonballs #Shorts"),
}
TAGS = "#StoneSpheres #CostaRica #LasBolas #AncientMysteries #Archaeology"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Costa-Rica-Stone-Spheres.mp4', "Costa Rica's Stone Spheres: Alien Orbs, Atlantis Markers or Ancient Craft? (Las Bolas Tested)", CLIPS, TAGS, n)
