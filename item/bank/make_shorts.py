"""5 vertical clip Shorts from Washington-Flap-1952.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3, 4], hook="UFOs OVER THE CAPITOL", title="1952: Radar showed 7 unknown objects over the White House. Jets were scrambled #Shorts"),
 2: dict(shots=[14, 15, 16, 17], hook="THE TARGETS VANISHED", title="Jets arrive over Washington in 1952 and the radar blips disappear #Shorts"),
 3: dict(shots=[28, 29, 30, 31], hook="BIGGEST PRESS CONFERENCE", title="The largest Pentagon press conference since WWII was about UFOs #Shorts"),
 4: dict(shots=[36, 37, 38, 39], hook="3 RADARS + EYEWITNESSES", title="Why the 1952 Washington UFO case is still unresolved #Shorts"),
 5: dict(shots=[54, 55, 56, 57], hook="WEATHER OR SOMETHING ELSE?", title="Our verdict on the 1952 Washington UFO radar case #Shorts"),
}
TAGS = "#Washington1952 #UFO #UFOs #AncientMysteries #ColdCase"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Washington-Flap-1952.mp4', "Washington 1952: UFOs Over the Capitol, Weather or Not?", CLIPS, TAGS, n)
