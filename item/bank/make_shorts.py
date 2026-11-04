"""5 vertical clip Shorts from Oklo-Natural-Reactor.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3, 66], hook="A NATURAL NUCLEAR REACTOR?", title="A 2-billion-year-old nuclear reactor was found in Gabon. Natural or built? #Shorts"),
 2: dict(shots=[7, 8, 9, 10, 11], hook="THE MISSING URANIUM", title="France found uranium missing from a Gabon mine in 1972. The truth shocked scientists #Shorts"),
 3: dict(shots=[16, 17, 18, 19], hook="FISSION FINGERPRINTS", title="How isotopes proved Oklo was a real nuclear reactor two billion years ago #Shorts"),
 4: dict(shots=[33, 34, 35, 36, 37], hook="THE XENON HEARTBEAT", title="Trapped gas shows Oklo's reactor switched on and off every few hours #Shorts"),
 5: dict(shots=[42, 43, 44, 45, 46], hook="ANCIENT ALIEN TECH?", title="Did aliens build Oklo's reactor? What the evidence says #Shorts"),
}
TAGS = "#Oklo #NaturalReactor #Gabon #Uranium #AncientMysteries"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Oklo-Natural-Reactor.mp4', "Oklo: The 2-Billion-Year-Old Nuclear Reactor. Natural or Ancient Technology?", CLIPS, TAGS, n)
