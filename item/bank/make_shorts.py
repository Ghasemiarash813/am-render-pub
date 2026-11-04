"""5 vertical clip Shorts from Hill-Abduction-1961.mp4 via bank/cloud/shorts_lib.py (hand-picked, each <=55.5 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 12, 20], hook="2 HOURS VANISHED?", title="Betty and Barney Hill: two missing hours on a dark road in 1961 #Shorts"),
 2: dict(shots=[18, 19, 20, 29], hook="WAS IT JUST JUPITER?", title="The Hill abduction: a bright planet, a long night drive, or something else? #Shorts"),
 3: dict(shots=[31, 32, 34, 36], hook="THE STAR MAP CLAIM", title="Betty Hill's star map: does it really point to Zeta Reticuli? #Shorts"),
 4: dict(shots=[38, 39, 41, 43], hook="CAN HYPNOSIS BE TRUSTED?", title="Hypnosis and the Hill case: what memory research says #Shorts"),
 5: dict(shots=[45, 46, 48, 50], hook="THE TV EPISODE BEFORE", title="An Outer Limits episode aired before Barney Hill described the aliens #Shorts"),
}
TAGS = "#BettyAndBarneyHill #UFO #AlienAbduction #AncientMysteries #Documentary"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Hill-Abduction-1961.mp4', "Betty and Barney Hill: The 1961 Abduction Case Examined, Evidence vs Theory", CLIPS, TAGS, n)
