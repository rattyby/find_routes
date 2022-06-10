import csv
from copy import deepcopy


def csv_to_list(file_path: str) -> list:
    """
    Читает файл с исходными данными и преобразует в список кортежей для дальнейшей обработки
    """
    res_list = []
    with open(file_path)  as csvfile:
        intro_data = csv.reader(csvfile)
        for row in intro_data:
            res_list.append(tuple(row))
    return res_list


def create_weighted_distances(ways_list: list) -> dict:
    """
    Создаёт из исходного списка симметричный словарь со взвешенными расстояниями до соседних пунктов
    """
    res_dict = {}
    for way in ways_list:
        if res_dict.get(way[0]):
            res_dict[way[0]][way[1]] = float(way[2]) * float(way[3])
        else:
            res_dict[way[0]] = {way[1]: float(way[2]) * float(way[3])}
        if res_dict.get(way[1]):
            res_dict[way[1]][way[0]] = float(way[2]) * float(way[3])
        else:
            res_dict[way[1]] = {way[0]: float(way[2]) * float(way[3])}
    return res_dict


def add_destination(route: list, destination: str, weight: float) -> list:
    """ Добавляет маршрут с новой точкой """
    new_route = deepcopy(route)
    if new_route[1] == float('inf'):
        new_route[1] = 0
    new_route[0].append(destination)
    new_route[1] += weight
    return new_route


if __name__ == '__main__':
    # q_ways = input('Имя файла с исходными данными\n')
    # data = csv_to_list(q_ways)
    data = csv_to_list('test_data.csv')
    distances = create_weighted_distances(data)

    # start_point = input('Введите начальный пункт\n').capitalize()
    start_point = 'A'
    # finish_point = input('Введите конечный пункт\n').capitalize()
    finish_point = 'F'
    # transit_points = input('Введите промежуточные пункты через пробел\n').split()
    # transit_points = [p.capitalize() for p in transit_points]
    transit_points = ['B', 'C']
    
    best_route = [['A'], float('inf')]  # [[whole_route], weight] - start=route[0][0], finish=route[0][-1]
    routes = [best_route]  # list of lists with routes

    # построение маршрутов
    while True:
        for point, weight in distances[routes[0][0][-1]].items():
            # если вес нового этапа пути больше веса лучшего, то пропускаем
            if weight >= best_route[1]:
                continue
            new_route = add_destination(routes[0], point, weight)
            # если вес нового маршрута больше или равен лучшего - пропускаем сразу
            if new_route[1] < best_route[1]:
                # если новая точка соответствует финишной - проверяем транзитные
                if new_route[0][-1] == finish_point:
                    check_transit = [t in new_route[0] for t in transit_points]
                    # если все транзитные есть - это новый лучший путь, его продлевать не имеет смысла, так что переходим дальше
                    if not False in check_transit:
                        best_route = new_route
                        continue
                # оставляем маршрут для дальнейшего расширения
                routes.append(new_route)
        # убираем рассмотренный маршрут; если routes опустел - варианты закончились
        del routes[0]
        if not routes:
            break
    
    print(best_route)
