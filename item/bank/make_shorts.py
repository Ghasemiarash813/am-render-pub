"""5 vertical clip Shorts from Ariel-School-1994.mp4 via bank/cloud/shorts_lib.py (hand-picked, each <=55 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[2, 3, 4], hook="62 CHILDREN SAW WHAT?", title="Ariel School 1994: 62 children, a silver disc and no evidence #Shorts"),
 2: dict(shots=[13, 14, 16], hook="THE FIGURES IN BLACK", title="Ariel School UFO: what the children said they saw on the playground #Shorts"),
 3: dict(shots=[30, 31, 32], hook="PROOF OR CONTAMINATION?", title="Ariel School: why 'they all told the same story' may not prove anything #Shorts"),
 4: dict(shots=[48, 49, 50], hook="'I MADE IT UP'?", title="Ariel School UFO: the Netflix confession and the 1994 interview that contradicts it #Shorts"),
 5: dict(shots=[62, 63, 64], hook="OUR VERDICT: UNPROVEN", title="Ariel School 1994 verdict: sincere children, no craft, no proof #Shorts"),
}
TAGS = "#ArielSchool #UFO #Zimbabwe #AncientMysteries #UAP"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Ariel-School-1994.mp4', "Ariel School 1994: 62 Children Saw a UFO. We Played the Tapes and Gave the Case a Verdict", CLIPS, TAGS, n)
