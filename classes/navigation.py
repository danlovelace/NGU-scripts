"""Navigation class handles navigation through the menus."""
import time
from classes.inputs import Inputs
import coordinates as coords
import usersettings as userset


class Navigation:
    """Navigate through menus."""

    menus = coords.MENU_ITEMS
    # equipment = coords.EQUIPMENT_SLOTS # deprecated?
    current_menu = ''
    
    @staticmethod
    def menu(target):
        """Navigate through main menu."""
        target = target.lower()
        if Navigation.current_menu == target:
            return
        Inputs.click(*Navigation.menus[target])
        time.sleep(userset.LONG_SLEEP)
        Navigation.current_menu = target
    
    @staticmethod
    def input_box():
        """Click input box."""
        Inputs.click(*coords.NUMBER_INPUT_BOX)
        time.sleep(userset.SHORT_SLEEP)
    
    @staticmethod
    def rebirth():
        """Click rebirth menu."""
        if Navigation.current_menu == 'rebirth':
            return
        Inputs.click(*coords.REBIRTH)
        time.sleep(userset.SHORT_SLEEP)
        Navigation.current_menu = 'rebirth'
    
    @staticmethod
    def confirm():
        """Click yes in confirm window."""
        Inputs.click(*coords.CONFIRM)
        time.sleep(userset.SHORT_SLEEP)
    
    @staticmethod
    def ngu_magic():
        """Navigate to NGU magic."""
        if Navigation.current_menu == 'ngu_magic':
            return
        Navigation.menu('ngu')
        Inputs.click(*coords.NGU_MAGIC)
        time.sleep(userset.SHORT_SLEEP)
        Navigation.current_menu = 'ngu_magic'
    
    @staticmethod
    def exp():
        """Navigate to EXP Menu."""
        if Navigation.current_menu == 'exp':
            return
        Inputs.click(*coords.XP_MENU)
        time.sleep(userset.SHORT_SLEEP)
        Navigation.current_menu = 'exp'
    
    @staticmethod
    def exp_magic():
        """Navigate to the magic menu within the EXP menu."""
        if Navigation.current_menu == 'exp_magic':
            return
        Navigation.exp()
        Inputs.click(*coords.MAGIC_MENU)
        time.sleep(userset.SHORT_SLEEP)
        Navigation.current_menu = 'exp_magic'
    
    @staticmethod
    def exp_adventure():
        """Navigate to the adventure menu within the EXP menu."""
        if Navigation.current_menu == "exp_adventure":
            return
        Navigation.exp()
        Inputs.click(*coords.ADVENTURE_MENU)
        time.sleep(userset.SHORT_SLEEP)
        Navigation.current_menu = "exp_adventure"
    
    @staticmethod
    def exp_rich():
        """Navigate to the misc menu within the EXP menu."""
        if Navigation.current_menu == "exp_rich":
            return
        Navigation.exp()
        Inputs.click(*coords.RICH_MENU)
        time.sleep(userset.SHORT_SLEEP)
        Navigation.current_menu = "exp_rich"
    
    @staticmethod
    def exp_hack():
        """Navigate to the hacks menu within the EXP menu."""
        if Navigation.current_menu == "exp_hack":
            return
        Navigation.exp()
        Inputs.click(*coords.EXP_HACK_MENU)
        time.sleep(userset.SHORT_SLEEP)
        Navigation.current_menu = "exp_hack"
    
    @staticmethod
    def info():
        """Click info 'n stuff."""
        if Navigation.current_menu == 'info':
            return
        Inputs.click(*coords.INFO)
        time.sleep(userset.SHORT_SLEEP)
        Navigation.current_menu = 'info'
    
    @staticmethod
    def misc():
        """Navigate to Misc stats."""
        if Navigation.current_menu == 'misc':
            return
        Navigation.info()
        Inputs.click(*coords.MISC)
        time.sleep(userset.SHORT_SLEEP)
        Navigation.current_menu = 'misc'
    
    @staticmethod
    def perks():
        """Navigate to Perks screen."""
        if Navigation.current_menu == 'perks':
            return
        Navigation.menu('adventure')
        Inputs.click(*coords.ITOPOD_PERKS)
        time.sleep(userset.SHORT_SLEEP)
        Navigation.current_menu = 'perks'
    
    @staticmethod
    def spells():
        """Navigate to the spells menu within the magic menu."""
        if Navigation.current_menu == 'spells':
            return
        Navigation.menu('bloodmagic')
        Inputs.click(*coords.BM_SPELL)
        time.sleep(userset.SHORT_SLEEP)
        Navigation.current_menu = 'spells'
    
    @staticmethod
    def sellout():
        """Navigate to sellout shop."""
        if Navigation.current_menu == 'sellout':
            return
        Inputs.click(*coords.SELLOUT)
        time.sleep(userset.SHORT_SLEEP)
        Navigation.current_menu = "sellout"
    
    @staticmethod
    def sellout_boost_2():
        """Navigate to Boost 2 menu within the sellout shop."""
        if Navigation.current_menu == 'boost_2':
            return
        Navigation.sellout()
        Inputs.click(*coords.SELLOUT_BOOST_2)
        time.sleep(userset.SHORT_SLEEP)
        Navigation.current_menu = "boost_2"
    
    @staticmethod
    def stat_breakdown():
        """Navigate to stat breakdown."""
        if Navigation.current_menu == 'stat_breakdown':
            return
        Navigation.misc()
        Inputs.click(*coords.STAT_BREAKDOWN)
        time.sleep(userset.SHORT_SLEEP)
        Navigation.current_menu = 'stat_breakdown'
