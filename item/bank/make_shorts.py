"""5 vertical clip Shorts from Derinkuyu-Underground-City.mp4 via bank/cloud/shorts_lib.py (hand-picked). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[20, 21, 22, 23, 25], hook="DOORS THAT ONLY OPEN FROM INSIDE", title="Derinkuyu's half-ton stone doors only roll shut from the inside. Here's why #Shorts"),
 2: dict(shots=[3, 10, 11, 12], hook="HIDING FROM THE SKY?", title="Did 20,000 people hide underground from aliens? Look at who the doors face #Shorts"),
 3: dict(shots=[55, 57, 59], hook="A 12,000-YEAR COMET BUNKER?", title="Derinkuyu as an Ice Age comet bunker? What the dirt inside actually says #Shorts"),
 4: dict(shots=[27, 28, 30, 31], hook="50 AIR SHAFTS, ZERO MACHINES", title="How a city 85 m underground breathed without any machines #Shorts"),
 5: dict(shots=[14, 15, 64], hook="FOUND BEHIND A BASEMENT WALL", title="In 1963 a man knocked down a wall and found a city for 20,000 people #Shorts"),
}
TAGS = "#Derinkuyu #Cappadocia #AncientAliens #UndergroundCity #History"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Derinkuyu-Underground-City.mp4', "Derinkuyu Underground City: Hiding From Aliens, a Comet, or Raiders? 20,000 People 85 m Down (Cappadocia)", CLIPS, TAGS, n)
