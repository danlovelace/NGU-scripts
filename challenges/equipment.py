"""Contains functions for running a basic challenge."""
from classes.features import Rebirth, Wandoos, BloodMagic, MoneyPit
from classes.features import GoldDiggers, Augmentation, FightBoss, Adventure
from classes.inputs   import Inputs

import coordinates as coords
import time

class Equipment:
    """Contains functions for running a basic challenge."""

    @staticmethod
    def speedrun(duration):
        """Start a speedrun.

        Keyword arguments
        duration -- duration in minutes to run
        f -- feature object
        """
        diggers = [2, 3, 11, 12]
        FightBoss.nuke()
        time.sleep(2)

        FightBoss.fight()
        Adventure.adventure(highest=True)
        time.sleep(2)

        rb_time = Rebirth.get_rebirth_time()
        while int(rb_time.timestamp.tm_min) < duration:
            GoldDiggers.gold_diggers(diggers)
            Wandoos.wandoos(True)
            Augmentation.augments({"SM": 1}, coords.INPUT_MAX)
            if not Inputs.check_pixel_color(*coords.COLOR_TM_LOCKED):
                BloodMagic.blood_magic(6)
            FightBoss.nuke()
            rb_time = Rebirth.get_rebirth_time()
        MoneyPit.pit()
        MoneyPit.spin()
        return

    @staticmethod
    def start():
        """Challenge rebirth sequence.

        If you wish to edit the length or sequence of the rebirths; change the for-loop values
        and durations in the Equipment.speedrun(duration) calls."""
        Wandoos.set_wandoos(0)  # wandoos 98, use 1 for meh

        for x in range(8):
            Equipment.speedrun(3)
            if not Rebirth.check_challenge():
                return
            Rebirth.do_rebirth()
        for x in range(5):
            Equipment.speedrun(7)
            if not Rebirth.check_challenge():
                return
            Rebirth.do_rebirth()
        for x in range(5):
            Equipment.speedrun(12)
            if not Rebirth.check_challenge():
                return
            Rebirth.do_rebirth()
        for x in range(5):
            Equipment.speedrun(60)
            if not Rebirth.check_challenge():
                return
            Rebirth.do_rebirth()
        return
