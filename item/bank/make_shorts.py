"""5 vertical clip Shorts from Baalbek-Trilithon.mp4 via bank/cloud/shorts_lib.py (hand-picked). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[13, 14, 16, 17], hook="2,000 TONS? LET'S MEASURE", title="Baalbek's Trilithon: we did the maths on the 'impossible' stones #Shorts"),
 2: dict(shots=[20, 21, 56, 57], hook="THE STONES THEY LEFT BEHIND", title="Why Baalbek's 1,000-ton Stone of the Pregnant Woman never left the quarry #Shorts"),
 3: dict(shots=[36, 37, 38, 40], hook="THEY MOVED A HEAVIER ROCK IN 1770", title="400 men moved a stone heavier than Baalbek's blocks — no engines, no aliens #Shorts"),
 4: dict(shots=[3, 53, 54], hook="WHO INVENTED THE 'LANDING PAD'?", title="The Baalbek alien landing pad idea started with a Soviet mathematician in 1959 #Shorts"),
 5: dict(shots=[27, 28, 29, 31], hook="IT NEVER GOES UPHILL", title="The secret of moving Baalbek's 800-ton stones: the route runs downhill #Shorts"),
}
TAGS = "#Baalbek #Trilithon #AncientAliens #Megaliths #Archaeology"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Baalbek-Trilithon.mp4', "Baalbek's 1,000-Ton Stones: Who Moved the Trilithon? Alien Landing Pad Claim Tested", CLIPS, TAGS, n)
