import json

def Node:
  def __init__(self, name, company, goodness):
    self.name = name
    self.company = company
    self.goodness = goodness
def Edge:
  def __init__(self, name1, name2, strength):
    self.name1, self.name2 = name1, name2
    self.strength = strength

def norm(v, s=None):
  s = s or sum(v)
  return [e/s for e in v]
#normalizes outgoing probabilities of a directed graph
def preprocess(net):
  return [norm(vec) for vec in net]

def makeJSON(nodes, edges):
  return json.dumps({
    'nodes': list(map(lambda n: [n.name, n.company, n.goodness], nodes)),
    'edges': list(map(lambda e: [e.name1, e.name2, e.strength], edges)),
  })

'''
graph - weighted adjacency matrix.
start - initial vertex for random walk.
P     - probability of stopping walk each step.
k     - iterations before quitting.
'''
def markovWalk(graph, start, P, k):
  V = len(graph)
  vals = [0]*V
  vals[start] = 1
  probs = [0]*V
  for itr in range(k):
    nextv = [0]*V
    for i in range(V):
      val = vals[i]
      for j,w in enumerate(graph[i]):
        nextv[j] += w*val
    vals = nextv
    for i in range(V):
      probs[i] += P*vals[i]
      vals[i] *= 1-P
  return [p+v for p,v in zip(probs,vals)]
'''
#usage:

g = [
  [0, 0.9, 0.1],
  [0.1, 0, 0.9],
  [0.1, 0.9, 0]
]

g2 = [
  [0, 0.9, 0.1],
  [0.1, 0, 0.9],
  [0.1, 0.9, 0]
]
#divides all the connection strengths by 3
g2 = [norm(v,3.0) for v in g2]

print(markovWalk(preprocess(g), 0, 0.1, 50))
print(markovWalk(preprocess(g2), 0, 0.1, 50))
'''