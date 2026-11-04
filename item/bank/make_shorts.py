"""5 vertical clip Shorts from Coso-Artifact.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 62], hook="SPARK PLUG IN A ROCK?", title="The Coso artifact: a spark plug inside a 'half-million-year-old' rock #Shorts"),
 2: dict(shots=[30, 31, 32], hook="ONE X-RAY SOLVED IT", title="Coso artifact: the X-ray that identified a 1920s Champion spark plug #Shorts"),
 3: dict(shots=[13, 14, 15], hook="WHO DATED IT?", title="The 500,000-year claim behind the Coso artifact had no named geologist #Shorts"),
 4: dict(shots=[37, 38, 39], hook="ROCK GROWS IN YEARS", title="How rust builds a 'geode' around a spark plug in years, not millennia #Shorts"),
 5: dict(shots=[44, 45, 46], hook="ALIENS OR TIME TRAVELER?", title="Coso artifact: ancient aliens, Atlantis or a time traveler? The verdict #Shorts"),
}
TAGS = "#CosoArtifact #OOPArts #UnsolvedMysteries #AncientMachines #Debunked"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Coso-Artifact.mp4', 'The Coso Artifact: The "500,000-Year-Old Spark Plug" Read Like an X-Ray', CLIPS, TAGS, n)
