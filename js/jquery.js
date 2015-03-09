//JQuery functions
	 	 
 function Jquery_Update_Scroller_Positions() {
	scroller_V = $(this).scrollTop() || scroller_V;
	scroller_H = $(this).scrollLeft() || scroller_H;
	switch(Planner_Get_Active_Panel()) {
		case "statistics":	break;
		case "skills":		if( this.id == "SkP_skills_training_container") { 
								$("#SkP_skills_info_container").scrollTop(scroller_V);						
							}
							else {
								$("#SkP_skills_training_container").scrollTop(scroller_V);
	//							$("#SkP_skills_training_container").scrollTop(scroller_H);
							}
							break;
		case "maneuvers":	if( this.id == "ManP_maneuvers_training_container") { 
								$("#ManP_maneuvers_info_container").scrollTop(scroller_V);						
							}
							else {
								$("#ManP_maneuvers_training_container").scrollTop(scroller_V);
							}
							break;							
	}
 }
 
 //This isn't working very well. Try to think of something else
 function Jquery_Scroller_Onmousedown() {	             //meant to fire when they move the scrollbar
	if( scroller_V != $(this).scrollTop() ) {	
		scroller_V = $(this).scrollTop();
		$("#SkP_skills_info_container").scrollTop(scroller_V);	
	}
	else if( scroller_H != $(this).scrollTop() ) {
		scroller_H = $(this).scrollLeft();		
		Jquery_Update_Scroller_Positions();
	}
	 
 }
 
 
 
 
 
$(document).ready(function(){	
//MAIN	
	 $(".panel_tab").click(function(){
		Planner_Show_Panel(this.id.split('_')[0]);
     });
	 
	 
//Statistics Tab	 
	 $("#StP_growth_container").scroll(Jquery_Update_Scroller_Positions);
	 
	 
//Skills Tab
	//$("#SkP_skills_training_container").mousedown(Jquery_Scroller_Onmousedown);
	$("#SkP_skills_training_container").scroll(Jquery_Update_Scroller_Positions);
	$("#SkP_skills_info_container").bind('mousewheel DOMMouseScroll', function(event){
		if (event.originalEvent.wheelDelta > 0 || event.originalEvent.detail < 0) {   // scroll up 			
			scroller_V -= 42;
			scroller_V = Math.max(scroller_V, 0);
			Jquery_Update_Scroller_Positions();
		}
		else {    // scroll down        
			scroller_V += 42;
			scroller_V = Math.min(scroller_V, document.getElementById("SkP_skills_info_container").scrollHeight);
			Jquery_Update_Scroller_Positions();
		}
	});

	
//Maneuvers Tab
	$("#ManP_maneuvers_training_container").scroll(Jquery_Update_Scroller_Positions);
	$("#ManP_maneuvers_info_container").bind('mousewheel DOMMouseScroll', function(event){
		if (event.originalEvent.wheelDelta > 0 || event.originalEvent.detail < 0) {   // scroll up 			
			scroller_V -= 42;
			scroller_V = Math.max(scroller_V, 0);
			Jquery_Update_Scroller_Positions();
		}
		else {    // scroll down        
			scroller_V += 42;
			scroller_V = Math.min(scroller_V, document.getElementById("ManP_maneuvers_info_container").scrollHeight);
			Jquery_Update_Scroller_Positions();
		}
	});
	
});
	
