"""
Greedy method: When solving a problem, always make the best choice in the current view,
Do not pursue the optimal solution, but quickly find a satisfactory solution.
"""
class Thing(object):
    """thing"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        """Price to weight ratio"""
        return self.price / self.weight


def input_thing():
    """Enter item information"""
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)


def main():
    """Main function"""
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'The thief took {thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'Total value: {total_price}$')


if __name__ == '__main__':
    main()