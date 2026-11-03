"""5 vertical clip Shorts from Kecksburg-1965.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 59], hook="ALIEN ACORN?", title="The Kecksburg UFO of 1965: the acorn-shaped craft legend and the verdict #Shorts"),
 2: dict(shots=[5, 6, 7], hook="23 PILOTS SAW IT", title="The Kecksburg fireball of 1965: 23 pilot reports and a seismograph record #Shorts"),
 3: dict(shots=[24, 25, 26], hook="THE SOVIET PROBE THEORY", title="Was Kecksburg a Soviet Venus probe? Kosmos 96 and what NASA's own catalog says #Shorts"),
 4: dict(shots=[29, 46, 47], hook="ONE WITNESS. ONE FLATBED.", title="Kecksburg's flatbed truck story: where it came from, and what locals said #Shorts"),
 5: dict(shots=[50, 51, 52], hook="NASA FILES MISSING?", title="Kecksburg lawsuit against NASA: what 2007-2009 documents really showed #Shorts"),
}
TAGS = "#Kecksburg #UFO #UnsolvedMysteries #Pennsylvania #Roswell"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Kecksburg-1965.mp4', "Kecksburg 1965: Alien Acorn or Fireball? The UFO That 'Crashed' in Pennsylvania", CLIPS, TAGS, n)
