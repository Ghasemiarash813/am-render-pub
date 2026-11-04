"""5 vertical clip Shorts from Socorro-1964.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3], hook="EGG-SHAPED CRAFT?", title="1964: a policeman saw an egg-shaped craft land in New Mexico #Shorts"),
 2: dict(shots=[12, 13, 14], hook="TWO FIGURES IN WHITE", title="Lonnie Zamora: what he really saw in the Socorro gully #Shorts"),
 3: dict(shots=[21, 22, 23], hook="THE RED SYMBOL", title="The red insignia on the Socorro craft Zamora drew on the spot #Shorts"),
 4: dict(shots=[28, 29, 30], hook="FOUR MARKS IN THE GROUND", title="Socorro 1964: the FBI measured four dents and burned brush #Shorts"),
 5: dict(shots=[43, 44, 45], hook="A STUDENT PRANK?", title="The 1968 note that says Socorro was a student prank #Shorts"),
}
TAGS = "#SocorroUFO #LonnieZamora #UFO #AncientMachines #ProjectBlueBook"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Socorro-1964.mp4', 'The Socorro UFO Landing (1964): The Officer, the Egg-Shaped Craft and the Burned Bushes', CLIPS, TAGS, n)
