"""5 vertical clip Shorts from Taos-Hum.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {

 1: dict(shots=[1, 2, 3, 4], hook="A SOUND ONLY SOME HEAR", title="The Taos Hum: a sound only some people can hear #Shorts"),
 2: dict(shots=[15, 16, 17, 18], hook="THEY SENT IN THE LABS", title="Sandia, Los Alamos and UNM hunted the Taos Hum. What they found #Shorts"),
 3: dict(shots=[25, 26, 27, 28], hook="8,000 FORMS. 161 HEARERS", title="The survey that counted who hears the Taos Hum #Shorts"),
 4: dict(shots=[41, 42, 43, 44], hook="ALIEN BASE?", title="Is an alien base humming under Taos? We checked #Shorts"),
 5: dict(shots=[59, 60, 61, 64], hook="THE REAL ANSWER", title="The Taos Hum scorecard: evidence vs theory #Shorts"),
}
TAGS = "#TaosHum #TheHum #AncientMysteries #Unexplained #UFO"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Taos-Hum.mp4', "The Taos Hum: The Sound Only 2% Can Hear. We Investigated", CLIPS, TAGS, n)
