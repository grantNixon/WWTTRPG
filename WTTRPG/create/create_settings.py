
class Races():
    races = ["Valley Human", "Forest Human", " Seven-Banded Armadill", "Five-Banded Armadill", "Village Hillock", "Stone Hillock", "Short-tailed Folinn", "Long-tailed Folinn", "Smooth Shikasa", "Rigid Shikasa", "Onyx Bak'wa", "Mossy Bak'wa","Roaming Egriss", "Lotus Grove Egriss","Solid Bolibar", "Speckled Bolibar","Triadic Cincindel", "Analogous Cincindel","Anointed Ambaazi", "Lost Ambaazi", "Desert Latran", "Mesa Latran", "Long-Haired Margart", "Short-Haired Margart"]

class Backgrounds():
    backgrounds = ["Cowboy", "Rancher", "Bounty Hunter", "Snake Oil Salesman", "Doctor", "Elemental Fella", "Wilderness Guide", "Worshipper", "Missionary", "Chef",
                   "Alchemist", "Ex-convict","Galvanism Scholar","Assassin", "Carpenter", "Shopkeep", "Luddite", "Street Urchin"]
    
class PointBuy():
    pointbuys = [30,20,16,15,10,5]

class Skills():
    skillz = ["Shotguns","Crushing Melee", "Hand-to-Hand","Athletics","Crafting","Pistols","Slashing Melee", "Archery","Ropework",
              "Acrobatics","Sneak","Thievery","Intimidation","Hunting","Cooking","Foraging","Animal Handling","Rifles","Intuition",
              "Investigation","Gambit","Brewing","Galvanism Magic","Religion","Medicine","History","Healing Magic","Utility Magic","Absolution Magic",
              "Foolery","Persuasion","Barter","Performance","Deception Magic","Ritual Magic","Destruction Magic"]
    
class WeaponProfs():
    weaponprof = {"Crushing Melee","Slashing Melee","Pistols","Rifles","Shotguns","Ropework","Archery","Hand-to-Hand"}

class Skills_to_ModelName():
    skilldic = {"Shotguns":"sk_shotguns","Crushing Melee":"sk_crushing", "Hand-to-Hand":"sk_hand","Athletics":"sk_athletics","Crafting":"sk_crafting","Pistols":"sk_pistols",
              "Slashing Melee":"sk_slashing", "Archery":"sk_archery","Ropework":"sk_ropework",
              "Acrobatics":" sk_acrobatics","Sneak":"sk_sneak","Thievery":"sk_thievery","Intimidation":"sk_intimidation","Hunting":"sk_hunting","Cooking":"sk_cooking",
              "Foraging":"sk_foraging","Animal Handling":"sk_animalhandling","Rifles":"sk_rifles","Intuition":"sk_intuition",
              "Investigation":"sk_investigation","Gambit":"sk_gambit","Brewing":"sk_brewing","Galvanism Magic":" sk_galvanismmagic","Religion":"sk_religion","Medicine":"sk_medicine",
              "History":"sk_history","Healing Magic":"sk_healingmagic","Utility Magic":"sk_utilitymagic","Absolution Magic":"sk_absolutionmagic",
              "Foolery":" sk_foolery","Persuasion":"sk_persuasion","Barter":"sk_barter","Performance":"sk_performance","Deception Magic":"sk_deceptionmagic","Ritual Magic":"sk_ritualmagic","Destruction Magic":"sk_destructionmagic"}

class BackgroundBonuses():
    bonuses = {
        "Cowboy": {
            "sk_pistols": 5,
            "sk_rifles": 5,
            "sk_ropework": 5,
            "sk_history": -5,
            "sk_foolery": -5,
            "sk_sneak": -5,
        },
        "Rancher": {
            "sk_animalhandling": 5,
            "sk_crafting": 5,
            "sk_ropework": 5,
            "sk_deceptionmagic": -5,
            "sk_healingmagic": -5,
            "sk_utilitymagic": -5,
            "sk_absolutionmagic": -5,
            "sk_galvanismmagic": -5,
            "sk_ritualmagic": -5,
            "sk_destructionmagic": -5,
        },
        "Bounty Hunter": {
            "sk_intuition": 5,
            "sk_investigation": 5,
            "sk_religion": -5,
            "sk_healingmagic": -5,
            "sk_performance": -5,
        },
        "Alchemist": {
            "sk_brewing": 10,
            "sk_foraging": 10,
            "sk_foolery": -5,
            "sk_intimidation": -5,
            "sk_crafting": -5,
        },
        "Assassin": {
            "sk_sneak": 5,
            "sk_acrobatics": 5,
            "sk_pistols": 5,
            "sk_repair": -5,
            "sk_crafting": -5,
            "sk_shotguns": -5,
        },
        "Chef": {
            "sk_cooking": 10,
            "sk_slashing": 5,
            "sk_crushing": 5,
            "sk_archery": -5,
            "sk_rifles": -5,
            "sk_pistols": -5,
        },
        "Doctor": {
            "sk_medicine": 10,
            "sk_slashing": 5,
            "sk_archery": -5,
            "sk_rifles": -5,
            "sk_pistols": -5,
            "sk_shotguns": -5,
            "sk_crushing": -5,
            "sk_hand": -5,
        },
        "Ex-convict": {
            "sk_hand": 5,
            "sk_slashing": 10,
            "sk_religion": 5,
            "sk_foolery": -5,
            "sk_foraging": -5,
            "sk_persuasion": -5,
        },
        'Elemental Fella': {
        },
        "Galvanism Scholar": {
            "sk_galvanismmagic": 15,
            "sk_deceptionmagic": -5,
            "sk_healingmagic": -5,
            "sk_utilitymagic": -5,
            "sk_absolutionmagic": -5,
            "sk_ritualmagic": -5,
            "sk_destructionmagic": -5,
        },
        "Carpenter": {
            "sk_crafting": 15,
            "sk_deceptionmagic": -5,
            "sk_healingmagic": -5,
            "sk_utilitymagic": -5,
            "sk_absolutionmagic": -5,
            "sk_ritualmagic": -5,
            "sk_destructionmagic": -5,
            "sk_galvanismmagic": -5,
        },
        "Snake Oil Salesman": {
            "sk_foolery": 5,
            "sk_persuasion": 5,
            "sk_barter": 5,
            "sk_pistols": -5,
            "sk_rifles": -5,
            "sk_archery": -5,
        },
        'Wilderness Guide': {
        },
        "Worshipper": {
            "sk_ritualmagic": 5,
            "sk_destructionmagic": 5,
            "sk_deceptionmagic": 5,
            "sk_persuasion": 5,
            "mysticism": -5,
        },
        "Shopkeep": {
            "sk_barter": 10,
            "sk_crafting": 10,
            "sk_shotguns": 5,
            "sk_cooking": -5,
            "sk_hunting": -5,
            "sk_animal": -5,
        },
        "Missionary": {
            "sk_healingmagic": 5,
            "sk_utilitymagic": 5,
            "sk_absolutionmagic": 5,
            "sk_ritualmagic": -5,
            "sk_destructionmagic": -5,
            "sk_deceptionmagic": -5,
        },
        "Luddite": {
            "sk_crushing": 5,
            "sk_slashing": 5,
            "sk_hand": 5,
            "sk_ropework": 5,
            "sk_archery": 5,
            "sk_rifles": -5,
            "sk_pistols": -5,
            "sk_shotguns": -5,
        },
        "Street Urchin": {
            "sk_thievery": 5,
            "sk_sneak": 5,
            "sk_foolery": 5,
            "sk_healingmagic": -5,
            "sk_utilitymagic": -5,
            "sk_absolutionmagic": -5,
            "sk_ritualmagic": -5,
            "sk_destructionmagic": -5,
            "sk_galvanismmagic": -5,
            "sk_history": -5
        },
    };

