var StP_MCV = {};

StP_MCV.controller = function() {
	var ctrl = this;
	
	ctrl.race = m.prop(race_list.GetObjectByName(selected_race));
	ctrl.prof = m.prop(profession_list.GetObjectByName(selected_prof));
	ctrl.race_name = ctrl.race().name;
	ctrl.prof_name = ctrl.prof().name;
	
	ctrl.strength = m.prop(strength_by_level);
	ctrl.constitution = m.prop(constitution_by_level);
	ctrl.dexterity = m.prop(dexterity_by_level);
	ctrl.agility = m.prop(agility_by_level);
	ctrl.discipline = m.prop(discipline_by_level);
	ctrl.aura = m.prop(aura_by_level);
	ctrl.logic = m.prop(logic_by_level);
	ctrl.intuition = m.prop(intuition_by_level);
	ctrl.wisdom = m.prop(wisdom_by_level);
	ctrl.influence = m.prop(influence_by_level);
	
	ctrl.stat_totals = m.prop(stat_total_by_level);
	ctrl.stat_bonus = m.prop(statistic_bonuses_by_level);
	
	ctrl.PTP = m.prop(PTP_by_level);
	ctrl.MTP = m.prop(MTP_by_level);
	
	ctrl.health = m.prop(health_by_level);
	ctrl.mana = m.prop(mana_by_level);
	ctrl.stamina = m.prop(stamina_by_level);
	ctrl.health = m.prop(health_by_level);
	ctrl.spirit = m.prop(spirit_by_level);
	
	ctrl.display_mode = m.prop("growth");

	ctrl.Get_Statistic_Value = {
		"strength" : function(val) { return  },
		"constitution" : function(val) { constitution_by_level[0] = parseInt(val); StatisticsPanel_Calculate_Growth("constitution"); StatisticsPanel_Calculate_Resources(); ctrl.Update_Controller("constitution"); },
		"dexterity" : function(val) { dexterity_by_level[0] = parseInt(val); StatisticsPanel_Calculate_Growth("dexterity"); StatisticsPanel_Calculate_Resources(); ctrl.Update_Controller("dexterity"); },
		"agility" : function(val) { agility_by_level[0] = parseInt(val); StatisticsPanel_Calculate_Growth("agility"); StatisticsPanel_Calculate_Resources(); ctrl.Update_Controller("agility"); },
		"discipline" : function(val) { discipline_by_level[0] = parseInt(val); StatisticsPanel_Calculate_Growth("discipline"); StatisticsPanel_Calculate_Resources(); ctrl.Update_Controller("discipline"); },
		"aura" : function(val) { aura_by_level[0] = parseInt(val); StatisticsPanel_Calculate_Growth("aura"); StatisticsPanel_Calculate_Resources(); ctrl.Update_Controller("aura"); },
		"logic" : function(val) { logic_by_level[0] = parseInt(val); StatisticsPanel_Calculate_Growth("logic"); StatisticsPanel_Calculate_Resources(); ctrl.Update_Controller("logic"); },
		"intuition" : function(val) { intuition_by_level[0] = parseInt(val); StatisticsPanel_Calculate_Growth("intuition"); StatisticsPanel_Calculate_Resources(); ctrl.Update_Controller("intuition"); },
		"wisdom" : function(val) { wisdom_by_level[0] = parseInt(val); StatisticsPanel_Calculate_Growth("wisdom"); StatisticsPanel_Calculate_Resources(); ctrl.Update_Controller("wisdom"); },
		"influence" : function(val) { influence_by_level[0] = parseInt(val); StatisticsPanel_Calculate_Growth("influence"); StatisticsPanel_Calculate_Resources(); ctrl.Update_Controller("influence"); }
	}

	ctrl.Set_Statistic_Value = { 
		"strength" : function(val) { strength_by_level[0] = parseInt(val); StatisticsPanel_Calculate_Growth("strength");  StatisticsPanel_Calculate_Resources(); ctrl.Update_Controller("strength"); },
		"constitution" : function(val) { constitution_by_level[0] = parseInt(val); StatisticsPanel_Calculate_Growth("constitution"); StatisticsPanel_Calculate_Resources(); ctrl.Update_Controller("constitution"); },
		"dexterity" : function(val) { dexterity_by_level[0] = parseInt(val); StatisticsPanel_Calculate_Growth("dexterity"); StatisticsPanel_Calculate_Resources(); ctrl.Update_Controller("dexterity"); },
		"agility" : function(val) { agility_by_level[0] = parseInt(val); StatisticsPanel_Calculate_Growth("agility"); StatisticsPanel_Calculate_Resources(); ctrl.Update_Controller("agility"); },
		"discipline" : function(val) { discipline_by_level[0] = parseInt(val); StatisticsPanel_Calculate_Growth("discipline"); StatisticsPanel_Calculate_Resources(); ctrl.Update_Controller("discipline"); },
		"aura" : function(val) { aura_by_level[0] = parseInt(val); StatisticsPanel_Calculate_Growth("aura"); StatisticsPanel_Calculate_Resources(); ctrl.Update_Controller("aura"); },
		"logic" : function(val) { logic_by_level[0] = parseInt(val); StatisticsPanel_Calculate_Growth("logic"); StatisticsPanel_Calculate_Resources(); ctrl.Update_Controller("logic"); },
		"intuition" : function(val) { intuition_by_level[0] = parseInt(val); StatisticsPanel_Calculate_Growth("intuition"); StatisticsPanel_Calculate_Resources(); ctrl.Update_Controller("intuition"); },
		"wisdom" : function(val) { wisdom_by_level[0] = parseInt(val); StatisticsPanel_Calculate_Growth("wisdom"); StatisticsPanel_Calculate_Resources(); ctrl.Update_Controller("wisdom"); },
		"influence" : function(val) { influence_by_level[0] = parseInt(val); StatisticsPanel_Calculate_Growth("influence"); StatisticsPanel_Calculate_Resources(); ctrl.Update_Controller("influence"); }
	};
	
	ctrl.Update_Controller = function(stat) { 
		if( stat == "strength" ) {
			ctrl.strength = m.prop(strength_by_level);
		}
		else if( stat == "constitution" ) {
			ctrl.constitution = m.prop(constitution_by_level);
		}
		else if( stat == "dexterity" ) {
			ctrl.dexterity = m.prop(dexterity_by_level);
		}
		else if( stat == "agility" ) {
			ctrl.agility = m.prop(agility_by_level);
		}
		else if( stat == "discipline" ) {
			ctrl.discipline = m.prop(discipline_by_level);
		}
		else if( stat == "aura" ) {
			ctrl.aura = m.prop(aura_by_level);
		}
		else if( stat == "logic" ) {
			ctrl.logic = m.prop(logic_by_level);
		}
		else if( stat == "intuition" ) {
			ctrl.intuition = m.prop(intuition_by_level);
		}
		else if( stat == "wisdom" ) {
			ctrl.wisdom = m.prop(wisdom_by_level);
		}
		else if( stat == "influence" ) {
			ctrl.influence = m.prop(influence_by_level);
		}
	
		ctrl.stat_totals = m.prop(stat_total_by_level);
		ctrl.stat_bonus = m.prop(statistic_bonuses_by_level);
	
		ctrl.PTP = m.prop(PTP_by_level);
		ctrl.MTP = m.prop(MTP_by_level);
	
		ctrl.health = m.prop(health_by_level);
		ctrl.mana = m.prop(mana_by_level);
		ctrl.stamina = m.prop(stamina_by_level);
		ctrl.health = m.prop(health_by_level);
		ctrl.spirit = m.prop(spirit_by_level);
	
	};
	
	ctrl.Update_Profession = function(val) { 
		selected_prof = val; 	
		ctrl.prof = m.prop(profession_list.GetObjectByName(val));
		Planner_Panels_Update_Profession_Race();
	}
	
	ctrl.Update_Race = function(val) { 
		selected_race = val; 		
		ctrl.race = m.prop(race_list.GetObjectByName(val));
		Planner_Panels_Update_Profession_Race();    
	}
	
}
	
StP_MCV.view = function(ctrl) {	
		var LT_view =  m("table", {width: "100%"}, [
								m("col", {style: {width: "25%"}}),
				m("tr", [
					m("td", {height: 23}, "Profession:"),
					m("td", {colspan: "3"}, m("select", {onchange: m.withAttr("value", ctrl.Update_Profession), value: ctrl.prof_name}, [
										 m("option", {value: "bard"}, "Bard"), 
										 m("option", {value: "cleric"}, "Cleric"),
										 m("option", {value: "empath"}, "Empath"),
										 m("option", {value: "monk"}, "Monk"),
										 m("option", {value: "paladin"}, "Paladin"),
										 m("option", {value: "ranger"}, "Ranger"),
						                 m("option", {value: "rogue"}, "Rogue"),
						                 m("option", {value: "sorcerer"}, "Sorcerer"),
							             m("option", {value: "warrior"}, "Warrior"),
						                 m("option", {value: "wizard"}, "Wizard") 
					] ) )				
				]),
				m("tr", [
					m("td", {height: 23}, "Race:"),
					m("td", {colspan: "2"}, m("select", {onchange: m.withAttr("value",ctrl.Update_Race), value: ctrl.race_name}, [
										 m("option", {value: "aelotoi"}, "Aelotoi"), 
										 m("option", {value: "burghal gnome"}, "Burghal Gnome"),
										 m("option", {value: "dark elf"}, "Dark Elf"),
										 m("option", {value: "dwarf"}, "Dwarf"),
										 m("option", {value: "elf"}, "Elf"),
										 m("option", {value: "erithian"}, "Erithian"),
						                 m("option", {value: "forest gnome"}, "Forest Gnome"),
						                 m("option", {value: "giantman"}, "Giantman"),
							             m("option", {value: "half krolvin"}, "Half Krolvin"),
						                 m("option", {value: "half elf"}, "Half Elf"),
						                 m("option", {value: "halfling"}, "Halfling"),
							             m("option", {value: "human"}, "Human"),
						                 m("option", {value: "sylvankind"}, "Sylvankind") 
					] ) )				
				]),		
				m("tr", [
					m("td", {colspan: "4", height: "23px"}, 
						m("table", {width: "100%"}, [
								m("col", {style: {width: "40%"}}),
								m("tr", {class:"stat_header_row"}, [ 	
									m("td", {height: "23px"}, m("div", "Statistics") ),
									m("td", m("div", "Race Bonus") ),
									m("td", m("div", "Growth Index") ),
									m("td", m("div", "Base") )
								])
						])
					)			
				])
		]);		
		
		var LM_view =  m("table", {width: "100%"}, [
					m("col", {width: ""}),
					m("col", {width: "25%"}),
					m("col", {width: "25%"}),
					m("col", {width: "1%"}),
						StatisticsPanel_Create_Info_Rows(ctrl),		
		]);		
		
		var LB_view = m("table", {width: "100%"}, [
					m("col", {style: {width: ""}} ),
					m("col", {style: {width: "25%"}} ),
					m("col", {style: {width: "15%"}} ),
					m("col", {style: {width: "12%"}}),		
					m("tr", [ 
						m("td", {colspan: "2"}, ""),
						m("td", m("div", {class:"resource_header"}, "Total") ),
						m("td", {class:"stat_cell"}, ctrl.stat_totals()[0] ),
					]),
					m("tr", [ 
						m("td", {colspan: "2"}, ""),
						m("td", m("div", {class:"resource_header"}, "PTP") ),
						m("td", {class:"stat_cell"}, ctrl.PTP()[0] ),
					]),
					m("tr", [ 
						m("td", {colspan: "2"}, ""),
						m("td", m("div", {class:"resource_header"}, "MTP") ),
						m("td", {class:"stat_cell"}, ctrl.MTP()[0] ),
					]),
					m("tr", [ 
						m("td", {colspan: "4"}, "")
					]),
					m("tr", [ 
						m("td", {colspan: "2"}, ""),
						m("td", m("div", {class:"resource_header"}, "Health") ),
						m("td", {class:"health_cell"}, ctrl.health()[0] ),
					]),
					m("tr", [ 
						m("td", {colspan: "2"}, ""),
						m("td", m("div", {class:"resource_header"}, "Mana") ),
						m("td", {class:"mana_cell"}, ctrl.mana()[0] ),
					]),
					m("tr", [ 
						m("td", {colspan: "2"}, ""),
						m("td", m("div", {class:"resource_header"}, "Stamina") ),
						m("td", {class:"stamina_cell"}, ctrl.stamina()[0] ),
					]),
					m("tr", [ 
						m("td", {colspan: "2"}, ""),
						m("td", m("div", {class:"resource_header"}, "Spirit") ),
						m("td", {class:"spirit_cell"}, ctrl.spirit()[0] ),
					]),

		          ]);
		
		var RT_view = m("table", {width: "100%"}, [
					m("tr", [ 
						m("td", {height: "23px"}, ""),				
					]),
					m("tr", [ 
						m("td", {colspan: "100",height: "23px"}, 
							m("form", {id: "StP_display_option1"}, [
								m("span", {class:"resource_header"}, "Statistics by Level"),
								m("input", {id: "StP_display_option1", type: "radio", name: "StP_display_options", value: "growth", checked:"checked", style: {"font-weight": "bold"}, onclick: m.withAttr("value", ctrl.display_mode)} ),
								m("span", "Show Statistics Growth"),
								m("input", {id: "StP_display_option2", type: "radio", name: "StP_display_options", value: "bonus", style: {"font-weight": "bold"}, onclick: m.withAttr("value", ctrl.display_mode)} ),
								m("span", "Show Statistic Bonuses")
							
							
							])
						
						
						),					
					]),
					m("tr", [ 
						m("td", {height: "23px"},
						 m("div", {class: "StP_linked_scroller_H", style: {"overflow-x": "hidden"}},				
							m("table", {width: "5500px"}, [	
								StatisticsPanel_Create_Level_Row()		
							])
						)),					
					])
				   ]);	
				  
					
		var RM_view = m("div", {class: "StP_linked_scroller_H", style: {"overflow-x": "hidden"}},
				   m("table", {name: "BUFFER_TABLE", width: "100%"}, [
					m("tr", [ 
						m("td", {height: "23px"}, 
						  m("table", {width: "5500px"}, StatisticsPanel_Create_Growth_Rows(ctrl))
						),				
					]),		
				   ])
				  );		
		
		
		var RB_view = m("div", {class: "StP_linked_scroller_H", onscroll: StatisticsPanel_Scroll_Div_Onscroll, onmouseup: StatisticsPanel_Scroll_Div_Onmouseup },
				   m("table", {name: "BUFFER_TABLE", width: "100%"}, [
					m("tr", [ 
						m("td", {height: "23px"}, 
							m("table", {width: "5500px"}, StatisticsPanel_Create_Resource_Rows(ctrl))		
						),
					]),		
				   ])
				  );		
		
		
		return m("table", {border: "1", width: "100%"}, [
				m("col", {style: {width: "70%"}} ),
				m("col", {style: {width: ""}} ),		
				m("tr", [
					m("td", {valign: "top"}, 		 
						m("table", {width: "100%"}, [
							m("tr", {height: "95px"}, m("td", LT_view) ),
							m("tr", {height: "279px"}, m("td", LM_view) ),
							m("tr", m("td", LB_view) )
						])
					),
					m("td", {valign: "top"},		 
						m("table", {width: "100%"},[
							m("tr", {height: "93px"}, m("td", RT_view) ),
							m("tr", {height: "280px"}, m("td", RM_view) ),
							m("tr", m("td", RB_view) )
						])
					)
				])
			]);
	}
	
	
	function StatisticsPanel_Create_Info_Rows(ctrl) {
		var rows = [], stat;		
		
		for(var i=0; i<statistics.length; i++) {
			stat = statistics[i].charAt(0).toUpperCase() + statistics[i].slice(1);
					
			rows.push(
				m("tr", {class:"stat_row"}, [
								m("td", {style: {textAlign: "left"}}, stat ),
								m("td", ctrl.race().statistic_bonus[statistics[i]] ),
								m("td", ctrl.race().growth_adj[statistics[i]] + ctrl.prof().statistic_growth[statistics[i]] ),
								m("td", {style: {"background-color": StatisticsPanel_Set_Input_Color(statistics[i])}}, m("input", {size: "3", maxlength: "3", value: ctrl[statistics[i]]()[0], onblur: m.withAttr("value", ctrl.Set_Statistic_Value[statistics[i]]), onkeydown: StatisticsPanel_Input_Box_Onkeydown } ) ),								
				])
			);			
		}
		
		return rows;	
	}

	function StatisticsPanel_Create_Level_Row() {
		var cells = [];
		
		for(var i=0; i <= 100; i++) {
			cells.push(	m("td", i )	);			
		}
		
		return m("tr", {class:"level_row"}, cells);			
	}

	function StatisticsPanel_Create_Growth_Rows(ctrl) {
		var rows = [];
		var cells = []
		var prev, cur, stat;
		
		for(var i=0; i < statistics.length; i++) {
			cells = [];
			stat = statistics[i];
			for( var j=0; j <= 100; j++ ) {
				if(ctrl.display_mode() == "growth") {
					cur = ctrl[stat]()[j];
					if( j > 0) { prev = ctrl[stat]()[j-1]; }
				}
				else {
					cur = ctrl.stat_bonus()[stat][j];
					if( j > 0) { prev = ctrl[stat]()[j-1] }					
				}
				cells.push(m("td", {style: {"background-color": (j > 0 && cur > prev) ? "#00FF00" : "lightgray" } }, cur ));
			}	
		  rows.push(m("tr", {class:"growth_row"}, cells));
		}
		
		return rows;			
	}

	function StatisticsPanel_Create_Resource_Rows(ctrl) {
		var rows = [];
		var cells = []
		var prev, cur, stat;
		
			cells = [];
			for( var j=0; j <= 100; j++ ) {
				cur = ctrl.stat_totals()[j];
				cells.push(m("td", {class: "stat_cell"}, ctrl.stat_totals()[j] ));
			}	
		    rows.push(m("tr", cells));
			
			cells = [];
			for( var j=0; j <= 100; j++ ) {
				cur = ctrl.PTP()[j];
				if( j > 0) { prev = ctrl.PTP()[j-1]; }
				cells.push(m("td", {class: "stat_cell", style: {"background-color": (j > 0 && cur > prev) ? "#00FF00" : "lightgray" } }, Math.floor(ctrl.PTP()[j]) ));
			}	
		    rows.push(m("tr", cells));
			
			cells = [];
			for( var j=0; j <= 100; j++ ) {
				cur = ctrl.MTP[j];
				if( j > 0) { prev = ctrl.MTP()[j-1]; }
				cells.push(m("td", {class: "stat_cell", style: {"background-color": (j > 0 && cur > prev) ? "#00FF00" : "lightgray" } }, Math.floor(ctrl.MTP()[j]) ));
			}	
		    rows.push(m("tr", cells));
			
		    rows.push(m("tr", []));			
			
			cells = [];
			for( var j=0; j <= 100; j++ ) {
				cur = ctrl.health()[j];
				cells.push(m("td", {class: "health_cell" }, ctrl.health()[j] ));
			}	
		    rows.push(m("tr", cells));
			
			cells = [];
			for( var j=0; j <= 100; j++ ) {
				cur = ctrl.mana()[j];
				cells.push(m("td", {class: "mana_cell" }, ctrl.mana()[j] ));
			}	
		    rows.push(m("tr", cells));
			
			cells = [];
			for( var j=0; j <= 100; j++ ) {
				cur = ctrl.stamina()[j];
				cells.push(m("td", {class: "stamina_cell" }, ctrl.stamina()[j] ));
			}	
		    rows.push(m("tr", cells));
			
			cells = [];
			for( var j=0; j <= 100; j++ ) {
				cur = ctrl.spirit()[j];
				cells.push(m("td", {class: "spirit_cell" }, ctrl.spirit()[j] ));
			}	
		    rows.push(m("tr",  cells));
		
		return rows;			
	}	

	function StatisticsPanel_Set_Input_Color(val) { 
		var prof = profession_list.GetObjectByName(selected_prof);
	
		if ( prof.prime_statistics.indexOf(val) != -1 && prof.mana_statistics.indexOf(val) != -1 ) {
			return "gold";		
		}
		else if ( prof.prime_statistics.indexOf(val) != -1 ) {
			return "black";
		}
		else if ( prof.mana_statistics.indexOf(val) != -1 ) {
			return "blue";	
		}
		else {
			return "white";	
		}	
	}	

	function StatisticsPanel_Scroll_Div_Onscroll() {
		var divs = document.getElementsByClassName("StP_linked_scroller_H");
		var pos = $(divs[2]).scrollLeft();
	
		$(divs[0]).scrollLeft(pos);
		$(divs[1]).scrollLeft(pos);	
	}

	function StatisticsPanel_Scroll_Div_Onmouseup(val) {
		scroller_H = val;	
	}

	function StatisticsPanel_Input_Box_Onkeydown(e) {
		var td = e.target.parentNode, tr = td.parentNode, table = tr.parentNode, box;
	
		switch(e.keyCode) {
			case 13:    //enter key
			case 27:    //escape key
						e.target.blur();
						break;
						
			case 38:	//up arrow
						box = table.childNodes[Math.max(4, tr.rowIndex + 3)].childNodes[td.cellIndex].firstChild;
						box.focus();
						box.setSelectionRange(box.value.length * 2, box.value.length * 2);	
						break;
						
			case 40:	//down arrow		
						box = table.childNodes[Math.min(table.childNodes.length-1, tr.rowIndex + 5)].childNodes[td.cellIndex].firstChild; 
						box.focus();
						box.setSelectionRange(box.value.length * 2, box.value.length * 2);
						break;
						
			default: 	m.redraw.strategy("none");
						break;
			
		}		
	}

    function StatisticsPanel_Calculate_Growth_All() {  
		for (var i=0; i < statistics.length; i++) {				
			StatisticsPanel_Calculate_Growth(statistics[i]);
		}
	}
   
    function StatisticsPanel_Calculate_Growth(stat) { 
		var prof = profession_list.GetObjectByName(selected_prof);
		var race = race_list.GetObjectByName(selected_race);
		var cell, bonus; 		
		var R = prof.statistic_growth[stat] + race.growth_adj[stat];
		var S = statistics_by_level[stat][0];		
			if ( isNaN(S) || S < 0 ) {
				S=0;
			}	
		var GI = Math.max(Math.floor(S/R),1);
		var prev_stat = S;
		var prev_bonus = StatisticsPanel_Get_Bonus(S, race.statistic_bonus[stat]);
			  
		for(var i=0; i <= 100; i++) {	 
			if (i > 0 && S < 100 && (i % GI) == 0) {
				S++; 
				GI = Math.max(Math.floor(S/R),1);
				prev_bonus = StatisticsPanel_Get_Bonus(S, race.statistic_bonus[stat])
			}			
			statistics_by_level[stat][i] = S;	
			statistic_bonuses_by_level[stat][i] = prev_bonus;	
		}  		
    }   
   
    function StatisticsPanel_Calculate_Resources() {
		var prof = selected_prof;
		var race = selected_race;	
		var total, STR, CON, DEX, AGL, DIS, AUR, LOG, INT, WISE, INF, PTP, MTP, health, mana, stamina, spirit;
		var PTP_sum = 0;
		var MTP_sum = 0;
		var PFranks, HPranks, HPmana, bonus1, bonus2, PFbonus, Combat_Toughness;
	
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
