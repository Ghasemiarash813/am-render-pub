"""5 vertical clip Shorts from Dyatlov-Pass-1959.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 62], hook="NINE HIKERS. ONE CUT TENT.", title="Dyatlov Pass 1959: nine hikers cut their way out of a tent #Shorts"),
 2: dict(shots=[20, 21, 22, 23], hook="CUT FROM INSIDE", title="Dyatlov Pass: the tent was cut open from the inside #Shorts"),
 3: dict(shots=[28, 29, 30], hook="THE PINE TREE FIRE", title="Dyatlov Pass: the first two bodies and the broken pine #Shorts"),
 4: dict(shots=[49, 50], hook="THE ORANGE LIGHTS", title="Dyatlov Pass: the orange spheres and the 1990 admission #Shorts"),
 5: dict(shots=[55, 56], hook="AVALANCHE SOLVED IT?", title="Dyatlov Pass: the 2021 snow-slab simulation explained #Shorts"),
}
TAGS = "#DyatlovPass #UFO #UnsolvedMysteries #Russia #Avalanche"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Dyatlov-Pass-1959.mp4', "Dyatlov Pass 1959: Nine Hikers, a Cut Tent and the Lights in the Sky", CLIPS, TAGS, n)
