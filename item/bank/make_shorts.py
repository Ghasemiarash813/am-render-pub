"""5 vertical clip Shorts from Piri-Reis-Map.mp4 via bank/cloud/shorts_lib.py (hand-picked). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[40, 48, 49], hook="ANTARCTICA WITH SNAKES?", title="The 1513 map that 'shows Antarctica' says that coast is very hot and full of snakes #Shorts"),
 2: dict(shots=[27, 28, 29, 32], hook="CUBA IS ASIA?", title="Columbus made his crews swear Cuba was Asia. This 1513 map still shows it #Shorts"),
 3: dict(shots=[42, 43, 44], hook="THE AIR FORCE LETTER", title="A 1960 Air Force letter said this map shows Antarctica. One gap says no #Shorts"),
 4: dict(shots=[53, 54, 55, 56], hook="A PHOTO FROM SPACE?", title="Von Daniken said the Piri Reis map is a photo from space over Cairo. We checked #Shorts"),
 5: dict(shots=[18, 19, 23], hook="HE LISTED HIS SOURCES", title="The 'impossible' Piri Reis map came with a source list written by its maker #Shorts"),
}
TAGS = "#PiriReis #AncientMysteries #Antarctica #AncientAliens #History"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Piri-Reis-Map.mp4', "The Piri Reis Map: Antarctica From Space, or a 1513 Ottoman Masterpiece?", CLIPS, TAGS, n)
