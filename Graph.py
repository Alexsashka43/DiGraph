import itertools
import inline as inline
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import networkx as nx
import itertools as it

G = nx.DiGraph()


cities = ['Наро-Фоминск', 'Сергиев Посад', 'Воскресенск', 'Лобня', 'Клин', 'Дубна', 'Чехов', 'Дмитров', 'Ступино',
        'Павловский Посад', 'Фрязино', 'Дзержинский', 'Балашиха', 'Солнечногорск', 'Кашира', 'Протвино', 'Шатура',
        'Ликино-Дулёво', 'Красноармейск', 'Химки']

coord_city = ["Наро-Фоминск, 55.39, 36.73, Сергиев Посад, 56.3, 38.13, Воскресенск, 55.32, 38.65, Лобня, 56.01, 37.48, "
         "Клин, 56.33, 36.73, Дубна, 56.73, 37.17, Чехов, 55.15, 37.48, Дмитров, 56.34, 37.52, Ступино, 54.9, 38.07, "
         "Павловский Посад, 55.78, 38.65,Фрязино, 55.96, 38.05, Дзержинский, 55.63, 37.85, Балашиха, 55.81, 37.96, "
         "Солнечногорск, 56.18, 36.98, Кашира, 54.50, 38.11, Протвино, 54.52, 37.12, Шатура,55.34, 39.32, "
         "Ликино-Дулёво, 55.42, 38.57, Красноармейск, 56.06, 38.08, Химки, 55.9, 37.43"]

distance_between_cities = [158, 150, 104, 137, 205, 90, 143, 139, 143, 115, 86, 95, 114, 148, 86, 223, 198, 148,
                           84, 160, 85, 110, 103, 157, 51, 187, 98, 58, 91, 81, 102, 196, 203, 154, 108, 44, 77,
                           134, 203, 210, 100, 170, 73, 67, 118, 82, 99, 170, 85, 120, 76, 51, 126, 126, 81, 105,
                           118, 48, 159, 100, 57, 63, 53, 48, 168, 164, 172, 125, 76, 21, 86, 179, 60, 220, 170,
                           127, 133, 123, 24, 229, 225, 252, 207, 121, 86, 146, 57, 136, 190, 135, 156, 146, 110,
                           130, 133, 246, 200, 120, 119, 157, 69, 130, 114, 73, 95, 149, 78, 40, 174, 148, 146, 98,
                           196, 114, 78, 100, 90, 59, 205, 201, 194, 149, 63, 62, 146, 142, 101, 123, 188, 12, 89,
                           146, 121, 174, 138, 59, 67, 51, 138, 156, 175, 73, 26, 71, 93, 48, 22, 93, 153, 160, 131,
                           84, 35, 48, 27, 99, 112, 119, 156, 86, 79, 54, 89, 133, 141, 123, 75, 57, 45, 198, 194,
                           211, 164, 94, 55, 98, 158, 133, 184, 147, 193, 168, 192, 144, 51, 143, 164, 96, 117, 63]

coord = [55.39, 36.73, 56.3, 38.13, 55.32, 38.65, 56.01, 37.48, 56.33,
         36.73, 56.73, 37.17, 55.15, 37.48, 56.34, 37.52, 54.9, 38.07,
         55.78, 38.65, 55.96, 38.05, 55.63, 37.85, 55.81, 37.96,
         56.18, 36.98, 54.50, 38.11, 54.52, 37.12, 55.34, 39.32,
         55.42, 38.57, 56.06, 38.08, 55.9, 37.43]

# Добавим 20 вершим
"""Добавляем города"""
G.add_nodes_from(cities)
"""Комбинация городов"""
comb_city = []
com_set = itertools.combinations(cities, 2)
for i in com_set:
    comb_city.append(i)


# Добавим ребра и связи между ними
for coupe_cities_1, coupe_cities_2 in comb_city:
    G.add_edge(coupe_cities_1, coupe_cities_2, weigth=distance_between_cities)


# Присвоим координаты вершинам
for coord_pos in cities:
    i = 0
    j = 1
    G.nodes[coord_pos]['pos'] = (coord[i + 2],coord[j + 2])


# Координаты вершин храняться в словаре
node_pos = nx.get_node_attributes(G, 'pos')

# Веса ребер и доп аттрибуты тоже храняться в словаре
arc_weight = nx.get_edge_attributes(G, 'length')

# Отрисовываем вершины
nx.draw_networkx(G, node_pos, node_size=10)

# Отрисовываем ребра
nx.draw_networkx_edges(G, node_pos)

# Подписываем вершины, ребра и веса
nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)

# Удалим координатные оси
plt.axis('off')

# Выводим
plt.show()

# Вычисляем кратчайший путь между вершинами (По умолчанию в shortest_path используется алгоритм Дейкстры)
for coupe_cities_1, coupe_cities_2 in comb_city:
    nx.shortest_path(G, source=coupe_cities_1, target=coupe_cities_2, weight="length")

# Получаем все варианты кратчайших путей, all_p - это Генератор
for coupe_cities_1, coupe_cities_2 in comb_city:
    all_p = nx.all_shortest_paths(G, source=coupe_cities_1, target=coupe_cities_2, weight="length")
    next(all_p)
# Вычисляем Кратчайший путь по алгоритму Дейкстры
for coupe_cities_1, coupe_cities_2 in comb_city:
    nx.dijkstra_path(G, source=coupe_cities_1, target=coupe_cities_2, weight="length")

# next(all_p)

# Вычисляем длину Кратчайшего пути по алгоритму Дейкстры
for coupe_cities_1, coupe_cities_2 in comb_city:
    nx.dijkstra_path_length(G, source=coupe_cities_1, target=coupe_cities_2, weight="length")

