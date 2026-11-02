"""5 vertical clip Shorts from Moai-Walking.mp4 via bank/cloud/shorts_lib.py (hand-picked). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[34, 35, 36, 37], hook="18 PEOPLE. 4 TONNES.", title="18 people made a 4-tonne Easter Island statue walk. Here's how #Shorts"),
 2: dict(shots=[23, 24, 26, 28], hook="THEY FELL STANDING", title="How the fallen moai on Easter Island's roads prove they walked upright #Shorts"),
 3: dict(shots=[9, 10, 12], hook="STEEL-HARD STONE?", title="Von Daniken said the moai stone was 'steel-hard'. Rapa Nui carvers proved him wrong #Shorts"),
 4: dict(shots=[40, 41, 44, 45], hook="THE LEGEND WAS RIGHT", title="Rapa Nui always said the moai walked. Science finally caught up #Shorts"),
 5: dict(shots=[15, 16, 17, 18], hook="THEY HAVE BODIES", title="The Easter Island 'heads' have bodies, and no, they didn't come from a sunken continent #Shorts"),
}
TAGS = "#EasterIsland #Moai #RapaNui #AncientMysteries #AncientAliens"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Moai-Walking.mp4', "How Easter Island's Moai Really Moved: Aliens vs the Experiment (Rapa Nui)", CLIPS, TAGS, n)
