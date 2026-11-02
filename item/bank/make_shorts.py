"""5 vertical clip Shorts from Bosnian-Pyramids.mp4 via bank/cloud/shorts_lib.py (hand-picked). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[36, 39, 41], hook="A 28 kHz ENERGY BEAM?", title="The Bosnian pyramid 'energy beam': what a 28 kHz signal really means #Shorts"),
 2: dict(shots=[22, 23, 24], hook="ANCIENT CONCRETE?", title="Ancient concrete blocks in Bosnia? One clue says it's natural rock #Shorts"),
 3: dict(shots=[14, 15, 16], hook="HE ORDERED THE TEST", title="The Bosnian pyramid's own foundation drilled it. Here's what the cores showed #Shorts"),
 4: dict(shots=[21, 26, 27, 28], hook="STEPS MADE BY SHOVELS?", title="How a natural hill in Bosnia got 'pyramid steps' #Shorts"),
 5: dict(shots=[44, 45, 47], hook="34,000 YEARS OLD?", title="A 34,000-year-old pyramid? What the radiocarbon date really dated #Shorts"),
}
TAGS = "#BosnianPyramids #Visoko #AncientMysteries #Archaeology #Geology"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Bosnian-Pyramids.mp4', "Bosnian Pyramids: World's Largest Pyramid or Natural Hills? (Visoko Energy Beam Tested)", CLIPS, TAGS, n)
