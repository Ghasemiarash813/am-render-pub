"""5 vertical clip Shorts from Rendlesham-Forest-1980.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3, 66], hook="BRITAIN'S ROSWELL?", title="Britain's Roswell: what the airmen saw in Rendlesham Forest, 1980 #Shorts"),
 2: dict(shots=[23, 24, 56, 57], hook="A FLASH EVERY 5 SECONDS", title="The 'UFO' light that flashed exactly every 5 seconds on Colonel Halt's own tape #Shorts"),
 3: dict(shots=[26, 27, 28], hook="THE RADIATION READING", title="Rendlesham's 'radiation proof': 0.07 milliroentgen per hour, explained #Shorts"),
 4: dict(shots=[37, 38, 39], hook="I TOUCHED THE CRAFT", title="The sergeant who said he touched the Rendlesham craft, and what the notes from that night say #Shorts"),
 5: dict(shots=[45, 46, 47, 48], hook="HOW A MYTH GREW", title="How a few odd lights became 'Britain's Roswell' #Shorts"),
}
TAGS = "#RendleshamForest #UFO #BritainsRoswell #UFOCase #Unexplained"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Rendlesham-Forest-1980.mp4', "Rendlesham Forest UFO 1980: Craft, Lighthouse or Fireball? We Cross-Examined the Night Shift Log", CLIPS, TAGS, n)
