
"""
The goal of this file is to ship the configuration for the pop up killer
into another file to minimize the size of __init__.py. Scrolling is a pain.
"""

def screen_cords(base_clist_value):
    standard_sleep_after = 0.0
    return [
    {
        "cords_dict": {"x": 1010, "y": 290, "w": 360, "h": 450},
        "hashes": [],
        "msg": "enemy_bombardment",
        "text_color": [(192,151,112), (239,239,239)],
        "search_text": [
            "Troop Transport",
            "Currently Enroute"
        ],
        "keys_press": [],
        "mv_to_click": [1100, 790],
        "mv_to_click_after_press": [],
        "sleap_after": standard_sleep_after
    },
    {
        "cords_dict": {"x": 1010, "y": 290, "w": 360, "h": 450},
        "hashes": [],
        "msg": "enemy_bombardment2",
        "text_color": [(192,151,112), (239,239,239)],
        "search_text": ["omb the Enemy Planet"],
        "keys_press": [],
        "mv_to_click": [1300, 790],
        "mv_to_click_after_press": ['esc'],
        "sleap_after": standard_sleep_after
    },
    { 
        "cords_dict": {"x": 1050, "y": 530, "w": 330, "h": 210},
        "hashes": [],
        "msg": "spies",
        "text_color": [(228,49,30)],
        "search_text": [
            "Spey destroyed",
            "spies destroyed",
            "Spies destroyed"
            ],
        "keys_press": ["esc"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": standard_sleep_after
    },
    { 
        "cords_dict": {"x": 600, "y": 890, "w": 300, "h": 35},
        "hashes": ['00ff0c7444560640','ffffc0e0c0c0c0c0','ffff086140400000','ffef854345c7c4c7',
            'ffdf070707070707','fff8b87878f8d8f8','40ff0d7341570440'],
        "msg": "space_battle",
        "text_color": [(228,49,30)],
        "search_text": [],
        "keys_press": ["a"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": standard_sleep_after
    },
    { 
        "cords_dict": {"x": 20, "y": 20, "w": 1400, "h": 200},
        "hashes": [],
        "msg": "groud_combat",
        "text_color": [(156,159,190),(181,183,206),(227,227,227)],
        "search_text": [
            "Successfully",
            "Successtully Defend",
            "Ground Combat",
            "Gapture",
            "factories captured",
            "Ground Gombat",
            "transports penetrate"
            ],
        "keys_press": ["esc", "esc"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": standard_sleep_after
    },
    { 
        "cords_dict": {"x": 270, "y": 240, "w": 500, "h": 50},
        "hashes": ["0000507e7e7e7e00"],
        "msg": "fleet_production",
        "text_color": [],
        "search_text": [],
        "keys_press": ["esc"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": standard_sleep_after
    },
    { 
        "cords_dict": {"x": 220, "y": 270, "w": 600, "h": 350},
        "hashes": [],
        "msg": "planetary_shield",
        "text_color": [(195,195,195)],
        "search_text": ["lanetary Shield"],
        "keys_press": [],
        "mv_to_click": base_clist_value,
        "mv_to_click_after_press": ["esc"],
        "sleap_after": standard_sleep_after + 0.2
    },
    {
        "cords_dict": {"x": 850, "y": 400, "w": 300, "h": 100},
        "hashes": ["ffff77ee88ee0000"],
        "msg": "select_ratio",
        "text_color": [],
        "search_text": [],
        "keys_press": [],
        "mv_to_click": [920, 460],
        "mv_to_click_after_press": [],
        "sleap_after": standard_sleep_after + 0.2
    },
    { 
        "cords_dict": {"x": 1020, "y": 300, "w": 380, "h": 400},
        "hashes": ["00503e7e7e7e0000"],
        "msg": "space_combat",
        "text_color": [(239,239,239)],
        "search_text": ["Space Combat"],
        "keys_press": ["c"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": standard_sleep_after
    },
    { 
        "cords_dict": {"x": 220, "y": 270, "w": 600, "h": 350},
        "hashes": [],
        "msg": "middle_notice",
        "text_color": [(195,195,195)],
        "search_text": [
            "be chonged at this time.",
            "transports attempting To land on",
            "transports attemptina to land on",
            "transports attempting to land on",
            "were all destroyed",
            "Without supplies and shelter. all have perished."
            ],
        "keys_press": ["esc"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": standard_sleep_after
    },
    { 
        "cords_dict": {"x": 155, "y": 640, "w": 1100, "h": 270},
        "hashes": [],
        "msg": "deplimate_talks",
        "text_color": [(0,0,0), (132,12,0)],
        "search_text": [
            "bring you an offer of peace",
            "Both our races have suffered greatly",
            "We can mo longer sustain this horrible war",
            "This war between us is senseless, Let us",
            "end to it with & peace treaty. * Accept ® Reject",
            "Can we agree to trading",
            "senseless wear. * Accept ® Reject"
            ],
        "keys_press": ["up","return"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": standard_sleep_after
    },
    { 
        "cords_dict": {"x": 155, "y": 640, "w": 1100, "h": 270},
        "hashes": [],
        "msg": "deplimate_talks_2",
        "text_color": [(0,0,0), (132,12,0)],
        "search_text": [
            "that we share common territory",
            "Your attacks against the insidious",
            "We shall make an example",
            "bears greetings from the most",
            "bear greetings from the most wise",
            "It would seem that our empires",
            "Hail glorious Emperor",
            "Greetings from",
            "Our patience is exhausted. Continue to expand and it will be war.",
            "You have spread like a plague throughout the galaxy. Cease your reckless expansion or we will be forced to eliminate your threat once and for all.",
            "star system an unprovoked act of war.",
            "Let us work for a mutually beneficial relationship.",
            "empire is tired of playing diplomatic games.",
            "We have known all along that the",
            "empire wishes mo contact with the filthy",
            "and hopes that you will prosper under our rule",
            "star system will soon place our empires",
            "you will soon pay",
            "clase ta the brink of war. (you were framed",
            "Warnings were mot enough. Mow you will Peel the might of the",
            "you have answered our requests for peace with unprovoked acts of war. So be it. We will crush the",
            "our actions can mo longer be tolerated, Prepare to perish beneath the wake of the",
            "Cambassador recalled?",
            "You cannot escape the wrath of the",
            "you to must mow realize the incredible threat",
            "Together we will smite the infidel dogs",
            "forced to annihilate the entire Sakkra race",
            "empire has been reluctant to enter an intergalactic war, your insufferable acts of terrorism can mo longer be permitted. (ambassador recalled?"
            "can mo longer be permitted."
            "(ambassador recalled",
            "Cambassadar recalled",
            "Together our empires can challenge the threat of the evil",
            "share a common enemy",
            "lf necessary we will save the universe from the",
            "the magnificent, lustricus and godlike",
            "you will be destroyed on sight",
            "Contact hat been broken with the"
            ],
        "keys_press": ["esc"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": standard_sleep_after
    },
    {
        "cords_dict": {"x": 850, "y": 400, "w": 300, "h": 100},
        "hashes": ["ffff77ee88ee0000"],
        "msg": "tech_select_ratio",
        "text_color": [],
        "search_text": [],
        "keys_press": [],
        "mv_to_click": [920, 460],
        "mv_to_click_after_press": [],
        "sleap_after": standard_sleep_after + .1
    },
    {
        "cords_dict": {"x": 680, "y": 180, "w": 600, "h": 300},
        "hashes": ['840040400080ffff'],
        "msg": "tech_reduce_usage",
        "text_color": [],
        "search_text": [],
        "keys_press": [],
        "mv_to_click": [1140, 466],
        "mv_to_click_after_press": [],
        "sleap_after": standard_sleep_after + .1
    },
    {
        "cords_dict": {"x": 1250, "y": 250, "w": 150, "h": 200},
        "hashes": ["090d0d0d091df9f1","0101010d0d0d8dd9"],
        "msg": "tech_inital",
        "text_color": [],
        "search_text": [],
        "keys_press": ["esc"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": standard_sleep_after + .5
    },
    {
        "cords_dict": {"x": 700, "y": 180, "w": 700, "h": 60},
        "hashes": [],
        "msg": "tech_select",
        "text_color": [(65,183,33)],
        "search_text": ["Technology"],
        "keys_press": ["esc"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": standard_sleep_after + .1
    },
    {
        "cords_dict": {"x": 1030, "y": 280, "w": 360, "h": 100},
        "hashes": [],
        "msg": "orbital_bombardment",
        "text_color": [(192,151,112), (239,239,239)],
        "search_text": ["Bombardment"],
        "keys_press": ["c", "esc"],
        "mv_to_click": [],
        "sleap_after": standard_sleep_after
    },
    {
        "cords_dict": {"x": 250, "y": 600, "w": 500, "h": 50},
        "hashes": ["fff8f0080809099e"],
        "msg": "news",
        "text_color": [],
        "search_text": [],
        "keys_press": ["esc"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": standard_sleep_after
    },
    {
        "cords_dict": {"x": 100, "y": 250, "w": 700, "h": 50},
        "hashes": ["41c3c3c0c3c3c3c3"],
        "msg": "voting",
        "text_color": [],
        "search_text": [],
        "keys_press": ["esc", "esc"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": standard_sleep_after
    },
    {
        "cords_dict": {"x": 1040, "y": 290, "w": 320, "h": 90},
        "hashes": ['060f2feffc103030','203c3c2009ff7e02','a03c3c0049ff7e02',
            'a03c3c240fdf7e00','203c3c2009fffe02','f8fc3c01dfff1a00','203c3c0009df7e02',
            '283c3c2009ff7e02', '203c3c3019ff7e02','203c3c3001ff7e12','283c3c2009df7e02',
            '203c3c2009df7e02', '203c3c3009ff7e02'],
        "msg": "new_colony",
        "text_color": [],
        "search_text": [],
        "keys_press": ["Y", "", "", "esc", "esc"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": standard_sleep_after
    },
    { 
        "cords_dict": {"x": 650, "y": 100, "w": 150, "h": 150},
        "hashes": ["ffcf0120ff8080ff"],
        "msg": "name_da_ship",
        "text_color": [],
        "search_text": [],
        "keys_press": ["esc"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": standard_sleep_after
    }
]
