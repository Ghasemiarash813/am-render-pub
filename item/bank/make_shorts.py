"""5 vertical clip Shorts from Teotihuacan-Mica-Mercury.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 36], hook="POWER PLANT UNDER A PYRAMID?", title="Liquid mercury under a Mexican pyramid: ancient power plant or sacred underworld? #Shorts"),
 2: dict(shots=[6, 7, 8], hook="A SINKHOLE OPENED...", title="A sinkhole at Teotihuacan revealed a tunnel sealed for 1,800 years #Shorts"),
 3: dict(shots=[25, 32, 33], hook="MICA FROM BRAZIL? NO.", title="Teotihuacan's 'Brazilian' mica was tested. The lab said Oaxaca #Shorts"),
 4: dict(shots=[35, 37, 38], hook="WHERE ARE THE WIRES?", title="If it was a power plant, where are the wires? Teotihuacan's parts list #Shorts"),
 5: dict(shots=[43, 44, 45], hook="STARS UNDERGROUND", title="Why a Teotihuacan tunnel was covered in fool's gold and mercury #Shorts"),
}
TAGS = "#Teotihuacan #AncientMexico #AncientMysteries #Archaeology #AncientAliens"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Teotihuacan-Mica-Mercury.mp4', "Teotihuacan's Hidden Mercury and Mica: Ancient Power Plant or Sacred Underworld?", CLIPS, TAGS, n)
