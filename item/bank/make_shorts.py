"""5 vertical clip Shorts from Ica-Stones.mp4 via bank/cloud/shorts_lib.py (hand-picked). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[2, 17, 18, 21], hook="DINOSAURS DRAWN BY EYEWITNESSES?", title="These 'ancient' Peruvian stones drew dinosaurs exactly like 1960s textbooks #Shorts"),
 2: dict(shots=[37, 39, 40, 43], hook="THE CHICKENS DID THE REST", title="The farmer who 'aged' the Ica stones in dung, boot polish and a chicken pen #Shorts"),
 3: dict(shots=[22, 24, 25, 26], hook="HEART SURGERY IN STONE?", title="Ancient heart transplants carved in stone? Look at the timing #Shorts"),
 4: dict(shots=[48, 51, 52], hook="OLD STONE. NEW GROOVES.", title="The lab test that exposed the Ica stones and their clay dinosaurs #Shorts"),
 5: dict(shots=[54, 55, 56, 57], hook="THE SECRET CAVE", title="The secret cave of 100,000 Ica stones that nobody was allowed to see #Shorts"),
}
TAGS = "#IcaStones #AncientMysteries #Peru #Dinosaurs #Archaeology"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Ica-Stones.mp4', "The Ica Stones: Dinosaurs, Heart Surgery & Telescopes Carved in Ancient Peru? (Tested)", CLIPS, TAGS, n)
