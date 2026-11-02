"""5 vertical clip Shorts from Baghdad-Battery.mp4 via bank/cloud/shorts_lib.py (hand-picked). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[32, 33, 34], hook="4 VOLTS FROM A CLAY JAR?", title="MythBusters got 4 volts from the 'Baghdad Battery'. Here's the catch #Shorts"),
 2: dict(shots=[18, 23, 24, 25], hook="WHY IT CAN'T WORK", title="The seal that kills the 2,000-year-old 'Baghdad Battery' #Shorts"),
 3: dict(shots=[39, 40, 41, 42], hook="NO WIRES. NO PLATING.", title="If the Baghdad Battery was a battery, where are the wires? #Shorts"),
 4: dict(shots=[8, 44, 45], hook="AN ANCIENT SECRET?", title="The 'ancient' gilding secret behind the Baghdad Battery was 99 years old #Shorts"),
 5: dict(shots=[46, 47, 50, 52], hook="WHAT WAS INSIDE?", title="The Baghdad Battery's cousins were opened. They held scrolls #Shorts"),
}
TAGS = "#BaghdadBattery #AncientMysteries #Archaeology #AncientAliens #AncientTechnology"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Baghdad-Battery.mp4', "The Baghdad Battery: 2,000-Year-Old Electricity or a Scroll Jar?", CLIPS, TAGS, n)
