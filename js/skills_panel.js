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

 var all_skills = [];   //contains all skills, including subskills. Needed for cycling through ALL skills.
	for( var i=0; i < skills.length; i++ ) {
		if( subskills[skills[i]] != undefined ) {
			for( var j=0; j < subskills[skills[i]].length; j++) {
				all_skills[all_skills.length] = skills[i]+", "+subskills[skills[i]][j];    
			}
		}
		else {
			all_skills[all_skills.length] = skills[i];
		}
	}
  
 var skill_redux = { "Two Weapon Combat":0.3, "Armor Use":0.4, "Shield Use":0.4, "Combat Maneuvers":0.3, "Edged Weapons":0.3, "Blunt Weapons":0.3, "Two-Handed Weapons":0.3, "Ranged Weapons":0.3, "Thrown Weapons":0.3, "Polearm Weapons":0.3, "Brawling":0.3, "Ambush":0.4, "Multi Opponent Combat":0.4, "Physical Fitness":1.0, "Dodging":0.4, "Arcane Symbols":0, "Magic Item Use":0, "Spell Aiming":0, "Harness Power":0, "Elemental Mana Control":0, "Mental Mana Control":0, "Spirit Mana Control":0, "Spell Research":0, "Elemental Lore":0, "Spiritual Lore":0, "Sorcerous Lore":0, "Mental Lore":0, "Survival":0, "Disarming Traps":0, "Picking Locks":0, "Stalking and Hiding":0, "Perception":0, "Climbing":0, "Swimming":0, "First Aid":0, "Trading":0, "Pickpocketing":0 };
 
 //var linked_skills = { "elemental lore, air": ele_lore_sub_skills, "elemental lore, earth": ele_lore_sub_skills };

 var bard_spell_circles = [ "Minor Elemental", "Bard" ];
 var cleric_spell_circles = [ "Minor Spiritual", "Major Spiritual", "Cleric" ];
 var empath_spell_circles = [ "Minor Spiritual", "Major Spiritual", "Empath" ];
 var monk_spell_circles = [ "Minor Spiritual", "Minor Mental" ];
 var paladin_spell_circles = [ "Minor Spiritual", "Paladin" ];
 var ranger_spell_circles = [ "Minor Spiritual", "Ranger" ];
 var rogue_spell_circles = [ "Minor Elemental", "Minor Spiritual" ];
 var sorcerer_spell_circles = [ "Minor Elemental", "Minor Spiritual", "Sorcerer" ];
 var warrior_spell_circles = [ "Minor elemental", "Minor spiritual" ];
 var wizard_spell_circles = [ "Minor Elemental", "Major Elemental", "Wizard" ];
 
 var profession_spell_circles = { "bard": bard_spell_circles, "cleric": cleric_spell_circles, "empath": empath_spell_circles, "monk": monk_spell_circles, "paladin": paladin_spell_circles, "ranger": ranger_spell_circles, "rogue": rogue_spell_circles, "sorcerer": sorcerer_spell_circles, "warrior": warrior_spell_circles, "wizard": wizard_spell_circles };
  
 var training_rate = {};  
  
 var ranks_by_level = [];
 var total_ranks_by_level = [];
 var total_bonus_by_level = [];
	for (var i=0; i <= 100; i++) {
		ranks_by_level[i] = {};
		total_ranks_by_level[i] = {};
		total_bonus_by_level[i] = {};
	}
    
  
	function SkillsPanel_Init() {
		var info_div = document.getElementById("SkP_skills_info_container");
		var training_div = document.getElementById("SkP_skills_training_container");
		var prof = document.getElementById("StP_selected_profession").value;
		
		var info_tbl = document.createElement('table');
		var training_tbl = document.createElement('table');
		var info_tbdy = document.createElement('tbody');
		var training_tbdy = document.createElement('tbody');
		var tr, td, level;
		
		var PTP, MTP, ranks, val;
		
		info_tbl.width = "100%";
	//	training_tbl.width = "100%";
		training_tbl.width = "4545px";	
		
		for( var i=0; i <= 100; i++ ) {
			col = document.createElement('colgroup');
			col.style.width = "43px";
			training_tbl.appendChild(col);			
		}
		

		col = document.createElement('col');
		col.style.width = "5%";
		info_tbl.appendChild(col);
		col = document.createElement('col');
		col.style.width = "";
		info_tbl.appendChild(col);
		col = document.createElement('col');
		col.style.width = "7%%";
		info_tbl.appendChild(col);
		col = document.createElement('col');
		col.style.width = "7%";
		info_tbl.appendChild(col);		
		col = document.createElement('col');
		col.style.width = "5%";
		info_tbl.appendChild(col);
		col = document.createElement('col');
		col.style.width = "5%";
		info_tbl.appendChild(col);	
			
		//Level Row		
		tr = document.createElement('tr');
		for(var j=0; j<=100; j++) {
			td=document.createElement('td');
			level = document.createElement('div');
			td.height="23";
			td.style.backgroundColor="black";
			level.style.color="white";
			level.style.fontWeight="bold";
			level.style.textAlign="center";			
			level.innerHTML = j;	
			td.appendChild(level);			
			tr.appendChild(td);    
		}    
		training_tbdy.appendChild(tr);		
		
		tr = document.createElement('tr');
		tr.style.fontWeight="bold";
	
		td = document.createElement('td');	
		td.height = "23px";			
		tr.appendChild(td);    			
		
		td = document.createElement('td');
		td.appendChild(document.createTextNode("Skill Name"));		
		tr.appendChild(td);    		
		
		td = document.createElement('td');
		td.appendChild(document.createTextNode("PTP"));
		td.style.textAlign="center";	
		tr.appendChild(td);  
		
		td = document.createElement('td');
		td.appendChild(document.createTextNode("MTP"));	
		td.style.textAlign="center";
		tr.appendChild(td);  
		
		td = document.createElement('td');		
		td.appendChild(document.createTextNode("Ranks"));
		td.style.textAlign="center";		
		tr.appendChild(td);  		
		
		td = document.createElement('td');		
		td.appendChild(document.createTextNode("Rate"));
		td.style.textAlign="center";		
		tr.appendChild(td); 		
		
		info_tbdy.appendChild(tr);
				
		//Skill Info and Training Rows
		for( var i=0; i < all_skills.length; i++ ) {
			val = profession_skill_costs[prof][all_skills[i].split(",")[0]].split("/");
			PTP = val[0];
			MTP = val[1];
			ranks = val[2];		
			
			tr = SkillsPanel_Create_Skill_Row_Left(all_skills[i], PTP, MTP, ranks);
			info_tbdy.appendChild(tr);
			tr = SkillsPanel_Create_Skill_Row_Right(all_skills[i]);
			training_tbdy.appendChild(tr);		
		}		
		
		//blank row
		tr = document.createElement('tr');
		td = document.createElement('td');
		td.height="23";
		tr.appendChild(td);
		info_tbdy.appendChild(tr); 
		tr = document.createElement('tr');
		td = document.createElement('td');
		td.height="23";
		tr.appendChild(td);
		training_tbdy.appendChild(tr); 		
		
		//PTP spent row		
		tr = SkillsPanel_Create_Label_Row_Left("PTP Used");
		info_tbdy.appendChild(tr);
		tr = SkillsPanel_Create_Label_Row_Right("PTP_used_", "0");
		training_tbdy.appendChild(tr);
	
		//MTP spent row	
		tr = SkillsPanel_Create_Label_Row_Left("MTP Used");
		info_tbdy.appendChild(tr);
		tr = SkillsPanel_Create_Label_Row_Right("MTP_used_", "0");
		training_tbdy.appendChild(tr);
				
		//Total PTP left
		tr = SkillsPanel_Create_Label_Row_Left("Total PTP Left");
		info_tbdy.appendChild(tr);
		tr = SkillsPanel_Create_Label_Row_Right("PTP_left_", "0");
		training_tbdy.appendChild(tr);
		
		//Total MTP left
		tr = SkillsPanel_Create_Label_Row_Left("Total MTP Left");
		info_tbdy.appendChild(tr);
		tr = SkillsPanel_Create_Label_Row_Right("MTP_left_", "0");
		training_tbdy.appendChild(tr);
		
		//Redux Points
		tr = SkillsPanel_Create_Label_Row_Left("Redux Points");
		info_tbdy.appendChild(tr);
		tr = SkillsPanel_Create_Label_Row_Right("redux_pts_", "0");
		training_tbdy.appendChild(tr);		

		//blank spacing row for info side to deal with scroll bar on training side
		tr = document.createElement('tr');
		td = document.createElement('td');
		td.height="23";
		tr.appendChild(td);
		info_tbdy.appendChild(tr); 				
		
		//append table to div
		info_tbl.appendChild(info_tbdy);
		info_div.appendChild(info_tbl);	
		training_tbl.appendChild(training_tbdy);
		training_div.appendChild(training_tbl);	 	
		
		
		tbl = document.createElement('table');
		tbdy = document.createElement('tbody');		
					
		SkillsPanel_Calculate_Remaining_TP(0);	
		SkillsPanel_Calculate_Redux_Points(0);
		SkillsPanel_Change_Displayed_Skills();
	}
	
	function SkillsPanel_Create_Skill_Row_Left(skill, PTP, MTP, ranks) {
		var	tr = document.createElement('tr');
		var td, checkbox, input;

		tr.id = skill + "_info_row";		
		tr.style.backgroundColor = "lightgray";
	
		td = document.createElement('td');	
		td.height = "23px";			
		checkbox = document.createElement('input');
		checkbox.id = skill + "_checkbox";	
		checkbox.type = "checkbox";
		td.appendChild(checkbox);
		tr.appendChild(td);    			
		
		td = document.createElement('td');
		td.appendChild(document.createTextNode(skill));		
		td.id = skill + "_text";		
		tr.appendChild(td);    		
		
		td = document.createElement('td');
		td.appendChild(document.createTextNode(PTP));
		td.style.textAlign="center";	
		td.id = skill + "_PTP_cost";
		tr.appendChild(td);  
		
		td = document.createElement('td');
		td.appendChild(document.createTextNode(MTP));	
		td.style.textAlign="center";
		td.id = skill + "_MTP_cost";		
		tr.appendChild(td);  
		
		td = document.createElement('td');		
		td.appendChild(document.createTextNode("(" + ranks + ")"));
		td.style.textAlign="center";	
		td.id = skill + "_max_ranks";		
		tr.appendChild(td);  		
		
		td = document.createElement('td');		
		
		input = document.createElement('input');
		input.maxLength = 5;
		input.size= 3;
		input.style.textAlign = "center";
		input.id = skill + "_rate";		
		input.onblur = function() {  SkillsPanel_Rate_Input_Onblur(this) };	
		input.click = function() {  this.focus() };                     //need this for a work around in the input_onkeyp function. lets the arrows the cursor move up/down
		input.onkeyup = function(event) {  SkillsPanel_Training_Input_Onkeyup(event, this) };	
		td.appendChild(input);
		tr.appendChild(td);  			
		
		return tr;
	}
  
 	function SkillsPanel_Create_Skill_Row_Right(skill) {
		var tr = document.createElement('tr');
		var td, input, div;
		
		tr.id = skill + "_training_row";	
		tr.style.backgroundColor = "lightgray";
		
		for(var j=0; j<=100; j++) {
			td = document.createElement('td');
			td.height = 23;
			td.id = skill + "_ranks_" + j;
			td.align="center";	
			td.onclick = function() { SkillsPanel_Training_Div_Onclick(this); };
						
			div = document.createElement('div');
			div.id = skill + "_div_" + j;
			div.style.width = 31;
			div.style.textAlign="center";	
			div.onclick = function() {  SkillsPanel_Training_Div_Onclick(this); };	
			td.appendChild(div);  				

			//input box for rank training per level
			input = document.createElement('input');
			input.id = skill + "_input_" + j;	
			input.style.display = "none";		
			input.size="2";		
			input.maxLength = "1";
			input.type="text";
			input.align="center";
			input.style.textAlign="center";
			input.onblur = function() {  SkillsPanel_Training_Input_Onblur(this) };	
			input.onkeyup = function(event) {  SkillsPanel_Training_Input_Onkeyup(event, this) };	
			td.appendChild(input);  
			
			tr.appendChild(td);    
		}  		
	
		return tr;
	} 
	
	function SkillsPanel_Create_Label_Row_Left(title) {
		tr = document.createElement('tr');
		td = document.createElement('td');
		td.height="23";
		td.colSpan = "6";
		td.align = "right";
		td.style.fontWeight="bold";
		td.appendChild(document.createTextNode(title));
		tr.appendChild(td);
		
		return tr;
	}

	function SkillsPanel_Create_Label_Row_Right(id, text) {
		tr = document.createElement('tr');
		for ( var i=0; i <= 100; i++ ) {
			td = document.createElement('td');
			td.id = id+i;
			td.appendChild(document.createTextNode(text));			
			td.height="23";
			td.style.textAlign="center";	
			td.style.backgroundColor="lightgray";
			tr.appendChild(td);    		
		}		
		return tr;
	}
	
	function SkillsPanel_Training_Div_Onclick(caller) {
		var arr = caller.id.split("_"); 
		var input = document.getElementById(arr[0] + "_input_" + arr[2]); 
		
		document.getElementById(arr[0]+"_div_"+arr[2]).style.display = "none";	
		input.style.display = "block"; 
				
		if( !isNaN(ranks_by_level[arr[2]][arr[0]]) && ranks_by_level[arr[2]][arr[0]] > 0 ) {
			input.value = ranks_by_level[arr[2]][arr[0]];
		}
		else {	
			input.value = "";
		}			
		input.select();
	}

	function SkillsPanel_Training_Input_Onblur(caller) {
		var arr = caller.id.split("_"); 
		var div = document.getElementById(arr[0] + "_div_" + arr[2]); 
	
		caller.style.display = "none";		
		div.style.display = "block"; 		
			
		if( !isNaN(caller.value)) {	
			if( caller.value == "" ) {				
				delete ranks_by_level[arr[2]][arr[0]];					
			}
			else {
				ranks_by_level[arr[2]][arr[0]] = parseInt(caller.value);				
			}	
			SkillsPanel_Calculate_Total_Ranks(arr[0], arr[2]);	
			SkillsPanel_Training_Update_Row(arr[0], arr[2]);		
		}					
		SkillsPanel_Calculate_Training_Costs(parseInt(arr[2]));		
		SkillsPanel_Calculate_Remaining_TP(parseInt(arr[2]));
		SkillsPanel_Calculate_Redux_Points(parseInt(arr[2]));
		
		if( arr[0] == "Harness Power" || arr[0] == "Physical Fitness" ) {
			StatisticsPanel_Calculate_Resources();
		}
	}	
	
	function SkillsPanel_Training_Input_Onkeyup(e, caller) {
		var num;
		var arr = caller.id.split("_"); 
		//var sub = 0;
		//var skillname = arr[0];
		//var i = skills.indexOf(skillname)+1;
		var nextskill;
		
		switch(e.which) {
			case 13:	// enter key	
						caller.blur();
						break;		
			case 27:    // escape key
						if ( arr[1] == "input" ) {
							caller.value = ranks_by_level[arr[2]][arr[0]];
						}
						caller.blur();
						break;
						
			case 40:	// down arrow
						for( var i=all_skills.indexOf(arr[0])+1; i < all_skills.length; i++ ) {
							nextskill = all_skills[i];
							if( document.getElementById(nextskill+"_info_row").style.display != "none" ) {	
								document.getElementById(nextskill + "_" + arr[1]).click();
								break;
							}
						}					
						break;
						
			case 38:    // up arrow
						for( var i=all_skills.indexOf(arr[0])-1; i > 0; i-- ) {
							nextskill = all_skills[i];
							if( document.getElementById(nextskill+"_info_row").style.display != "none" ) {	
								document.getElementById(nextskill + "_" + arr[1]).click();
								break;
							}
						}					
						break;
						
			case 37:    // left arrow
						num = parseInt(arr[2]) - 1;
						if (num >= 0) {
							document.getElementById(arr[0] +  "_" + arr[1] + "_" + num).click();
						}
						else if( num < 0 ) {
							document.getElementById(arr[0] +  "_rate").focus();							
						}
						break;

			case 39:    // right arrow
						num = parseInt(arr[2]) + 1;
						if (num <= 100) {
							box = document.getElementById(arr[0] +  "_" + arr[1] + "_" + num).click();
						}
						else if( arr[1] == "train" ) {
							document.getElementById(arr[0] +  "_ranks_0").click();							
						}
						break;	
		}				
	}		
	
	function SkillsPanel_Rate_Input_Onblur(caller) {
		var prof = document.getElementById("StP_selected_profession").value;
		var skillname = caller.id.split("_")[0].split(",")[0];
		
		var max_rpl = parseInt(profession_skill_costs[prof][skillname].split("/")[2]);
		var val = caller.value;
		var len = val.length;
		var t_lvl = 100;
		
		if( isNaN(val)) {	
			if ( val.search(/^[1-3][x|X]$/) != -1 ||      //1x
			 val.search(/^\.[1-9][x|X]$/) != -1 ||            //.5x
			 val.search(/^\.[1-9][0-9][x|X]$/) != -1 ||          //.25x
			 val.search(/^[1-2]\.[0-9][1-9][x|X]$/) != -1 ||        //2.04x
			 val.search(/^[1-3]\.0?[x|X]$/) != -1 ||        //3.0x
			 val.search(/^[0-2]\.[1-9][0-9]?[x|X]$/) != -1	) {   		  //0.10x
				 training_rate[caller.id.split("_")[0]] = val;
			}
			else {	
				caller.value = training_rate[caller.id.split("_")[0]] || "";
			}
		}
		else if( parseInt(val) <= (max_rpl * (t_lvl+1)) && parseInt(val) != 0 ) {	
			 training_rate[caller.id.split("_")[0]] = Math.floor(parseInt(val));		
			 caller.value = Math.floor(parseInt(val));
		}
		else if( val == "" || val == 0) {
			delete training_rate[caller.id.split("_")[0]];
			caller.value = training_rate[caller.id.split("_")[0]] || "";	
		}
		else {	
			caller.value = training_rate[caller.id.split("_")[0]] || "";		
		}		
	}
	
	function SkillsPanel_Autofill_Training() {
		var ok = confirm("WARNING! This will override your existing training plan. Click Yes to continue or No to cancel.");
		var t_lvl = 100;
		var val, adj, wtrain, ptrain;
		var max, cur;
		
		if ( !ok ) { return; }
		
		for( var i=0; i < all_skills.length; i++ ) {		
			key = all_skills[i];
			
			if( training_rate[key] == undefined ) {
				for( var j=0; j <= 100; j++ ) {		
					delete ranks_by_level[j][key];
				}
				SkillsPanel_Calculate_Total_Ranks(key, 0);	
			}		
			else if( isNaN(training_rate[key]) ) {
				val = training_rate[key].substr(0,training_rate[key].length-1);
				ptrain = parseInt(val.split(".")[1]) || 0;
			    wtrain = parseFloat(val);
				cur = 0;
				adj = 0;				
		
				for( var j=0; j <= t_lvl; j++ ) {	
					max = wtrain * (j + 1); 					
					if ( (j+1) % 3 == 0 && ptrain == 33) {           //dang: 1/3 + 1/3 + 1/3 = 1; .33 + .33 + .33 != 1
						max = Math.ceil(max);
					}
					else {
						max = Math.floor(max);
					}
					
					adj = max - cur;
					cur = max;					
					if( adj > 0 ) {
						ranks_by_level[j][key] = adj;
					}
					else {
						delete ranks_by_level[j][key];
					}
					
					SkillsPanel_Calculate_Total_Ranks(key, j);	
				}			
			}
			else {						
				max = training_rate[key];
				cur = 0;	
				adj = 0;
				
				for( var j=0; j <= t_lvl; j++ ) {		
					if ( max == undefined || max-cur <= 0) {
						delete ranks_by_level[j][key];
						SkillsPanel_Calculate_Total_Ranks(key, j);	
						continue;
					}
					else if( max >= (t_lvl+1)*2 ) {
						if( (max - (t_lvl+1)*2) >= (j+1) ) {
							adj = 3;
						}
						else {
							adj = 2;						
						}				
					}
					else if( max >= (t_lvl+1) ) {
						if( (max - (t_lvl+1)) >= (j+1) ) {		
							adj = 2;								
						}
						else {			
							adj = 1;								
						}										
					}
					else {								
						adj = 1;
					}									
					
					ranks_by_level[j][key] = adj;
					cur += adj;		
					SkillsPanel_Calculate_Total_Ranks(key, j);										
				}				
			}		
			SkillsPanel_Training_Update_Row(key, 0);			
		}
				
		for( var i=0; i <= 100; i++ ) {
			SkillsPanel_Calculate_Training_Costs(i);			
		}
		
		SkillsPanel_Calculate_Remaining_TP(0);
		SkillsPanel_Calculate_Redux_Points(0);
		StatisticsPanel_Calculate_Resources();
	}				
		
	function SkillsPanel_Change_Displayed_Skills() {
		var prof = document.getElementById("StP_selected_profession").value;
		
		for( var i=0; i < all_skills.length; i++ ) {
			if( document.getElementById("SkP_hide_skills").checked && !document.getElementById(all_skills[i]+"_checkbox").checked &&        
			total_ranks_by_level[100][all_skills[i]] == undefined && training_rate[all_skills[i]] == undefined ) {    
				document.getElementById(all_skills[i]+"_info_row").style.display = "none";
				document.getElementById(all_skills[i]+"_training_row").style.display = "none";
			}
			else if( all_skills[i].indexOf("Spell Research") != -1 && !SkillsPanel_Prof_Has_Spell_Circle(prof, all_skills[i].split(", ")[1]) ) {
				document.getElementById(all_skills[i]+"_info_row").style.display = "none";
				document.getElementById(all_skills[i]+"_training_row").style.display = "none";				
			}
			else {
				document.getElementById(all_skills[i]+"_info_row").style.display = "";
				document.getElementById(all_skills[i]+"_training_row").style.display = "";					
			}
		}
	}		
			
	function SkillsPanel_Training_Change_Style(start_level=0) {
		for( var i=0; i < all_skills.length; i++ ) {
			SkillsPanel_Training_Update_Row(all_skills[i], 0);				
		}
	}
	
	function SkillsPanel_Training_Update_Row(skill, start_level) {		
		var div, tranks, tbonus, lranks;
		
		for (var k=start_level; k <= 100; k++) {	
			div = document.getElementById(skill + "_div_" + k);
			lranks = ranks_by_level[k][skill] || 0;
			tranks = total_ranks_by_level[k][skill] || 0;
			tbonus = total_bonus_by_level[k][skill] || 0;
			
			if( document.getElementById("SkP_show_total_ranks").checked && tranks > 0 ){
				div.innerHTML = tranks;		
			}
			else if( document.getElementById("SkP_show_total_bonus").checked && tbonus > 0 ){
				div.innerHTML = tbonus;
			}
			else if( document.getElementById("SkP_show_level_ranks").checked && lranks > 0 ){
				div.innerHTML = lranks;
			}	
			else if( div.innerHTML != "" ) {
				div.innerHTML = "";	
			}			
		}	
	}

	function SkillsPanel_Prof_Has_Spell_Circle(prof, circle) {
		if( profession_spell_circles[prof].indexOf(circle) != -1 ) {
			return true;
		}
		else {
			return false;
		}		
	}
	
	function SkillsPanel_Get_Skill_Bonus(ranks) {
		var bonus = 0;
		
		bonus += Math.min(ranks*5, 50);
		bonus += Math.min(Math.max(ranks-10,0)*4, 40);
		bonus += Math.min(Math.max(ranks-20,0)*3, 30);
		bonus += Math.min(Math.max(ranks-30,0)*2, 20);
		bonus += Math.max(ranks-40, 0);		

		return bonus;
	}
	
	function SkillsPanel_Set_Skill_Costs(prof) {
		var skill_info;
		for( var i=0; i < all_skills.length; i++ ) {
			skill_info = profession_skill_costs[prof][all_skills[i].split(",")[0]].split("/");
			document.getElementById(all_skills[i] + "_PTP_cost").innerHTML = skill_info[0];
			document.getElementById(all_skills[i] + "_MTP_cost").innerHTML = skill_info[1];
			document.getElementById(all_skills[i] + "_max_ranks").innerHTML = "("+skill_info[2]+")";	
		}		
	}
	
	function SkillsPanel_Calculate_Total_Ranks(skill, start_level) {
		var rtotal = 0;		
		var cur = ranks_by_level[start_level][skill];
		
		if( start_level > 0 && total_ranks_by_level[start_level-1][skill] != undefined ) {
			rtotal = total_ranks_by_level[start_level-1][skill];
		}
		
		for( var i=start_level; i <= 100; i++) {
			if( ranks_by_level[i][skill] != undefined ) {
				rtotal += parseInt(ranks_by_level[i][skill]);			
			}	
			
			if( rtotal != 0 ) {
				total_ranks_by_level[i][skill] = rtotal;
				total_bonus_by_level[i][skill] = SkillsPanel_Get_Skill_Bonus(rtotal);
			}
			else {
				delete total_ranks_by_level[i][skill];
				delete total_bonus_by_level[i][skill];				
			}
		}
	}	
	
	function SkillsPanel_Calculate_Training_Costs(level=0) {
		var prof = document.getElementById("StP_selected_profession").value;
		var total_PTP=0, total_MTP=0, PTP_cost, MTP_cost;
		
		for( var key in ranks_by_level[level] ) {
			rate = parseInt(ranks_by_level[level][key]);
  
			if (rate == 0) {
				continue;  
			}

			PTP_cost = parseInt(profession_skill_costs[prof][key.split(",")[0]].split("/")[0]);
			MTP_cost = parseInt(profession_skill_costs[prof][key.split(",")[0]].split("/")[1]);
  
			for( var i=1; i < rate; i++ ) {
				PTP_cost += PTP_cost * 2;
				MTP_cost += MTP_cost * 2;	  	
			}
		
			total_PTP += PTP_cost;
			total_MTP += MTP_cost;	  
		}	

		document.getElementById("PTP_used_"+level).innerHTML = total_PTP;		
		document.getElementById("MTP_used_"+level).innerHTML = total_MTP;		
	}

	function SkillsPanel_Calculate_Remaining_TP(start_level) {
		var PTP, MTP, PTP_cost, MTP_cost, PTP_prev=0, MTP_prev=0;
		var convertedPTP=0, convertedMTP=0;
	
		for( var i=start_level; i <= 100; i++ ) {
			if( i > 0 ) {
				PTP_prev = parseInt(document.getElementById("PTP_left_"+(i-1)).innerHTML);
				MTP_prev = parseInt(document.getElementById("MTP_left_"+(i-1)).innerHTML);	
			}
			
			PTP = parseInt(document.getElementById("StP_PTP_"+i).innerHTML);
			MTP = parseInt(document.getElementById("StP_MTP_"+i).innerHTML);
			PTP_cost = parseInt(document.getElementById("PTP_used_"+i).innerHTML);
			MTP_cost = parseInt(document.getElementById("MTP_used_"+i).innerHTML);
			
			PTP_prev = PTP + PTP_prev - PTP_cost;
			MTP_prev = MTP + MTP_prev - MTP_cost;					
						
			while( convertedPTP > 0 && MTP_prev > 0 ) {    //convert MTP back into PTP
				MTP_prev -= 1;
				PTP_prev += 2;
				convertedPTP -= 2;
			}
			
			while( convertedMTP > 0 && PTP_prev > 0 ) {    //convert PTP back into MTP
				PTP_prev -= 1;
				MTP_prev += 2;
				convertedMTP -= 2;
			}
			
			while( PTP_prev < 0 && MTP_prev > 1 ) {  //convert MTP to PTP
					PTP_prev += 1;
					MTP_prev -= 2;
					convertedMTP += 2;
			}
			
			while( MTP_prev < 0 && PTP_prev > 1 ) {  //convert PTP to MTP
					MTP_prev += 1;
					PTP_prev -= 2;
					convertedPTP += 2;
			}	
		
			document.getElementById("PTP_left_"+i).innerHTML = PTP_prev;
			document.getElementById("MTP_left_"+i).innerHTML = MTP_prev;	
		}		
	}
		
	function SkillsPanel_Calculate_Redux_Points(start_level) {
		var prev_redux = 0, redux = 0;
		
		if( start_level > 0 ) {
			prev_redux = parseFloat(document.getElementById("redux_pts_"+(start_level-1)).innerHTML);			
		}
		
		redux += prev_redux;
		for( var i=start_level; i <= 100; i++ ) {
			for( var key in ranks_by_level[i] ) {
				rate = parseInt(ranks_by_level[i][key]);
				redux += skill_redux[key.split(",")[0]] * rate;  		
			}
			document.getElementById("redux_pts_"+i).innerHTML = redux.toFixed(1);
		}		
	}
	
	function SkillsPanel_Zero_Out_Skill_Row(skill) {
		delete training_rate[skills];
		document.getElementById(skill+"_checkbox").checked = false;
		document.getElementById(skill+"_rate").value = "";
		
		for( var i = 0; i <= 100; i++ ) {
			delete ranks_by_level[i][skill];
			delete total_ranks_by_level[i][skill];
			delete total_bonus_by_level[i][skill];
		}
		
		SkillsPanel_Training_Update_Row(skill, 0);
	}
	
	function SkillsPanel_On_Prof_Change(prof) {	
		SkillsPanel_Set_Skill_Costs(prof);
		
		for( var i=0; i < subskills["Spell Research"].length; i++ ) {			
			if( !SkillsPanel_Prof_Has_Spell_Circle(prof, subskills["Spell Research"][i]) ) {
				SkillsPanel_Zero_Out_Skill_Row("Spell Research, "+subskills["Spell Research"][i]);
			}
		}
		
		for( var i=0; i < 100; i++) {
			SkillsPanel_Calculate_Training_Costs(i);	
		}
		SkillsPanel_Change_Displayed_Skills();	
		SkillsPanel_Calculate_Remaining_TP(0);
		SkillsPanel_Calculate_Redux_Points(0);
	}
