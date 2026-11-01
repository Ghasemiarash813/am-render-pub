"""5 vertical clip Shorts from UFOs-in-Ancient-Art.mp4 via bank/cloud/shorts_lib.py. usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[35, 36, 37, 39, 41], hook="THE MADONNA'S UFO?", title="The 'UFO' in this 500-year-old Madonna painting is an angel that lost its gold #Shorts"),
 2: dict(shots=[26, 27, 28, 30, 32], hook="PILOTS AT THE CRUCIFIXION?", title="Two 'pilots' in a 1350 Crucifixion fresco? Meet the Sun and the Moon #Shorts"),
 3: dict(shots=[42, 44, 45, 46, 50], hook="1561: ALIEN SKY BATTLE?", title="The 1561 Nuremberg 'UFO battle' was probably ice crystals #Shorts"),
 4: dict(shots=[53, 54, 55, 56, 57], hook="LOOK INSIDE THE 'SAUCER'", title="There's a dove inside this painting's 'flying saucer' #Shorts"),
 5: dict(shots=[7, 8, 10, 11], hook="WHY NO MOUTH?", title="Why the Wandjina have no mouth (it's not a space helmet) #Shorts"),
}
TAGS = "#UFO #AncientAliens #ArtHistory #AncientMysteries #UAP"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'UFOs-in-Ancient-Art.mp4', 'UFOs in Ancient & Renaissance Art?', CLIPS, TAGS, n)
