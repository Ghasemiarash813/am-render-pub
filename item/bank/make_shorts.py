"""5 vertical clip Shorts from Kelly-Hopkinsville-1955.mp4 via bank/cloud/shorts_lib.py (hand-picked, each <=55 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 14, 33, 63], hook="LITTLE MEN, 1955?", title="Kelly-Hopkinsville 1955: a family fought 'little men' for four hours #Shorts"),
 2: dict(shots=[17, 18, 19, 20], hook="THE BULLETS RANG LIKE A BUCKET", title="They shot the creature point blank. It flipped and ran. The Kelly siege #Shorts"),
 3: dict(shots=[26, 27, 28, 29], hook="POLICE FOUND BULLET HOLES", title="Police and soldiers searched the farm at Kelly, Kentucky. What they found #Shorts"),
 4: dict(shots=[42, 43, 44, 45], hook="OR JUST AN OWL?", title="Great horned owls: the skeptic's explanation for the Kelly 'aliens' #Shorts"),
 5: dict(shots=[50, 51, 52, 53], hook="WHAT THE EVIDENCE SAYS", title="Kelly-Hopkinsville: evidence vs the alien theory, and the verdict #Shorts"),
}
TAGS = "#KellyHopkinsville #UFO #AncientMysteries #Unexplained #Aliens"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Kelly-Hopkinsville-1955.mp4', "The Kelly-Hopkinsville Siege (1955): Aliens or Owls?", CLIPS, TAGS, n)
