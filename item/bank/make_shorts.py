"""5 vertical clip Shorts from Vitrified-Forts.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=55 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3, 5], hook="ROCK MELTED INTO GLASS?", title="Scotland's hilltop forts have walls melted into glass. Lasers? #Shorts"),
 2: dict(shots=[26, 27, 28, 29], hook="THEY BURNED A WALL ON PURPOSE", title="In the 1930s archaeologists burned a wall to test the melted-fort mystery #Shorts"),
 3: dict(shots=[33, 34, 35, 36], hook="28 HOURS OF FIRE", title="A TV crew burned a full-size Iron Age wall for 28 hours. It barely melted #Shorts"),
 4: dict(shots=[39, 41, 42], hook="1,100 DEGREES, FOR HOURS", title="How hot did the Iron Age fires get? Hotter than a blacksmith's forge #Shorts"),
 5: dict(shots=[52, 53, 54, 55], hook="ANCIENT NUCLEAR BLAST?", title="Four tests show why Scotland's melted forts were not an ancient atomic blast #Shorts"),
}
TAGS = "#VitrifiedForts #Scotland #IronAge #AncientMysteries #Archaeology"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Vitrified-Forts.mp4', "Scotland's Vitrified Forts: Ancient Lasers or Burning Ramparts?", CLIPS, TAGS, n)
