#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решить индивидуальное задание 2 лабораторной работы 7, оформив каждую команду в виде
# отдельной функции.

# Условие из Лабораторной работы 7.
# В лабораторной работе 6 необходимо дополнительно
# реализовать сохранение и чтение данных из файла формата JSON.

# Использовать словарь, содержащий следующие ключи: название товара; название
# магазина, в котором продается товар; стоимость товара в руб. Написать программу,
# выполняющую следующие действия: ввод с клавиатуры данных в список, состоящий из
# словарей заданной структуры; записи должны быть размещены в алфавитном порядке по
# названиям магазинов; вывод на экран информации о товарах, продающихся в магазине,
# название которого введено с клавиатуры; если такого магазина нет, выдать на дисплей
# соответствующее сообщение.

import sys
import json

def add(market, product, shop, price):
    # Создать словарь.

    markets = {
        'product': product,
        'shop': shop,
        'price': price,
    }

    # Добавить словарь в список.
    market.append(markets)
    # Отсортировать список в случае необходимости.
    if len(market) > 1:
        market.sort(key=lambda item: item.get('product', ''))

def list(market):
    table = []
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 20
    )
    table.append(line)
    table.append(
        '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
            "No",
            "Товар",
            "Магазин",
            "Стоимость в руб."
        )
    )
    table.append(line)

    # Вывести данные о всех товарах.
    for idx, markets in enumerate(market, 1):
        table.append(
            '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                idx,
                markets.get('product', ''),
                markets.get('shop', ''),
                markets.get('price', 0)
            )
        )

    table.append(line)
    return '\n'.join(table)

def select(market, plane):

    # Инициализировать результат.
    result = []
    # Проверить сведения продукта из списка.
    for markets in market:
        if plane == markets.get('place'):
            result.append(markets)

    return result


def load(filename):
    with open(filename, 'r') as fin:
        return json.load(fin)


def save(produckts, filename):
    with open(filename, 'w') as fout:
        json.dump(produckts, fout)

if __name__ == '__main__':
    # Список магазинов.
    market = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о товаре.
            product = input("Название товара? ")
            shop = input("Название магазина? ")
            price = float(input("Стоимость товара в руб.? "))

            add(market, product, shop, price)

        elif command == 'list':
            print(list(market))

        elif command.startswith('select '):
            # Разбить команду на части.
            parts = command.split(' ', maxsplit=1)
            # Получить список товаров.
            selected = select(market, parts[1])
            period = str(parts[1])
            # Инициализировать счетчик.
            count = 0
            # Проверить сведения товара из списка.
            for markets in market:
                if markets.get('product') >= period:
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, markets.get('product', ''))
                    )
                    print('Название магазина:', markets.get('shop', ''))
                    print('Стоимость в руб.:', markets.get('price', ''))

            # Если счетчик равен 0, то товары не найдены.
            if count == 0:
                print("Продукт не найден.")

        elif command.startswith('load '):
            # Разбить команду на части для имени файла.
            plane = command.split(maxsplit=1)
            # Загрузить данные из файла
            market = load(plane[1])

        elif command.startswith('save '):
            # Разбить команду на части для имени файла.
            plane = command.split(maxsplit=1)
            # Сохранить данные в файл
            save(market, plane[1])

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n"
                  "add - добавить продукт\n"
                  "list - вывести список продуктов\n"
                  "select <товар> - информация о товаре\n"
                  "help - отобразить справку\n"
                  "exit - завершить работу с программой")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
