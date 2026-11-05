"""5 vertical clip Shorts from Mount-Shasta.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 4, 63], hook="A CITY INSIDE A VOLCANO?", title="Is there a lost Lemurian city inside Mount Shasta? What the evidence says #Shorts"),
 2: dict(shots=[14, 15, 17, 18], hook="LEMURIA WAS REAL SCIENCE", title="Lemuria began as a respectable 1860s scientific guess, then plate tectonics ended it #Shorts"),
 3: dict(shots=[21, 22, 24, 28], hook="THE BOY WHO MET A SPIRIT", title="How a 1883 teenager's book planted the Mount Shasta legend #Shorts"),
 4: dict(shots=[30, 31, 32, 36], hook="HOW TWO LEGENDS MERGED", title="In 1931 an author merged Lemuria with Mount Shasta. Here is the paper trail #Shorts"),
 5: dict(shots=[37, 38, 41, 44], hook="WE SEARCHED INSIDE SHASTA", title="If a city hid inside Mount Shasta, would we find it? Geology says... #Shorts"),
}
TAGS = "#MountShasta #Lemuria #AncientMysteries #LostCivilization #Shorts"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Mount-Shasta.mp4', "Mount Shasta and Lemuria: A Lost City Inside a Volcano? The Evidence", CLIPS, TAGS, n)
