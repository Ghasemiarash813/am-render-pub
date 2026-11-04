"""5 vertical clip Shorts from Mantell-1948.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 19, 22, 29], hook="DIED CHASING A UFO?", title="1948: A decorated pilot chased a UFO to his death. What was it really? #Shorts"),
 2: dict(shots=[23, 24, 25, 26], hook="THE RULE HE BROKE", title="Why Captain Mantell blacked out at 25,000 ft: the oxygen rule every pilot knew #Shorts"),
 3: dict(shots=[40, 41, 42, 43, 44], hook="SHOT DOWN BY A RAY?", title="Mantell 1948: the 'ray', the bullets, the radioactive wreck: what the report found #Shorts"),
 4: dict(shots=[47, 49, 50, 51], hook="WAS IT VENUS?", title="The Venus explanation for the Mantell UFO crash: why even its author took it back #Shorts"),
 5: dict(shots=[55, 56, 59, 63], hook="THE SECRET BALLOON", title="The classified Skyhook balloon behind the Mantell UFO case, and the missing launch record #Shorts"),
}
TAGS = "#Mantell #UFO #Skyhook #ProjectBlueBook #AncientMachines"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Mantell-1948.mp4', "Captain Mantell 1948: The Pilot Who Chased a UFO to His Death (Evidence vs Theory)", CLIPS, TAGS, n)
