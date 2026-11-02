"""5 vertical clip Shorts from Bimini-Road.mp4 via bank/cloud/shorts_lib.py (hand-picked). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[3, 8, 11], hook="CAYCE SAID '68 AND '69", title="Edgar Cayce predicted Atlantis would rise in '68 and '69. Then the Bimini Road was found #Shorts"),
 2: dict(shots=[24, 26, 28, 29], hook="17 CORES. ONE TEST.", title="The clever test that showed the Bimini Road was never built #Shorts"),
 3: dict(shots=[16, 19, 20, 21], hook="HOW OLD IS IT?", title="Radiocarbon vs Atlantis: how old the Bimini Road really is #Shorts"),
 4: dict(shots=[43, 44, 45, 46], hook="ATLANTIS COLUMNS?", title="The 'Atlantis columns' near Bimini were 1800s cement barrels #Shorts"),
 5: dict(shots=[48, 49, 51, 53], hook="NATURE CAN'T DRAW LINES?", title="Nature can't make straight stone roads? These beachrock roads say otherwise #Shorts"),
}
TAGS = "#BiminiRoad #Atlantis #EdgarCayce #AncientMysteries #Geology"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Bimini-Road.mp4', "Bimini Road: Edgar Cayce's Atlantis Highway or Natural Beachrock? (The Underwater Road Tested)", CLIPS, TAGS, n)
