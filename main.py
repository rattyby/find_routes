import csv
from copy import deepcopy
from vehicles import Car, Truck, Bus, Suv


def csv_to_list(file_path: str) -> list:
    """
    Читает файл с исходными данными и преобразует в список кортежей для дальнейшей обработки
    """
    res_list = []
    with open(file_path) as csvfile:
        intro_data = csv.reader(csvfile)
        # пропускаем headers
        next(intro_data)
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


def route_print(route: list, start: str, finish: str, transit: list, gas: float) -> None:
    print(f'Для поездки из {start} в {finish} на выбранном транспорте потребуется {gas:.2f}л топлива.')
    print(f'Обязательны к посещению {", ".join(transit)}.')
    print('Маршрут передвижения следующий:')
    for point in route[0][:-1]:
        print(point, end=' -> ')
    print(route[0][-1])
    return None


if __name__ == '__main__':
    data = csv_to_list('map.csv')
    distances = create_weighted_distances(data)

    start_point = input('Введите начальный пункт\n')
    # start_point = 'brest'
    finish_point = input('Введите конечный пункт\n')
    # finish_point = 'vilna'
    transit_points = input('Введите промежуточные пункты через пробел\n').split()
    transit_points = [p for p in transit_points]
    # transit_points = ['lida', 'polack', 'hrodna', 'minsk']

    best_route = [[start_point], float('inf')]  # [[whole_route], weight] - start=route[0][0], finish=route[0][-1]
    routes = [best_route]  # list of lists with routes

    # построение маршрутов
    # maxroutes = 0
    while True:
        for point, weight in distances[routes[0][0][-1]].items():
            # если вес нового этапа пути больше веса лучшего, то пропускаем
            if weight >= best_route[1] - routes[0][1]:
                continue
            new_route = add_destination(routes[0], point, weight)
            # если маршрут более 4 точек, и последние 4 выглядят как ABAB, то это точно не лучший вариант
            if len(new_route[0]) >= 4 and new_route[0][-1] == new_route[0][-3] and new_route[0][-2] == new_route[0][-4]:
                continue
            # если вес нового маршрута больше или равен лучшего - пропускаем сразу
            # также если повторяются одни и те же пункты - видимо, мы ездим по кругу
            if new_route[1] < best_route[1] and len(new_route[0]) / len(set(new_route[0])) < 3:
                # если новая точка соответствует финишной - проверяем транзитные
                if new_route[0][-1] == finish_point:
                    check_transit = [t in new_route[0] for t in transit_points]
                    # если все транзитные есть - это новый лучший путь, его продлевать незачем, так что переходим дальше
                    if not False in check_transit:
                        best_route = new_route
                        continue
                # оставляем маршрут для дальнейшего расширения
                routes.append(new_route)
                # if len(routes) > maxroutes:
                #     maxroutes = len(routes)
        # убираем рассмотренный маршрут; если routes опустел - варианты закончились
        del routes[0]
        if not routes:
            break

    # выбор транспортного средства
    vehicle_type = input('Введите транспорт (1 - легковой, 2 - автобус, 3 - грузовой, 4 - внедорожник)')
    if vehicle_type == '1':
        vehicle = Car()
    elif vehicle_type == '2':
        vehicle = Bus()
    elif vehicle_type == '3':
        vehicle = Truck()
    else:
        vehicle = Suv()
    print()
    # расход топлива
    gasoline = best_route[1] * vehicle.consumption / 100 / vehicle.patency

    route_print(best_route, start_point, finish_point, transit_points, gasoline)
    # print('max count routes', maxroutes)
