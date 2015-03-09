	var panel_list = [ "statistics", "skills", "maneuvers", "magic", "combat", "summary" ];
	var scroller_H = 0;
	var scroller_V = 0;
	var char_data = "";
	var VERSION = "v1.0";
	
	function Planner_Show_Panel(id) {
		if ( panel_list.indexOf(id) != -1 ) {
			for (var i=0; i < panel_list.length; i++) {
				document.getElementById(panel_list[i]+"_panel").style.display = "none";
				document.getElementById(panel_list[i]+"_tab").style.backgroundColor = "#dedbde";
			}			
			document.getElementById(id+"_panel").style.display = "block";
			document.getElementById(id+"_tab").style.backgroundColor = "#f1f0ee";			
			
			switch(Planner_Get_Active_Panel()) {
				case "statistics":	$("#StP_growth_container").scrollLeft(scroller_H);
									break;
				case "skills":	//	$("#SkP_skills_info_container").scrollTop(scroller_V);
								//	$("#SkP_skills_training_container").scrollTop(scroller_V);
									$("#SkP_skills_training_container").scrollLeft(scroller_H);
									break;
				case "maneuvers":	//$("#SkP_skills_info_container").scrollTop(scroller_V);
									//$("#SkP_skills_training_container").scrollTop(scroller_V);
									$("#ManP_maneuvers_training_container").scrollLeft(scroller_H);
									break;
			}
		}
	}
	
	function Planner_Init() {				
		StatisticsPanel_Init();
		SkillsPanel_Init();
		ManeuversPanel_Init();
		
		Planner_Show_Panel("statistics");	
	}
	
	function Planner_Panels_Update_Profession(prof) {
		StatisticsPanel_Refresh_All();
		SkillsPanel_On_Prof_Change(prof);
		ManeuversPanel_On_Prof_Change(prof);
	}
	
	function Planner_Get_Active_Panel() {
		for( var i=0; i < panel_list.length; i++ ) {
			if( document.getElementById(panel_list[i]+"_panel").style.display != "none" ) {
					return panel_list[i];				
			}			
		}
		return false;
	}
		
	function Planner_File_Onchange(caller) {
		var reader = new FileReader();
		reader.onload = function(e) {
			Planner_Load_Character(e.target.result);			
		};	
		reader.readAsText(caller.files[0]);		
	}
	
	function Planner_Load_Character(filedata) {
		var lines = filedata.split("\n");
		var parts, subparts, mode = 0, prof;
		
		//Planner_Clean_Pannel("skills");
		//Planner_Clean_Pannel("maneuvers");
		
		for( var i=0; i < lines.length; i++ ) {
			if( lines[i].length  <= 0 ){
				continue;
			}
			
			if( lines[i] == "STATISTICS" ) {
				mode = 1;				
			}			
			else if( lines[i] == "SKILLS" ) {
				mode = 2;				
			}
			else if( lines[i] == "MANEUVERS" ) {
				mode = 3;			
			}
			else {
				parts = lines[i].split(":");
				if( parts.length < 2 ) {
					alert("PARSE ERROR FOR LINE: "+parts.length);
					break;
				}
				
				switch(mode) {
					case 0: //PLANNER
							switch(parts[0]) {
								case "VERSION": 			break;
								
								case "BUILDNAME": document.getElementById("build_name").value = parts[1];
															break;
								case "SKILLPANEL_HIDE": 	if( parts[1] == "true" ) {
																document.getElementById('SkP_hide_skills').checked = true;
															}
															break;
														
								case "MANEUVERPANEL_HIDE": 	if( parts[1] == "true" ) {
																document.getElementById('ManP_hide_maneuvers').checked = true;
															}
															break;		

								case "PROFESSION": 			document.getElementById('StP_selected_profession').value = parts[1];
															break;
															
								case "RACE": 				document.getElementById('StP_selected_race').value = parts[1];
															break;
							}
							break;
					
					case 1: //STATISTICS
							document.getElementById('StP_base_'+parts[0]).value = parts[1];
							break;
				
					case 2: //SKILLS
							parts = lines[i].split("|");
							name = parts[0].split(":")[0];
							
							if( parts[0].split(":")[1] == "true" ) {
								document.getElementById(name+'_checkbox').checked= true;
							}
							
							if( parts[1].split(":")[1] != "undefined" ) {     //rate
								training_rate[name]= parts[1].split(":")[1];							
							}
							
							if( parts[2].split(":").length > 1 ) {
								subparts = parts[2].split(":")[1].split(",");
								
								for(var j=0; j < subparts.length-1; j++) {		
									ranks_by_level[parseInt(subparts[j].split("=")[0])][name] = parseInt(subparts[j].split("=")[1])
								}
								
								SkillsPanel_Calculate_Total_Ranks(name, 0);
								SkillsPanel_Training_Update_Row(name, 0);
							}
							break;
							
					case 3: //MANEUVERS
							parts = lines[i].split("|");
							name = parts[0].split(":")[0];
							
							if( parts[0].split(":")[1] == "true" ) {
								document.getElementById(name+'_checkbox').checked= true;
							}
							
							if( parts[1].split(":").length > 1 ) {
								subparts = parts[1].split(":")[1].split(",");
								
								for(var j=0; j < subparts.length-1; j++) {									
									man_ranks_by_level[parseInt(subparts[j].split("=")[0])][name] = parseInt(subparts[j].split("=")[1])
								}
					//			alert(name.split("-")[0]);
								ManeuversPanel_Calculate_Total_Ranks(name.split("@")[0], 0);
								ManeuversPanel_Training_Update_Row(name.split("@")[0], 0);
							}
							break;
				}
			}			
		}		
		
		prof = document.getElementById("StP_selected_profession").value;
		StatisticsPanel_Refresh_All();
		SkillsPanel_On_Prof_Change(prof);
		ManeuversPanel_On_Prof_Change(prof);		
	}
	
	function Planner_Save_Character() {
		char_data = "";
		var man;
		/*FORMAT FOR CHARACTER SAVE FILE
		 //PLANNER
		 VERSION:xxx
		 BUILDNAME:xxxxx
		 SKILLPANEL_HIDE:xxx
		 MANEUVERPANEL_HIDE:xxx
		 PROFESSION:xxx
		 RACE:xxx
		 //STATISTICS		 
		 strength:xxx
		 constitution:xxx
		 dexterity:xxx
		 agility:xxx
		 displine:xxx
		 aura:xxx
		 logic:xxx
		 intuition:xxx
		 wisdom:xxx
		 influence:xxx
		 //SKILLS, entry only appears if training for it exists
		 <skill name>:<0-1 for checkbox>|rate:<rate>|training:<Lvl#=ranks@lvl>,<Lvl#=ranks@lvl>, ...
		 ...
		 ...
		 //MANEUVERS, entry only appears if training for it exists
		 <maneuvers name>-<maneuver type>:<0-1 for checkbox>|rate:<rate>|training:<Lvl#=ranks@lvl>,<Lvl#=ranks@lvl>, ...
		 ...
		 ...		
		*/		
		char_data += "VERSION:" + VERSION + "\n";
		char_data += "BUILDNAME:" + Planner_Escape_Special(document.getElementById("build_name").value || "YourChar") + "\n";
		char_data += "SKILLPANEL_HIDE:" + document.getElementById('SkP_hide_skills').checked + "\n";
		char_data += "MANEUVERPANEL_HIDE:" + document.getElementById('ManP_hide_maneuvers').checked + "\n";	
		char_data += "PROFESSION:" + document.getElementById('StP_selected_profession').value + "\n";	
		char_data += "RACE:" + document.getElementById('StP_selected_race').value + "\n";	
		char_data += "STATISTICS" + "\n";
		for( var i=0; i < statistics.length; i++ ) {
			char_data += statistics[i] + ":" + document.getElementById('StP_base_'+statistics[i]).value + "\n"; 		
		}
		
		char_data += "SKILLS" + "\n";
		for( var i=0; i < all_skills.length; i++ ) {
			char_data += all_skills[i] + ":" + document.getElementById(all_skills[i]+'_checkbox').checked;
			char_data += "|rate:" + training_rate[all_skills[i]];
			char_data += "|training:"; 
			
			for( var j=0; j <= 100; j++ ) {
				if( ranks_by_level[j][all_skills[i]] != undefined ) {
					char_data += j + "=" + ranks_by_level[j][all_skills[i]] +",";
				}				
			}	
			char_data += "\n"; 		
		}
		
		char_data += "MANEUVERS" + "\n";
		for( var i=0; i < all_maneuvers.list.length; i++ ) {
			man = all_maneuvers.list[i].name +"@" + all_maneuvers.list[i].type;
			
			char_data += man + ":" + document.getElementById(man+'_checkbox').checked;
			char_data += "|training:"; 
			
			for( var j=0; j <= 100; j++ ) {
				if( man_ranks_by_level[j][man] != undefined ) {
					char_data += j + "=" + man_ranks_by_level[j][man] +",";
				}				
			}			
			char_data += "\n"; 
		}		
		
		document.getElementById('save_char_link').click();	
	}
	
	function Planner_Escape_Special(txt) {
		return txt
         .replace(/:/g, "")
         .replace(/\*/g, "")
         .replace(/\?/g, "")
         .replace(/\|/g, "")
         .replace(/"/g, "")
         .replace(/&/g, "")
         .replace(/</g, "")
         .replace(/>/g, "")
         .replace(/\//g, "")
         .replace(/\\/g, "");
 
	}
