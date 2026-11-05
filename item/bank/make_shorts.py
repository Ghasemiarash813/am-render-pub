"""5 vertical clip Shorts from Lake-Vostok.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 34, 63], hook="A LAKE UNDER 4 KM OF ICE", title="Lake Vostok: the hidden lake humans finally touched in 2012 #Shorts"),
 2: dict(shots=[7, 8, 10, 11], hook="-89C ABOVE, WATER BELOW", title="How can liquid water exist under Antarctica's ice? Lake Vostok #Shorts"),
 3: dict(shots=[25, 26, 27, 28], hook="THE DRILLING FLUID SCARE", title="Did Russia risk poisoning an untouched Antarctic lake? Lake Vostok #Shorts"),
 4: dict(shots=[43, 44, 45, 51], hook="IS ANYTHING ALIVE DOWN THERE?", title="What lives in Lake Vostok? The honest answer, and why Europa matters #Shorts"),
 5: dict(shots=[53, 54, 55, 56], hook="NAZI BASE? MONSTER? ALIENS?", title="Lake Vostok myths: Nazi base, monster, alien bunker, what is true #Shorts"),
}
TAGS = "#LakeVostok #Antarctica #AncientMysteries #Science #Mystery"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Lake-Vostok.mp4', "Lake Vostok: The Hidden Lake Under 4 km of Antarctic Ice, What Did the Drill Really Find?", CLIPS, TAGS, n)
