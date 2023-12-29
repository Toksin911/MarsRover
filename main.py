# 104042728
def mars_rover(robots: list[int], limit: int) -> int:
    """Рассчитать количество платформ."""
    platforms: int = 0  # Число платформ.
    position_max: int = len(robots) - 1  # Наибольшое число в моссиве.
    position_min: int = 0  # Наименьшое число в моссиве.
    while position_max >= position_min:
        if (robots[position_max] + robots[position_min]) <= limit:
            position_min += 1
        position_max -= 1
        platforms += 1
    return platforms


if __name__ == '__main__':
    robots: list[int] = [int(array_count) for array_count in input().split()]
    limit = int(input())
    robots.sort()
    print(mars_rover(robots, limit))
