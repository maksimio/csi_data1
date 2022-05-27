# Аннотация
Эксперимент по классификации металлических объектов с наличием искажений физической обстановки. Дата: 27.05.2022.

Полученные данные предназначены для изучения задачи детектирования (сначала детектирование, а потом распознавание конкретного металлического объекта), а также на фиксацию влияния изменения физической обстановки на результаты классификации и уменьшение этого влияния

## Объекты
Расстояние между роутерами: 2 метра. Объект размещается примерно посередине между ними. Угол наклона антенн ~ 15 градусов суммарно (расстояние между концами антенн 20см). Установлен 11 канал Wi-Fi, 20 МГц (56 поднесущих на пару антенн Tx-Rx), расстояние между кончиками антенн 20 см. Суммарно для каждого из 6 экспериментов было снято по 30 000 пакетов. Они имеют следующий баланс данных:

1. Нет объекта - empty.dat (40%, ~12000 пакетов)
2. Кастрюля - casserole.dat (20%, ~6000 пакетов)
3. Термос - bottle.dat (20%, ~6000 пакетов)
4. Терка - grater.dat (20% данных, ~6000 пакетов)

![](./img/objects.jpg)

## Эксперименты:
1) Базовый эксперимент (комната, 2 метра расстояние, нет посторонних предметов рядом): ![](./img/1.jpg)
2) Сбоку от места размещения объекта фиксированно стоит полная бутылка воды 1.5 литра: ![](./img/2.jpg)
3) Над местом размещения объекта стоит стул с металлическими ножками: ![](./img/3.jpg)
4) Расстояние увеличено до 3 метров, оба маршрутизатора отодвигаются на 0.5 метров: ![](./img/4.jpg)
5) Другое помещение: ![](./img/5.jpg)
6) Базовый эксперимент - повтор в целях отладки (как test dataset для эксперимента №1)

## Сценарий исследования
Обучить модели на данных 1 эксперимента. Протестировать на 6 - если точность высока, то классификация возможна, и нужно тестировать модели на экспериментах 2-5. Если точность упала, то нужно обрабатывать данные CSI.

## Результаты
> Этот раздел будет дополнен