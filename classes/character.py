



# characters will have dimensions: name, stats, background, 
# need some classes to do things with the character 
# instantion of characters will be unique by the id and can be tracked by their id itself 

class Stats:
    stats_id = 0

    def __init__(self, stat_hp, stat_str, stat_mag, stat_dex, stat_spd, stat_lck, stat_def, stat_res):
        stats_id += 1
        self.stats_id = stats_id
        self.stat_hp = stat_hp
        self.stat_str = stat_str
        self.stat_mag = stat_mag
        self.stat_dex = stat_dex
        self.stat_spd = stat_spd
        self.stat_lck = stat_lck
        self.stat_def = stat_def
        self.stat_res = stat_res

    # do we add methods to increase a specific stat? 

class Character:
    character_id = 0
    def __init__(self, name, stats, background):
        character_id += 1
        self.character_id = character_id 
        self.name = name
        self.stats
        self.background = background


## bind the char with board properties to have board stats 
