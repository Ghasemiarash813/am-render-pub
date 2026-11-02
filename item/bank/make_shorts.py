"""5 vertical clip Shorts from Tunguska-1908.mp4 via bank/cloud/shorts_lib.py (hand-picked). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[49, 50, 51, 62], hook="THE UFO STORY HAS A BIRTHDAY", title="The Tunguska 'alien spaceship' began as a 1946 short story #Shorts"),
 2: dict(shots=[20, 25, 41], hook="A HUGE BLAST. NO CRATER.", title="Tunguska 1908: why there is no crater (the trees tell you) #Shorts"),
 3: dict(shots=[12, 13, 14, 16], hook="\"THE SKY SPLIT IN TWO\"", title="A 1908 eyewitness: 'the sky was split in two' — Tunguska #Shorts"),
 4: dict(shots=[48, 52, 53], hook="ALIEN WRECKAGE IN SIBERIA?", title="Geiger counters and a 2004 'alien device': testing the Tunguska UFO #Shorts"),
 5: dict(shots=[57, 61, 64], hook="IT HAPPENED AGAIN IN 2013", title="Chelyabinsk 2013 is the key to the Tunguska mystery #Shorts"),
}
TAGS = "#Tunguska #UFO #Asteroid #Siberia #Mystery"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Tunguska-1908.mp4', "Tunguska 1908: Comet, Asteroid, or Crashed Alien Craft? The Siberian Explosion Investigated", CLIPS, TAGS, n)
