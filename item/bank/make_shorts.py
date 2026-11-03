"""5 vertical clip Shorts from Pakal-Palenque-Lid.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[2, 8, 9, 44], hook="PILOT OR KING?", title="The 'astronaut' on Pakal's tomb lid only works if you turn the picture sideways #Shorts"),
 2: dict(shots=[28, 32, 33, 34], hook="THE FLAMES ARE JAWS", title="Pakal's sarcophagus lid: the 'rocket flames' are the open jaws of the Maya underworld #Shorts"),
 3: dict(shots=[14, 15, 17, 18, 19], hook="SEALED FOR 1,200 YEARS", title="How an archaeologist found Pakal's hidden tomb under a Palenque pyramid in 1952 #Shorts"),
 4: dict(shots=[45, 46, 47, 49], hook="80 OR 45?", title="Pakal's bones looked 40 years too young. The real mystery inside the tomb at Palenque #Shorts"),
 5: dict(shots=[52, 53, 54, 55], hook="A CLOUD, NOT A ROCKET", title="Why Pakal's lid looks like a pilot to us: the cloud that looks like a dog #Shorts"),
}
TAGS = "#Palenque #Pakal #Maya #AncientMysteries #Documentary"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Pakal-Palenque-Lid.mp4', "Pakal's Tomb Lid: Ancient Astronaut or Maya King? We Went Down the Hidden Stair", CLIPS, TAGS, n)
