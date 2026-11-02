"""5 vertical clip Shorts from Sphinx-Water-Erosion.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[5, 6, 44], hook="IS THE SPHINX 9,000 YEARS OLD?", title="A geologist said rain proves the Sphinx is 9,000 years old. A third geologist checked #Shorts"),
 2: dict(shots=[21, 22, 23, 24], hook="THE SPHINX TALKED TO A PRINCE", title="The Sphinx 'spoke' to a prince in a dream. His stone is a recycled door #Shorts"),
 3: dict(shots=[27, 28, 29, 31], hook="THE SPHINX WASN'T BUILT", title="The Sphinx wasn't built. It was cut, and the rock layers prove when #Shorts"),
 4: dict(shots=[8, 47, 48], hook="BUILT TO FACE LEO?", title="Was the Sphinx built to face Leo in 10,500 BC? Astronomers checked #Shorts"),
 5: dict(shots=[53, 54, 62], hook="NATURE MADE A LION?", title="Scientists made 'mini Sphinxes' with nothing but flowing water #Shorts"),
}
TAGS = "#Sphinx #AncientEgypt #AncientMysteries #AncientAliens #Archaeology"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Sphinx-Water-Erosion.mp4', 'Is the Sphinx 10,000 Years Old? The Water Erosion Theory Tested Layer by Layer', CLIPS, TAGS, n)
