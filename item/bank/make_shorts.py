"""5 vertical clip Shorts from Tuts-Meteorite-Dagger.mp4 via bank/cloud/shorts_lib.py (hand-picked). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[2, 15, 16, 20], hook="KING TUT'S DAGGER IS FROM SPACE?", title="King Tut's dagger really is made of space iron. Here's the proof (and the catch) #Shorts"),
 2: dict(shots=[36, 37, 39, 41], hook="3,300 YEARS AND NO RUST?", title="Why hasn't Tutankhamun's iron dagger rusted in 3,300 years? #Shorts"),
 3: dict(shots=[28, 30, 31, 33], hook="FORGED BY ALIENS?", title="Who forged King Tut's meteorite dagger? The blade itself tells us #Shorts"),
 4: dict(shots=[45, 47, 48], hook="A GIFT FROM A FOREIGN KING?", title="Was King Tut's space dagger a royal wedding gift? The Amarna letters clue #Shorts"),
 5: dict(shots=[51, 52, 54, 56], hook="IRON THAT FELL FROM THE SKY", title="Before the Iron Age, kings used iron that fell from the sky #Shorts"),
}
TAGS = "#Tutankhamun #KingTut #Meteorite #AncientEgypt #AncientAliens"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Tuts-Meteorite-Dagger.mp4', "Tutankhamun's Meteorite Dagger: Alien Metal or Bronze Age Craft? 7 Questions, Real Science", CLIPS, TAGS, n)
