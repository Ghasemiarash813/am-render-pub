"""5 vertical clip Shorts from Tall-el-Hammam.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3, 4], hook="A COMET DESTROYED SODOM?", title="A comet blast wiped out a Bronze Age city in Jordan? A top journal said yes, then took it back #Shorts"),
 2: dict(shots=[29, 30, 31, 32], hook="THE PAPER WAS RETRACTED", title="The famous Sodom airburst paper was retracted in 2025. Here is why #Shorts"),
 3: dict(shots=[20, 21, 22, 23], hook="MELTED BY A COMET?", title="Tiny glass beads, shocked quartz and 2000 degrees: the airburst evidence explained #Shorts"),
 4: dict(shots=[34, 35, 36, 37, 41], hook="WHAT REALLY BURNED IT?", title="Tall el-Hammam was a real city that really burned. But what burned it? #Shorts"),
 5: dict(shots=[51, 52, 53, 54], hook="TUNGUSKA VS HAMMAM", title="Real airbursts flattened forests but never melted cities. Why Hammam does not fit #Shorts"),
}
TAGS = "#TallElHammam #Sodom #Archaeology #AncientMysteries #Airburst"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Tall-el-Hammam.mp4', "Did a Comet Destroy Sodom? Tall el-Hammam and the Retracted Airburst Paper", CLIPS, TAGS, n)
