from BaseClasses import Item
import typing
from .Names import itemName
from .Names import locationName


class SSSV64Item(Item):
    #start at 1230380
    game: str = "SSSV64"
class ItemData(typing.NamedTuple):
    id: int = 0
    type: str = ""
    default_location: str = "",
    qty: int = 1

animals_table = {
    itemName.DOG:                       ItemData(1230381, "progress", None, 1),
    itemName.SHEEP:                     ItemData(1230382, "progress", None, 1),
    itemName.RAT:                       ItemData(1230383, "progress", None, 1),
    itemName.RACING_MOUSE:              ItemData(1230384, "progress", None, 1),
    itemName.SEAGULL:                   ItemData(1230385, "progress", None, 1),
    itemName.LION:                      ItemData(1230386, "progress", None, 1),
    itemName.HIPPO:                     ItemData(1230387, "progress", None, 1),
    itemName.RACING_DOG:                ItemData(1230388, "progress", None, 1),
    itemName.FLYING_DOG:                ItemData(1230389, "progress", None, 1),
    itemName.RABBIT:                    ItemData(1230390, "progress", None, 1),
    itemName.HELI_RABBIT:               ItemData(1230391, "progress", None, 1),
    itemName.RAT_KING:                  ItemData(1230392, "progress", None, 1),
    itemName.PARROT:                    ItemData(1230393, "progress", None, 1),
    itemName.BEAR:                      ItemData(1230394, "progress", None, 1),
    itemName.RACING_BEAR:               ItemData(1230395, "progress", None, 1),
    itemName.FOX:                       ItemData(1230396, "progress", None, 1),
    itemName.RACING_FOX:                ItemData(1230397, "progress", None, 1),
    itemName.TURTLE_TANK:               ItemData(1230398, "progress", None, 1),
    itemName.RACING_TURTLE:             ItemData(1230399, "progress", None, 1),
    itemName.PIRANHA:                   ItemData(1230400, "progress", None, 1),
    itemName.RAM:                       ItemData(1230401, "progress", None, 1),
    itemName.SPRING_SHEEP:              ItemData(1230402, "progress", None, 1),
    itemName.SPRING_RAM:                ItemData(1230403, "progress", None, 1),
    itemName.PENGUIN:                   ItemData(1230404, "progress", None, 1),
    itemName.POLAR_BEAR:                ItemData(1230405, "progress", None, 1),
    itemName.POLAR_TANK:                ItemData(1230406, "progress", None, 1),
    itemName.HUSKY:                     ItemData(1230407, "progress", None, 1),
    itemName.SKI_HUSKY:                 ItemData(1230408, "progress", None, 1),
    itemName.WALRUS:                    ItemData(1230409, "progress", None, 1),
    itemName.VULTURE:                   ItemData(1230410, "progress", None, 1),
    itemName.CAMEL:                     ItemData(1230411, "progress", None, 1),
    itemName.CANNON_CAMEL:              ItemData(1230412, "progress", None, 1),
    itemName.POGO_KANGAROO:             ItemData(1230413, "progress", None, 1),
    itemName.BOXING_KANGAROO:           ItemData(1230414, "progress", None, 1),
    itemName.DESERT_FOX:                ItemData(1230415, "progress", None, 1),
    itemName.ARMED_DESERT_FOX:          ItemData(1230416, "progress", None, 1),
    itemName.SCORPION:                  ItemData(1230417, "progress", None, 1),
    itemName.GORILLA:                   ItemData(1230418, "progress", None, 1),
    itemName.ELEPHANT:                  ItemData(1230419, "progress", None, 1),
    itemName.HYENA:                     ItemData(1230420, "progress", None, 1),
    itemName.CHAMELEON:                 ItemData(1230421, "progress", None, 1),
    itemName.PENGUIN_KING:              ItemData(1230422, "progress", None, 1),
    itemName.COOL_COD:                  ItemData(1230423, "progress", None, 1),
}

levels_table = {
    itemName.SMASHING_START:            ItemData(1230440, "progress", locationName.MENU_STARTING_LEVEL, 1),
    itemName.HAVE_A_NICE_DAY:           ItemData(1230441, "progress", None, 1),
    itemName.HONEYMOON_LAGOON:          ItemData(1230442, "progress", None, 1),
    itemName.THE_BATTERY_FARM:          ItemData(1230443, "progress", None, 1),
    itemName.THE_ENGINE_ROOM:           ItemData(1230444, "progress", None, 1),
    itemName.FAT_BEAR_MOUNTAIN:         ItemData(1230445, "progress", None, 1),
    itemName.ROCKY_HARD_PLACE:          ItemData(1230446, "progress", None, 1),
    itemName.STINKY_SEWER:              ItemData(1230447, "progress", None, 1),
    itemName.RAT_O_MATIC:               ItemData(1230448, "progress", None, 1),
    itemName.GIVE_A_DOG_A_BONUS:        ItemData(1230449, "progress", None, 1),
    itemName.SNOW_JOKE:                 ItemData(1230450, "progress", None, 1),
    itemName.ICE_N_EASY_DOES_IT:        ItemData(1230451, "progress", None, 1),
    itemName.PENGUIN_PLAYPEN:           ItemData(1230452, "progress", None, 1),
    itemName.PINBALL_BLIZZARD:          ItemData(1230453, "progress", None, 1),
    itemName.HOPPA_CHOPPA:              ItemData(1230454, "progress", None, 1),
    itemName.SOMETHING_FISHY:           ItemData(1230455, "progress", None, 1),
    itemName.WALRACE_64:                ItemData(1230456, "progress", None, 1),
    itemName.JUNGLE_JAPES:              ItemData(1230457, "progress", None, 1),
    itemName.JUNGLE_DOLDRUMS:           ItemData(1230458, "progress", None, 1),
    itemName.SWAMP_OF_ETERNAL_STENCH:   ItemData(1230459, "progress", None, 1),
    itemName.WEIGHT_FOR_IT:             ItemData(1230460, "progress", None, 1),
    itemName.JUNGLE_JUMPS:              ItemData(1230461, "progress", None, 1),
    itemName.EVO_ESCAPE:                ItemData(1230462, "progress", None, 1),
    itemName.FUN_IN_THE_SUN:            ItemData(1230463, "progress", None, 1),
    itemName.HOT_CROSS_BUNS:            ItemData(1230464, "progress", None, 1),
    itemName.STING_IN_THE_TAIL:         ItemData(1230465, "progress", None, 1),
    itemName.BORASSIC_PARK:             ItemData(1230466, "progress", None, 1),
    itemName.WHIRLWIND_TOUR:            ItemData(1230467, "progress", None, 1),
    itemName.SHIFTING_SANDS:            ItemData(1230468, "progress", None, 1),
    itemName.PUNCH_UP_PYRAMID:          ItemData(1230469, "progress", None, 1),
    itemName.BIG_CELEBRATION_PARADE:    ItemData(1230470, "progress", None, 1),
}

groups_table = {
    itemName.EUROPE:                    ItemData(1230480, "progress", None, 1),
    itemName.ARCTIC:                    ItemData(1230481, "progress", None, 1),
    itemName.JUNGLE:                    ItemData(1230482, "progress", None, 1),
    itemName.DESERT:                    ItemData(1230483, "progress", None, 1),
}

collectables_table = {
    itemName.POWER_CELL:                ItemData(1230490, "useful", None, 390),
    itemName.TROPHY:                    ItemData(1230491, "useful", None, 26),
}


all_item_table = {
    **animals_table,
    **levels_table,
    **groups_table,
    **collectables_table
}

all_group_table = {
    "animals": animals_table,
    "levels": level_table,
    "collectables": collectables_table
}