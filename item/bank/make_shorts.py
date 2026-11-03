"""5 vertical clip Shorts from Dogon-Sirius-B.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3, 5], hook="A STAR NO EYE CAN SEE", title="A Mali tribe 'knew' an invisible star. Aliens, or something else? #Shorts"),
 2: dict(shots=[17, 18, 19, 20], hook="THE DIGITARIA STAR", title="What the Dogon actually told researchers about Sirius B #Shorts"),
 3: dict(shots=[23, 24, 25, 28], hook="THE BOOK THAT MADE IT FAMOUS", title="How The Sirius Mystery turned a Mali tribe into 'proof' of aliens #Shorts"),
 4: dict(shots=[40, 41, 42, 43], hook="WE ASKED THEM AGAIN", title="An anthropologist returned to the Dogon. He found no Sirius B secret #Shorts"),
 5: dict(shots=[53, 54, 55, 58], hook="THE ALIEN TEST", title="Temple's Sirius C test: what astronomers found #Shorts"),
}
TAGS = "#Dogon #SiriusB #SiriusMystery #AncientMysteries #AncientAliens"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Dogon-Sirius-B.mp4', "The Dogon and Sirius B: How Did a Mali Tribe Know About an Invisible Star?", CLIPS, TAGS, n)
