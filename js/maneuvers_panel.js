	function ManeuversPanel_Init() {
		var info_div = document.getElementById("ManP_maneuvers_info_container");
		var training_div = document.getElementById("ManP_maneuvers_training_container");
//		var prof = document.getElementById("StP_selected_profession").value;
		
		var info_tbl = document.createElement('table');
		var training_tbl = document.createElement('table');
		var info_tbdy = document.createElement('tbody');
		var training_tbdy = document.createElement('tbody');
		var tr, td, level;
		
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
		col.style.width = "8%";
		info_tbl.appendChild(col);
		col = document.createElement('col');
		col.style.width = "8%";
		info_tbl.appendChild(col);		
		col = document.createElement('col');
		col.style.width = "8%";
		info_tbl.appendChild(col);
		col = document.createElement('col');
		col.style.width = "8%";
		info_tbl.appendChild(col);	
		col = document.createElement('col');
		col.style.width = "8%";
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
		//	level.style.width = 31;
			level.innerHTML = j;	
			td.appendChild(level);			
			tr.appendChild(td);    
		}    
		training_tbdy.appendChild(tr);		
		
		tr = document.createElement('tr');
		tr.style.fontWeight="bold";
	
		td = document.createElement('td');	
		td.height = "23px";			
		td.width = "5%";
		tr.appendChild(td);    			
		
		td = document.createElement('td');
		td.appendChild(document.createTextNode("Maneuver Name"));		
		tr.appendChild(td);    		
		
		td = document.createElement('td');
		td.appendChild(document.createTextNode("Costs per Rank"));
		td.colSpan = 5;
		td.style.textAlign="center";	
		tr.appendChild(td);  
		
		info_tbdy.appendChild(tr);
				
		//Skill Info and Training Rows
		for( var i=0; i < avail_maneuvers.list.length; i++ ) {			
			tr = ManeuversPanel_Create_Maneuver_Row_Left(avail_maneuvers.list[i]);
			info_tbdy.appendChild(tr);
			tr = ManeuversPanel_Create_Maneuver_Row_Right(avail_maneuvers.list[i]);
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
		
		//Points used row		
		tr = ManeuversPanel_Create_Label_Row_Left("Points Used", "man_points_used");
		info_tbdy.appendChild(tr);
		tr = ManeuversPanel_Create_Label_Row_Right("points_used_", "0");
		training_tbdy.appendChild(tr);
		
		//Points remaining row		
		tr = ManeuversPanel_Create_Label_Row_Left("Points Left", "man_points_left");
		info_tbdy.appendChild(tr);
		tr = ManeuversPanel_Create_Label_Row_Right("points_left_", "0");
		training_tbdy.appendChild(tr);
	
		//Total points gained Points row	
		tr = ManeuversPanel_Create_Label_Row_Left("Total Points", "man_points_total");
		info_tbdy.appendChild(tr);
		tr = ManeuversPanel_Create_Label_Row_Right("points_total_", "0");
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
					
		ManeuversPanel_Update_LeftSide();
		ManeuversPanel_Update_Rightside();
		ManeuversPanel_Change_Maneuver_View();		
		ManeuversPanel_Calculate_Points();
	}
	
    function ManeuversPanel_Term() {
		var info_div = document.getElementById("ManP_maneuvers_info_container");
		var training_div = document.getElementById("ManP_maneuvers_training_container");
		
		while (info_div.firstChild) {
			info_div.removeChild(info_div.firstChild);
		}
		
		while (training_div.firstChild) {
			training_div.removeChild(training_div.firstChild);
		}		
	}  		
	
	function ManeuversPanel_Create_Maneuver_Row_Left(man) {
		var	tr = document.createElement('tr');
		var td, checkbox, input;

		tr.id = man.name + "@" + man.type + "_info_row";		
		tr.style.backgroundColor = "lightgray";
		
	
		td = document.createElement('td');	
		td.height = "23px";			
		checkbox = document.createElement('input');
		checkbox.id = man.name + "@" + man.type + "_checkbox";	
		checkbox.type = "checkbox";
		checkbox.onclick = function() { if( this.checked ) { hidden_maneuvers[this.id.split("_")[0]] = true; } else {delete hidden_maneuvers[this.id.split("_")[0]]; } };
		td.appendChild(checkbox);
		tr.appendChild(td);    			
		
		td = document.createElement('td');
		td.appendChild(document.createTextNode(man.name));		
		td.id = man.name + "@" + man.type + "_text";		
		tr.appendChild(td);  
		
		for( var i=0; i < 5; i++ ) {
			td = document.createElement('td');
			rank = document.createElement('div');	
			rank.id = man.name + "@" + man.type + "_cost"+(i+1);	
			rank.style.textAlign="center";			
			rank.style.width = "31";
			rank.innerHTML = man.rank_costs[i] || "-";	
			td.appendChild(rank);				
			tr.appendChild(td);  				
		}
		
		return tr;
	}
  
 	function ManeuversPanel_Create_Maneuver_Row_Right(man) {
		var tr = document.createElement('tr');
		var td, input, div;
		
		tr.id = man.name + "@" + man.type + "_training_row";	
		tr.style.backgroundColor = "lightgray";
		
		for(var j=0; j<=100; j++) {
			td = document.createElement('td');
			td.height = 23;
			td.id = man.name + "@" + man.type + "_ranks_" + j;
			td.align="center";
			td.onclick = function() { ManeuversPanel_Training_Div_Onclick(this); };
						
			div = document.createElement('div');
			div.id = man.name + "@" + man.type + "_div_" + j;
			div.style.width = 31;
			div.style.textAlign="center";	
			div.onclick = function() {  ManeuversPanel_Training_Div_Onclick(this); };	
			td.appendChild(div);  				

			//input box for rank training per level
			input = document.createElement('input');
			input.id = man.name + "@" + man.type + "_input_" + j;	
			input.style.display = "none";		
			input.size = "2";		
			input.maxLength = "1";
			input.type="text";
			input.align="center";
			input.style.textAlign="center";
			input.onblur = function() {  ManeuversPanel_Training_Input_Onblur(this) };	
			input.onkeyup = function(event) {  ManeuversPanel_Training_Input_Onkeyup(event, this) };	
			td.appendChild(input);  
			
			tr.appendChild(td);    
		}  		
	
		return tr;
	} 
	
	function ManeuversPanel_Create_Label_Row_Left(title, id) {
		tr = document.createElement('tr');			
		td = document.createElement('td');
		td.id = id;
		td.height="23";
		td.colSpan = "100";
		td.style.fontWeight="bold";
		td.align = "right";
		td.appendChild(document.createTextNode(title));
		tr.appendChild(td);
		
		return tr;
	}

	function ManeuversPanel_Create_Label_Row_Right(id, text) {
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
	
	function ManeuversPanel_Training_Div_Onclick(caller) {
		var arr = caller.id.split("_"); 
		var input = document.getElementById(arr[0] + "_input_" + arr[2]); 
		
		document.getElementById(arr[0]+"_div_"+arr[2]).style.display = "none";	
		input.style.display = "block"; 
				
		if( !isNaN(man_ranks_by_level[arr[2]][arr[0]]) && man_ranks_by_level[arr[2]][arr[0]] > 0 ) {
			input.value = man_ranks_by_level[arr[2]][arr[0]];
		}
		else {	
			input.value = "";
		}			
		input.select();
	}

	function ManeuversPanel_Training_Input_Onblur(caller) {
		var arr = caller.id.split("_"); 
		var div = document.getElementById(arr[0] + "_div_" + arr[2]); 
	
		caller.style.display = "none";		
		div.style.display = "block"; 		
			
		if( !isNaN(caller.value) && man_ranks_by_level[arr[2]][arr[0]] != parseInt(caller.value) ) {	
			if( caller.value == "" ) {				
				delete man_ranks_by_level[arr[2]][arr[0]];					
			}
			else {
				man_ranks_by_level[arr[2]][arr[0]] = parseInt(caller.value);				
			}	
			
			ManeuversPanel_Calculate_Total_Ranks(arr[0].split("@")[0], arr[2]);	
			ManeuversPanel_Training_Update_Row(arr[0].split("@")[0], arr[2]);	
			ManeuversPanel_Calculate_Points();	
		}					
		
//		if( arr[0] == "Combat Toughness-combat" ) {
//			StatisticsPanel_Calculate_Resources();
//		}
	}	
	
	function ManeuversPanel_Training_Input_Onkeyup(e, caller) {
		var num;
		var arr = caller.id.split("_"); 
		var nextskill;
		
		switch(e.which) {
			case 13:	// enter key	
						caller.blur();
						break;		
			case 27:    // escape key
						if ( arr[1] == "input" ) {
							caller.value = man_ranks_by_level[arr[2]][arr[0]];
						}
						caller.blur();
						break;
						
			case 40:	// down arrow
						for( var i=avail_maneuvers.list.indexOf(avail_maneuvers.GetObjectByName(caller.id.split("@")[0]))+1; i <= avail_maneuvers.list.length-1; i++ ) {
							nextskill = avail_maneuvers.list[i].name+"@"+avail_maneuvers.list[i].type;
							if( document.getElementById(nextskill+"_info_row").style.display != "none" ) {	
								document.getElementById(nextskill + "_" + arr[1] + "_" + arr[2]).click();
								break;
							}
						}					
						break;
						
			case 38:    // up arrow
						for( var i=avail_maneuvers.list.indexOf(avail_maneuvers.GetObjectByName(caller.id.split("@")[0]))-1; i >= 0; i-- ) {
							nextskill = avail_maneuvers.list[i].name+"@"+avail_maneuvers.list[i].type;
							if( document.getElementById(nextskill+"_info_row").style.display != "none" ) {	
								document.getElementById(nextskill + "_" + arr[1] + "_" + arr[2]).click();
								break;
							}
						}					
						break;
						
			case 37:    // left arrow
						num = parseInt(arr[2]) - 1;
						if (num >= 0) {
							document.getElementById(arr[0] +  "_" + arr[1] + "_" + num).click();
						}
						break;

			case 39:    // right arrow
						num = parseInt(arr[2]) + 1;
						if (num <= 100) {
							box = document.getElementById(arr[0] +  "_" + arr[1] + "_" + num).click();
						}
						break;	
		}				
	}		
	
	function ManeuversPanel_Clear_All_Button() {
		var ok = confirm("Are you sure you want erase all training and options. Click Yes to continue or No to cancel.");
		
		if( ok ) {
			ManeuversPanel_Erase_Training();	
		}
	}
	
	function ManeuversPanel_Erase_Training() {
		var title;
		hide_unused_maneuvers = false;
		document.getElementById("ManP_show_cm").checked = true;
		document.getElementById("ManP_show_level_ranks").checked = true;
		
		for( var i=0; i < maneuvers.list.length; i++ ) {
			title = maneuvers.list[i].name+"@"+maneuvers.list[i].type
			delete hidden_maneuvers[title];
			delete training_rate[title];
			
			for( var j=0; j <= 100; j++ ) {				
				delete man_ranks_by_level[j][title]
				delete total_man_ranks_by_level[j][title];
			}
		}		
		
		ManeuversPanel_Update_LeftSide();
		ManeuversPanel_Update_Rightside();
	//	StatisticsPanel_Calculate_Resources();
	}	
	
	function ManeuversPanel_Change_Maneuver_View() {
	//	var prof = document.getElementById("StP_selected_profession").value;
		var maneuver, multiplier = 2;
		
		if( selected_prof == "warrior" || selected_prof == "rogue" || selected_prof == "monk" ) {
			multiplier = 1;
		}
		else if( selected_prof == "bard" || selected_prof == "ranger" || selected_prof == "paladin" ) 	{
			multiplier = 1.5;
		}		
	
/*		
if( document.getElementById("ManP_hide_maneuvers").checked ) {		
		$(".test_class").hide();
		$(".test_class").hide();	
}
else {	
		$(".test_class").show();
		$(".test_class").show();		
}	
*/
		for( var i=0; i < avail_maneuvers.list.length; i++ ) {	
			maneuver = avail_maneuvers.list[i].name+"@"+avail_maneuvers.list[i].type;		
			
			//yeah I don't like the huge if statement either, but this panels causes sooooo much lag that I'll deal with it. For now.
			if( (avail_maneuvers.list[i].availability[selected_prof] == 1) &&
			(!document.getElementById("ManP_hide_maneuvers").checked || (document.getElementById("ManP_hide_maneuvers").checked &&  
			(document.getElementById(maneuver+"_checkbox").checked || total_man_ranks_by_level[100][maneuver] != undefined ))) &&
			((document.getElementById("ManP_show_cm").checked && avail_maneuvers.list[i].type == "combat") || 			
			(document.getElementById("ManP_show_sm").checked && avail_maneuvers.list[i].type == "shield") ||
			(document.getElementById("ManP_show_as").checked && avail_maneuvers.list[i].type == "armor"))				
			) {					
				document.getElementById(maneuver+"_info_row").style.display = "";
				document.getElementById(maneuver+"_training_row").style.display = "";	
		//		if( document.getElementById("ManP_show_cm").checked ) {
					document.getElementById(maneuver+"_cost1").innerHTML = Math.floor((avail_maneuvers.list[i].rank_costs[0] * multiplier)) || "-";
					document.getElementById(maneuver+"_cost2").innerHTML = Math.floor((avail_maneuvers.list[i].rank_costs[1] * multiplier)) || "-";
					document.getElementById(maneuver+"_cost3").innerHTML = Math.floor((avail_maneuvers.list[i].rank_costs[2] * multiplier)) || "-";
					document.getElementById(maneuver+"_cost4").innerHTML = Math.floor((avail_maneuvers.list[i].rank_costs[3] * multiplier)) || "-";
					document.getElementById(maneuver+"_cost5").innerHTML = Math.floor((avail_maneuvers.list[i].rank_costs[4] * multiplier)) || "-";
	//			}
			}			
			else {
				document.getElementById(maneuver+"_info_row").style.display = "none";
				document.getElementById(maneuver+"_training_row").style.display = "none";					
			}
		}		
		
	}

	function ManeuversPanel_Update_LeftSide() {
		document.getElementById("ManP_hide_maneuvers").checked = hide_unused_maneuvers;
		
		for( var i=0; i < avail_maneuvers.list.length; i++ ) {
			if( hidden_skills[avail_maneuvers.list[i]] != undefined ) {
				document.getElementById(avail_maneuvers.list[i].name+"@"+avail_maneuvers.list[i].type+"_checkbox").checked = true;
			}
			else {
				document.getElementById(avail_maneuvers.list[i].name+"@"+avail_maneuvers.list[i].type+"_checkbox").checked = false;						
			}			
		}		
	}	
		
	function ManeuversPanel_Update_Rightside(start_level=0) {
		for( var i=0; i < avail_maneuvers.list.length; i++ ) {
			ManeuversPanel_Training_Update_Row(avail_maneuvers.list[i].name, start_level);			
		}
		
		ManeuversPanel_Change_Maneuver_View();	
		ManeuversPanel_Calculate_Points();	
	}
	
	function ManeuversPanel_Calculate_Total_Ranks(man, start_level) {
		var rtotal = 0;				
		man = avail_maneuvers.GetObjectByName(man);		
		man_title = man.name + "@" + man.type;
		
		if( start_level > 0 && total_man_ranks_by_level[start_level-1][man_title] != undefined ) {
			rtotal = total_man_ranks_by_level[start_level-1][man_title];
		}
		
		for( var i=start_level; i <= 100; i++) {
			if( man_ranks_by_level[i][man_title] != undefined ) {
				rtotal += parseInt(man_ranks_by_level[i][man_title]);			
			}	
			
			if( rtotal != 0 ) {
				total_man_ranks_by_level[i][man_title] = rtotal;
			}
			else {
				delete total_man_ranks_by_level[i][man_title];	
			}
		}
	}	

	function ManeuversPanel_Training_Update_Row(man, start_level) {		
		var div, tranks, lranks;
		man = avail_maneuvers.GetObjectByName(man);
		man_title = man.name + "@" + man.type;
		
		for (var k=start_level; k <= 100; k++) {	
			div = document.getElementById(man_title + "_div_" + k);
			lranks = man_ranks_by_level[k][man_title] || 0;
			tranks = total_man_ranks_by_level[k][man_title] || 0;
			
			if( document.getElementById("ManP_show_total_ranks").checked && tranks > 0 ){
				div.innerHTML = tranks;		
			}
			else if( document.getElementById("SkP_show_level_ranks").checked && lranks > 0 ){
				div.innerHTML = lranks;
			}	
			else if( div.innerHTML != "" ) {
				div.innerHTML = "";	
			}			
		}	
	}	
	
	function ManeuversPanel_Calculate_Points() {		
		var skillname, multiplier = 2, man, man_title, lsum, usum;
	//	var prof = document.getElementById("StP_selected_profession").value;
		
		if( selected_prof == "warrior" || selected_prof == "rogue" || selected_prof == "monk" ) {
			multiplier = 1;
		}
		else if( selected_prof == "bard" || selected_prof == "ranger" || selected_prof == "paladin" ) 	{
			multiplier = 1.5;
		}
		
		if( document.getElementById("ManP_show_cm").checked ) {
			document.getElementById("man_points_used").innerHTML = "Combat Maneuver Points Used";
			document.getElementById("man_points_left").innerHTML = "Combat Maneuver Points Left";
			document.getElementById("man_points_total").innerHTML = "Combat Maneuver Points Total";
			skillname = "Combat Maneuvers";
		}
		else if( document.getElementById("ManP_show_sm").checked ) {
			document.getElementById("man_points_used").innerHTML = "Shield Maneuver Points Used";
			document.getElementById("man_points_left").innerHTML = "Shield Maneuver Points Left";
			document.getElementById("man_points_total").innerHTML = "Shield Maneuver Points Total";		
			skillname = "Shield Use";	
		}
		else {
			document.getElementById("man_points_used").innerHTML = "Armor Specialization Points Used";
			document.getElementById("man_points_left").innerHTML = "Armor Specialization Points Left";
			document.getElementById("man_points_total").innerHTML = "Armor Specialization Points Total";	
			skillname = "Armor Use";		
		}
				
		for(var i=0; i <= 100; i++) {
			usum = 0;
			lsum = 0;
			
			for(var j=0; j <= avail_maneuvers.list.length-1; j++) {
				man = avail_maneuvers.list[j];
				man_title = man.name+"@"+man.type;
				
				if( (avail_maneuvers.list[j].type == "combat" && skillname != "Combat Maneuvers") ||
				((avail_maneuvers.list[j].type == "shield" && skillname != "Shield Use")) ||
				((avail_maneuvers.list[j].type == "armor" && skillname != "Armor Use")) 
			    ) {
					continue;
				}
				if( man_ranks_by_level[i][man_title] != undefined ) {				
					for( var k=1; k <= man_ranks_by_level[i][man_title]; k++) {
						usum += Math.floor(man.GetCostAtRank(k+total_man_ranks_by_level[i][man_title]-man_ranks_by_level[i][man_title]) * multiplier);
					}				
				}
				
				for( var k=1; k <= total_man_ranks_by_level[i][man_title]; k++) {
					lsum += Math.floor(man.GetCostAtRank(k) * multiplier);
				}	
				
				document.getElementById("points_total_"+i).innerHTML = total_ranks_by_level[i][skillname] || 0 ;
			}			
			
			document.getElementById("points_used_"+i).innerHTML = usum;			
			document.getElementById("points_left_"+i).innerHTML = (total_ranks_by_level[i][skillname] || 0) - lsum;
		}		
	}
	
	function ManeuversPanel_Zero_Out_Maneuver_Row(man) {
		delete hidden_maneuvers[man]
		
		for( var i = 0; i <= 100; i++ ) {
			delete man_ranks_by_level[i][man];
			delete total_man_ranks_by_level[i][man];
		}
		
		ManeuversPanel_Training_Update_Row(man.split("@")[0], 0);
	}
	
	function ManeuversPanel_On_Prof_Change() {			
		for( var i=0; i < avail_maneuvers.list.length; i++ ) {			
			if( avail_maneuvers.list[i].availability[selected_prof] == 0  ) {
				ManeuversPanel_Zero_Out_Maneuver_Row(avail_maneuvers.list[i].name+"@"+avail_maneuvers.list[i].type);
			}
		}
		
		ManeuversPanel_Update_LeftSide();
		ManeuversPanel_Update_Rightside();
	}	
	
	function ManeuversPanel_Update_Available_Maneuvers() {
		avail_maneuvers = new Object_List();
		for( var i=0; i < maneuvers.list.length; i++ ) {
			if( maneuvers.list[i].availability[selected_prof] == 1 ) {
				avail_maneuvers.AddObject(maneuvers.list[i]);
			}	
		}		
	}	
