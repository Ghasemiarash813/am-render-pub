"""5 vertical clip Shorts from Sacsayhuaman-Walls.mp4 via bank/cloud/shorts_lib.py (hand-picked). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[15, 47, 48, 49], hook="'MELTED' ROCK?", title="Von Däniken called this Inca rock 'vitrified'. A 1914 geologist explained it #Shorts"),
 2: dict(shots=[25, 26, 27, 28], hook="POUNDED, NOT POURED", title="The tiny white scars that prove Sacsayhuamán's stones were never melted #Shorts"),
 3: dict(shots=[30, 34, 35], hook="20,000 WORKERS", title="How the Inca moved 100-tonne stones: 20,000 workers, grass rope and a 'tired stone' #Shorts"),
 4: dict(shots=[38, 39, 44], hook="THE SECRET OF THE FIT", title="How Inca masons got joints so tight paper won't fit — trial and error #Shorts"),
 5: dict(shots=[50, 51, 52], hook="A PLANT THAT MELTS ROCK?", title="The Inca 'stone-softening plant' legend, traced to a 1638 woodpecker tale #Shorts"),
}
TAGS = "#Sacsayhuaman #Inca #Cusco #Peru #AncientMysteries #AncientAliens"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Sacsayhuaman-Walls.mp4', "Sacsayhuamán: Melted Stone, Alien Tools, or Inca Genius? (Peru's \"Impossible\" Walls Tested)", CLIPS, TAGS, n)
