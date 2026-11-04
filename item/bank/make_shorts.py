"""5 vertical clip Shorts from Puma-Punku.mp4 via bank/cloud/shorts_lib.py (hand-picked). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3, 20], hook="MACHINED BY ALIENS?", title="Puma Punku's razor-sharp H-blocks: lost technology or patient masons? #Shorts"),
 2: dict(shots=[11, 12, 13, 16], hook="131 TONNES. HOW?", title="How did Tiwanaku move 131-tonne stone slabs with no wheels or iron? #Shorts"),
 3: dict(shots=[29, 30, 33], hook="WE TESTED THE CLAIM", title="Archaeologists carved andesite with flint and hematite. The result? #Shorts"),
 4: dict(shots=[35, 36, 37, 38], hook="METAL IN THE STONE", title="Puma Punku's cast metal cramps: what they prove about the builders #Shorts"),
 5: dict(shots=[50, 52, 53, 54], hook="ALIENS? THE VERDICT", title="Puma Punku verdict: machined stone or patient masons? #Shorts"),
}
TAGS = "#PumaPunku #Tiwanaku #AncientMysteries #Archaeology #AncientAliens"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Puma-Punku.mp4', "Puma Punku: Were the H-Blocks Machined by Lost Technology? We Audited the Claim", CLIPS, TAGS, n)
