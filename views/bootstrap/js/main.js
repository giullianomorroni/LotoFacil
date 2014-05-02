var HOST = location.host;
var PROTOCOL = location.protocol;

$("#estouComSorteLink").click(function(event){
	$.ajax({
		url: _url('estoucomsorte'),
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
    mg = data['magic_numbers'];
    numbers = '';
    for (m in mg){
        dv = '<div class="numbers">'+mg[m]+'</div>'
        $("#luckNumbers").append(dv);
    }
    $("#luckPercent").html('<h4> Probabilidade de Acerto: ' + data['percent'] + ' % <h4>');
}

function showOrderNumbers(data){
    $("#orderNumbers").html(data['magic_numbers']);
    $("#orderPercent").html(data['percent']);
}

function order(method){
    u = _url('pastelaria/'+method);
    $.ajax({
        url: u,
        type: "get",
        async: false,
        success: function(data) { showOrderNumbers(data); },
        dataType: "json",
        accepts: {
            text: "application/json"
        }
    });
}

function _url(method){
	return (PROTOCOL+"//"+HOST+"/"+method);
}
