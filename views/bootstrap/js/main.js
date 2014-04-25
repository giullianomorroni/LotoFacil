var HOST = location.host;
var PROTOCOL = location.protocol;

$("#estouComSorteLink").click(function(event){

	$.ajax({
		url: _url('estoucomsorte/'),
		type: "get",
		async: false,
		success: function(data) { showLuckNumbers(data); },
		dataType: "json",
		accepts: {
			text: "application/json"
		}
	});	

});

function showLuckNumbers(data) {
	console.log("showLuckNumbers " + data['magic_numbers'])
	$("#luckNumbers").html(data['magic_numbers']);
}

function _url(method){
	return (PROTOCOL+"//"+HOST+"/"+method);
}
