	var statistics = [ "strength", "constitution", "dexterity", "agility", "discipline", "aura", "logic", "intuition", "wisdom", "influence" ];
   
   //PROFESSION INFORMATION
   //profession growth
    var bard_growth =     { "strength": 25, "constitution": 20, "dexterity": 25, "agility": 20, "discipline": 15, "aura": 25, "logic": 10, "intuition": 15, "wisdom": 20, "influence": 30 };
    var cleric_growth =   { "strength": 20, "constitution": 20, "dexterity": 10, "agility": 15, "discipline": 25, "aura": 15, "logic": 25, "intuition": 25, "wisdom": 30, "influence": 20 };
    var empath_growth =   { "strength": 10, "constitution": 20, "dexterity": 15, "agility": 15, "discipline": 25, "aura": 20, "logic": 25, "intuition": 20, "wisdom": 30, "influence": 25 };
    var monk_growth =     { "strength": 25, "constitution": 25, "dexterity": 20, "agility": 30, "discipline": 25, "aura": 15, "logic": 20, "intuition": 20, "wisdom": 15, "influence": 10 };
    var paladin_growth =  { "strength": 30, "constitution": 25, "dexterity": 20, "agility": 20, "discipline": 25, "aura": 15, "logic": 10, "intuition": 15, "wisdom": 25, "influence": 20 };
    var ranger_growth =   { "strength": 25, "constitution": 20, "dexterity": 30, "agility": 20, "discipline": 20, "aura": 15, "logic": 15, "intuition": 15, "wisdom": 25, "influence": 10 };
    var rogue_growth =    { "strength": 25, "constitution": 20, "dexterity": 25, "agility": 30, "discipline": 20, "aura": 15, "logic": 20, "intuition": 25, "wisdom": 10, "influence": 15 };
    var sorcerer_growth = { "strength": 10, "constitution": 15, "dexterity": 20, "agility": 15, "discipline": 25, "aura": 30, "logic": 25, "intuition": 20, "wisdom": 25, "influence": 20 };
    var warrior_growth =  { "strength": 30, "constitution": 25, "dexterity": 25, "agility": 25, "discipline": 20, "aura": 15, "logic": 10, "intuition": 20, "wisdom": 15, "influence": 20 };
    var wizard_growth =   { "strength": 10, "constitution": 15, "dexterity": 25, "agility": 15, "discipline": 20, "aura": 30, "logic": 25, "intuition": 25, "wisdom": 20, "influence": 20 };
    var profession_growth = { "bard": bard_growth, "cleric": cleric_growth, "empath": empath_growth, "monk": monk_growth, "paladin": paladin_growth, "ranger": ranger_growth, "rogue": rogue_growth, "sorcerer": sorcerer_growth, "warrior": warrior_growth, "wizard": wizard_growth };
 
	//profession prime requisites
    var bard_prime_req =     [ "influence", "aura" ];
    var cleric_prime_req =   [ "wisdom", "intuition" ];
    var empath_prime_req =   [ "wisdom", "influence" ];
    var monk_prime_req =     [ "agility", "strength" ];
    var paladin_prime_req =  [ "wisdom", "strength" ];
    var ranger_prime_req =   [ "dexterity", "intuition" ];
    var rogue_prime_req =    [ "dexterity", "agility" ];
    var sorcerer_prime_req = [ "aura", "wisdom" ];
    var warrior_prime_req =  [ "constitution", "strength" ];
    var wizard_prime_req =   [ "aura", "logic"];	
    var profession_prime_req = { "bard": bard_prime_req, "cleric": cleric_prime_req, "empath": empath_prime_req, "monk": monk_prime_req, "paladin": paladin_prime_req, "ranger": ranger_prime_req, "rogue": rogue_prime_req, "sorcerer": sorcerer_prime_req, "warrior": warrior_prime_req, "wizard": wizard_prime_req };	
 
	//profession mana statistics
    var bard_mana =     [ "influence", "aura" ];
    var cleric_mana =   [ "wisdom", "wisdom" ];
    var empath_mana =   [ "wisdom", "influence" ];
    var monk_mana =     [ "wisdom", "logic" ];
    var paladin_mana =  [ "wisdom", "wisdom" ];
    var ranger_mana =   [ "wisdom", "wisdom" ];
    var rogue_mana =    [ "aura", "wisdom" ];
    var sorcerer_mana = [ "aura", "wisdom" ];
    var warrior_mana =  [ "aura", "wisdom" ];
    var wizard_mana =   [ "aura", "aura"];	
    var profession_mana = { "bard": bard_mana, "cleric": cleric_mana, "empath": empath_mana, "monk": monk_mana, "paladin": paladin_mana, "ranger": ranger_mana, "rogue": rogue_mana, "sorcerer": sorcerer_mana, "warrior": warrior_mana, "wizard": wizard_mana };		 
 
   //RACE INFORMATION 
   //race growth
    var aelotoi_growth =       { "strength": 0, "constitution": -2, "dexterity": 3, "agility": 3, "discipline": 2, "aura": 0, "logic": 0, "intuition": 2, "wisdom": 0, "influence": 3 };
    var burghal_gnome_growth = { "strength": -5, "constitution": 0, "dexterity": 3, "agility": 3, "discipline": -3, "aura": -2, "logic": 5, "intuition": 5, "wisdom": 0, "influence": 0 };
    var dark_elf_growth =      { "strength": 0, "constitution": -2, "dexterity": 5, "agility": 5, "discipline": -2, "aura": 0, "logic": 0, "intuition": 0, "wisdom": 0, "influence": 0 };
    var dwarf_growth =         { "strength": 5, "constitution": 5, "dexterity": -3, "agility": -5, "discipline": 3, "aura": 0, "logic": 0, "intuition": 0, "wisdom": 3, "influence": -2 };
    var elf_growth =           { "strength": 0, "constitution": -5, "dexterity": 5, "agility": 3, "discipline": -5, "aura": 5, "logic": 0, "intuition": 0, "wisdom": 0, "influence": 3 };
    var erithian_growth =      { "strength": -2, "constitution": 0, "dexterity": 0, "agility": 0, "discipline": 3, "aura": 0, "logic": 2, "intuition": 0, "wisdom": 0, "influence": 3 };
    var forest_gnome_growth =  { "strength": -3, "constitution": 2, "dexterity": 2, "agility": 3, "discipline": 2, "aura": 0, "logic": 0, "intuition": 0, "wisdom": 0, "influence": 0 };
    var giantman_growth =      { "strength": 5, "constitution": 3, "dexterity": -2, "agility": -2, "discipline": 0, "aura": 0, "logic": 0, "intuition": 2, "wisdom": 0, "influence": 0 };
    var half_krolvin_growth =  { "strength": 3, "constitution": 5, "dexterity": 2, "agility": 2, "discipline": 0, "aura": -2, "logic": -2, "intuition": 0, "wisdom": 0, "influence": -2 };
    var half_elf_growth =      { "strength": 2, "constitution": 0, "dexterity": 2, "agility": 2, "discipline": -2, "aura": 0, "logic": 0, "intuition": 0, "wisdom": 0, "influence": 0 };
    var halfling_growth =      { "strength": -5, "constitution": 5, "dexterity": 5, "agility": 5, "discipline": -2, "aura": 0, "logic": -2, "intuition": 0, "wisdom": 0, "influence": 0 };
    var human_growth =         { "strength": 2, "constitution": 2, "dexterity": 0, "agility": 0, "discipline": 0, "aura": 0, "logic": 0, "intuition": 2, "wisdom": 0, "influence": 0 };
    var sylvankind_growth =    { "strength": -3, "constitution": -2, "dexterity": 5, "agility": 5, "discipline": -5, "aura": 3, "logic": 0, "intuition": 0, "wisdom": 0, "influence": 3 };
    var race_growth = { "aelotoi": aelotoi_growth, "burghal_gnome": burghal_gnome_growth, "dark_elf": dark_elf_growth, "dwarf": dwarf_growth, "elf": elf_growth, "erithian": erithian_growth, "forest_gnome": forest_gnome_growth, "giantman": giantman_growth, "half_krolvin": half_krolvin_growth, "half_elf": half_elf_growth, "halfling": halfling_growth, "human": human_growth, "sylvankind": sylvankind_growth };
   
   //race bonus  
    var aelotoi_bonus =       { "strength": -5, "constitution": 0, "dexterity": 5, "agility": 10, "discipline": 5, "aura": 0, "logic": 5, "intuition": 5, "wisdom": 0, "influence": 0 };
    var burghal_gnome_bonus = { "strength": -15, "constitution": 10, "dexterity": 10, "agility": 10, "discipline": -5, "aura": 5, "logic": 10, "intuition": 5, "wisdom": 0, "influence": -5 };
    var dark_elf_bonus =      { "strength": 0, "constitution": -5, "dexterity": 10, "agility": 5, "discipline": -10, "aura": 10, "logic": 0, "intuition": 5, "wisdom": 5, "influence": -5 };  
    var dwarf_bonus =         { "strength": 10, "constitution": 15, "dexterity": 0, "agility": -5, "discipline": 10, "aura": -10, "logic": 0, "intuition": 0, "wisdom": 0, "influence": -10 };  
    var elf_bonus =           { "strength": 0, "constitution": 0, "dexterity": 5, "agility": 15, "discipline": -15, "aura": 5, "logic": 0, "intuition": 0, "wisdom": 0, "influence": 10 };    
    var erithian_bonus =      { "strength": -5, "constitution": 10, "dexterity": 0, "agility": 0, "discipline": 5, "aura": 0, "logic": 5, "intuition": 0, "wisdom": 0, "influence": 10 }; 
    var forest_gnome_bonus =  { "strength": -10, "constitution": 10, "dexterity": 5, "agility": 10, "discipline": 5, "aura": 0, "logic": 5, "intuition": 0, "wisdom": 5, "influence": -5 };   
    var giantman_bonus =      { "strength": 15, "constitution": 10, "dexterity": -5, "agility": -5, "discipline": 0, "aura": -5, "logic": 0, "intuition": 0, "wisdom": 0, "influence": 5 };    
    var half_krolvin_bonus =  { "strength": 10, "constitution": 10, "dexterity": 0, "agility": 5, "discipline": 0, "aura": 0, "logic": -10, "intuition": 0, "wisdom": -5, "influence": -5 };   
    var half_elf_bonus =      { "strength": 0, "constitution": 0, "dexterity": 5, "agility": 10, "discipline": -5, "aura": 0, "logic": 0, "intuition": 0, "wisdom": 0, "influence": 5 };  
    var  halfling_bonus =      { "strength": -15, "constitution": 10, "dexterity": 15, "agility": 10, "discipline": -5, "aura": -5, "logic": 5, "intuition": 10, "wisdom": 0, "influence": -5 }; 
    var human_bonus =         { "strength": 5, "constitution": 0, "dexterity": 0, "agility": 0, "discipline": 0, "aura": 0, "logic": 5, "intuition": 5, "wisdom": 0, "influence": 0 };   
    var sylvankind_bonus =    { "strength": 0, "constitution": 0, "dexterity": 10, "agility": 5, "discipline": -5, "aura": 5, "logic": 0, "intuition": 0, "wisdom": 0, "influence": 0 };  
    var race_bonus = { "aelotoi": aelotoi_bonus, "burghal_gnome": burghal_gnome_bonus, "dark_elf": dark_elf_bonus, "dwarf": dwarf_bonus, "elf": elf_bonus, "erithian": erithian_bonus, "forest_gnome": forest_gnome_bonus, "giantman": giantman_bonus, "half_krolvin": half_krolvin_bonus, "half_elf": half_elf_bonus, "halfling": halfling_bonus, "human": human_bonus, "sylvankind": sylvankind_bonus };   
   
   //race max health
    var race_max_health = { "aelotoi": 120, "burghal_gnome": 90, "dark_elf": 120, "dwarf": 140, "elf": 130, "erithian": 120, "forest_gnome": 100, "giantman": 200, "half_krolvin": 165, "half_elf": 135, "halfling": 100, "human": 150, "sylvankind": 130 };   

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

	var stat_total_by_level = [];
	var PTP_by_level = [];
	var MTP_by_level = [];
	var health_by_level = [];
	var mana_by_level = [];
	var stamina_by_level = [];
	var spirit_by_level = [];
	
	

	function StatisticsPanel_Init() {
	//	var stat_div = document.getElementById("StP_left_side");
		var growth_div = document.getElementById("StP_growth_container");
	//	var stat_tbl = document.createElement('table');
		var stat_tbl = document.getElementById("StP_left_side");
		var growth_tbl = document.createElement('table');
		var stat_tbdy = document.createElement('tbody');
		var growth_tbdy = document.createElement('tbody');
		
		var tr = document.createElement('tr');
		var td = document.createElement('td');
		var col;
		var level, title;

		growth_tbl.width = "4545px";
/*		
		for( var i=0; i <= 100; i++ ) {
			col = document.createElement('colgroup');
			col.style.width = "43px";
			growth_tbl.appendChild(col);			
		}
*/
		
		col = document.createElement('col');
		col.style.width = "";
		stat_tbl.appendChild(col);
		col = document.createElement('col');
		col.style.width = "25%";
		stat_tbl.appendChild(col);
		col = document.createElement('col');
		col.style.width = "25%";
		stat_tbl.appendChild(col);
		col = document.createElement('col');
		col.style.width = "1%";
		stat_tbl.appendChild(col);
		
		
		//Create Left Statistics Titles
		tr = document.createElement('tr');
		tr.style.fontWeight="bold";
		td = document.createElement('td');
		td.height = "26";
		title = document.createElement('div');
		title.style.fontWeight="bold";
		title.style.textAlign="center";	
		title.innerHTML = "Statistic";			
		td.appendChild(title); 		
		tr.appendChild(td);    
							
		td=document.createElement('td');
		title = document.createElement('div');
		title.style.textAlign="center";	
		title.innerHTML = "Race Bonus";			
		td.appendChild(title); 		
		tr.appendChild(td);    
							
		td=document.createElement('td');
		title = document.createElement('div');
		title.style.textAlign="center";	
		title.innerHTML = "Growth Index";			
		td.appendChild(title); 		
		tr.appendChild(td);    
							
		td=document.createElement('td');
		title = document.createElement('div');
		title.style.textAlign="center";	
		title.innerHTML = "Base";			
		td.appendChild(title); 		
		tr.appendChild(td);    		
		
		stat_tbdy.appendChild(tr);		
		
		
		//Statistics left side Stats
		stat_tbdy.appendChild(StatisticsPanel_Create_Statistics_Row("Strength"));
		stat_tbdy.appendChild(StatisticsPanel_Create_Statistics_Row("Constitution"));
		stat_tbdy.appendChild(StatisticsPanel_Create_Statistics_Row("Dexterity"));
		stat_tbdy.appendChild(StatisticsPanel_Create_Statistics_Row("Agility"));
		stat_tbdy.appendChild(StatisticsPanel_Create_Statistics_Row("Discipline"));
		stat_tbdy.appendChild(StatisticsPanel_Create_Statistics_Row("Aura"));
		stat_tbdy.appendChild(StatisticsPanel_Create_Statistics_Row("Logic"));
		stat_tbdy.appendChild(StatisticsPanel_Create_Statistics_Row("Intuition"));
		stat_tbdy.appendChild(StatisticsPanel_Create_Statistics_Row("Wisdom"));
		stat_tbdy.appendChild(StatisticsPanel_Create_Statistics_Row("Influence"));
		
		//blank row
		tr = document.createElement('tr');
		td = document.createElement('td');
		td.height="14";
		tr.appendChild(td);
		stat_tbdy.appendChild(tr); 
		
		//
		stat_tbdy.appendChild(StatisticsPanel_Create_Label_Row("Total", "total", "black", "lightgray"));
		stat_tbdy.appendChild(StatisticsPanel_Create_Label_Row("PTP", "PTP", "black", "lightgray"));
		stat_tbdy.appendChild(StatisticsPanel_Create_Label_Row("MTP", "MTP", "black", "lightgray"));
		
		//blank row
		tr = document.createElement('tr');
		td = document.createElement('td');
		td.height="14";
		tr.appendChild(td);
		stat_tbdy.appendChild(tr); 
		
		//Statistics left side 
		stat_tbdy.appendChild(StatisticsPanel_Create_Label_Row("Health", "health", "white", "red"));
		stat_tbdy.appendChild(StatisticsPanel_Create_Label_Row("Mana", "mana", "white", "blue"));
		stat_tbdy.appendChild(StatisticsPanel_Create_Label_Row("Stamina", "stamina", "black", "yellow"));
		stat_tbdy.appendChild(StatisticsPanel_Create_Label_Row("Spirit", "spirit", "black", "lightgray"));
		
		
		//Create Right Statistic Panel
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
	//		level.style.width = "31";
			level.innerHTML = j;	
			td.appendChild(level);			
			tr.appendChild(td);    
		}    
		growth_tbdy.appendChild(tr);
	
		//All 10 Statistic Rows			
		for (var i=0; i < statistics.length; i++) {
			growth_tbdy.appendChild(StatisticsPanel_Create_Growth_Row("StP_"+statistics[i]+"_growth", "23", "lightgray", "black"));		
		}

		//blank row
		tr = document.createElement('tr');
		td = document.createElement('td');
		td.height="14";
		tr.appendChild(td);
		growth_tbdy.appendChild(tr);
		
		//Statistics Total, PTP, MTP
		growth_tbdy.appendChild(StatisticsPanel_Create_Growth_Row("StP_growth_total", "23", "lightgray", "black"));			
		growth_tbdy.appendChild(StatisticsPanel_Create_Growth_Row("StP_PTP", "23", "lightgray", "black"));		
		growth_tbdy.appendChild(StatisticsPanel_Create_Growth_Row("StP_MTP", "23", "lightgray", "black"));		

		//blank row
		tr = document.createElement('tr');
		td = document.createElement('td');
		td.height="14";
		tr.appendChild(td);
		growth_tbdy.appendChild(tr);
		
		//health, mana, stamina, spirit
		growth_tbdy.appendChild(StatisticsPanel_Create_Growth_Row("StP_health", "23", "red", "white"));
		growth_tbdy.appendChild(StatisticsPanel_Create_Growth_Row("StP_mana", "23", "blue", "white"));
		growth_tbdy.appendChild(StatisticsPanel_Create_Growth_Row("StP_stamina", "23", "yellow"));
		growth_tbdy.appendChild(StatisticsPanel_Create_Growth_Row("StP_spirit", "23", "lightgray"));		
		
		//append table to div
		growth_tbl.appendChild(growth_tbdy);
		growth_div.appendChild(growth_tbl);	 	
		
		stat_tbl.appendChild(stat_tbdy);	
	  
	  	  
		//Initialize values		
		StatisticsPanel_Refresh_All();
	}
		
	function StatisticsPanel_Create_Statistics_Row(id) {
		var tr = document.createElement('tr');
		var td;
		
		tr.style.backgroundColor = "lightgray";
				
		td = document.createElement('td');
		td.appendChild(document.createTextNode(id));  
		tr.appendChild(td);    
		
		id = id.toLowerCase();
		
		td = document.createElement('td');		
		td.height = "23";
		td.id = "StP_race_bonus_" + id;
		td.style.textAlign = "center";
		tr.appendChild(td);    
		
		td = document.createElement('td');
		td.id = "StP_GI_" + id;
		td.style.textAlign = "center";
		tr.appendChild(td);    
		
		
		td = document.createElement('td');
		input = document.createElement('input');
		input.id = "StP_base_" + id;	
		input.name = id;
		input.type = "text";
		input.size = 3;
		input.style.textAlign = "center";
		input.maxLength = "3";
		input.onblur = function() {  StatisticsPanel_Base_StatBox_Onblur(this) };	
		input.onkeyup = function(event) {  StatisticsPanel_Statbox_Onkeyup(event, this); };	
		td.appendChild(input);
		td.id = "StP_base_" + id + "_cell";
		td.style.textAlign = "center";
		tr.appendChild(td);  							
		
		return tr;		
		
	}
	
	function StatisticsPanel_Create_Label_Row(title, id, textcolor, bgcolor) {
		var tr = document.createElement('tr');
		var td;
		
				
		td = document.createElement('td');
		td.height = "23";
		td.colSpan = "3";
		td.style.fontWeight="bold";
		td.style.textAlign = "right";
		td.innerHTML = title;		
		tr.appendChild(td);    
			
		td = document.createElement('td');
		td.style.backgroundColor = bgcolor;
		td.id = "StP_base_" + id;	
		td.style.textAlign = "center";
		td.style.color = textcolor;
		tr.appendChild(td);  

		return tr;
		
	}
	
	function StatisticsPanel_Create_Growth_Row(id, height, bgcolor, fontcolor) {
		var tr = document.createElement('tr');
		var td;
		
		for(var j=0; j<=100; j++) {
			td = document.createElement('td');
			td.id = id + "_" + j;
			td.height = height;
			td.style.backgroundColor = bgcolor;
			td.style.color = fontcolor;
			td.style.textAlign = "center";			
			td.appendChild(document.createTextNode("0"));  
			tr.appendChild(td);    
		}  		
	
		return tr;
	}
 
	function StatisticsPanel_Refresh_All() {
		StatisticsPanel_Set_Statbox_Defaults_Colors();
		StatisticsPanel_Display_Stat_Extras();					
		StatisticsPanel_Calculate_Growth_All();
		StatisticsPanel_Calculate_Resources();		
	}
 	
	function StatisticsPanel_Display_Stat_Extras() {
		var prof = document.getElementById("StP_selected_profession").value;
		var race = document.getElementById("StP_selected_race").value;		
		for (var i=0; i < statistics.length; i++) {		
			document.getElementById("StP_race_bonus_"+statistics[i]).innerHTML = race_bonus[race][statistics[i]];
			document.getElementById("StP_GI_"+statistics[i]).innerHTML = profession_growth[prof][statistics[i]] + race_growth[race][statistics[i]];
		}	
	}
	
    function StatisticsPanel_Base_StatBox_Onblur(caller) {
	    if (isNaN(caller.value)) {
			caller.value = "";
		}
		else if (caller.value > 100) {
			caller.value = 100;
		}
		
		StatisticsPanel_Calculate_Growth(caller);
		StatisticsPanel_Calculate_Resources();		
		SkillsPanel_Calculate_Remaining_TP(0);	
	}
	
	//set prime requisites and mana colors and default values if the cell is empty
    function StatisticsPanel_Set_Statbox_Defaults_Colors() {
		var prof = document.getElementById("StP_selected_profession").value;
		var cell, box;
		
		for (var i=0; i < statistics.length; i++) {		
			cell = document.getElementById("StP_base_"+statistics[i]+"_cell");
			box = document.getElementById("StP_base_"+statistics[i]);
			
			if ( profession_prime_req[prof].indexOf(statistics[i]) != -1 && profession_mana[prof].indexOf(statistics[i]) != -1 ) {
				cell.style.backgroundColor = "gold";				
				if (box.value == "" || parseInt(box.value) < 30) {
					box.value = 30;
				}
			}
			else if ( profession_prime_req[prof].indexOf(statistics[i]) != -1 ) {
				cell.style.backgroundColor = "black";
				if (box.value == "" || parseInt(box.value) < 30) {
					box.value = 30;
				}				
			}
			else if ( profession_mana[prof].indexOf(statistics[i]) != -1 ) {
				cell.style.backgroundColor = "blue";	
				if (box.value == "" ) {
					box.value = 20;
				}
			}
			else {
				cell.style.backgroundColor = "white";	
				if (box.value == "" ) {
					box.value = 20;
				}				
			}			
		}
	}	
		
    function StatisticsPanel_Statbox_Onkeyup(e, caller) {				
		var num, box;
		
		switch(e.which) {
			case 13:	// enter key
			case 27:    // escape key
						caller.blur();
						break;
						
			case 40:	// down arrow
						num = statistics.indexOf(caller.id.split("_")[2]) + 1;
						if (num < statistics.length) {
							box = document.getElementById("StP_base_"+statistics[num]);
//							document.getElementById("StP_base_"+statistics[num]).select();
							box.focus();
							box.setSelectionRange(box.value.length * 2, box.value.length * 2);
						}
						break;
						
			case 38:    // up arrow
		              	num = statistics.indexOf(caller.id.split("_")[2]) - 1;
						if (num >= 0) {
							box = document.getElementById("StP_base_"+statistics[num]);
//							document.getElementById("StP_base_"+statistics[num]).select();
							box.focus();
							box.setSelectionRange(box.value.length * 2, box.value.length * 2);
						}
						break;
		
		}		
    }
   
    function StatisticsPanel_Calculate_Growth_All() {  
		for (var i=0; i < statistics.length; i++) {				
			StatisticsPanel_Calculate_Growth(document.getElementById("StP_base_"+statistics[i]));
		}
	}
   
    function StatisticsPanel_Calculate_Growth(caller) {  
		var prof = document.getElementById("StP_selected_profession").value;
		var race = document.getElementById("StP_selected_race").value;		
		var cell, bonus; 		
		var R = profession_growth[prof][caller.name] + race_growth[race][caller.name];
		var S = parseInt(caller.value);		
			if ( isNaN(S) || S < 0 ) {
				S=0;
			}	
		var GI = Math.max(Math.floor(S/R),1);
		var prev_stat = S;
		var prev_bonus = Get_Bonus(S, race_bonus[race][caller.name]);
	  
		for(var i=0; i <= 100; i++) {	 
			if (i > 0 && S < 100 && (i % GI) == 0) {
				S++; 
				GI = Math.max(Math.floor(S/R),1);
			}			
			statistics_by_level[caller.name][i] = S;			
			cell = document.getElementById("StP_"+caller.name+ "_growth_" + i);
			
			if(document.getElementById("StP_show_statistics").checked) {
				cell.innerHTML = S;
				cell.style.color = "black";
				
				if ( prev_stat < S ) {
					prev_stat = S;
					cell.style.backgroundColor="#00FF00";
				}
				else {
					cell.style.backgroundColor="lightgray";				
				}				
			}
			else {
				bonus = Get_Bonus(S, race_bonus[race][caller.name]);
				cell.innerHTML = bonus; 	
				
				if ( bonus < 0) {
					cell.style.color = "red";
				}
				else {
					cell.style.color = "black";				
				}
				
				if (prev_bonus < bonus ) {
					prev_bonus = bonus;
					cell.style.backgroundColor="#00FF00";
				}
				else {
					cell.style.backgroundColor="lightgray";				
				}					
			}			
		}  
    }   
   
    function StatisticsPanel_Calculate_Resources() {
		var prof = document.getElementById("StP_selected_profession").value;
		var race = document.getElementById("StP_selected_race").value;	

		var STR = statistics_by_level["strength"][0];
		var CON = statistics_by_level["constitution"][0];
		var DEX = statistics_by_level["dexterity"][0];
		var AGL = statistics_by_level["agility"][0];
		var DIS = statistics_by_level["discipline"][0];
		var AUR = statistics_by_level["aura"][0];
		var LOG = statistics_by_level["logic"][0];
		var INT = statistics_by_level["intuition"][0];
		var WIS = statistics_by_level["wisdom"][0];
		var INF = statistics_by_level["influence"][0];
		var PTP_sum = 0;
		var MTP_sum = 0;
		var	health, mana, stamina, spirit;
		var PFranks, HPranks, HPmana, bonus1, bonus2, PFbonus;
	
		if (isNaN(STR)) {	STR = 0;	}
		if (isNaN(CON)) {	CON = 0;	}
		if (isNaN(DEX)) {	DEX = 0;	}
		if (isNaN(AGL)) {	AGL = 0;	}
		if (isNaN(DIS)) {	DIS = 0;	}
		if (isNaN(AUR)) {	AUR = 0;	}
		if (isNaN(LOG)) {	LOG = 0;	}
		if (isNaN(INT)) {	INT = 0;	}
		if (isNaN(WIS)) {	WIS = 0;	}
		if (isNaN(INF)) {	INF = 0;	}		
		
		
		for(var i=0; i<=100; i++) {
			total = document.getElementById("StP_growth_total_" + i);
			STR = statistics_by_level["strength"][i];
			CON = statistics_by_level["constitution"][i];
			DEX = statistics_by_level["dexterity"][i];
			AGL = statistics_by_level["agility"][i];
			DIS = statistics_by_level["discipline"][i];
			AUR = statistics_by_level["aura"][i];
			LOG = statistics_by_level["logic"][i];
			INT = statistics_by_level["intuition"][i];
			WIS = statistics_by_level["wisdom"][i];
			INF = statistics_by_level["influence"][i];		
			PTP = document.getElementById("StP_PTP_"+i);
			MTP = document.getElementById("StP_MTP_"+i);
			health = document.getElementById("StP_health_"+i);
			mana = document.getElementById("StP_mana_"+i);
			stamina = document.getElementById("StP_stamina_"+i);
			spirit = document.getElementById("StP_spirit_"+i);
			
			//statistic total
			stat_total_by_level[i] = STR + CON + DEX + AGL + DIS + AUR + LOG + INT + WIS + INF;
			total.innerHTML = stat_total_by_level[i];
			
			//PTP
			PTP_sum = ((AUR * (profession_prime_req[prof].indexOf("aura") != -1 ? 2 : 1)) + (DIS * (profession_prime_req[prof].indexOf("discipline") != -1 ? 2 : 1))) / 2;		
			PTP_sum = ((STR * (profession_prime_req[prof].indexOf("strength") != -1 ? 2 : 1)) + (CON * (profession_prime_req[prof].indexOf("constitution") != -1 ? 2 : 1)) + 
				   (DEX * (profession_prime_req[prof].indexOf("dexterity") != -1 ? 2 : 1)) + (AGL * (profession_prime_req[prof].indexOf("agility") != -1 ? 2 : 1)) + PTP_sum) / 20;	
				   
			if( i == 0 ) { 
				PTP_by_level[i] = (25 + PTP_sum).toFixed(2); 
				PTP.innerHTML = Math.floor(PTP_by_level[i]); 				
			} 
			else { 
				PTP_by_level[i] = Math.floor(25 + PTP_sum); 
				PTP.innerHTML = PTP_by_level[i]; 
				if ( PTP_by_level[i] > PTP_by_level[i-1] ) {				
					PTP.style.backgroundColor="#00FF00";		
				}
				else {		
					PTP.style.backgroundColor="lightgray";							
				}
			}	

			//MTP
			MTP_sum = ((AUR * (profession_prime_req[prof].indexOf("aura") != -1 ? 2 : 1)) + (DIS * (profession_prime_req[prof].indexOf("discipline") != -1 ? 2 : 1))) / 2;		
			MTP_sum = ((LOG * (profession_prime_req[prof].indexOf("logic") != -1 ? 2 : 1)) + (INT * (profession_prime_req[prof].indexOf("intuition") != -1 ? 2 : 1)) + 
		           (WIS * (profession_prime_req[prof].indexOf("wisdom") != -1 ? 2 : 1)) + (INF * (profession_prime_req[prof].indexOf("influence") != -1 ? 2 : 1)) + MTP_sum) / 20;	
				   
			if( i == 0 ) { 
				MTP_by_level[i] = (25 + MTP_sum).toFixed(2); 
				MTP.innerHTML = Math.floor(MTP_by_level[i]); 
			} 
			else { 
				MTP_by_level[i] = Math.floor(25 + MTP_sum); MTP.innerHTML = MTP_by_level[i]; 
				if ( MTP_by_level[i] > MTP_by_level[i-1] ) {				
					MTP.style.backgroundColor="#00FF00";		
				}
				else {		
					MTP.style.backgroundColor="lightgray";							
				}
			}				

			//health
			PFranks = total_ranks_by_level[i]["Physical Fitness"] || 0;
			var Combat_Toughness = (10 * total_man_ranks_by_level[i]["Combat Toughness-combat"] + 5) || 0; 
			health_by_level[i] = Math.min(Math.floor((statistics_by_level["strength"][0] + statistics_by_level["constitution"][0]) / 10) + PFranks*5, race_max_health[race]+Get_Bonus(CON, race_bonus[race]["constitution"])) + Combat_Toughness;
			health.innerHTML = health_by_level[i];			
		
			//mana
			HPranks = total_ranks_by_level[i]["Harness Power"] || 0;			
			HPmana = (HPranks > i) ? i*3 + HPranks-i : HPranks*3;			
			bonus1 = statistics_by_level[profession_mana[prof][0]][0];
			bonus2 = statistics_by_level[profession_mana[prof][1]][0];

			bonus1 = Get_Bonus(bonus1, race_bonus[race][profession_mana[prof][0]]);
			bonus2 = Get_Bonus(bonus2, race_bonus[race][profession_mana[prof][1]]);	
			mana_by_level[i] = Math.max(Math.floor((bonus1 + bonus2) / 4), 0) + HPmana;
			mana.innerHTML = mana_by_level[i];
	
			//stamina
			PFbonus = total_bonus_by_level[i]["Physical Fitness"] || 0;
			stamina.innerHTML = Get_Bonus(CON, race_bonus[race]["constitution"]) +
								Math.floor((Get_Bonus(STR, race_bonus[race]["strength"]) + Get_Bonus(AGL, race_bonus[race]["agility"]) +
								Get_Bonus(DIS, race_bonus[race]["discipline"])) / 3) + 
								Math.floor(PFbonus / 3);
			stamina.innerHTML = Math.max(parseInt(stamina.innerHTML), 0);
			
			stamina_by_level[i] = Math.max(Get_Bonus(CON, race_bonus[race]["constitution"]) +
								Math.floor((Get_Bonus(STR, race_bonus[race]["strength"]) + Get_Bonus(AGL, race_bonus[race]["agility"]) +
								Get_Bonus(DIS, race_bonus[race]["discipline"])) / 3) + 
								Math.floor(PFbonus / 3), 0);
			stamina.innerHTML = stamina_by_level[i];			
			
			//spirit
			spirit_by_level[i] = Math.round(AUR / 10);
			spirit.innerHTML = spirit_by_level[i];
		}
		
			//set the left panel values too
			document.getElementById("StP_base_total").innerHTML = stat_total_by_level[0];
			document.getElementById("StP_base_PTP").innerHTML = PTP_by_level[0];
			document.getElementById("StP_base_MTP").innerHTML = MTP_by_level[0];			
			document.getElementById("StP_base_health").innerHTML = health_by_level[0];
			document.getElementById("StP_base_mana").innerHTML = mana_by_level[0];
			document.getElementById("StP_base_stamina").innerHTML = stamina_by_level[0];	
			document.getElementById("StP_base_spirit").innerHTML = spirit_by_level[0];
		
    }
	
	//Calculates the bonus of statistic including the race modifier
	function Get_Bonus(num, bonus) {  
		return Math.floor((num - 50) / 2) + bonus;
	}	
