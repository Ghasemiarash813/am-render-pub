"""5 vertical clip Shorts from Shag-Harbour-1967.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3, 4], hook="WHAT FELL IN THE SEA?", title="1967: Lights fell into the sea off Canada. Navy divers found nothing. What was it? #Shorts"),
 2: dict(shots=[7, 8, 9, 10], hook="THE TEENAGERS' CALL", title="Five teenagers saw lights fall into the sea. Then the payphone rang back #Shorts"),
 3: dict(shots=[32, 33, 34, 35], hook="7 DIVERS. NOTHING.", title="The Canadian Navy searched the seabed for a UFO. Here is what the divers found #Shorts"),
 4: dict(shots=[28, 29, 52, 53], hook="RULED OUT FLARES?", title="Did the Canadian government rule out flares at Shag Harbour? Read the telex #Shorts"),
 5: dict(shots=[43, 44, 49, 50], hook="FIREBALL OR FLARE?", title="Shag Harbour UFO: a meteor, or a flare gun? The two best explanations #Shorts"),
}
TAGS = "#ShagHarbour #UFO #UAP #Canada #AncientMysteries"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Shag-Harbour-1967.mp4', "Shag Harbour 1967: The UFO That Fell Into the Sea. What Really Happened?", CLIPS, TAGS, n)
