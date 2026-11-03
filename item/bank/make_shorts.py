"""5 vertical clip Shorts from Voynich-Manuscript.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 63], hook="ALIEN ALPHABET?", title="Is the Voynich manuscript an alien alphabet? Yale's unreadable book, and the verdict #Shorts"),
 2: dict(shots=[20, 21, 22, 23, 24], hook="DATED TO 1404", title="Carbon dating the Voynich manuscript: the calfskin dates to 1404-1438 #Shorts"),
 3: dict(shots=[35, 36, 37, 38], hook="BOUND IN THE WRONG ORDER", title="The Voynich manuscript may have been bound in the wrong order, new 2026 study #Shorts"),
 4: dict(shots=[46, 47, 50], hook="A GALAXY IN THE BOOK?", title="A spiral galaxy in the Voynich manuscript? The 1921 claim that fell apart #Shorts"),
 5: dict(shots=[56, 57, 58], hook="'READ' IN TWO WEEKS", title="Someone claimed to read the Voynich manuscript in two weeks. Here is why it failed #Shorts"),
}
TAGS = "#Voynich #VoynichManuscript #UnsolvedMysteries #AncientMysteries #Yale"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Voynich-Manuscript.mp4', "The Voynich Manuscript: Alien Alphabet or Medieval Mystery? (Yale's Unreadable Book)", CLIPS, TAGS, n)
