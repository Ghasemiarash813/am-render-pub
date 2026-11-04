"""5 vertical clip Shorts from Westall-1966.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 17], hook="200 STUDENTS SAW WHAT?", title="Westall 1966: Australia's biggest UFO sighting. What did 200 students see? #Shorts"),
 2: dict(shots=[24, 25, 28, 30], hook="NO PHOTO. NO FILM.", title="The Westall UFO landing circle: why nobody has a single photo #Shorts"),
 3: dict(shots=[32, 33, 34, 36], hook="TOLD TO KEEP QUIET?", title="Were Westall students silenced by men in suits? What the 1966 papers say #Shorts"),
 4: dict(shots=[47, 48, 50], hook="A RUNAWAY BALLOON?", title="The Westall UFO balloon theory: a secret HIBAL launch, a missing memo and the weather #Shorts"),
 5: dict(shots=[55, 56, 64], hook="60 YEARS LATER", title="Westall UFO 60 years on: memory, contagion and our verdict #Shorts"),
}
TAGS = "#Westall #UFO #Australia #AncientMysteries #UAP"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Westall-1966.mp4', "Westall 1966: The Biggest UFO Sighting in Australia? We Gave the Case a Report Card", CLIPS, TAGS, n)
