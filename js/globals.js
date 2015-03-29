	var VERSION = "v1.0";
	var char_data = "";
//	var panel_list = [ "statistics", "skills", "maneuvers", "magic", "combat", "summary" ];
	var panel_list = [ "statistics", "skills", "maneuvers" ];
	var scroller_H = 0;
	var scroller_V = 0;
	
		
	function Object_List() {
		this.list = [];
		
		this.GetObjectByName = function( name ) {
			for( var i=0; i < this.list.length; i++ ) {
				if( this.list[i].name == name ) {
					return this.list[i];
				}
			}
		}		
		
		this.AddObject = function( obj ) {
			this.list[this.list.length] = obj;
		}
	}
	
	
	
	
	
	
	


	var statistics = [ "strength", "constitution", "dexterity", "agility", "discipline", "aura", "logic", "intuition", "wisdom", "influence" ];
   
	var strength_by_level = [];
	var constitution_by_level = [];
	var dexterity_by_level = [];
	var agility_by_level = [];
	var discipline_by_level = [];
	var aura_by_level = [];
	var logic_by_level = [];
	var intuition_by_level = [];
	var wisdom_by_level = [];
	var influence_by_level = [];
	var statistics_by_level = { "strength": strength_by_level, "constitution": constitution_by_level, "dexterity": dexterity_by_level, "agility": agility_by_level, "discipline": discipline_by_level, "aura": aura_by_level, "logic": logic_by_level, "intuition": intuition_by_level, "wisdom": wisdom_by_level, "influence": influence_by_level };

	var strength_bonus_by_level = [];
	var constitution_bonus_by_level = [];
	var dexterity_bonus_by_level = [];
	var agility_bonus_by_level = [];
	var discipline_bonus_by_level = [];
	var aura_bonus_by_level = [];
	var logic_bonus_by_level = [];
	var intuition_bonus_by_level = [];
	var wisdom_bonus_by_level = [];
	var influence_bonus_by_level = [];
	var statistic_bonuses_by_level = { "strength": strength_bonus_by_level, "constitution": constitution_bonus_by_level, "dexterity": dexterity_bonus_by_level, "agility": agility_bonus_by_level, "discipline": discipline_bonus_by_level, "aura": aura_bonus_by_level, "logic": logic_bonus_by_level, "intuition": intuition_bonus_by_level, "wisdom": wisdom_bonus_by_level, "influence": influence_bonus_by_level };	
	
	var stat_total_by_level = [];
	var PTP_by_level = [];
	var MTP_by_level = [];
	var health_by_level = [];
	var mana_by_level = [];
	var stamina_by_level = [];
	var spirit_by_level = [];
	
	var selected_prof = "warrior";
	var selected_race = "human";	
	var StP_show_mode = "growth";
	
	strength_by_level[0] = 30;
	constitution_by_level[0] = 30;
	dexterity_by_level[0] = 20;
	agility_by_level[0] = 20;
	discipline_by_level[0] = 20;
	aura_by_level[0] = 20;
	logic_by_level[0] = 20;
	intuition_by_level[0] = 20;
	wisdom_by_level[0] = 20;
	influence_by_level[0] = 20;
	
	
	
	var profession_list = new Object_List();
	var race_list = new Object_List();
	
	function Race( name, health, bonus, adj) {
		this.name = name;
		this.max_health = health;
		this.statistic_bonus = bonus;
		this.growth_adj = adj;
	}	
	
	function Profession( name, type, prime, mana, spell, growth) {
		this.name = name;
		this.type = type;
		this.prime_statistics = prime;
		this.mana_statistics = mana;
		this.spell_circles = spell;
		this.statistic_growth = growth;
	}	
	
	
	
	
	race_list.AddObject(new Race("aelotoi", 120,
		{ "strength": -5, "constitution": 0, "dexterity": 5, "agility": 10, "discipline": 5, "aura": 0, "logic": 5, "intuition": 5, "wisdom": 0, "influence": 0 },
		{ "strength": 0, "constitution": -2, "dexterity": 3, "agility": 3, "discipline": 2, "aura": 0, "logic": 0, "intuition": 2, "wisdom": 0, "influence": 3 }		
	));
	race_list.AddObject(new Race("burghal gnome", 90, 
		{ "strength": -15, "constitution": 10, "dexterity": 10, "agility": 10, "discipline": -5, "aura": 5, "logic": 10, "intuition": 5, "wisdom": 0, "influence": -5 },
		{ "strength": -5, "constitution": 0, "dexterity": 3, "agility": 3, "discipline": -3, "aura": -2, "logic": 5, "intuition": 5, "wisdom": 0, "influence": 0 }		
	));	
	race_list.AddObject(new Race("dark elf", 120, 
		{ "strength": 0, "constitution": -5, "dexterity": 10, "agility": 5, "discipline": -10, "aura": 10, "logic": 0, "intuition": 5, "wisdom": 5, "influence": -5 },
		{ "strength": 0, "constitution": -2, "dexterity": 5, "agility": 5, "discipline": -2, "aura": 0, "logic": 0, "intuition": 0, "wisdom": 0, "influence": 0 }		
	));	
	race_list.AddObject(new Race("dwarf", 140, 
		{ "strength": 10, "constitution": 15, "dexterity": 0, "agility": -5, "discipline": 10, "aura": -10, "logic": 0, "intuition": 0, "wisdom": 0, "influence": -10 },
		{ "strength": 5, "constitution": 5, "dexterity": -3, "agility": -5, "discipline": 3, "aura": 0, "logic": 0, "intuition": 0, "wisdom": 3, "influence": -2 }		
	));	
	race_list.AddObject(new Race("elf", 130, 
		{ "strength": 0, "constitution": 0, "dexterity": 5, "agility": 15, "discipline": -15, "aura": 5, "logic": 0, "intuition": 0, "wisdom": 0, "influence": 10 },
		{ "strength": 0, "constitution": -5, "dexterity": 5, "agility": 3, "discipline": -5, "aura": 5, "logic": 0, "intuition": 0, "wisdom": 0, "influence": 3 }		
	));	
	race_list.AddObject(new Race("erithian", 120, 
		{ "strength": -5, "constitution": 10, "dexterity": 0, "agility": 0, "discipline": 5, "aura": 0, "logic": 5, "intuition": 0, "wisdom": 0, "influence": 10 },
		{ "strength": -2, "constitution": 0, "dexterity": 0, "agility": 0, "discipline": 3, "aura": 0, "logic": 2, "intuition": 0, "wisdom": 0, "influence": 3 }		
	));	
	race_list.AddObject(new Race("forest gnome", 100, 
		{ "strength": -10, "constitution": 10, "dexterity": 5, "agility": 10, "discipline": 5, "aura": 0, "logic": 5, "intuition": 0, "wisdom": 5, "influence": -5 },
		{ "strength": -3, "constitution": 2, "dexterity": 2, "agility": 3, "discipline": 2, "aura": 0, "logic": 0, "intuition": 0, "wisdom": 0, "influence": 0 }		
	));
	race_list.AddObject(new Race("giantman", 200, 
		{ "strength": 15, "constitution": 10, "dexterity": -5, "agility": -5, "discipline": 0, "aura": -5, "logic": 0, "intuition": 0, "wisdom": 0, "influence": 5 },
		{ "strength": 5, "constitution": 3, "dexterity": -2, "agility": -2, "discipline": 0, "aura": 0, "logic": 0, "intuition": 2, "wisdom": 0, "influence": 0 }		
	));	
	race_list.AddObject(new Race("half krolvin", 165, 
		{ "strength": 10, "constitution": 10, "dexterity": 0, "agility": 5, "discipline": 0, "aura": 0, "logic": -10, "intuition": 0, "wisdom": -5, "influence": -5 },
		{ "strength": 3, "constitution": 5, "dexterity": 2, "agility": 2, "discipline": 0, "aura": -2, "logic": -2, "intuition": 0, "wisdom": 0, "influence": -2 }		
	));	
	race_list.AddObject(new Race("half elf", 135, 
		{ "strength": 0, "constitution": 0, "dexterity": 5, "agility": 10, "discipline": -5, "aura": 0, "logic": 0, "intuition": 0, "wisdom": 0, "influence": 5 },
		{ "strength": 2, "constitution": 0, "dexterity": 2, "agility": 2, "discipline": -2, "aura": 0, "logic": 0, "intuition": 0, "wisdom": 0, "influence": 0 }		
	));	
	race_list.AddObject(new Race("halfling", 100, 
		{ "strength": -15, "constitution": 10, "dexterity": 15, "agility": 10, "discipline": -5, "aura": -5, "logic": 5, "intuition": 10, "wisdom": 0, "influence": -5 },
		{ "strength": -5, "constitution": 5, "dexterity": 5, "agility": 5, "discipline": -2, "aura": 0, "logic": -2, "intuition": 0, "wisdom": 0, "influence": 0 }		
	));	
	race_list.AddObject(new Race("human", 150, 
		{ "strength": 5, "constitution": 0, "dexterity": 0, "agility": 0, "discipline": 0, "aura": 0, "logic": 5, "intuition": 5, "wisdom": 0, "influence": 0 },
		{ "strength": 2, "constitution": 2, "dexterity": 0, "agility": 0, "discipline": 0, "aura": 0, "logic": 0, "intuition": 2, "wisdom": 0, "influence": 0 }		
	));		
	race_list.AddObject(new Race("sylvankind", 130, 
		{ "strength": 0, "constitution": 0, "dexterity": 10, "agility": 5, "discipline": -5, "aura": 5, "logic": 0, "intuition": 0, "wisdom": 0, "influence": 0 },
		{ "strength": -3, "constitution": -2, "dexterity": 5, "agility": 5, "discipline": -5, "aura": 3, "logic": 0, "intuition": 0, "wisdom": 0, "influence": 3 }		
	));		
	
	
	profession_list.AddObject(new Profession( "bard", "semi", [ "influence", "aura" ], [ "influence", "aura" ], [ "Minor Elemental", "Bard" ],
		{ "strength": 25, "constitution": 20, "dexterity": 25, "agility": 20, "discipline": 15, "aura": 25, "logic": 10, "intuition": 15, "wisdom": 20, "influence": 30 }	
	));
	profession_list.AddObject(new Profession( "cleric", "pure", [ "wisdom", "intuition" ], [ "wisdom", "wisdom" ], [ "Minor Spiritual", "Major Spiritual", "Cleric" ],
		{ "strength": 20, "constitution": 20, "dexterity": 10, "agility": 15, "discipline": 25, "aura": 15, "logic": 25, "intuition": 25, "wisdom": 30, "influence": 20 }	
	));
	profession_list.AddObject(new Profession( "empath", "pure", [ "wisdom", "influence" ], [ "wisdom", "influence" ], [ "Minor Spiritual", "Major Spiritual", "Empath" ],
		{ "strength": 10, "constitution": 20, "dexterity": 15, "agility": 15, "discipline": 25, "aura": 20, "logic": 25, "intuition": 20, "wisdom": 30, "influence": 25 }	
	));
	profession_list.AddObject(new Profession( "monk", "square", [ "agility", "strength" ], [ "wisdom", "logic" ], [ "Minor Spiritual", "Minor Mental" ],
		{ "strength": 25, "constitution": 25, "dexterity": 20, "agility": 30, "discipline": 25, "aura": 15, "logic": 20, "intuition": 20, "wisdom": 15, "influence": 10 }	
	));
	profession_list.AddObject(new Profession( "paladin", "semi", [ "wisdom", "strength" ], [ "wisdom", "wisdom" ], [ "Minor Spiritual", "Paladin" ],
		{ "strength": 30, "constitution": 25, "dexterity": 20, "agility": 20, "discipline": 25, "aura": 15, "logic": 10, "intuition": 15, "wisdom": 25, "influence": 20 }	
	));
	profession_list.AddObject(new Profession( "ranger", "semi", [ "dexterity", "intuition" ], [ "wisdom", "wisdom" ], [ "Minor Spiritual", "Ranger" ],
		{ "strength": 25, "constitution": 20, "dexterity": 30, "agility": 20, "discipline": 20, "aura": 15, "logic": 15, "intuition": 15, "wisdom": 25, "influence": 10 }	
	));
	profession_list.AddObject(new Profession( "rogue", "square", [ "dexterity", "agility" ], [ "aura", "wisdom" ], [ "Minor Elemental", "Minor Spiritual" ],
		{ "strength": 25, "constitution": 20, "dexterity": 25, "agility": 30, "discipline": 20, "aura": 15, "logic": 20, "intuition": 25, "wisdom": 10, "influence": 15 }	
	));
	profession_list.AddObject(new Profession( "sorcerer", "pure", [ "aura", "wisdom" ], [ "aura", "wisdom" ], [ "Minor Elemental", "Minor Spiritual", "Sorcerer" ],
		{ "strength": 10, "constitution": 15, "dexterity": 20, "agility": 15, "discipline": 25, "aura": 30, "logic": 25, "intuition": 20, "wisdom": 25, "influence": 20 }	
	));
	profession_list.AddObject(new Profession( "warrior", "square", [ "constitution", "strength" ], [ "aura", "wisdom" ], [ "Minor Elemental", "Minor Spiritual" ],
		{ "strength": 30, "constitution": 25, "dexterity": 25, "agility": 25, "discipline": 20, "aura": 15, "logic": 10, "intuition": 20, "wisdom": 15, "influence": 20 }	
	));
	profession_list.AddObject(new Profession( "wizard", "pure", [ "aura", "logic"], [ "aura", "aura"], [ "Minor Elemental", "Major Elemental", "Wizard" ],
		{ "strength": 30, "constitution": 25, "dexterity": 25, "agility": 25, "discipline": 20, "aura": 15, "logic": 10, "intuition": 20, "wisdom": 15, "influence": 20 }	
	));
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
 var bard_skill_costs = { "Two Weapon Combat": "3/2/2", "Armor Use": "5/0/2", "Shield Use": "5/0/2", "Combat Maneuvers": "8/4/2", "Edged Weapons": "3/1/2", "Blunt Weapons": "4/1/2", "Two-Handed Weapons": "7/2/2", "Ranged Weapons": "4/1/2", "Thrown Weapons": "3/1/2", "Polearm Weapons": "6/1/2", "Brawling": "3/1/2", "Ambush": "4/4/1", "Multi Opponent Combat": "7/3/1", "Physical Fitness": "4/0/2", "Dodging": "6/6/2", "Arcane Symbols": "0/4/2", "Magic Item Use": "0/4/2", "Spell Aiming": "3/10/1", "Harness Power": "0/5/1", "Elemental Mana Control": "0/6/1", "Mental Mana Control": "0/6/1", "Spirit Mana Control": "0/12/1", "Spell Research": "0/17/2", "Elemental Lore": "0/8/1", "Spiritual Lore": "0/20/1", "Sorcerous Lore": "0/18/1", "Mental Lore": "0/8/1", "Survival": "2/2/2", "Disarming Traps": "2/3/2", "Picking Locks": "2/1/2", "Stalking and Hiding": "3/2/2", "Perception": "0/3/2", "Climbing": "3/0/2", "Swimming": "3/0/2", "First Aid": "2/1/2", "Trading": "0/2/2", "Pickpocketing": "2/1/2" };
 var cleric_skill_costs = { "Two Weapon Combat": "9/9/1", "Armor Use": "8/0/1", "Shield Use": "13/0/1", "Combat Maneuvers": "10/6/1", "Edged Weapons": "4/2/1", "Blunt Weapons": "4/2/1", "Two-Handed Weapons": "10/3/1", "Ranged Weapons": "9/3/1", "Thrown Weapons": "9/3/1", "Polearm Weapons": "11/3/1", "Brawling": "6/1/1", "Ambush": "12/12/1", "Multi Opponent Combat": "15/8/1", "Physical Fitness": "7/0/1", "Dodging": "20/20/1", "Arcane Symbols": "0/2/2", "Magic Item Use": "0/2/2", "Spell Aiming": "3/2/2", "Harness Power": "0/4/3", "Elemental Mana Control": "0/12/1", "Mental Mana Control": "0/12/1", "Spirit Mana Control": "0/3/3", "Spell Research": "0/8/3", "Elemental Lore": "0/20/1", "Spiritual Lore": "0/6/2", "Sorcerous Lore": "0/10/1", "Mental Lore": "0/20/1", "Survival": "3/2/2", "Disarming Traps": "2/6/1", "Picking Locks": "2/4/2", "Stalking and Hiding": "5/4/1", "Perception": "0/3/2", "Climbing": "4/0/1", "Swimming": "3/0/1", "First Aid": "1/1/2", "Trading": "0/3/2", "Pickpocketing": "3/3/1" };
 var empath_skill_costs = { "Two Weapon Combat": "12/12/1", "Armor Use": "15/0/1", "Shield Use": "13/0/1", "Combat Maneuvers": "10/8/1", "Edged Weapons": "6/2/1", "Blunt Weapons": "6/2/1", "Two-Handed Weapons": "13/3/1", "Ranged Weapons": "14/3/1", "Thrown Weapons": "9/3/1", "Polearm Weapons": "14/3/1", "Brawling": "10/2/1", "Ambush": "15/15/1", "Multi Opponent Combat": "15/10/1", "Physical Fitness": "2/0/3", "Dodging": "20/20/1", "Arcane Symbols": "0/2/2", "Magic Item Use": "0/2/2", "Spell Aiming": "3/1/2", "Harness Power": "0/4/3", "Elemental Mana Control": "0/12/1", "Mental Mana Control": "0/3/2", "Spirit Mana Control": "0/3/2", "Spell Research": "0/8/3", "Elemental Lore": "0/20/1", "Spiritual Lore": "0/6/2", "Sorcerous Lore": "0/12/1", "Mental Lore": "0/6/2", "Survival": "3/2/2", "Disarming Traps": "2/6/1", "Picking Locks": "2/4/2", "Stalking and Hiding": "5/4/1", "Perception": "0/3/2", "Climbing": "4/0/1", "Swimming": "3/0/1", "First Aid": "1/0/3", "Trading": "0/3/2", "Pickpocketing": "3/3/1" };
 var monk_skill_costs = { "Two Weapon Combat": "2/2/2", "Armor Use": "10/0/2", "Shield Use": "8/0/2", "Combat Maneuvers": "5/3/2", "Edged Weapons": "2/1/2", "Blunt Weapons": "3/1/2", "Two-Handed Weapons": "5/2/2", "Ranged Weapons": "4/1/2", "Thrown Weapons": "2/1/2", "Polearm Weapons": "6/2/2", "Brawling": "2/1/2", "Ambush": "3/2/2", "Multi Opponent Combat": "5/2/2", "Physical Fitness": "2/0/3", "Dodging": "1/1/3", "Arcane Symbols": "0/6/1", "Magic Item Use": "0/7/1", "Spell Aiming": "5/20/1", "Harness Power": "0/6/1", "Elemental Mana Control": "0/15/1", "Mental Mana Control": "0/8/1", "Spirit Mana Control": "0/8/1", "Spell Research": "0/38/1", "Elemental Lore": "0/40/1", "Spiritual Lore": "0/12/1", "Sorcerous Lore": "0/35/1", "Mental Lore": "0/12/1", "Survival": "2/2/2", "Disarming Traps": "3/4/2", "Picking Locks": "3/3/2", "Stalking and Hiding": "3/2/2", "Perception": "0/2/2", "Climbing": "1/0/2", "Swimming": "2/0/2", "First Aid": "1/2/2", "Trading": "0/3/2", "Pickpocketing": "2/2/2" };
 var paladin_skill_costs = { "Two Weapon Combat": "3/3/2", "Armor Use": "3/0/3", "Shield Use": "3/0/3", "Combat Maneuvers": "5/4/2", "Edged Weapons": "3/1/2", "Blunt Weapons": "3/1/2", "Two-Handed Weapons": "4/2/2", "Ranged Weapons": "6/2/2", "Thrown Weapons": "5/1/2", "Polearm Weapons": "5/2/2", "Brawling": "4/1/2", "Ambush": "4/5/1", "Multi Opponent Combat": "5/2/1", "Physical Fitness": "3/0/2", "Dodging": "5/3/2", "Arcane Symbols": "0/5/1", "Magic Item Use": "0/6/1", "Spell Aiming": "5/20/1", "Harness Power": "0/5/2", "Elemental Mana Control": "0/15/1", "Mental Mana Control": "0/15/1", "Spirit Mana Control": "0/6/1", "Spell Research": "0/27/2", "Elemental Lore": "0/20/1", "Spiritual Lore": "0/7/2", "Sorcerous Lore": "0/18/1", "Mental Lore": "0/20/1", "Survival": "2/2/2", "Disarming Traps": "2/5/1", "Picking Locks": "2/4/2", "Stalking and Hiding": "4/4/1", "Perception": "0/3/2", "Climbing": "3/0/2", "Swimming": "2/0/2", "First Aid": "1/1/2", "Trading": "0/3/2", "Pickpocketing": "4/4/1" };
 var ranger_skill_costs = { "Two Weapon Combat": "3/2/2", "Armor Use": "5/0/2", "Shield Use": "5/0/2", "Combat Maneuvers": "6/4/2", "Edged Weapons": "3/1/2", "Blunt Weapons": "4/1/2", "Two-Handed Weapons": "6/2/2", "Ranged Weapons": "3/1/2", "Thrown Weapons": "3/1/2", "Polearm Weapons": "7/2/2", "Brawling": "4/1/2", "Ambush": "3/3/2", "Multi Opponent Combat": "10/4/1", "Physical Fitness": "4/0/2", "Dodging": "7/5/2", "Arcane Symbols": "0/5/1", "Magic Item Use": "0/5/1", "Spell Aiming": "5/15/1", "Harness Power": "0/5/2", "Elemental Mana Control": "0/15/1", "Mental Mana Control": "0/15/1", "Spirit Mana Control": "0/5/1", "Spell Research": "0/17/2", "Elemental Lore": "0/20/1", "Spiritual Lore": "0/10/1", "Sorcerous Lore": "0/18/1", "Mental Lore": "0/20/1", "Survival": "1/1/2", "Disarming Traps": "2/4/1", "Picking Locks": "2/3/2", "Stalking and Hiding": "2/1/2", "Perception": "0/2/2", "Climbing": "2/0/2", "Swimming": "2/0/2", "First Aid": "2/1/2", "Trading": "0/3/2", "Pickpocketing": "2/3/1" }; 
 var rogue_skill_costs = { "Two Weapon Combat": "2/2/2", "Armor Use": "5/0/2", "Shield Use": "4/0/2", "Combat Maneuvers": "4/4/2", "Edged Weapons": "2/1/2", "Blunt Weapons": "3/1/2", "Two-Handed Weapons": "6/2/2", "Ranged Weapons": "3/1/2", "Thrown Weapons": "2/1/2", "Polearm Weapons": "7/2/2", "Brawling": "3/1/2", "Ambush": "2/1/2", "Multi Opponent Combat": "10/3/1", "Physical Fitness": "3/0/3", "Dodging": "2/1/3", "Arcane Symbols": "0/7/1", "Magic Item Use": "0/8/1", "Spell Aiming": "4/22/1", "Harness Power": "0/9/1", "Elemental Mana Control": "0/10/1", "Mental Mana Control": "0/15/1", "Spirit Mana Control": "0/10/1", "Spell Research": "0/67/1", "Elemental Lore": "0/15/1", "Spiritual Lore": "0/15/1", "Sorcerous Lore": "0/30/1", "Mental Lore": "0/40/1", "Survival": "2/2/2", "Disarming Traps": "1/1/3", "Picking Locks": "1/1/3", "Stalking and Hiding": "1/1/3", "Perception": "0/1/3", "Climbing": "1/0/2", "Swimming": "2/0/2", "First Aid": "1/2/2", "Trading": "0/3/2", "Pickpocketing": "1/0/2" };
 var sorcerer_skill_costs = { "Two Weapon Combat": "12/12/1", "Armor Use": "15/0/1", "Shield Use": "13/0/1", "Combat Maneuvers": "12/8/1", "Edged Weapons": "6/2/1", "Blunt Weapons": "6/2/1", "Two-Handed Weapons": "14/3/1", "Ranged Weapons": "14/3/1", "Thrown Weapons": "9/3/1", "Polearm Weapons": "14/3/1", "Brawling": "10/2/1", "Ambush": "15/14/1", "Multi Opponent Combat": "15/10/1", "Physical Fitness": "8/0/1", "Dodging": "20/20/1", "Arcane Symbols": "0/2/2", "Magic Item Use": "0/2/2", "Spell Aiming": "3/1/2", "Harness Power": "0/4/3", "Elemental Mana Control": "0/3/2", "Mental Mana Control": "0/12/1", "Spirit Mana Control": "0/3/2", "Spell Research": "0/8/3", "Elemental Lore": "0/7/2", "Spiritual Lore": "0/7/2", "Sorcerous Lore": "0/6/2", "Mental Lore": "0/20/1", "Survival": "3/2/2", "Disarming Traps": "2/6/1", "Picking Locks": "2/4/2", "Stalking and Hiding": "5/4/1", "Perception": "0/3/2", "Climbing": "4/0/1", "Swimming": "3/0/1", "First Aid": "2/1/2", "Trading": "0/3/2", "Pickpocketing": "3/3/1" };
 var warrior_skill_costs = { "Two Weapon Combat": "2/2/2", "Armor Use": "2/0/3", "Shield Use": "2/0/3", "Combat Maneuvers": "4/3/2", "Edged Weapons": "2/1/2", "Blunt Weapons": "2/1/2", "Two-Handed Weapons": "3/1/2", "Ranged Weapons": "2/1/2", "Thrown Weapons": "2/1/2", "Polearm Weapons": "3/1/2", "Brawling": "2/1/2", "Ambush": "3/4/2", "Multi Opponent Combat": "4/3/2", "Physical Fitness": "2/0/3", "Dodging": "4/2/3", "Arcane Symbols": "0/7/1", "Magic Item Use": "0/8/1", "Spell Aiming": "5/25/1", "Harness Power": "0/10/1", "Elemental Mana Control": "0/10/1", "Mental Mana Control": "0/15/1", "Spirit Mana Control": "0/10/1", "Spell Research": "0/120/1", "Elemental Lore": "0/15/1", "Spiritual Lore": "0/15/1", "Sorcerous Lore": "0/30/1", "Mental Lore": "0/40/1", "Survival": "1/3/2", "Disarming Traps": "2/4/2", "Picking Locks": "2/3/2", "Stalking and Hiding": "3/2/2", "Perception": "0/3/2", "Climbing": "3/0/2", "Swimming": "2/0/2", "First Aid": "1/2/2", "Trading": "0/4/2", "Pickpocketing": "2/3/1" };
 var wizard_skill_costs = { "Two Weapon Combat": "12/12/1", "Armor Use": "14/0/1", "Shield Use": "13/0/1", "Combat Maneuvers": "12/8/1", "Edged Weapons": "6/1/1", "Blunt Weapons": "6/1/1", "Two-Handed Weapons": "14/3/1", "Ranged Weapons": "14/3/1", "Thrown Weapons": "8/2/1", "Polearm Weapons": "14/3/1", "Brawling": "10/2/1", "Ambush": "15/10/1", "Multi Opponent Combat": "15/10/1", "Physical Fitness": "8/0/1", "Dodging": "20/20/1", "Arcane Symbols": "0/1/2", "Magic Item Use": "0/1/2", "Spell Aiming": "2/1/2", "Harness Power": "0/4/3", "Elemental Mana Control": "0/4/2", "Mental Mana Control": "0/15/1", "Spirit Mana Control": "0/15/1", "Spell Research": "0/8/3", "Elemental Lore": "0/6/2", "Spiritual Lore": "0/20/1", "Sorcerous Lore": "0/10/1", "Mental Lore": "0/20/1", "Survival": "3/2/1", "Disarming Traps": "2/6/1", "Picking Locks": "2/4/2", "Stalking and Hiding": "5/4/1", "Perception": "0/3/2", "Climbing": "4/0/1", "Swimming": "3/0/1", "First Aid": "2/1/1", "Trading": "0/3/2", "Pickpocketing": "3/3/1" };
 var profession_skill_costs = { "bard": bard_skill_costs, "cleric": cleric_skill_costs, "empath": empath_skill_costs, "monk": monk_skill_costs, "paladin": paladin_skill_costs, "ranger": ranger_skill_costs, "rogue": rogue_skill_costs, "sorcerer": sorcerer_skill_costs, "warrior": warrior_skill_costs, "wizard": wizard_skill_costs };
    
 var ele_lore_sub_skills = [ "air", "earth", "fire", "water" ]; 
 var spirit_lore_sub_skills = [ "blessings", "religion", "summoning" ]; 
 var sorc_lore_sub_skills = [ "demonology", "necromancy" ]; 
 var mental_lore_sub_skills = [ "divination", "manipulation", "telepathy", "transference", "transformation" ]; 
 var spell_research_sub_skills = [ "Minor Spiritual", "Major Spiritual", "Cleric", "Minor Elemental", "Major Elemental", "Ranger", "Sorcerer", "Wizard", "Bard", "Empath", "Savant", "Minor Mental", "Major Mental", "Paladin" ];
 
 var subskills = { "Spell Research": spell_research_sub_skills, "Elemental Lore": ele_lore_sub_skills, "Spiritual Lore": spirit_lore_sub_skills, "Sorcerous Lore": sorc_lore_sub_skills, "Mental Lore": mental_lore_sub_skills }; 

 var skills = [ "Two Weapon Combat", "Armor Use", "Shield Use", "Combat Maneuvers", "Edged Weapons", "Blunt Weapons", "Two-Handed Weapons", "Ranged Weapons", "Thrown Weapons", "Polearm Weapons", "Brawling", "Ambush", "Multi Opponent Combat", "Physical Fitness", "Dodging", "Arcane Symbols", "Magic Item Use", "Spell Aiming", "Harness Power", "Elemental Mana Control", "Mental Mana Control", "Spirit Mana Control", "Spell Research", "Elemental Lore", "Spiritual Lore", "Sorcerous Lore", "Mental Lore", "Survival", "Disarming Traps", "Picking Locks", "Stalking and Hiding", "Perception", "Climbing", "Swimming", "First Aid", "Trading", "Pickpocketing" ];

 var available_skills = [];   //contains all skills, including subskills. Needed for cycling through ALL skills.

  
 var skill_redux = { "Two Weapon Combat":0.3, "Armor Use":0.4, "Shield Use":0.4, "Combat Maneuvers":0.3, "Edged Weapons":0.3, "Blunt Weapons":0.3, "Two-Handed Weapons":0.3, "Ranged Weapons":0.3, "Thrown Weapons":0.3, "Polearm Weapons":0.3, "Brawling":0.3, "Ambush":0.4, "Multi Opponent Combat":0.4, "Physical Fitness":1.0, "Dodging":0.4, "Arcane Symbols":0, "Magic Item Use":0, "Spell Aiming":0, "Harness Power":0, "Elemental Mana Control":0, "Mental Mana Control":0, "Spirit Mana Control":0, "Spell Research":0, "Elemental Lore":0, "Spiritual Lore":0, "Sorcerous Lore":0, "Mental Lore":0, "Survival":0, "Disarming Traps":0, "Picking Locks":0, "Stalking and Hiding":0, "Perception":0, "Climbing":0, "Swimming":0, "First Aid":0, "Trading":0, "Pickpocketing":0 };
 
 //var linked_skills = { "elemental lore, air": ele_lore_sub_skills, "elemental lore, earth": ele_lore_sub_skills };

 var training_rate = {};  
 var hide_unused_skills = false;
 var checked_skills = {};
  
  
 var ranks_by_level = [];
 var total_ranks_by_level = [];
 var total_bonus_by_level = [];
	for (var i=0; i <= 100; i++) {
		ranks_by_level[i] = {};
		total_ranks_by_level[i] = {};
		total_bonus_by_level[i] = {};
	}	
	
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
function Maneuver(name, mnemonic, type, rank_costs, avail, prereq) {
 this.name = name;
 this.mnemonic = mnemonic;
 this.type = type; //combat, shield, armor
 this.rank_costs = rank_costs.split(",");
 this.availability = {"bard":0, "cleric":0, "empath":0, "monk":0, "paladin":0, "ranger":0, "rogue":0, "savant":0, "sorcerer":0, "warrior":0, "wizard":0}; 
 this.prerequisites = {};  //"CM|Shadow Mastery":4, "Skill|Multi-Opponent Combat":30

 this.GetCostAtRank = function( rank ) { return this.rank_costs[rank-1] || 0; };
 
 //CONSTRUCTOR
 var parts;
	
	parts = avail.split(",");
	for( var i=0; i<parts.length; i++ ) {
	 this.availability[parts[i]] = 1;
	}
	if( prereq != "" ) {
		parts = prereq.split(",");	
		for( var i=0; i<parts.length; i++ ) {
			this.prerequisites[parts[i].split(":")[0]] = parts[i].split(":")[1];
		}	
	}
}



 var hide_unused_maneuvers = false;
 var hidden_maneuvers = {};
 var avail_maneuvers = new Object_List();
 var maneuvers = new Object_List();
 
//Add all Combat Maneuvers to list
maneuvers.AddObject(new Maneuver("Armor Spike Focus", "SPIKEFOCUS", "combat", "5,10", "warrior,rogue,paladin", ""));
maneuvers.AddObject(new Maneuver("Bearhug", "BEARHUG", "combat", "2,4,6,8,10", "warrior,monk", ""));
maneuvers.AddObject(new Maneuver("Berserk", "BERSERK", "combat", "2,4,6,8,10", "warrior", ""));
maneuvers.AddObject(new Maneuver("Block Mastery", "BMASTERY", "combat", "4,8,12", "warrior", ""));
maneuvers.AddObject(new Maneuver("Bull Rush", "BULLRUSH", "combat", "2,4,6,8,10", "warrior,paladin", ""));
maneuvers.AddObject(new Maneuver("Burst of Swiftness", "BURST", "combat", "2,4,6,8,10", "monk", ""));
maneuvers.AddObject(new Maneuver("Charge", "Charge", "combat", "2,4,6,8,10", "warrior,bard,monk,paladin", ""));
maneuvers.AddObject(new Maneuver("Cheapshots", "CHEAPSHOTS", "combat", "2,3,4,5,6", "bard,monk,rogue", ""));
maneuvers.AddObject(new Maneuver("Combat Focus", "FOCUS", "combat", "2,4,6,8,10", "warrior,rogue,ranger,bard,monk,paladin", ""));
maneuvers.AddObject(new Maneuver("Combat Mastery", "CMASTERY", "combat", "2,4", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", ""));
maneuvers.AddObject(new Maneuver("Combat Mobility", "MOBILITY", "combat", "5,10", "warrior,rogue,monk", ""));
maneuvers.AddObject(new Maneuver("Combat Movement", "CMOVEMENT", "combat", "2,3,4,5,6", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", ""));
maneuvers.AddObject(new Maneuver("Combat Toughness", "TOUGHNESS", "combat", "6,8,10", "warrior,rogue,monk,paladin", ""));
maneuvers.AddObject(new Maneuver("Coup de Grace", "COUPDEGRACE", "combat", "2,4,6,8,10", "warrior,rogue", ""));
maneuvers.AddObject(new Maneuver("Crowd Press", "CPRESS", "combat", "2,4,6,8,10", "warrior,rogue,monk,paladin", ""));
maneuvers.AddObject(new Maneuver("Cunning Defense", "CDEFENSE", "combat", "2,3,4,5,6", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", ""));
maneuvers.AddObject(new Maneuver("Cutthroat", "CUTTROAT", "combat", "2,4,6,8,10", "warrior,rogue,monk,paladin", ""));
maneuvers.AddObject(new Maneuver("Dirtkick", "DIRTKICK", "combat", "2,3,4,5,6", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", ""));
maneuvers.AddObject(new Maneuver("Disarm Weapon", "DISARM", "combat", "2,4,6,8,10", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", ""));
maneuvers.AddObject(new Maneuver("Divert", "DIVERT", "combat", "2,3,4,5,6", "rogue", ""));
maneuvers.AddObject(new Maneuver("Duck and Weave", "WEAVE", "combat", "4,8,12", "rogue,monk", "CM|Evade Mastery:2"));
maneuvers.AddObject(new Maneuver("Dust Shroud", "SHROUD", "combat", "2,3,4,5,6", "rogue", "CM|Dirtkick:4"));
maneuvers.AddObject(new Maneuver("Evade Mastery", "EMASTERY", "combat", "4,8,12", "warrior,rogue,monk", ""));
maneuvers.AddObject(new Maneuver("Executioner's Stance", "EXECUTIONER", "combat", "4,8,12", "warrior", ""));
maneuvers.AddObject(new Maneuver("Feint", "FEINT", "combat", "2,3,5,7,10", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", ""));
maneuvers.AddObject(new Maneuver("Flurry of Blows", "FLURRY", "combat", "3,6,9", "monk", ""));
maneuvers.AddObject(new Maneuver("Garrote", "GARROTE", "combat", "2,4,6,8,10", "rogue,ranger,bard,monk", ""));
maneuvers.AddObject(new Maneuver("Grapple Mastery", "GMASTERY", "combat", "4,8,12", "warrior,rogue,monk", ""));
maneuvers.AddObject(new Maneuver("Griffin's Voice", "GRIFFIN", "combat", "3,6,9", "warrior", ""));
maneuvers.AddObject(new Maneuver("Groin Kick", "GKICK", "combat", "2,4,6,8,10", "rogue", ""));
maneuvers.AddObject(new Maneuver("Hamstring", "HAMSTRING", "combat", "2,4,6,8,10", "warrior,ranger,bard,rogue", ""));
maneuvers.AddObject(new Maneuver("Haymaker", "HAYMAKER", "combat", "2,4,6,8,10", "warrior", ""));
maneuvers.AddObject(new Maneuver("Headbutt", "HEADBUTT", "combat", "2,3,4,5,6", "warrior,monk", ""));
maneuvers.AddObject(new Maneuver("Inner Harmony", "IHARMONY", "combat", "4,8,12", "monk", ""));
maneuvers.AddObject(new Maneuver("Internal Power", "IPOWER", "combat", "2,4,6,8,10", "monk", ""));
maneuvers.AddObject(new Maneuver("Ki Focus", "KIFOCUS", "combat", "3,6,9", "monk", ""));
maneuvers.AddObject(new Maneuver("Kick Mastery", "KMASTERY", "combat", "4,8,12", "warrior,rogue,monk", ""));
maneuvers.AddObject(new Maneuver("Mighty Blow", "MBLOW", "combat", "2,4,6,8,10", "warrior", ""));
maneuvers.AddObject(new Maneuver("Multi-Fire", "MFIRE", "combat", "2,4,6,8,10", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", ""));
maneuvers.AddObject(new Maneuver("Mystic Strike", "MYSTICSTRIKE", "combat", "2,3,4,5,6", "monk", ""));
maneuvers.AddObject(new Maneuver("Parry Mastery", "PMASTERY", "combat", "4,8,12", "warrior", ""));
maneuvers.AddObject(new Maneuver("Perfect Self", "PERFECTSELF", "combat", "2,4,6,8,10", "monk", "CM|Burst of Speed:3,CM|Surge of Strength:3"));
maneuvers.AddObject(new Maneuver("Precision", "PRECISION", "combat", "4,6", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", ""));
maneuvers.AddObject(new Maneuver("Predator's Eye", "PREDATOR", "combat", "4,6,8", "rogue", ""));
maneuvers.AddObject(new Maneuver("Punch Mastery", "PUNCHMASTERY", "combat", "4,8,12", "warrior,rogue,monk", ""));
maneuvers.AddObject(new Maneuver("Quickstrike", "QSTRIKE", "combat", "2,4,6,8,10", "warrior,rogue,monk", ""));
maneuvers.AddObject(new Maneuver("Rolling Krynch Stance", "KRYNCH", "combat", "4,8,12", "monk", ""));
maneuvers.AddObject(new Maneuver("Shadow Mastery", "SMASTERY", "combat", "2,4,6,8,10", "ranger,rogue", ""));
maneuvers.AddObject(new Maneuver("Shield Bash", "SBASH", "combat", "2,4,6,8,10", "ranger,rogue,warrior,bard,paladin", ""));
maneuvers.AddObject(new Maneuver("Shield Charge", "SCHARGE", "combat", "2,4,6,8,10", "warrior,paladin", ""));
maneuvers.AddObject(new Maneuver("Side By Side", "SIDEBYSIDE", "combat", "2,4,6,8,10", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", "CM:Combat Movement:2"));
maneuvers.AddObject(new Maneuver("Silent Strike", "SILENTSTRIKE", "combat", "2,4,6,8,10", "rogue", "CM|Shadow Mastery:2"));
maneuvers.AddObject(new Maneuver("Slippery Mind", "SLIPPERYMIND", "combat", "4,8,12", "rogue", "CM|Shadow Mastery:2"));
maneuvers.AddObject(new Maneuver("Specialization I", "WSPEC1", "combat", "2,4,6,8,10", "warrior,rogue,paladin", ""));
maneuvers.AddObject(new Maneuver("Specialization II", "WSPEC2", "combat", "2,4,6,8,10", "warrior,rogue,paladin", ""));
maneuvers.AddObject(new Maneuver("Specialization III", "WSPEC3", "combat", "2,4,6,8,10", "warrior,rogue,paladin", ""));
maneuvers.AddObject(new Maneuver("Spell Cleaving", "SCLEAVE", "combat", "2,4,6,8,10", "warrior,monk", ""));
maneuvers.AddObject(new Maneuver("Spell Parry", "SPARRY", "combat", "4,8,12", "warrior,Rouge,monk", ""));
maneuvers.AddObject(new Maneuver("Spell Thieve", "SATTACK", "combat", "2,4,6,8,10", "rogue", ""));
maneuvers.AddObject(new Maneuver("Spin Attack", "THIEVE", "combat", "2,4,6,8,10", "warrior,rogue, bard,monk", ""));
maneuvers.AddObject(new Maneuver("Staggering Blow", "SBLOW", "combat", "2,4,6,8,10", "warrior", ""));
maneuvers.AddObject(new Maneuver("Stance of the Mongoose", "MONGOOSE", "combat", "4,8,12", "warrior,monk", ""));
maneuvers.AddObject(new Maneuver("Stun Maneuvers", "STUNMAN", "combat", "2,4,6,8,10", "warrior,monk,rogue", ""));
maneuvers.AddObject(new Maneuver("Subdual Strike", "SSTRIKE", "combat", "2,3,4,5,6", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", ""));
maneuvers.AddObject(new Maneuver("Subdue", "SUBDUE", "combat", "2,3,4,5,6", "rogue", ""));
maneuvers.AddObject(new Maneuver("Sucker Punch", "SPUNCH", "combat", "2,3,4,5,6", "rogue", ""));
maneuvers.AddObject(new Maneuver("Sunder Shield", "SUNDER", "combat","2,4,6,8,10", "warrior", ""));
maneuvers.AddObject(new Maneuver("Surge of Strength", "SURGE", "combat", "2,4,6,8,10", "warrior,monk,rogue,paladin", ""));
maneuvers.AddObject(new Maneuver("Sweep", "SWEEP", "combat", "2,4,6,8,10", "bard,monk,ranger,rogue", ""));
maneuvers.AddObject(new Maneuver("Tackle", "TACKLE", "combat", "2,4,6,8,10", "warrior", ""));
maneuvers.AddObject(new Maneuver("Tainted Bond", "TAINTED", "combat", "20", "warrior,paladin", "CM|Weapon Bonding:5~Skill|Spell Research, Paladin Base:25"));
maneuvers.AddObject(new Maneuver("Trip", "TRIP", "combat", "2,4,6,8,10", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", ""));
maneuvers.AddObject(new Maneuver("Truehand", "TRUEHAND", "combat", "2,4,6,8,10", "warrior,paladin,rogue", ""));
maneuvers.AddObject(new Maneuver("Twin Hammerfists", "TWINHAMM", "combat", "2,4,6,8,10", "warrior", ""));
maneuvers.AddObject(new Maneuver("Unarmed Specialist", "UNARMEDSPEC", "combat", "6", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", ""));
maneuvers.AddObject(new Maneuver("Vanish", "VANISH", "combat", "4,8,12", "rogue", "CM|Shadow Mastery:4"));
maneuvers.AddObject(new Maneuver("Weapon Bonding", "BOND", "combat", "2,4,6,8,10", "warrior", "CM|Specialization I:3~CM|Specialization II:3~CM|Specialization III:3"));
maneuvers.AddObject(new Maneuver("Whirling Dervish", "DERVISH", "combat", "4,8,12", "warrior,rogue", ""));

// Add all Shield Maneuvers to the list
maneuvers.AddObject(new Maneuver("Small Shield Focus", "SFOCUS", "shield", "4,6,8,10,12", "warrior,rogue", ""));
maneuvers.AddObject(new Maneuver("Medium Shield Focus", "MFOCUS", "shield", "4,6,8,10,12", "warrior,rogue,paladin", ""));
maneuvers.AddObject(new Maneuver("Large Shield Focus", "LFOCUS", "shield", "4,6,8,10,12", "warrior,paladin", ""));
maneuvers.AddObject(new Maneuver("Tower Shield Focus", "TFOCUS", "shield", "4,6,8,10,12", "warrior,paladin", ""));
maneuvers.AddObject(new Maneuver("Shield Bash", "SBASH", "shield", "2,4,6,8,10", "warrior,rogue,paladin", ""));
maneuvers.AddObject(new Maneuver("Shield Charge", "SCHARGE", "shield", "2,4,6,8,10", "warrior,paladin", "SM|Shield Bash:2~CM|Shield Bash:2"));
maneuvers.AddObject(new Maneuver("Shield Push", "PUSH", "shield", "2,4,6,8,10", "warrior,paladin", "SM|Shield Bash:2~CM|Shield Bash:2"));
maneuvers.AddObject(new Maneuver("Shield Pin", "PIN", "shield", "2,4,6,8,10", "warrior", "SM|Shield Bash:2~CM|Shield Bash:2"));
maneuvers.AddObject(new Maneuver("Shield Swiftness", "SWIFTNESS", "shield", "6,12,18", "warrior,rogue", "SM|Small Shield Focus:3~SM|Medium Shield Focus:3"));
maneuvers.AddObject(new Maneuver("Shield Brawler", "BRAWLER", "shield", "6,8,10,12,14", "warrior,rogue,paladin", "SM|Small Shield Focus:3~SM|Medium Shield Focus:3~SM|Large Shield Focus:3~SM|Tower Shield Focus:3"));
maneuvers.AddObject(new Maneuver("Prop Up", "PROP", "shield", "6,12,18", "warrior,paladin", "SM|Large Shield Focus:3~SM|Tower Shield Focus:3"));
maneuvers.AddObject(new Maneuver("Adamantine Bulwark", "BULWARK", "shield", "6,12,18", "warrior", "SM|Prop Up:2"));
maneuvers.AddObject(new Maneuver("Shield Riposte", "RIPOSTE", "shield", "4,8,12", "warrior,rogue", "SM|Shield Bash:2~CM|Shield Bash:2"));
maneuvers.AddObject(new Maneuver("Shield Forward", "FORWARD", "shield", "4,8,12", "warrior,rogue,paladin", ""));
maneuvers.AddObject(new Maneuver("Shield Spike Focus", "SPIKEFOCUS", "shield", "8,12", "warrior,rogue,paladin", ""));
maneuvers.AddObject(new Maneuver("Shield Spike Mastery", "SPIKEMASTERY", "shield", "8,12", "warrior,rogue,paladin", "SM|Shield Spike Focus:2"));
maneuvers.AddObject(new Maneuver("Deflection Training", "DTRAINING", "shield", "6,12,18", "warrior,rogue", "SM|Small Shield Focus:3~SM|Medium Shield Focus:3~SM|Large Shield Focus:3~SM|Tower Shield Focus:3"));
maneuvers.AddObject(new Maneuver("Deflection Mastery", "DMASTERY", "shield", "8,10,12,14,16", "warrior,rogue", "SM|Deflection Training:3"));
maneuvers.AddObject(new Maneuver("Block the Elements", "EBLOCK", "shield", "6,12,18", "warrior,paladin", ""));
maneuvers.AddObject(new Maneuver("Deflect the Elements", "DEFLECT", "shield", "6,12,18", "warrior,rogue", ""));
maneuvers.AddObject(new Maneuver("Steady Shield", "STEADY", "shield", "4,6", "warrior,rogue", "CM|Stun Maneuvers:2"));
maneuvers.AddObject(new Maneuver("Disarming Presence", "DPRESENCE", "shield", "6,12,18", "warrior,rogue", "CM|Disarm Weapon:2"));
maneuvers.AddObject(new Maneuver("Guard Mastery", "GUARDMASTERY", "shield", "6,12,18", "warrior", ""));
maneuvers.AddObject(new Maneuver("Tortoise Stance", "TORTOISE", "shield", "6,12,18", "warrior", "SM|Block Mastery:2"));
maneuvers.AddObject(new Maneuver("Spell Block", "SPELLBLOCK", "shield", "6,12,18", "warrior,rogue,paladin", "SM|Small Shield Focus:3~SM|Medium Shield Focus:3~SM|Large Shield Focus:3~SM|Tower Shield Focus:3"));
maneuvers.AddObject(new Maneuver("Shield Mind", "MIND", "shield", "6,12,18", "warrior,rogue,paladin", "SM|Spell Block:2"));
maneuvers.AddObject(new Maneuver("Protective Wall", "PWALL", "shield", "4,6", "warrior,rogue,paladin", "SM|Tower Shield Focus:2"));
maneuvers.AddObject(new Maneuver("Shield Strike", "STRIKE", "shield", "2,4,6,8,10", "warrior,rogue,paladin", "SM|Shield Bash:2~CM|Shield Bash:2"));
maneuvers.AddObject(new Maneuver("Shield Strike Mastery", "STRIKEMASTERY", "shield", "30", "warrior,rogue,paladin", "SM|Shield Strike:2,Skill|Multi Opponent Combat:30"));
maneuvers.AddObject(new Maneuver("Shield Trample", "TRAMPLE", "shield", "2,4,6,8,10", "warrior", "SM|Shield Charge:2"));
maneuvers.AddObject(new Maneuver("Shield Trample Mastery", "TMASTERY", "shield", "8,10,12", "warrior", "SM|Shield Trample:3,Skill|Multi Opponent Combat:30"));
maneuvers.AddObject(new Maneuver("Steely Resolve", "RESOLVE", "shield", "6,12,18", "warrior,paladin", "SM|Tower Shield Focus:3"));
maneuvers.AddObject(new Maneuver("Phalanx", "PHALANX", "shield", "2,4,6,8,10", "warrior,rogue,paladin", ""));

// Add all Armor Specializations to the list
maneuvers.AddObject(new Maneuver("Crush Protection", "CRUSH", "armor", "20,30,40,50,60", "warrior", ""));
maneuvers.AddObject(new Maneuver("Puncture Protection", "PUNCTURE", "armor", "20,30,40,50,60", "warrior", ""));
maneuvers.AddObject(new Maneuver("Slash Protection", "SLASH", "armor", "20,30,40,50,60", "warrior", ""));
maneuvers.AddObject(new Maneuver("Armored Casting", "CASTING", "armor", "20,30,40,50,60", "paladin", ""));
maneuvers.AddObject(new Maneuver("Armored Evasion", "EVASION", "armor", "20,30,40,50,60", "rogue", ""));
maneuvers.AddObject(new Maneuver("Armored Fluidity", "FLUIDITY", "armor", "20,30,40,50,60", "paladin", ""));
maneuvers.AddObject(new Maneuver("Armor Reinforcement", "REINFORCE", "armor", "20,30,40,50,60", "warrior", ""));
maneuvers.AddObject(new Maneuver("Armored Stealth", "STEALTH", "armor", "20,30,40,50,60", "rogue", ""));
maneuvers.AddObject(new Maneuver("Armor Support", "SUPPORT", "armor", "20,30,40,50,60", "warrior", ""));

 
 var man_ranks_by_level = [];
 var total_man_ranks_by_level = [];
	for (var i=0; i <= 100; i++) {
		man_ranks_by_level[i] = {};
		total_man_ranks_by_level[i] = {};
	} 
  
  
  
  
  
  
  
  
  
