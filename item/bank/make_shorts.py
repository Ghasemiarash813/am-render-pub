"""5 vertical clip Shorts from Mohenjo-Daro.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3, 4], hook="NUKED IN 2000 BC?", title="Was an ancient Indus city destroyed by an atomic bomb? We traced the claim #Shorts"),
 2: dict(shots=[20, 22, 23, 24], hook="THE MASSACRE THAT WASN'T", title="Mohenjo-daro's skeletons: the 'massacre' that never happened #Shorts"),
 3: dict(shots=[28, 32, 33, 34], hook="MELTED BY A BOMB?", title="The 'vitrified' Mohenjo-daro bricks: atomic glass or kiln waste? #Shorts"),
 4: dict(shots=[37, 40, 41], hook="RADIOACTIVE BONES?", title="Radioactive skeletons at Mohenjo-daro? The physics says no #Shorts"),
 5: dict(shots=[47, 48, 49], hook="A SOURCE THAT NEVER EXISTED", title="The fake magazine behind the 'ancient nuclear war' legend #Shorts"),
}
TAGS = "#MohenjoDaro #IndusValley #AncientMysteries #Archaeology #AncientAliens"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Mohenjo-Daro.mp4', "Mohenjo-daro: Destroyed by an Ancient Nuclear Bomb? We Traced the Claim to Its Source", CLIPS, TAGS, n)
