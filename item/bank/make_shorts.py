"""5 vertical clip Shorts from Snippy-Horse.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 13, 62], hook="KILLED BY A UFO?", title="A horse found with her head stripped to bone in 1967: UFO or nature? #Shorts"),
 2: dict(shots=[22, 23, 24, 36], hook="THE PATHOLOGIST'S CLAIM", title="A pathologist said the cut was 'surgical'. Here is why it is disputed #Shorts"),
 3: dict(shots=[28, 29, 30, 31], hook="WHAT THE INVESTIGATOR FOUND", title="The government investigator's findings on the 1967 Snippy horse case #Shorts"),
 4: dict(shots=[38, 40, 41, 42], hook="THE GREAT COW PANIC", title="Why ranchers sat up with rifles: the 1970s cattle mutilation panic #Shorts"),
 5: dict(shots=[16, 17, 33, 56], hook="THE GEIGER COUNTER CLAIM", title="The Geiger counter reading everyone repeats about Snippy, and the catch #Shorts"),
}
TAGS = "#Snippy #CattleMutilation #UFO #AncientMysteries #Unexplained"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Snippy-Horse.mp4', "Snippy the Horse: Killed by Aliens? The 1967 Cattle Mutilation Inquest", CLIPS, TAGS, n)
