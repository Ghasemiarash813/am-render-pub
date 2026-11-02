"""5 vertical clip Shorts from Baigong-Pipes.mp4 via bank/cloud/shorts_lib.py (hand-picked). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[10, 15, 17, 18], hook="8% ALIEN METAL?", title="The '8% unknown alien metal' in China's Baigong pipes was... potassium #Shorts"),
 2: dict(shots=[21, 23, 24], hook="150,000-YEAR-OLD IRON?", title="150,000-year-old iron pipes? Here's why that date kills the alien story #Shorts"),
 3: dict(shots=[44, 46, 47, 50], hook="TREE RINGS INSIDE?", title="Scientists found tree rings inside China's 'alien pipes' #Shorts"),
 4: dict(shots=[2, 4, 17, 18], hook="PIPES IN A MOUNTAIN?", title="Iron pipes inside a mountain in China. Aliens? The lab said no #Shorts"),
 5: dict(shots=[31, 32, 34, 36], hook="RADIOACTIVE PIPES?", title="Some of the Baigong pipes are radioactive. Did a volcano make them? #Shorts"),
}
TAGS = "#BaigongPipes #AncientMysteries #AncientAliens #OOPArts #China"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Baigong-Pipes.mp4', 'The Baigong Pipes: Who Made the "Alien" Iron Pipes Inside a Chinese Mountain?', CLIPS, TAGS, n)
