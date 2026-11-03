"""5 vertical clip Shorts from Coral-Castle.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=55 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 36, 64], hook="NO WITNESSES?", title="One man, 1,100 tons of stone, 'no witnesses'… except the photos #Shorts"),
 2: dict(shots=[49, 50, 52, 53], hook="THE 9-TON GATE SECRET", title="Coral Castle's 'nine-ton' gate turned with one finger. Then a crane crew looked inside #Shorts"),
 3: dict(shots=[36, 37, 38], hook="HOW ONE MAN LIFTS TONS", title="How a 5-foot man lifted multi-ton blocks alone: no magnets, just gearing #Shorts"),
 4: dict(shots=[11, 29, 32], hook="IT'S NOT EVEN CORAL", title="Coral Castle isn't coral, and the 'nine-ton' gate probably isn't nine tons #Shorts"),
 5: dict(shots=[45, 46, 47], hook="THE WITNESS THEY FORGOT", title="'Nobody saw him move the stones'… except the farmer who towed them #Shorts"),
}
TAGS = "#CoralCastle #EdLeedskalnin #Mystery #Florida #AncientAliens"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Coral-Castle.mp4', "Coral Castle: How One Man Moved 1,100 Tons of Stone With No Witnesses", CLIPS, TAGS, n)
