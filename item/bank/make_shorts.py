"""5 vertical clip Shorts from Hessdalen-Lights.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 62], hook="ALIEN ORBS IN NORWAY?", title="The Hessdalen lights: Norway's glowing orbs and the verdict #Shorts"),
 2: dict(shots=[29, 30, 31], hook="IT ANSWERED A LASER", title="Hessdalen 1984: the light that changed its flash when a laser hit it #Shorts"),
 3: dict(shots=[19, 20, 21], hook="RADAR SAW SOMETHING", title="Hessdalen radar echoes as strong as mountains: what the 1984 team recorded #Shorts"),
 4: dict(shots=[35, 36, 37], hook="188 SIGHTINGS. 53 REAL.", title="Project Hessdalen sorted 188 reports: only 53 were the real phenomenon #Shorts"),
 5: dict(shots=[52, 53, 54], hook="JUST AIRPLANES?", title="Are the Hessdalen lights airplane landing lights? The skeptic case #Shorts"),
}
TAGS = "#Hessdalen #UFO #Norway #UnsolvedMysteries #Plasma"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Hessdalen-Lights.mp4', "Hessdalen Lights: Norway's Glowing Orbs Tested With Radar, Spectrum and a Laser", CLIPS, TAGS, n)
