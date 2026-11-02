"""5 vertical clip Shorts from Nimitz-Tic-Tac.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[15, 16, 17, 18], hook="IT OUTRAN A FIGHTER JET?", title="The Tic Tac that left a Navy fighter behind, 2004 #Shorts"),
 2: dict(shots=[28, 29, 30, 31], hook="THE FAMOUS 'DART' LEFT", title="Did the Tic Tac really dart away, or did the camera lose it? #Shorts"),
 3: dict(shots=[35, 36, 37, 40], hook="5,000 G?", title="5,000 g and Mach 60: the Tic Tac math, and its catch #Shorts"),
 4: dict(shots=[45, 46, 47, 49], hook="THE TAPES ARE GONE", title="The Navy lost the Tic Tac radar tapes #Shorts"),
 5: dict(shots=[14, 19, 20, 21], hook="TWO PILOTS, TWO CLOCKS", title="Two Navy pilots saw the Tic Tac. Their clocks disagree #Shorts"),
}
TAGS = "#TicTac #UFO #UAP #Nimitz #NavyUFO"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Nimitz-Tic-Tac.mp4', 'Nimitz Tic Tac UFO: Sensor Glitch or Real Craft?', CLIPS, TAGS, n)
