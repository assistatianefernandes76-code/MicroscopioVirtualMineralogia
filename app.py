import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi
import random

# Minerais e cores
minerais = {
    "HM": "#6d6d6d",
    "HE": "#c0c0c0",
    "Magnetita": "#000000",
    "Goethita": "#b8860b",
    "Quartzo": "#ffffff"
}

# Número de grãos
n_graos = 100

# Geração aleatória
np.random.seed(42)
pontos = np.random.rand(n_graos, 2)

# Voronoi
vor = Voronoi(pontos)

fig, ax = plt.subplots(figsize=(8,8))

for region_index in vor.point_region:

    region = vor.regions[region_index]

    if -1 in region or len(region) == 0:
        continue

    polygon = [vor.vertices[i] for i in region]

    mineral = random.choice(list(minerais.keys()))

    ax.fill(
        [p[0] for p in polygon],
        [p[1] for p in polygon],
        color=minerais[mineral],
        edgecolor="gray"
    )

ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect("equal")

plt.show()
