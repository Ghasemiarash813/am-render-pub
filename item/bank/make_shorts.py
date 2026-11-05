"""5 vertical clip Shorts from Tehran-UFO-1976.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3, 57], hook="CHASED BY A UFO?", title="Two Iranian F-4 jets chased a UFO over Tehran in 1976. What really happened? #Shorts"),
 2: dict(shots=[15, 16, 17, 18], hook="THE JET WENT DEAD", title="The F-4 pilot's instruments died 25 miles from the Tehran UFO #Shorts"),
 3: dict(shots=[22, 23, 24, 26], hook="THE MISSILE FROZE?", title="The second pilot tried to fire at the Tehran UFO. Then everything failed #Shorts"),
 4: dict(shots=[31, 32, 34, 35], hook="THE BEEPING SIGNAL", title="Searchers found a beeping signal after the Tehran UFO. Here is what it was #Shorts"),
 5: dict(shots=[42, 43, 44, 47], hook="JUST JUPITER?", title="Was the Tehran 1976 UFO just Jupiter and meteors? The gap in that theory #Shorts"),
}
TAGS = "#Tehran1976 #UFO #UAP #Iran #AncientMysteries"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Tehran-UFO-1976.mp4', "Tehran 1976: The Night Two F-4 Jets Chased a UFO. What Really Happened?", CLIPS, TAGS, n)
