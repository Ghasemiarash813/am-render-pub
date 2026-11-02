"""5 vertical clip Shorts from Hayu-Marca-Gate-of-the-Gods.mp4 via bank/cloud/shorts_lib.py (hand-picked). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[2, 24, 29, 30], hook="INVENTED IN 1961?", title="Peru's 'Gate of the Gods' priest Aramu Muru comes from a 1961 UFO contactee book #Shorts"),
 2: dict(shots=[13, 14, 19], hook="HE DREAMED IT FIRST", title="The guide who 'discovered' Peru's stargate said he saw it in his dreams first #Shorts"),
 3: dict(shots=[1, 17, 9], hook="A DOOR TO NOWHERE", title="A 7-metre door carved into a Peruvian cliff that opens onto solid rock #Shorts"),
 4: dict(shots=[32, 33, 34, 35], hook="THE PRIEST WHO NEVER EXISTED", title="The Inca priest who opened a portal with a golden disk? No chronicle names him #Shorts"),
 5: dict(shots=[57, 58, 59], hook="WHY YOU FEEL 'ENERGY'", title="Why visitors feel 'energy' at Peru's Gate of the Gods (and what's really harming it) #Shorts"),
}
TAGS = "#AramuMuru #GateOfTheGods #LakeTiticaca #AncientMysteries #Archaeology"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Hayu-Marca-Gate-of-the-Gods.mp4', "Peru's Gate of the Gods: Ancient Stargate or Inca Shrine? (Aramu Muru, Lake Titicaca)", CLIPS, TAGS, n)
