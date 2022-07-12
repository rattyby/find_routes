# Поиск оптимального маршрута

## Задача
Имеется набор населённых пунктов и дорог между некоторыми из них. Эти данные задаются в файле _map.csv_ в формате 
`START_POINT,FINISH_POINT,DESTINATION,HARDNESS`, 
где `START` и `FINISH` - пункты, соединённые дорогой, `DESTINATION` - расстояние между ними, `HARDNESS` - сложность дороги.

Задаются начальная и конечная точки маршрута, а также промежуточные, обязательнын к посещению, пункты.
Также задаётся транспорт, один из доступных:
- Легковой автомобиль (расход топлива 10л/100км, проходимость 3)
- Грузовой автомобиль (расход 12, проходимость 2)
- Автобус (расход 15, проходимость 1)
- Внедорожник (расход 18, проходимость 6)

Расход топлива вычисляется по следующей формуле:
`Расстояние * (Расход / 100км) * (Сложность_дороги / Проходимость)`

### Требуется
Найти маршрут от начальной до конечной точки с посещением всех промежуточных пунктов минимум один раз, при котором для заданного транспорта будет **минимальный расход топлива**.

## Решение
Сначала строится карта связанности пунктов из файла _map.csv_, данные заносятся в симметричный словарь.
Для веса дорог используется произведение расстояния на сложность дороги.
Таким образом достигается универсальность полученного маршрута для любого транспортного средства.

Изначально длина лучшего маршрута устанавливается в бесконечность, чтобы любой найденный вариант был лучше.
Сам маршрут при этом состоит из начальной точки.
Далее, начиная от стартовой точки, совершается проход по словарю - заполняются все возможные варианты развития маршрута.
Сами маршруты складываются в список по принципу FIFO.
После каждой итерации продления маршрутов, текущий маршрут удаляется. 
Если очередной найденный пункт совпадает в конечным - проверяется вхождение всех промежуточных пунктов в текущий маршрут.
В случае совпадения - найденный маршрут становится лучшим, при условии, что его вес меньше действующего лучшего маршрута.

Далее итерации повторяются. 
Для уменьшения времени работы алгоритма применяются дополнительные проверки.
Маршрут не заносится в очередь, если:
- вес новой ветви пути превышает разницу веса между действующим лучшим маршрутом и текущим; 
- его вес превышает вес действующего лучшего маршрута;
- последние 2 пункта повторяются: ...-A-B-A-B. Это значит, что маршрут заведомо не лучший;
- количество точек маршрута в 3 и более раз превышает количество уникальных точек. Значит, маршрут закольцевался в лёгких ветвях.

### Ограничения
1. Алгоритм полного перебора - работает очень долго.
Поэтому добавлен вывод промежуточных найденных маршрутов, чтобы максимально быстро появились варианты движения.
2. Занимает много памяти для хранения всех маршрутов. 
Для минимизации добавлены условия, по которым маршруты отбрасываются без внесения в очередь.