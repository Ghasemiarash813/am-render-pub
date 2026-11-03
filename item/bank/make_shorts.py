"""5 vertical clip Shorts from Tassili-Great-Martian-God.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 25, 63], hook="ALIEN IN A HELMET?", title="Is the Sahara's 'Great Martian God' an astronaut? What the painting really shows #Shorts"),
 2: dict(shots=[47, 48, 49], hook="A JOKE WENT VIRAL", title="How a nickname became 'proof' of ancient aliens: the Tassili Martian God #Shorts"),
 3: dict(shots=[42, 43, 44], hook="THEY SPONGED THE ART", title="Explorers sponged ancient Sahara paintings to photograph them. The damage #Shorts"),
 4: dict(shots=[31, 32, 33], hook="ROUND HEADS WORE MASKS", title="The Sahara's 'alien' round heads were dancers in masks, not astronauts #Shorts"),
 5: dict(shots=[21, 22, 23, 25], hook="THE GIANT OF JABBAREN", title="The giant painted figure of Jabbaren, no face, no eyes: helmet or just a round head? #Shorts"),
}
TAGS = "#Tassili #GreatMartianGod #AncientAliens #Sahara #AncientMysteries"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Tassili-Great-Martian-God.mp4', "The Great Martian God of the Sahara: Alien in a Spacesuit or Ancient Ritual Mask? (Tassili n'Ajjer)", CLIPS, TAGS, n)
