"""5 vertical clip Shorts from Lalibela-Rock-Churches.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 21, 63], hook="A CHURCH NEVER BUILT", title="A church carved downward from solid rock? How Lalibela was made #Shorts"),
 2: dict(shots=[20, 21, 22, 31], hook="BUILT FROM THE TOP DOWN", title="How workers carved Lalibela's rock churches from the top down #Shorts"),
 3: dict(shots=[38, 39, 40, 43], hook="24 YEARS OR CENTURIES?", title="Lalibela's churches: made in 24 years, or over centuries? The dating problem #Shorts"),
 4: dict(shots=[47, 48, 51, 54], hook="ALIENS AT LALIBELA?", title="Did aliens carve Lalibela? Three claims checked against the evidence #Shorts"),
 5: dict(shots=[2, 53, 54, 62], hook="ANGELS OR MASONS?", title="The angels legend of Lalibela and the real verdict #Shorts"),
}
TAGS = "#Lalibela #Ethiopia #AncientMysteries #Archaeology #AncientAliens"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Lalibela-Rock-Churches.mp4', "Lalibela: Churches Carved From Living Rock. Angels, Aliens or Human Hands?", CLIPS, TAGS, n)
