"""5 vertical clip Shorts from Pascagoula-1973.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3], hook="ALIEN ABDUCTION TAPE?", title="1973: two men said aliens took them, then police secretly recorded them #Shorts"),
 2: dict(shots=[18, 19, 22, 23], hook="THE SECRET RECORDING", title="Police left two abduction witnesses alone with a hidden recorder. What it caught #Shorts"),
 3: dict(shots=[30, 31, 32], hook="CAN HYPNOSIS LIE?", title="Hypnosis and a lie detector were used on the Pascagoula abductees. Why neither proves anything #Shorts"),
 4: dict(shots=[10, 11, 12, 13], hook="CLAW-HANDED CREATURES", title="The Pascagoula 1973 creatures: what the two witnesses described #Shorts"),
 5: dict(shots=[40, 41, 42], hook="NOT A HOAX?", title="Skeptic Joe Nickell says Pascagoula was not a hoax. His explanation #Shorts"),
}
TAGS = "#Pascagoula1973 #UFO #UAP #Belgium #AncientMysteries"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Pascagoula-1973.mp4', "Pascagoula 1973: The Alien Abduction Tape. What Really Happened?", CLIPS, TAGS, n)
