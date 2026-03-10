from enum import StrEnum, auto

BULKY_VOLUME = 1_000_000
BULKY_DIMENSION = 150
HEAVY_WEIGHT = 20

class PackageType(StrEnum):
    STANDARD = auto()
    SPECIAL = auto()
    REJECTED = auto()

def sort(width: float, height: float, length: float, mass: float) -> str:
    """

    :param width: width of package in cm
    :param height: height of package in cm
    :param length: length of package in cm
    :param mass: mass of package in kg
    :return: string designating stack package should go to
    """

    package_type = PackageType.STANDARD

    is_bulky_volume = (width * height * length) >= BULKY_VOLUME
    is_bulky_dimension = (width >= BULKY_DIMENSION
                               or height >= BULKY_DIMENSION
                               or length >= BULKY_VOLUME)

    is_bulky = is_bulky_volume or is_bulky_dimension

    is_heavy = mass >= HEAVY_WEIGHT

    if is_bulky and is_heavy:
        package_type = PackageType.REJECTED
    elif is_bulky or is_heavy:
        package_type = PackageType.SPECIAL

    return package_type.upper()

if __name__ == '__main__':
    # STANDARD
    print(sort(10, 10, 10, 5))
    print(sort(100, 99, 100, 19))
    print(sort(149, 1, 1, 1))
    print(sort(50, 40, 30, 10))

    # SPECIAL - bulky
    print(sort(150, 1, 1, 1))
    print(sort(200, 10, 10, 5))
    print(sort(100, 100, 100, 5))
    print(sort(200, 200, 200, 1))

    # SPECIAL - heavy
    print(sort(10, 10, 10, 20))
    print(sort(10, 10, 10, 25))
    print(sort(149, 1, 1, 50))

    # REJECTED
    print(sort(150, 1, 1, 20))
    print(sort(200, 200, 200, 25))
    print(sort(100, 100, 100, 20))
    print(sort(10, 10, 10000, 30))
