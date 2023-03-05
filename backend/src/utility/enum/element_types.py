import enum


class PokemonElementTypes(enum.Enum):
    BUG = 0
    DARK = 1
    DRAGON = 2
    ELECTRIC = 3
    FAIRY = 4
    FIGHTING = 5
    FIRE = 6
    FLYING = 7
    GHOST = 8
    GRASS = 9
    GROUND = 10
    ICE = 11
    NORMAL = 12
    POISON = 13
    PSYCHIC = 14
    ROCK = 15
    STEEL = 16
    WATER = 17

    def __str__(self):
        return str(self.name).lower()
