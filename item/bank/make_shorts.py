"""5 vertical clip Shorts from Simulation-Hypothesis.mp4 via bank/cloud/shorts_lib.py. usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[6, 7, 8, 11, 12], hook="THE 2,400-YEAR-OLD MATRIX", title="Plato described 'the Matrix' 2,400 years ago. Or did he? #Shorts"),
 2: dict(shots=[14, 15, 16, 17], hook="BUTTERFLY OR MAN?", title="A man who dreamed he was a butterfly, and the simulation question #Shorts"),
 3: dict(shots=[43, 44, 45, 46, 50], hook="PICK A DOOR: 1, 2 OR 3", title="Bostrom's simulation argument: pick a door, 1, 2 or 3 #Shorts"),
 4: dict(shots=[52, 53, 54, 55], hook="THE PIXELS OF REALITY?", title="Physicists tried to find the pixels of reality #Shorts"),
 5: dict(shots=[56, 57, 58], hook="THE HEADLINE THAT LIED", title="'Proof we're not in a simulation'? Read the paper #Shorts"),
}
TAGS = "#SimulationTheory #Simulation #Philosophy #Physics #Bostrom"
PIN = "Door 1, 2 or 3? Comment your pick. Full investigation on the channel. \U0001F447"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Simulation-Hypothesis.mp4', 'Are We Living in a Simulation? From Plato to Bostrom', CLIPS, TAGS, n, PIN if n == 3 else None)
