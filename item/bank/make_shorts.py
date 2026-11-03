"""5 vertical clip Shorts from Iron-Pillar-of-Delhi.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3, 4], hook="1,600 YEARS WITHOUT RUST?", title="The Iron Pillar of Delhi: 1,600 years without rust? We filed the claim #Shorts"),
 2: dict(shots=[11, 12, 13, 14], hook="IT DOES RUST...", title="The Delhi Iron Pillar does rust. Here's the catch #Shorts"),
 3: dict(shots=[39, 40, 41], hook="THE SECRET INGREDIENT", title="Why the Delhi Iron Pillar survived: phosphorus, not aliens #Shorts"),
 4: dict(shots=[48, 49, 50], hook="DRY AIR OR ALLOY?", title="Delhi's dry air vs ancient Indian iron: what really saved the pillar #Shorts"),
 5: dict(shots=[54, 55, 56], hook="THE ALIEN CLAIM HE DROPPED", title="Von Daniken dropped the Delhi Iron Pillar claim in 1974 #Shorts"),
}
TAGS = "#IronPillarOfDelhi #Gupta #AncientMysteries #Archaeology #AncientAliens"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Iron-Pillar-of-Delhi.mp4', "The Iron Pillar of Delhi: 1,600 Years Without Rust? Ancient Super-Metal or Aliens?", CLIPS, TAGS, n)
