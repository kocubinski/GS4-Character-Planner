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

function Maneuver_List() {
 this.list = [];	

 this.AddManeuver = function(name, mnemonic, type, rank_costs, avail, prereq) {
  this.list[this.list.length] = new Maneuver(name, mnemonic, type, rank_costs, avail, prereq);
 };
  
 this.GetManeuverByName = function( input ) {
	for (var i=0; i < this.list.length; i++) {
		if( this.list[i].name == input ) {
			return this.list[i];
		}
	}
	return null;	 
 };	 
 
 this.GetListPositionByMnemonic = function( input ) {
	for (var i=0; i < this.list.length; i++) {
		if( this.list[i].name == input ) {
			return i;
		}
	}
	return -1;
 };
	

}


 var all_maneuvers = new Maneuver_List();
//Add all Combat Maneuvers to list
all_maneuvers.AddManeuver("Armor Spike Focus", "SPIKEFOCUS", "combat", "5,10", "warrior,rogue,paladin", "");
all_maneuvers.AddManeuver("Bearhug", "BEARHUG", "combat", "2,4,6,8,10", "warrior,monk", "");
all_maneuvers.AddManeuver("Berserk", "BERSERK", "combat", "2,4,6,8,10", "warrior", "");
all_maneuvers.AddManeuver("Block Mastery", "BMASTERY", "combat", "4,8,12", "warrior", "");
all_maneuvers.AddManeuver("Bull Rush", "BULLRUSH", "combat", "2,4,6,8,10", "warrior,paladin", "");
all_maneuvers.AddManeuver("Burst of Swiftness", "BURST", "combat", "2,4,6,8,10", "monk", "");
all_maneuvers.AddManeuver("Charge", "Charge", "combat", "2,4,6,8,10", "warrior,bard,monk,paladin", "");
all_maneuvers.AddManeuver("Cheapshots", "CHEAPSHOTS", "combat", "2,3,4,5,6", "bard,monk,rogue", "");
all_maneuvers.AddManeuver("Combat Focus", "FOCUS", "combat", "2,4,6,8,10", "warrior,rogue,ranger,bard,monk,paladin", "");
all_maneuvers.AddManeuver("Combat Mastery", "CMASTERY", "combat", "2,4", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", "");
all_maneuvers.AddManeuver("Combat Mobility", "MOBILITY", "combat", "5,10", "warrior,rogue,monk", "");
all_maneuvers.AddManeuver("Combat Movement", "CMOVEMENT", "combat", "2,3,4,5,6", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", "");
all_maneuvers.AddManeuver("Combat Toughness", "TOUGHNESS", "combat", "6,8,10", "warrior,rogue,monk,paladin", "");
all_maneuvers.AddManeuver("Coup de Grace", "COUPDEGRACE", "combat", "2,4,6,8,10", "warrior,rogue", "");
all_maneuvers.AddManeuver("Crowd Press", "CPRESS", "combat", "2,4,6,8,10", "warrior,rogue,monk,paladin", "");
all_maneuvers.AddManeuver("Cunning Defense", "CDEFENSE", "combat", "2,3,4,5,6", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", "");
all_maneuvers.AddManeuver("Cutthroat", "CUTTROAT", "combat", "2,4,6,8,10", "warrior,rogue,monk,paladin", "");
all_maneuvers.AddManeuver("Dirtkick", "DIRTKICK", "combat", "2,3,4,5,6", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", "");
all_maneuvers.AddManeuver("Disarm Weapon", "DISARM", "combat", "2,4,6,8,10", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", "");
all_maneuvers.AddManeuver("Divert", "DIVERT", "combat", "2,3,4,5,6", "rogue", "");
all_maneuvers.AddManeuver("Duck and Weave", "WEAVE", "combat", "4,8,12", "rogue,monk", "CM|Evade Mastery:2");
all_maneuvers.AddManeuver("Dust Shroud", "SHROUD", "combat", "2,3,4,5,6", "rogue", "CM|Dirtkick:4");
all_maneuvers.AddManeuver("Evade Mastery", "EMASTERY", "combat", "4,8,12", "warrior,rogue,monk", "");
all_maneuvers.AddManeuver("Executioner's Stance", "EXECUTIONER", "combat", "4,8,12", "warrior", "");
all_maneuvers.AddManeuver("Feint", "FEINT", "combat", "2,3,5,7,10", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", "");
all_maneuvers.AddManeuver("Flurry of Blows", "FLURRY", "combat", "3,6,9", "monk", "");
all_maneuvers.AddManeuver("Garrote", "GARROTE", "combat", "2,4,6,8,10", "rogue,ranger,bard,monk", "");
all_maneuvers.AddManeuver("Grapple Mastery", "GMASTERY", "combat", "4,8,12", "warrior,rogue,monk", "");
all_maneuvers.AddManeuver("Griffin's Voice", "GRIFFIN", "combat", "3,6,9", "warrior", "");
all_maneuvers.AddManeuver("Groin Kick", "GKICK", "combat", "2,4,6,8,10", "rogue", "");
all_maneuvers.AddManeuver("Hamstring", "HAMSTRING", "combat", "2,4,6,8,10", "warrior,ranger,bard,rogue", "");
all_maneuvers.AddManeuver("Haymaker", "HAYMAKER", "combat", "2,4,6,8,10", "warrior", "");
all_maneuvers.AddManeuver("Headbutt", "HEADBUTT", "combat", "2,3,4,5,6", "warrior,monk", "");
all_maneuvers.AddManeuver("Inner Harmony", "IHARMONY", "combat", "4,8,12", "monk", "");
all_maneuvers.AddManeuver("Internal Power", "IPOWER", "combat", "2,4,6,8,10", "monk", "");
all_maneuvers.AddManeuver("Ki Focus", "KIFOCUS", "combat", "3,6,9", "monk", "");
all_maneuvers.AddManeuver("Kick Mastery", "KMASTERY", "combat", "4,8,12", "warrior,rogue,monk", "");
all_maneuvers.AddManeuver("Mighty Blow", "MBLOW", "combat", "2,4,6,8,10", "warrior", "");
all_maneuvers.AddManeuver("Multi-Fire", "MFIRE", "combat", "2,4,6,8,10", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", "");
all_maneuvers.AddManeuver("Mystic Strike", "MYSTICSTRIKE", "combat", "2,3,4,5,6", "monk", "");
all_maneuvers.AddManeuver("Parry Mastery", "PMASTERY", "combat", "4,8,12", "warrior", "");
all_maneuvers.AddManeuver("Perfect Self", "PERFECTSELF", "combat", "2,4,6,8,10", "monk", "CM|Burst of Speed:3,CM|Surge of Strength:3");
all_maneuvers.AddManeuver("Precision", "PRECISION", "combat", "4,6", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", "");
all_maneuvers.AddManeuver("Predator's Eye", "PREDATOR", "combat", "4,6,8", "rogue", "");
all_maneuvers.AddManeuver("Punch Mastery", "PUNCHMASTERY", "combat", "4,8,12", "warrior,rogue,monk", "");
all_maneuvers.AddManeuver("Quickstrike", "QSTRIKE", "combat", "2,4,6,8,10", "warrior,rogue,monk", "");
all_maneuvers.AddManeuver("Rolling Krynch Stance", "KRYNCH", "combat", "4,8,12", "monk", "");
all_maneuvers.AddManeuver("Shadow Mastery", "SMASTERY", "combat", "2,4,6,8,10", "ranger,rogue", "");
all_maneuvers.AddManeuver("Shield Bash", "SBASH", "combat", "2,4,6,8,10", "ranger,rogue,warrior,bard,paladin", "");
all_maneuvers.AddManeuver("Shield Charge", "SCHARGE", "combat", "2,4,6,8,10", "warrior,paladin", "");
all_maneuvers.AddManeuver("Side By Side", "SIDEBYSIDE", "combat", "2,4,6,8,10", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", "CM:Combat Movement:2");
all_maneuvers.AddManeuver("Silent Strike", "SILENTSTRIKE", "combat", "2,4,6,8,10", "rogue", "CM|Shadow Mastery:2");
all_maneuvers.AddManeuver("Slippery Mind", "SLIPPERYMIND", "combat", "4,8,12", "rogue", "CM|Shadow Mastery:2");
all_maneuvers.AddManeuver("Specialization I", "WSPEC1", "combat", "2,4,6,8,10", "warrior,rogue,paladin", "");
all_maneuvers.AddManeuver("Specialization II", "WSPEC2", "combat", "2,4,6,8,10", "warrior,rogue,paladin", "");
all_maneuvers.AddManeuver("Specialization III", "WSPEC3", "combat", "2,4,6,8,10", "warrior,rogue,paladin", "");
all_maneuvers.AddManeuver("Spell Cleaving", "SCLEAVE", "combat", "2,4,6,8,10", "warrior,monk", "");
all_maneuvers.AddManeuver("Spell Parry", "SPARRY", "combat", "4,8,12", "warrior,Rouge,monk", "");
all_maneuvers.AddManeuver("Spell Thieve", "SATTACK", "combat", "2,4,6,8,10", "rogue", "");
all_maneuvers.AddManeuver("Spin Attack", "THIEVE", "combat", "2,4,6,8,10", "warrior,rogue, bard,monk", "");
all_maneuvers.AddManeuver("Staggering Blow", "SBLOW", "combat", "2,4,6,8,10", "warrior", "");
all_maneuvers.AddManeuver("Stance of the Mongoose", "MONGOOSE", "combat", "4,8,12", "warrior,monk", "");
all_maneuvers.AddManeuver("Stun Maneuvers", "STUNMAN", "combat", "2,4,6,8,10", "warrior,monk,rogue", "");
all_maneuvers.AddManeuver("Subdual Strike", "SSTRIKE", "combat", "2,3,4,5,6", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", "");
all_maneuvers.AddManeuver("Subdue", "SUBDUE", "combat", "2,3,4,5,6", "rogue", "");
all_maneuvers.AddManeuver("Sucker Punch", "SPUNCH", "combat", "2,3,4,5,6", "rogue", "");
all_maneuvers.AddManeuver("Sunder Shield", "SUNDER", "combat","2,4,6,8,10", "warrior", "");
all_maneuvers.AddManeuver("Surge of Strength", "SURGE", "combat", "2,4,6,8,10", "warrior,monk,rogue,paladin", "");
all_maneuvers.AddManeuver("Sweep", "SWEEP", "combat", "2,4,6,8,10", "bard,monk,ranger,rogue", "");
all_maneuvers.AddManeuver("Tackle", "TACKLE", "combat", "2,4,6,8,10", "warrior", "");
all_maneuvers.AddManeuver("Tainted Bond", "TAINTED", "combat", "20", "warrior,paladin", "CM|Weapon Bonding:5~Skill|Spell Research, Paladin Base:25");
all_maneuvers.AddManeuver("Trip", "TRIP", "combat", "2,4,6,8,10", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", "");
all_maneuvers.AddManeuver("Truehand", "TRUEHAND", "combat", "2,4,6,8,10", "warrior,paladin,rogue", "");
all_maneuvers.AddManeuver("Twin Hammerfists", "TWINHAMM", "combat", "2,4,6,8,10", "warrior", "");
all_maneuvers.AddManeuver("Unarmed Specialist", "UNARMEDSPEC", "combat", "6", "warrior,rogue,ranger,bard,monk,paladin,cleric,empath,sorcerer,wizard,savant", "");
all_maneuvers.AddManeuver("Vanish", "VANISH", "combat", "4,8,12", "rogue", "CM|Shadow Mastery:4");
all_maneuvers.AddManeuver("Weapon Bonding", "BOND", "combat", "2,4,6,8,10", "warrior", "CM|Specialization I:3~CM|Specialization II:3~CM|Specialization III:3");
all_maneuvers.AddManeuver("Whirling Dervish", "DERVISH", "combat", "4,8,12", "warrior,rogue", "");

// Add all Shield Maneuvers to the list
all_maneuvers.AddManeuver("Small Shield Focus", "SFOCUS", "shield", "4,6,8,10,12", "warrior,rogue", "");
all_maneuvers.AddManeuver("Medium Shield Focus", "MFOCUS", "shield", "4,6,8,10,12", "warrior,rogue,paladin", "");
all_maneuvers.AddManeuver("Large Shield Focus", "LFOCUS", "shield", "4,6,8,10,12", "warrior,paladin", "");
all_maneuvers.AddManeuver("Tower Shield Focus", "TFOCUS", "shield", "4,6,8,10,12", "warrior,paladin", "");
all_maneuvers.AddManeuver("Shield Bash", "SBASH", "shield", "2,4,6,8,10", "warrior,rogue,paladin", "");
all_maneuvers.AddManeuver("Shield Charge", "SCHARGE", "shield", "2,4,6,8,10", "warrior,paladin", "SM|Shield Bash:2~CM|Shield Bash:2");
all_maneuvers.AddManeuver("Shield Push", "PUSH", "shield", "2,4,6,8,10", "warrior,paladin", "SM|Shield Bash:2~CM|Shield Bash:2");
all_maneuvers.AddManeuver("Shield Pin", "PIN", "shield", "2,4,6,8,10", "warrior", "SM|Shield Bash:2~CM|Shield Bash:2");
all_maneuvers.AddManeuver("Shield Swiftness", "SWIFTNESS", "shield", "6,12,18", "warrior,rogue", "SM|Small Shield Focus:3~SM|Medium Shield Focus:3");
all_maneuvers.AddManeuver("Shield Brawler", "BRAWLER", "shield", "6,8,10,12,14", "warrior,rogue,paladin", "SM|Small Shield Focus:3~SM|Medium Shield Focus:3~SM|Large Shield Focus:3~SM|Tower Shield Focus:3");
all_maneuvers.AddManeuver("Prop Up", "PROP", "shield", "6,12,18", "warrior,paladin", "SM|Large Shield Focus:3~SM|Tower Shield Focus:3");
all_maneuvers.AddManeuver("Adamantine Bulwark", "BULWARK", "shield", "6,12,18", "warrior", "SM|Prop Up:2");
all_maneuvers.AddManeuver("Shield Riposte", "RIPOSTE", "shield", "4,8,12", "warrior,rogue", "SM|Shield Bash:2~CM|Shield Bash:2");
all_maneuvers.AddManeuver("Shield Forward", "FORWARD", "shield", "4,8,12", "warrior,rogue,paladin", "");
all_maneuvers.AddManeuver("Shield Spike Focus", "SPIKEFOCUS", "shield", "8,12", "warrior,rogue,paladin", "");
all_maneuvers.AddManeuver("Shield Spike Mastery", "SPIKEMASTERY", "shield", "8,12", "warrior,rogue,paladin", "SM|Shield Spike Focus:2");
all_maneuvers.AddManeuver("Deflection Training", "DTRAINING", "shield", "6,12,18", "warrior,rogue", "SM|Small Shield Focus:3~SM|Medium Shield Focus:3~SM|Large Shield Focus:3~SM|Tower Shield Focus:3");
all_maneuvers.AddManeuver("Deflection Mastery", "DMASTERY", "shield", "8,10,12,14,16", "warrior,rogue", "SM|Deflection Training:3");
all_maneuvers.AddManeuver("Block the Elements", "EBLOCK", "shield", "6,12,18", "warrior,paladin", "");
all_maneuvers.AddManeuver("Deflect the Elements", "DEFLECT", "shield", "6,12,18", "warrior,rogue", "");
all_maneuvers.AddManeuver("Steady Shield", "STEADY", "shield", "4,6", "warrior,rogue", "CM|Stun Maneuvers:2");
all_maneuvers.AddManeuver("Disarming Presence", "DPRESENCE", "shield", "6,12,18", "warrior,rogue", "CM|Disarm Weapon:2");
all_maneuvers.AddManeuver("Guard Mastery", "GUARDMASTERY", "shield", "6,12,18", "warrior", "");
all_maneuvers.AddManeuver("Tortoise Stance", "TORTOISE", "shield", "6,12,18", "warrior", "SM|Block Mastery:2");
all_maneuvers.AddManeuver("Spell Block", "SPELLBLOCK", "shield", "6,12,18", "warrior,rogue,paladin", "SM|Small Shield Focus:3~SM|Medium Shield Focus:3~SM|Large Shield Focus:3~SM|Tower Shield Focus:3");
all_maneuvers.AddManeuver("Shield Mind", "MIND", "shield", "6,12,18", "warrior,rogue,paladin", "SM|Spell Block:2");
all_maneuvers.AddManeuver("Protective Wall", "PWALL", "shield", "4,6", "warrior,rogue,paladin", "SM|Tower Shield Focus:2");
all_maneuvers.AddManeuver("Shield Strike", "STRIKE", "shield", "2,4,6,8,10", "warrior,rogue,paladin", "SM|Shield Bash:2~CM|Shield Bash:2");
all_maneuvers.AddManeuver("Shield Strike Mastery", "STRIKEMASTERY", "shield", "30", "warrior,rogue,paladin", "SM|Shield Strike:2,Skill|Multi Opponent Combat:30");
all_maneuvers.AddManeuver("Shield Trample", "TRAMPLE", "shield", "2,4,6,8,10", "warrior", "SM|Shield Charge:2");
all_maneuvers.AddManeuver("Shield Trample Mastery", "TMASTERY", "shield", "8,10,12", "warrior", "SM|Shield Trample:3,Skill|Multi Opponent Combat:30");
all_maneuvers.AddManeuver("Steely Resolve", "RESOLVE", "shield", "6,12,18", "warrior,paladin", "SM|Tower Shield Focus:3");
all_maneuvers.AddManeuver("Phalanx", "PHALANX", "shield", "2,4,6,8,10", "warrior,rogue,paladin", "");

// Add all Armor Specializations to the list
all_maneuvers.AddManeuver("Crush Protection", "CRUSH", "armor", "20,30,40,50,60", "warrior", "");
all_maneuvers.AddManeuver("Puncture Protection", "PUNCTURE", "armor", "20,30,40,50,60", "warrior", "");
all_maneuvers.AddManeuver("Slash Protection", "SLASH", "armor", "20,30,40,50,60", "warrior", "");
all_maneuvers.AddManeuver("Armored Casting", "CASTING", "armor", "20,30,40,50,60", "paladin", "");
all_maneuvers.AddManeuver("Armored Evasion", "EVASION", "armor", "20,30,40,50,60", "rogue", "");
all_maneuvers.AddManeuver("Armored Fluidity", "FLUIDITY", "armor", "20,30,40,50,60", "paladin", "");
all_maneuvers.AddManeuver("Armor Reinforcement", "REINFORCE", "armor", "20,30,40,50,60", "warrior", "");
all_maneuvers.AddManeuver("Armored Stealth", "STEALTH", "armor", "20,30,40,50,60", "rogue", "");
all_maneuvers.AddManeuver("Armor Support", "SUPPORT", "armor", "20,30,40,50,60", "warrior", "");

 
 var man_ranks_by_level = [];
 var total_man_ranks_by_level = [];
	for (var i=0; i <= 100; i++) {
		man_ranks_by_level[i] = {};
		total_man_ranks_by_level[i] = {};
	} 



	function ManeuversPanel_Init() {
		var info_div = document.getElementById("ManP_maneuvers_info_container");
		var training_div = document.getElementById("ManP_maneuvers_training_container");
		var prof = document.getElementById("StP_selected_profession").value;
		
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
		for( var i=0; i < all_maneuvers.list.length; i++ ) {			
			tr = ManeuversPanel_Create_Maneuver_Row_Left(all_maneuvers.list[i]);
			info_tbdy.appendChild(tr);
			tr = ManeuversPanel_Create_Maneuver_Row_Right(all_maneuvers.list[i]);
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
					
		ManeuversPanel_Change_Maneuver_View();		
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
			
		if( !isNaN(caller.value)) {	
			if( caller.value == "" ) {				
				delete man_ranks_by_level[arr[2]][arr[0]];					
			}
			else {
				man_ranks_by_level[arr[2]][arr[0]] = parseInt(caller.value);				
			}	
			ManeuversPanel_Calculate_Total_Ranks(arr[0].split("@")[0], arr[2]);	
			ManeuversPanel_Training_Update_Row(arr[0].split("@")[0], arr[2]);		
		}					
		ManeuversPanel_Calculate_Points();
		
		if( arr[0] == "Combat Toughness-combat" ) {
			StatisticsPanel_Calculate_Resources();
		}
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
						for( var i=all_maneuvers.GetListPositionByMnemonic(arr[0].split("@")[0])+1; i <= all_maneuvers.list.length-1; i++ ) {
							nextskill = all_maneuvers.list[i].name+"@"+all_maneuvers.list[i].type;
							if( document.getElementById(nextskill+"_info_row").style.display != "none" ) {	
								document.getElementById(nextskill + "_" + arr[1] + "_" + arr[2]).click();
								break;
							}
						}					
						break;
						
			case 38:    // up arrow
						for( var i=all_maneuvers.GetListPositionByMnemonic(arr[0].split("@")[0])-1; i >= 0; i-- ) {
							nextskill = all_maneuvers.list[i].name+"@"+all_maneuvers.list[i].type;
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
	
	function ManeuversPanel_Change_Maneuver_View() {
		var prof = document.getElementById("StP_selected_profession").value;
		var maneuver, multiplier = 2;
		
		if( prof == "warrior" || prof == "rogue" || prof == "monk" ) {
			multiplier = 1;
		}
		else if( prof == "bard" || prof == "ranger" || prof == "paladin" ) 	{
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
		for( var i=0; i < all_maneuvers.list.length; i++ ) {	
			maneuver = all_maneuvers.list[i].name+"@"+all_maneuvers.list[i].type;		
			
			//yeah I don't like the huge if statement either, but this panels causes sooooo much lag that I'll deal with it. For now.
			if( (all_maneuvers.list[i].availability[prof] == 1) &&
			(!document.getElementById("ManP_hide_maneuvers").checked || (document.getElementById("ManP_hide_maneuvers").checked &&  
			(document.getElementById(maneuver+"_checkbox").checked || total_man_ranks_by_level[100][maneuver] != undefined ))) &&
			((document.getElementById("ManP_show_cm").checked && all_maneuvers.list[i].type == "combat") || 			
			(document.getElementById("ManP_show_sm").checked && all_maneuvers.list[i].type == "shield") ||
			(document.getElementById("ManP_show_as").checked && all_maneuvers.list[i].type == "armor"))				
			) {					
				document.getElementById(maneuver+"_info_row").style.display = "";
				document.getElementById(maneuver+"_training_row").style.display = "";	
		//		if( document.getElementById("ManP_show_cm").checked ) {
					document.getElementById(maneuver+"_cost1").innerHTML = (all_maneuvers.list[i].rank_costs[0] * multiplier) || "-";
					document.getElementById(maneuver+"_cost2").innerHTML = (all_maneuvers.list[i].rank_costs[1] * multiplier) || "-";
					document.getElementById(maneuver+"_cost3").innerHTML = (all_maneuvers.list[i].rank_costs[2] * multiplier) || "-";
					document.getElementById(maneuver+"_cost4").innerHTML = (all_maneuvers.list[i].rank_costs[3] * multiplier) || "-";
					document.getElementById(maneuver+"_cost5").innerHTML = (all_maneuvers.list[i].rank_costs[4] * multiplier) || "-";
	//			}
			}			
			else {
				document.getElementById(maneuver+"_info_row").style.display = "none";
				document.getElementById(maneuver+"_training_row").style.display = "none";					
			}
		}
		
		ManeuversPanel_Calculate_Points();
	}

	function ManeuversPanel_Training_Change_Style(start_level=0) {
		for( var i=0; i < all_maneuvers.list.length; i++ ) {
			ManeuversPanel_Training_Update_Row(all_maneuvers.list[i].name, start_level);			
		}
	}
	
	function ManeuversPanel_Calculate_Total_Ranks(man, start_level) {
		var rtotal = 0;				
		man = all_maneuvers.GetManeuverByName(man);		
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
		man = all_maneuvers.GetManeuverByName(man);
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
		var prof = document.getElementById("StP_selected_profession").value;
		
		if( prof == "warrior" || prof == "rogue" || prof == "monk" ) {
			multiplier = 1;
		}
		else if( prof == "bard" || prof == "ranger" || prof == "paladin" ) 	{
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
			
			for(var j=0; j <= all_maneuvers.list.length-1; j++) {
				man = all_maneuvers.list[j];
				man_title = man.name+"@"+man.type;
				
				if( (all_maneuvers.list[j].type == "combat" && skillname != "Combat Maneuvers") ||
				((all_maneuvers.list[j].type == "shield" && skillname != "Shield Use")) ||
				((all_maneuvers.list[j].type == "armor" && skillname != "Armor Use")) 
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
		document.getElementById(man+"_checkbox").checked = false;
		
		for( var i = 0; i <= 100; i++ ) {
			delete man_ranks_by_level[i][man];
			delete total_man_ranks_by_level[i][man];
		}
		
		ManeuversPanel_Training_Update_Row(man.split("@")[0], 0);
	}
	
	function ManeuversPanel_On_Prof_Change(prof) {			
		for( var i=0; i < all_maneuvers.list.length; i++ ) {			
			if( all_maneuvers.list[i].availability[prof] == 0  ) {
				ManeuversPanel_Zero_Out_Maneuver_Row(all_maneuvers.list[i].name+"@"+all_maneuvers.list[i].type);
			}
		}
		
		ManeuversPanel_Change_Maneuver_View();
	}	
