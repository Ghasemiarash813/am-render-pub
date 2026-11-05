"""5 vertical clip Shorts from Maury-Island.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[2, 9, 10, 22], hook="6 UFOs OVER PUGET SOUND?", title="Maury Island 1947: the first UFO 'cover-up' that wasn't #Shorts"),
 2: dict(shots=[20, 21, 22, 23], hook="ALIEN METAL OR SLAG?", title="The 'alien' debris from Maury Island 1947 looked exactly like local slag #Shorts"),
 3: dict(shots=[28, 29, 30, 31], hook="THE B-25 THAT FELL", title="The 1947 B-25 crash at Kelso that gave Maury Island its dark legend #Shorts"),
 4: dict(shots=[36, 39, 40, 41], hook="THE FIRST MAN IN BLACK?", title="Did a man in black warn Harold Dahl? What the FBI file really says #Shorts"),
 5: dict(shots=[44, 45, 46, 50], hook="HOAX? FOLLOW THE MONEY", title="Maury Island hoax: the dog, the slag and the pulp magazine #Shorts"),
}
TAGS = "#MauryIsland #UFO #AncientMysteries #Archaeology #AncientAliens"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Maury-Island.mp4', "Maury Island 1947: The UFO Cover-Up That Was Never Proven", CLIPS, TAGS, n)
