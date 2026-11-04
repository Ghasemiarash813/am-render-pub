"""5 vertical clip Shorts from Valentich-Disappearance.mp4 via bank/cloud/shorts_lib.py. usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3, 63], hook="17 SECONDS OF SCRAPING", title="1978: a pilot reports a UFO, then 17 seconds of metal noise. He was never found #Shorts"),
 2: dict(shots=[20, 23, 25, 28], hook="'IT IS NOT AN AIRCRAFT'", title="The last words of Frederick Valentich, from the real radio tape #Shorts"),
 3: dict(shots=[44, 45, 46, 51], hook="THE BLACK HOLE EFFECT", title="The pilot explanation for Valentich's UFO: how a night sea fools your brain #Shorts"),
 4: dict(shots=[52, 54, 56, 57], hook="UFO OR STAGED?", title="Valentich: the alien theory and the 'staged disappearance' theory, tested #Shorts"),
 5: dict(shots=[35, 36, 41, 59], hook="THE ENGINE COWL", title="The only piece of wreckage that may belong to Valentich's Cessna #Shorts"),
}
TAGS = "#Valentich #UFO #BassStrait #AncientMysteries #Unsolved"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Valentich-Disappearance.mp4', "The Valentich Disappearance: The Pilot Who Vanished Chasing a UFO", CLIPS, TAGS, n)
