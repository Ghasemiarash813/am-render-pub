"""5 vertical clip Shorts from Nimrud-Lens.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3], hook="3,000-YEAR-OLD TELESCOPE?", title="Did the Assyrians have a telescope? The Nimrud lens #Shorts"),
 2: dict(shots=[21, 22, 23, 24], hook="3X MAGNIFICATION", title="The Nimrud lens really magnifies: what it was used for #Shorts"),
 3: dict(shots=[28, 29, 30, 31], hook="COULD IT START A FIRE?", title="Nimrud lens: could it burn like a magnifying glass? #Shorts"),
 4: dict(shots=[35, 36, 37, 38], hook="SATURN'S RINGS IN 700 BC?", title="The 1999 claim: Assyrians saw Saturn's rings #Shorts"),
 5: dict(shots=[47, 48, 49, 50], hook="THE BORING TRUTH?", title="What the British Museum thinks the Nimrud lens really was #Shorts"),
}
TAGS = "#NimrudLens #Assyria #Archaeology #AncientMachines #AncientMystery"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Nimrud-Lens.mp4', 'The Nimrud Lens: Assyrian Telescope or Jewel?', CLIPS, TAGS, n)
