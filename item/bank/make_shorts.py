"""5 vertical clip Shorts from Gorman-Dogfight-1948.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 11, 12], hook="A LIGHT FOUGHT HIM?", title="1948: A pilot said a round white light dogfought him for 27 minutes over Fargo. What was it? #Shorts"),
 2: dict(shots=[23, 24, 27, 28, 29], hook="THE HEAD-ON PASS", title="The Gorman dogfight: the light turned head-on, passed over his canopy, then shot straight up #Shorts"),
 3: dict(shots=[16, 17, 18, 19], hook="SIX WITNESSES SAW IT", title="Fargo 1948: tower controllers and a Piper Cub pilot saw the light too #Shorts"),
 4: dict(shots=[40, 41, 45, 46], hook="JUST A BALLOON?", title="The official explanation for the Gorman UFO dogfight: a weather balloon. Gorman never believed it #Shorts"),
 5: dict(shots=[55, 56, 57, 59], hook="WAS IT JUPITER?", title="Jupiter, a mirage, or something else? The suspects in the 1948 Gorman dogfight #Shorts"),
}
TAGS = "#Gorman #UFO #Fargo #ProjectBlueBook #AncientMachines"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Gorman-Dogfight-1948.mp4', "The Gorman Dogfight 1948: The Pilot Who Fought a Light Over Fargo (Evidence vs Theory)", CLIPS, TAGS, n)
