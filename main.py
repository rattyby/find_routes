import csv


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
            res_dict[way[0]][way[1]] = int(way[2]) * int(way[3])
        else:
            res_dict[way[0]] = {way[1]: int(way[2]) * int(way[3])}
        if res_dict.get(way[1]):
            res_dict[way[1]][way[0]] = int(way[2]) * int(way[3])
        else:
            res_dict[way[1]] = {way[0]: int(way[2]) * int(way[3])}
    return res_dict

if __name__ == '__main__':
    data = csv_to_list('test_data.csv')
    distances = create_weighted_distances(data)
    best_route = []  # [start, finish, [whole_route], weight]
    routes = []
