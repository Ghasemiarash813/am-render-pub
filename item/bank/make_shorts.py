"""5 vertical clip Shorts from Belgian-UFO-Wave.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3, 66], hook="F-16s VS UFOs?", title="Two F-16s chased black triangles over Belgium in 1990. What really happened? #Shorts"),
 2: dict(shots=[44, 45, 47, 48], hook="BEST UFO PHOTO EVER?", title="Labs could not prove the famous Belgian UFO photo was fake. Then the man confessed #Shorts"),
 3: dict(shots=[33, 34, 35, 39], hook="150 TO 1,000 KNOTS?", title="The radar lock that jumped from 150 to 970 knots, and the pilots saw nothing #Shorts"),
 4: dict(shots=[16, 17, 18, 19], hook="THE POLICE SAW IT TOO", title="Belgian police officers watched the triangle lights too. Here is what they reported #Shorts"),
 5: dict(shots=[41, 53, 54, 62], hook="THE RADAR GLITCH?", title="Did a radar glitch make the Belgian UFO speeds? What Air Force engineers found #Shorts"),
}
TAGS = "#BelgianUFOWave #UFO #UAP #Belgium #AncientMysteries"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Belgian-UFO-Wave.mp4', "The Belgian UFO Wave: Black Triangles, F-16s and a Hoax Photo. What Really Happened?", CLIPS, TAGS, n)
