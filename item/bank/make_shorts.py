"""5 vertical clip Shorts from Roswell-1947.mp4 via bank/cloud/shorts_lib.py (hand-picked). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[16, 24, 40], hook="REMEMBER THE FLOWER TAPE", title="The flower-printed tape that solves the Roswell UFO crash #Shorts"),
 2: dict(shots=[30, 31, 33, 34], hook="THE NURSE WHO NEVER EXISTED", title="The Roswell alien-autopsy nurse? He admitted he made her up #Shorts"),
 3: dict(shots=[44, 45, 46], hook="FILMED IN A LIVING ROOM", title="The 1995 'Alien Autopsy' film was staged in a London flat #Shorts"),
 4: dict(shots=[2, 37, 38, 61], hook="THE ARMY DID LIE. JUST NOT ABOUT ALIENS", title="What really crashed at Roswell in 1947: Project Mogul #Shorts"),
 5: dict(shots=[51, 52, 54], hook="A SEALED CONFESSION", title="Walter Haut's sealed Roswell affidavit: how strong is it really? #Shorts"),
}
TAGS = "#Roswell #UFO #ProjectMogul #Aliens #History"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Roswell-1947.mp4', "Roswell 1947: Weather Balloon, Project Mogul, or Crashed Saucer? The Evidence, Edition by Edition", CLIPS, TAGS, n)
