"""5 vertical clip Shorts from Lycurgus-Cup.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 35, 63], hook="GREEN... THEN RED?", title="This 1,600-year-old Roman cup turns from green to red. Here's the real reason #Shorts"),
 2: dict(shots=[30, 31, 33, 35], hook="NANOPARTICLES IN ROMAN GLASS", title="An electron microscope found nanoparticles inside a Roman cup #Shorts"),
 3: dict(shots=[25, 26, 27, 28], hook="15 GRAMS OF GOLD", title="How the Romans hid gold in glass at 40 parts per million #Shorts"),
 4: dict(shots=[44, 45, 46, 49], hook="DID THEY KNOW?", title="Did the Romans understand their 'nanotechnology'? The evidence says no #Shorts"),
 5: dict(shots=[52, 55, 56], hook="ROMAN TRICK, MODERN TECH", title="A 1,600-year-old Roman trick inspired a modern sensor, and a 2026 replica #Shorts"),
}
TAGS = "#LycurgusCup #AncientRome #Nanotechnology #AncientMysteries #Archaeology"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Lycurgus-Cup.mp4', "The Lycurgus Cup: Did the Romans Really Have Nanotechnology?", CLIPS, TAGS, n)
