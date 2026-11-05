"""5 vertical clip Shorts from Rendlesham-Forest.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 10, 55], hook="BRITAIN'S ROSWELL?", title="Rendlesham Forest 1980: what did the airmen really see? #Shorts"),
 2: dict(shots=[16, 17, 18, 19], hook="THE LIGHT MOVED AWAY", title="Rendlesham: the airmen's first statements say they chased a light that moved away #Shorts"),
 3: dict(shots=[22, 23, 24, 48], hook="BINARY CODE... 30 YEARS LATER", title="The Rendlesham claims that only appeared decades after the night #Shorts"),
 4: dict(shots=[26, 27, 30, 31], hook="THE HALT TAPE", title="The Halt tape: a pulsing light, and a lighthouse that fits too well #Shorts"),
 5: dict(shots=[36, 37, 42, 55], hook="THE MEMO THAT STARTED IT", title="Halt's 1981 memo made Rendlesham Britain's most famous UFO case #Shorts"),
}
TAGS = "#Rendlesham #UFO #BritainsRoswell #AncientMysteries #Unexplained"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Rendlesham-Forest.mp4', "Rendlesham Forest 1980: UFO Landing or Lighthouse? The Case File", CLIPS, TAGS, n)
