"""5 vertical clip Shorts from Kaikoura-Lights-1978.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3, 5], hook="ALIEN ESCORT AT 30,000 FT?", title="A cargo plane, a TV crew and mystery lights off New Zealand in 1978. What were they? #Shorts"),
 2: dict(shots=[27, 28, 31, 32], hook="WAS IT JUST VENUS?", title="Kaikoura UFO: Venus explains some lights, but not all. Here is the timing problem #Shorts"),
 3: dict(shots=[33, 34, 35], hook="THE WINDOW TRICK", title="Scientists recreated the famous Kaikoura UFO flares with a torch and a window #Shorts"),
 4: dict(shots=[37, 38, 39, 41], hook="RADAR SAW IT TOO?", title="Kaikoura 1978: Wellington radar tracked it. Why that does not prove aliens #Shorts"),
 5: dict(shots=[43, 44, 47, 52], hook="THE SCIENTIST WHO DISAGREED", title="A physicist said the Kaikoura UFO was building-sized. Skeptics disagree #Shorts"),
}
TAGS = "#Kaikoura #UFO #UAP #NewZealand #AncientMysteries"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Kaikoura-Lights-1978.mp4', "Kaikoura 1978: The UFO Filmed From a Cargo Plane. What Really Happened?", CLIPS, TAGS, n)
