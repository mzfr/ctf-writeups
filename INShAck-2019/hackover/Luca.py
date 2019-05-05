import random

with open("routes.txt") as f:
   routes = f.readlines()

with open("sol.txt") as f:
   sol = [l.strip() for l in f.readlines()]

routes = [set(r.strip().split(',')) for r in routes]

routes.sort(key = lambda s: len(s))

def fix_cover(cover):
   for r in routes:
       if len(cover & r) == 0:
           chosen = random.sample(r, 1)[0]
           cover.add(chosen)
   return cover

cover = set(sol)

def compute_importance(cover, routes):
   nodes = list(cover)
   importances = []
   for n in nodes:
       importance = 0
       for r in routes:
           if n in r:
               importance += 1.0 / 10**(len(cover & r))
       importances.append(importance)

   nodes = [[nodes[i], importances[i]] for i in range(len(nodes))]
   nodes.sort(key = lambda s: s[1])

   new_cover = set()
   for n in nodes[30:]:
       new_cover.add(n[0])
   return new_cover


score = len(cover)
while True:
   new_cover = compute_importance(cover, routes)
   new_cover = fix_cover(new_cover)
   new_score = len(new_cover)
   if new_score < score:
       print(new_score)
       score = new_score
       cover = new_cover
   if score == 126:
       with open("sol126.txt", "w") as f:
           for c in cover:
               f.write(c+"\n")
       break
