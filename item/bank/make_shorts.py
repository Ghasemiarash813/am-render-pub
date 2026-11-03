"""5 vertical clip Shorts from Phoenix-Lights-1997.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 3, 4, 63], hook="TWO EVENTS, ONE LEGEND", title="The Phoenix Lights were TWO different events: the V and the 10 PM row. Here's the verdict #Shorts"),
 2: dict(shots=[22, 23, 24, 28], hook="HE SAW WINGS", title="An astronomer pointed a telescope at the Phoenix Lights V. Each light was a pair on square wings #Shorts"),
 3: dict(shots=[37, 38, 40, 42], hook="FLARES, 4 MONTHS LATE", title="The Phoenix Lights 10 PM row: how the Air National Guard explained it, and why it took 4 months #Shorts"),
 4: dict(shots=[46, 47, 52, 54], hook="THE ALIEN COSTUME", title="The governor mocked the Phoenix Lights with an alien costume. Ten years later he said he saw it #Shorts"),
 5: dict(shots=[14, 15, 19, 20], hook="A MILE-WIDE CRAFT?", title="Phoenix Lights: the mile-wide craft claim vs the one video of the V #Shorts"),
}
TAGS = "#PhoenixLights #UFO #Arizona #AncientMysteries #Documentary"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Phoenix-Lights-1997.mp4', "The Phoenix Lights (1997): Alien Craft or Flares? We Split the Case in Two", CLIPS, TAGS, n)
