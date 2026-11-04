"""5 vertical clip Shorts from Terracotta-Army-Chromium.mp4 via bank/cloud/shorts_lib.py (hand-picked: claim + payoff, each <=59 s). usage: python3 make_shorts.py [n ...]"""
import sys, os; E = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(E, '..', 'cloud')); import shorts_lib as L
CLIPS = {
 1: dict(shots=[1, 2, 3, 4], hook="LOST TECH SWORDS?", title="The Terracotta Army's swords stayed sharp for 2,200 years. Was it a lost chrome technology? #Shorts"),
 2: dict(shots=[33, 34, 35, 38, 39], hook="THE CHROME CLUE", title="Chromium was on fewer than 10% of Terracotta Army weapons. Here is what that proves #Shorts"),
 3: dict(shots=[6, 7, 8, 9], hook="A WELL DUG IN 1974", title="Farmers digging a well in 1974 hit a clay head. The army of Qin Shi Huang #Shorts"),
 4: dict(shots=[49, 50, 52, 53, 54], hook="THE REAL SECRET", title="Why Terracotta Army weapons survived 2,200 years: it was the soil, not magic chrome #Shorts"),
 5: dict(shots=[63, 64, 65, 66], hook="CHROME COATING: TRUE?", title="Terracotta Army chrome coating myth: the final verdict from the lab #Shorts"),
}
TAGS = "#TerracottaArmy #AncientMysteries #China #Archaeology #History"
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else CLIPS):
        L.build(E, 'Terracotta-Army-Chromium.mp4', "Terracotta Army Swords: Lost Technology or Lacquer? The Lab Report", CLIPS, TAGS, n)
