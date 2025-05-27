from typing import NamedTuple, Union
import logging

from BaseClasses import Item, Tutorial, ItemClassification

from ..AutoWorld import World, WebWorld
from NetUtils import SlotType


class SSSVWeb(WebWorld):
    theme = "party"
    setup = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up SSSV for Archipelago on your computer.",
        "English",
        "multiworld_en.md",
        "multiworld/en",
        ["Xandervile"]
    )

    tutorials = [setup]


class SSSVWorld(World):
    game = "Archipelago"
    topology_present = False
    item_name_to_id = {
        "Nothing": -1
    }
    location_name_to_id = {
        "Cheat Console": -1,
        "Server": -2
    }
    hidden = True
    web = GenericWeb()

    def generate_early(self):
        self.multiworld.player_types[self.player] = SlotType.spectator  # mark as spectator

    def create_item(self, name: str) -> Item:
        if name == "Nothing":
            return Item(name, ItemClassification.filler, -1, self.player)
        raise KeyError(name)


class PlandoItem(NamedTuple):
    item: str
    location: str
    world: Union[bool, str] = False  # False -> own world, True -> not own world
    from_pool: bool = True  # if item should be removed from item pool
    force: str = 'silent'  # false -> warns if item not successfully placed. true -> errors out on failure to place item.

    def warn(self, warning: str):
        if self.force in ['true', 'fail', 'failure', 'none', 'false', 'warn', 'warning']:
            logging.warning(f'{warning}')
        else:
            logging.debug(f'{warning}')

    def failed(self, warning: str, exception=Exception):
        if self.force in ['true', 'fail', 'failure']:
            raise exception(warning)
        else:
            self.warn(warning)
