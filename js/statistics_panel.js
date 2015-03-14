	function StatisticsPanel_Init() {
		var stat_div = document.getElementById("StP_stat_info_container");
		var growth_div = document.getElementById("StP_growth_container");
		//var stat_tbl = document.getElementById("StP_left_side");
		var stat_tbl = document.createElement('table');
		var growth_tbl = document.createElement('table');
		var stat_tbdy = document.createElement('tbody');
		var growth_tbdy = document.createElement('tbody');		
		var tr, td, col, level, title;
		
		growth_tbl.width = "4545px";
		
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
		stat_div.appendChild(stat_tbl);	 		
	  
	  	  
		StatisticsPanel_Update_Leftside();
		StatisticsPanel_Update_Rightside();	
	}
		
	function StatisticsPanel_Term() {
		var growth_div = document.getElementById("StP_growth_container");
		var stat_div = document.getElementById("StP_stat_info_container");
				
		while (stat_div.firstChild) {
			stat_div.removeChild(stat_div.firstChild);
		}		
		
		while (growth_div.firstChild) {
			growth_div.removeChild(growth_div.firstChild);
		}
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
		input.onblur = function() {  StatisticsPanel_StatBox_Onblur(this) };	
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
	//	StatisticsPanel_Calculate_Growth_All();
	//	StatisticsPanel_Calculate_Resources();		
		StatisticsPanel_Update_Leftside();
		StatisticsPanel_Update_Rightside();	
	}
 	
	function StatisticsPanel_Update_Leftside() {
		var prof = selected_prof;
		var race = selected_race;		
		var cell, box;
				
		document.getElementById("StP_selected_profession").value = selected_prof;
		document.getElementById("StP_selected_race").value = selected_race;		
		
		for (var i=0; i < statistics.length; i++) {		
			cell = document.getElementById("StP_base_"+statistics[i]+"_cell");
		//	box = document.getElementById("StP_base_"+statistics[i]);			
			
			document.getElementById("StP_race_bonus_"+statistics[i]).innerHTML = race_list.GetObjectByName(race).statistic_bonus[statistics[i]];
			document.getElementById("StP_GI_"+statistics[i]).innerHTML = profession_list.GetObjectByName(prof).statistic_growth[statistics[i]] + race_list.GetObjectByName(race).growth_adj[statistics[i]];
			document.getElementById("StP_base_"+statistics[i]).value = statistics_by_level[statistics[i]][0];
			

			if ( profession_list.GetObjectByName(prof).prime_statistics.indexOf(statistics[i]) != -1 && profession_list.GetObjectByName(prof).mana_statistics.indexOf(statistics[i]) != -1 ) {
				cell.style.backgroundColor = "gold";		
			}
			else if ( profession_list.GetObjectByName(prof).prime_statistics.indexOf(statistics[i]) != -1 ) {
				cell.style.backgroundColor = "black";
			}
			else if ( profession_list.GetObjectByName(prof).mana_statistics.indexOf(statistics[i]) != -1 ) {
				cell.style.backgroundColor = "blue";	
			}
			else {
				cell.style.backgroundColor = "white";	
			}			
		}
		
	}
	
	function StatisticsPanel_Update_Rightside() {
		var prev_stat = 0;
		var total, STR, CON, DEX, AGL, DIS, AUR, LOG, INT, WISE, INF, PTP, MTP, health, mana, stamina, spirit;
		
		for(var i=0; i <= 100; i++) {	 
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
			
			for (var j=0; j < statistics.length; j++) {		
				cell = document.getElementById("StP_"+statistics[j]+ "_growth_" + i);
			
				if(document.getElementById("StP_show_statistics").checked) {
					cell.innerHTML = statistics_by_level[statistics[j]][i];
					cell.style.color = "black";
				
					if ( i > 0 && statistics_by_level[statistics[j]][i-1] < statistics_by_level[statistics[j]][i] ) {
					//	prev_stat = statistics_by_level[statistics[j]][i];
						cell.style.backgroundColor="#00FF00";
					}
					else {
						cell.style.backgroundColor="lightgray";				
					}				
				}
				else {
					bonus = StatisticsPanel_Get_Bonus(statistics_by_level[statistics[j]][i], race_list.GetObjectByName(race).statistic_bonus[caller.name]);
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
			
			
				total.innerHTML = stat_total_by_level[i];
				
				if( i == 0 ) { 
					MTP.innerHTML = Math.floor(MTP_by_level[i]); 
					PTP.innerHTML = Math.floor(PTP_by_level[i]); 
				//set the left panel values too
					document.getElementById("StP_base_total").innerHTML = stat_total_by_level[0];
					document.getElementById("StP_base_PTP").innerHTML = PTP_by_level[0];
					document.getElementById("StP_base_MTP").innerHTML = MTP_by_level[0];			
					document.getElementById("StP_base_health").innerHTML = health_by_level[0];
					document.getElementById("StP_base_mana").innerHTML = mana_by_level[0];
					document.getElementById("StP_base_stamina").innerHTML = stamina_by_level[0];	
					document.getElementById("StP_base_spirit").innerHTML = spirit_by_level[0];
				} 
				else { 
					PTP.innerHTML = PTP_by_level[i]; 
					MTP.innerHTML = MTP_by_level[i]; 
					if ( MTP_by_level[i] > MTP_by_level[i-1] ) {				
						MTP.style.backgroundColor="#00FF00";		
					}
					else {		
						MTP.style.backgroundColor="lightgray";							
					}
					
					if ( PTP_by_level[i] > PTP_by_level[i-1] ) {				
						PTP.style.backgroundColor="#00FF00";		
					}
					else {		
						PTP.style.backgroundColor="lightgray";							
					}
				}					
								
				health.innerHTML = health_by_level[i];			
				mana.innerHTML = mana_by_level[i];
	//			stamina.innerHTML = Math.max(parseInt(stamina.innerHTML), 0);
				stamina.innerHTML = stamina_by_level[i];			
				spirit.innerHTML = spirit_by_level[i];
		}  		
		
	}
	
    function StatisticsPanel_StatBox_Onblur(caller) {
	    if (isNaN(caller.value)) {
			caller.value = "";
		}
		else if (caller.value > 100) {
			caller.value = 100;
		}
		
		if( statistics_by_level[caller.name][0] != parseInt(caller.value) ) {
			statistics_by_level[caller.name][0] = parseInt(caller.value);
		
			StatisticsPanel_Calculate_Growth(caller.name);
			StatisticsPanel_Calculate_Resources();		
			StatisticsPanel_Update_Rightside()
			//SkillsPanel_Calculate_Remaining_TP(0);	
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
			StatisticsPanel_Calculate_Growth(statistics[i]);
		}
	}
   
    function StatisticsPanel_Calculate_Growth(stat) {  
		var prof = selected_prof;
		var race = selected_race;		
		var cell, bonus; 		
		var R = profession_list.GetObjectByName(prof).statistic_growth[stat] + race_list.GetObjectByName(race).growth_adj[stat];
		var S = statistics_by_level[stat][0];		
			if ( isNaN(S) || S < 0 ) {
				S=0;
			}	
		var GI = Math.max(Math.floor(S/R),1);
		var prev_stat = S;
		var prev_bonus = StatisticsPanel_Get_Bonus(S, race_list.GetObjectByName(race).statistic_bonus[stat]);
	  
		for(var i=0; i <= 100; i++) {	 
			if (i > 0 && S < 100 && (i % GI) == 0) {
				S++; 
				GI = Math.max(Math.floor(S/R),1);
			}			
			statistics_by_level[stat][i] = S;		
		}  		
    }   
   
    function StatisticsPanel_Calculate_Resources() {
		var prof = selected_prof;
		var race = selected_race;	
		var total, STR, CON, DEX, AGL, DIS, AUR, LOG, INT, WISE, INF, PTP, MTP, health, mana, stamina, spirit;
		var PTP_sum = 0;
		var MTP_sum = 0;
		var PFranks, HPranks, HPmana, bonus1, bonus2, PFbonus, Combat_Toughness;
/*	
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
*/		
		
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
			
			//PTP
			PTP_sum = ((AUR * (profession_list.GetObjectByName(prof).prime_statistics.indexOf("aura") != -1 ? 2 : 1)) + (DIS * (profession_list.GetObjectByName(prof).prime_statistics.indexOf("discipline") != -1 ? 2 : 1))) / 2;		
			PTP_sum = ((STR * (profession_list.GetObjectByName(prof).prime_statistics.indexOf("strength") != -1 ? 2 : 1)) + (CON * (profession_list.GetObjectByName(prof).prime_statistics.indexOf("constitution") != -1 ? 2 : 1)) + 
				   (DEX * (profession_list.GetObjectByName(prof).prime_statistics.indexOf("dexterity") != -1 ? 2 : 1)) + (AGL * (profession_list.GetObjectByName(prof).prime_statistics.indexOf("agility") != -1 ? 2 : 1)) + PTP_sum) / 20;	
				   
			if( i == 0 ) { 
				PTP_by_level[i] = (25 + PTP_sum).toFixed(2); 			
			} 
			else { 
				PTP_by_level[i] = Math.floor(25 + PTP_sum); 
			}	

			//MTP
			MTP_sum = ((AUR * (profession_list.GetObjectByName(prof).prime_statistics.indexOf("aura") != -1 ? 2 : 1)) + (DIS * (profession_list.GetObjectByName(prof).prime_statistics.indexOf("discipline") != -1 ? 2 : 1))) / 2;		
			MTP_sum = ((LOG * (profession_list.GetObjectByName(prof).prime_statistics.indexOf("logic") != -1 ? 2 : 1)) + (INT * (profession_list.GetObjectByName(prof).prime_statistics.indexOf("intuition") != -1 ? 2 : 1)) + 
		           (WIS * (profession_list.GetObjectByName(prof).prime_statistics.indexOf("wisdom") != -1 ? 2 : 1)) + (INF * (profession_list.GetObjectByName(prof).prime_statistics.indexOf("influence") != -1 ? 2 : 1)) + MTP_sum) / 20;	
				   
			if( i == 0 ) { 
				MTP_by_level[i] = (25 + MTP_sum).toFixed(2); 
			} 
			else { 
				MTP_by_level[i] = Math.floor(25 + MTP_sum); 
			}				

			//health
			PFranks = total_ranks_by_level[i]["Physical Fitness"] || 0; 
			Combat_Toughness = (10 * total_man_ranks_by_level[i]["Combat Toughness-combat"] + 5) || 0; 
			health_by_level[i] = Math.min(Math.floor((statistics_by_level["strength"][0] + statistics_by_level["constitution"][0]) / 10) + PFranks*5, race_list.GetObjectByName(race).max_health+StatisticsPanel_Get_Bonus(CON, race_list.GetObjectByName(race).statistic_bonus["constitution"])) + Combat_Toughness;
		
			//mana
			HPranks = total_ranks_by_level[i]["Harness Power"] || 0;	
			HPmana = (HPranks > i) ? i*3 + HPranks-i : HPranks*3;			
			bonus1 = statistics_by_level[profession_list.GetObjectByName(prof).mana_statistics[0]][0];
			bonus2 = statistics_by_level[profession_list.GetObjectByName(prof).mana_statistics[1]][0];

			bonus1 = StatisticsPanel_Get_Bonus(bonus1, race_list.GetObjectByName(race).statistic_bonus[profession_list.GetObjectByName(prof).mana_statistics[0]]);
			bonus2 = StatisticsPanel_Get_Bonus(bonus2, race_list.GetObjectByName(race).statistic_bonus[profession_list.GetObjectByName(prof).mana_statistics[1]]);	
			mana_by_level[i] = Math.max(Math.floor((bonus1 + bonus2) / 4), 0) + HPmana;
	
			//stamina
			PFbonus = total_bonus_by_level[i]["Physical Fitness"] || 0;			
			stamina_by_level[i] = Math.max(StatisticsPanel_Get_Bonus(CON, race_list.GetObjectByName(race).statistic_bonus["constitution"]) +
								Math.floor((StatisticsPanel_Get_Bonus(STR, race_list.GetObjectByName(race).statistic_bonus["strength"]) + StatisticsPanel_Get_Bonus(AGL, race_list.GetObjectByName(race).statistic_bonus["agility"]) +
								StatisticsPanel_Get_Bonus(DIS, race_list.GetObjectByName(race).statistic_bonus["discipline"])) / 3) + 
								Math.floor(PFbonus / 3), 0);
						
			//spirit
			spirit_by_level[i] = Math.round(AUR / 10);	

		}
    }	
	
	//Calculates the bonus of statistic including the race modifier
	function StatisticsPanel_Get_Bonus(num, bonus) {  
		return Math.floor((num - 50) / 2) + bonus;
	}	
	
	function StatisticsPanel_On_Prof_Change() {
		StatisticsPanel_Update_Leftside();
		StatisticsPanel_Update_Rightside();			
	}
