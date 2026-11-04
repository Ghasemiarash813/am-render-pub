"""5 vertical clip Shorts from Gobekli-Tepe-Pillars.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3, 5], hook="BUILT BY HUNTERS?", title="11,600 years ago hunters raised 15-ton pillars. No farms, no metal. Who taught them? #Shorts"),
 2: dict(shots=[41, 42, 43, 52], hook="A COMET OR ALIENS?", title="Did a comet or aliens inspire Gobekli Tepe? What the evidence says #Shorts"),
 3: dict(shots=[23, 24, 25, 26], hook="THE STONE ZOO", title="Foxes, snakes, scorpions and vultures carved 11,600 years ago at Gobekli Tepe #Shorts"),
 4: dict(shots=[31, 32, 33, 34], hook="THE SKULL CULT", title="Carved and drilled skulls found at Gobekli Tepe. What they reveal #Shorts"),
 5: dict(shots=[56, 57, 52, 1], hook="WHAT IS NEXT?", title="Gobekli Tepe is 90% unexcavated. What could still be buried? #Shorts"),
}
TAGS = "#GobekliTepe #Archaeology #Turkey #Prehistory #AncientMysteries"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Gobekli-Tepe-Pillars.mp4', "Gobekli Tepe: The 11,600-Year-Old Temple Aliens Did Not Build", CLIPS, TAGS, n)
