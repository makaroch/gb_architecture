from typing import List

from item_fabric import *
from random import randint


def create_one_items_lst(count: int, generator: ItemFabric) -> List[ItemFabric]:
    return [generator() for i in range(count)]


def create_items_generators(count_gold: int, count_gem: int, count_item1: int, count_item2: int,
                            count_item3: int, count_item4: int, count_item5: int) -> List[ItemFabric]:
    return (create_one_items_lst(count_gold, GoldGenerator) +
            create_one_items_lst(count_gem, GemGenerator) +
            create_one_items_lst(count_item1, Item1Generator) +
            create_one_items_lst(count_item2, Item2Generator) +
            create_one_items_lst(count_item3, Item3Generator) +
            create_one_items_lst(count_item4, Item4Generator) +
            create_one_items_lst(count_item5, Item5Generator))


def main():
    items_generator = create_items_generators(3, 1, 10,
                                              10, 10, 10, 10)

    for _ in range(10):
        items_generator[randint(0, len(items_generator)-1)].create_item().open()


if __name__ == "__main__":
    main()
