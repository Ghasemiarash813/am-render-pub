"""5 vertical clip Shorts from Phaistos-Disc.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=55 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 48, 63], hook="NOBODY CAN READ THIS", title="A 3,700-year-old message nobody on Earth can read: the Phaistos Disc #Shorts"),
 2: dict(shots=[13, 14, 15, 18], hook="PRINTED 3,000 YEARS EARLY?", title="The Phaistos Disc was 'printed' with stamps 3,000 years before Gutenberg #Shorts"),
 3: dict(shots=[42, 43, 46, 49], hook="EVERYONE CRACKED IT", title="Greek, Luwian, a goddess prayer: everyone 'cracked' the Phaistos Disc. Nobody agrees #Shorts"),
 4: dict(shots=[50, 53, 54], hook="A 1908 HOAX?", title="Was the Phaistos Disc faked in 1908? The clue that was still underground #Shorts"),
 5: dict(shots=[56, 57, 58, 59], hook="AN ALIEN MESSAGE?", title="Is the Phaistos Disc an alien message? Read what the signs actually show #Shorts"),
}
TAGS = "#PhaistosDisc #Minoans #AncientMysteries #Archaeology #AncientAliens"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Phaistos-Disc.mp4', "The Phaistos Disc: A 3,700-Year-Old Message No One Can Read — We Tried to Crack It", CLIPS, TAGS, n)
