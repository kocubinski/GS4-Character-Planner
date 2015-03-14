	function SkillsPanel_Init() {
		var info_div = document.getElementById("SkP_skills_info_container");
		var training_div = document.getElementById("SkP_skills_training_container");
		
		var info_tbl = document.createElement('table');
		var training_tbl = document.createElement('table');
		var info_tbdy = document.createElement('tbody');
		var training_tbdy = document.createElement('tbody');
		var tr, td, level;
		
		var PTP, MTP, ranks, val;
		
		info_tbl.width = "100%";
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
			val = profession_skill_costs[selected_prof][all_skills[i].split(",")[0]].split("/");
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
							
		SkillsPanel_Update_LeftSide();		
		SkillsPanel_Update_RightSide();					
		SkillsPanel_Change_Displayed_Skills();		
	}	
  
    function SkillsPanel_Term() {
		var info_div = document.getElementById("SkP_skills_info_container");
		var training_div = document.getElementById("SkP_skills_training_container");

		
		while (info_div.firstChild) {
			info_div.removeChild(info_div.firstChild);
		}
		
		while (training_div.firstChild) {
			training_div.removeChild(training_div.firstChild);
		}		
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
		checkbox.onclick = function() { if( this.checked ) { hidden_skills[skill] = true; } else {delete hidden_skills[skill]; } };
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
		input.id = skill + "_train_rate";		
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
			
		if( !isNaN(caller.value) && parseInt(caller.value) != ranks_by_level[arr[2]][arr[0]]) {	
			if( caller.value == "" ) {				
				delete ranks_by_level[arr[2]][arr[0]];					
			}
			else {
				ranks_by_level[arr[2]][arr[0]] = parseInt(caller.value);				
			}	
			SkillsPanel_Calculate_Total_Ranks(arr[0], arr[2]);	
			SkillsPanel_Training_Update_Row(arr[0], arr[2]);
			SkillsPanel_Calculate_Training_Costs(parseInt(arr[2]));		
			SkillsPanel_Calculate_Remaining_TP(parseInt(arr[2]));
			SkillsPanel_Calculate_Redux_Points(parseInt(arr[2]));		
		}		

		
	//		if( arr[0] == "Harness Power" || arr[0] == "Physical Fitness" ) {
	//			StatisticsPanel_Calculate_Resources();
	//		}
	}	
	
	function SkillsPanel_Training_Input_Onkeyup(e, caller) {
		var num;
		var arr = caller.id.split("_"); 
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
								document.getElementById(nextskill + "_" + arr[1]+ "_" + arr[2]).click();
								break;
							}
						}					
						break;
						
			case 38:    // up arrow
						for( var i=all_skills.indexOf(arr[0])-1; i >= 0; i-- ) {
							nextskill = all_skills[i];
							if( document.getElementById(nextskill+"_info_row").style.display != "none" ) {	
								document.getElementById(nextskill + "_" + arr[1]+ "_" + arr[2]).click();
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
							document.getElementById(arr[0] +  "_train_rate").focus();							
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
		var skillname = caller.id.split("_")[0].split(",")[0];
		
		var max_rpl = parseInt(profession_skill_costs[selected_prof][skillname].split("/")[2]);
		var val = caller.value;
		var len = val.length;
		var t_lvl = 100;
		
		if( val == training_rate[caller.id.split("_")[0]] || (val == "" && training_rate[caller.id.split("_")[0]] == undefined) ) {
				return;
		}
		
		
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
		
		SkillsPanel_Update_RightSide();
	//	StatisticsPanel_Calculate_Resources();
	}				
	
	function SkillsPanel_Clear_All_Button() {
		var ok = confirm("Are you sure you want erase all training and options. Click Yes to continue or No to cancel.");
		
		if( ok ) {
			SkillsPanel_Erase_Training();	
		}
	}
	
	function SkillsPanel_Erase_Training() {
		hide_unused_skills = false;
		document.getElementById("SkP_show_level_ranks").checked = true;
		
		for( var i=0; i < akills.length; i++ ) {
			delete hidden_skills[akills[i]];
			delete training_rate[akills[i]];
			
			for( var j=0; j <= 100; j++ ) {				
				delete ranks_by_level[j][akills[i]]
				delete total_ranks_by_level[j][akills[i]];
				delete total_bonus_by_level[j][akills[i]];
			}
		}		
		SkillsPanel_Update_LeftSide();	
		SkillsPanel_Update_RightSide();					
		SkillsPanel_Change_Displayed_Skills();		
	//	StatisticsPanel_Calculate_Resources();
	}
	
	function SkillsPanel_Change_Displayed_Skills() {			
		hide_unused_skills = document.getElementById("SkP_hide_skills").checked;	
		
		for( var i=0; i < all_skills.length; i++ ) {
			if( document.getElementById(all_skills[i]+"_info_row").style.display == "" ) {
				if( hide_unused_skills && !document.getElementById(all_skills[i]+"_checkbox").checked &&        
				total_ranks_by_level[100][all_skills[i]] == undefined && training_rate[all_skills[i]] == undefined ) {    
					document.getElementById(all_skills[i]+"_info_row").style.display = "none";
					document.getElementById(all_skills[i]+"_training_row").style.display = "none";
				}
			}			
			else if( !hide_unused_skills ) {    
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
	
	function SkillsPanel_Training_Update_Row(skill, start_level=0) {		
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
	
	function SkillsPanel_Update_LeftSide() {
		document.getElementById("SkP_hide_skills").checked = hide_unused_skills;
	
		for( var i=0; i < all_skills.length; i++ ) {
			if( hidden_skills[all_skills[i]] != undefined ) {
				document.getElementById(all_skills[i]+"_checkbox").checked = true;
			}
			else {
				document.getElementById(all_skills[i]+"_checkbox").checked = false;						
			}
			
			if( training_rate[all_skills[i]] != undefined ) {
				document.getElementById(all_skills[i]+"_train_rate").value = training_rate[all_skills[i]];
			}
			else {
				document.getElementById(all_skills[i]+"_train_rate").value = "";	
			}			
		}		
	}
	
	function SkillsPanel_Update_RightSide() {
		SkillsPanel_Training_Change_Style();
		SkillsPanel_Calculate_Remaining_TP();	
		SkillsPanel_Calculate_Redux_Points();		
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
	
	function SkillsPanel_Calculate_Total_Ranks(skill, start_level=0) {
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

	function SkillsPanel_Calculate_Remaining_TP(start_level=0) {
		var PTP, MTP, PTP_cost, MTP_cost, PTP_prev=0, MTP_prev=0;
		var convertedPTP=0, convertedMTP=0;
	
		for( var i=start_level; i <= 100; i++ ) {
			if( i > 0 ) {
				PTP_prev = parseInt(document.getElementById("PTP_left_"+(i-1)).innerHTML);
				MTP_prev = parseInt(document.getElementById("MTP_left_"+(i-1)).innerHTML);	
			}
			
			PTP = PTP_by_level[i];
			MTP = MTP_by_level[i];
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
		
	function SkillsPanel_Calculate_Redux_Points(start_level=0) {
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
		delete training_rate[skill];
		delete hidden_skills[skill];
	//	document.getElementById(skill+"_checkbox").checked = false;
	//	document.getElementById(skill+"_rate").value = "";
		
		for( var i = 0; i <= 100; i++ ) {
			delete ranks_by_level[i][skill];
			delete total_ranks_by_level[i][skill];
			delete total_bonus_by_level[i][skill];
		}
		
	//	SkillsPanel_Training_Update_Row(skill, 0);
	}
	
	function SkillsPanel_On_Prof_Change() {	 
		for( var i=0; i < subskills["Spell Research"].length; i++ ) {			
			if( profession_list.GetObjectByName(selected_prof).spell_circles.indexOf(subskills["Spell Research"][i]) == -1 ) {
				SkillsPanel_Zero_Out_Skill_Row("Spell Research, "+subskills["Spell Research"][i]);
			}
		}
		
		
		
		if( Planner_Get_Active_Panel() == "skills" ) {
			SkillsPanel_Set_Skill_Costs(selected_prof);		
			for( var i=0; i < 100; i++) {
				SkillsPanel_Calculate_Training_Costs(i);	
			}
			
			SkillsPanel_Change_Displayed_Skills();	
			SkillsPanel_Calculate_Remaining_TP();
			SkillsPanel_Calculate_Redux_Points();
		}
	}
		
	function SkillsPanel_Update_Available_Skills() {
		all_skills = [];
		
		for( var i=0; i < skills.length; i++ ) {
			if( subskills[skills[i]] != undefined ) {
				for( var j=0; j < subskills[skills[i]].length; j++) {
					if( skills[i] == "Spell Research" ) {
						if( profession_list.GetObjectByName(selected_prof).spell_circles.indexOf(subskills["Spell Research"][j]) != -1 ) {
							all_skills[all_skills.length] = skills[i]+", "+subskills[skills[i]][j];    							
						}					
					}
					else {
						all_skills[all_skills.length] = skills[i]+", "+subskills[skills[i]][j];    
					}
				}
			}	
			else {
				all_skills[all_skills.length] = skills[i];
			}
		}		
	}
	
