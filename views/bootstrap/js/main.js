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
    $("#luckNumbers").empty();
    $("#luckPercent").empty();
    
    mg = data['magic_numbers'];
    numbers = '';
    for (m in mg){
        num = mg[m];
        if (num < 10){
            num = '0'+num;
        }
        dv = '<div class="luck_numbers">'+num+'</div>'
        $("#luckNumbers").append(dv);
    }
    $("#luckPercent").html('<h4> Probabilidade de Acerto: ' + data['percent'] + ' % <h4>');
}

function showOrderNumbers(data){
    $("#orderNumbers").empty();
    $("#orderPercent").empty();
    
    mg = data['magic_numbers'];
    numbers = '';
    for (m in mg){
        num = mg[m];
        if (num < 10){
            num = '0'+num;
        }
        dv = '<div class="numbers">'+num+'</div>'
        $("#orderNumbers").append(dv);
    }
    $("#orderPercent").html('<h4> Probabilidade de Acerto: ' + data['percent'] + ' % <h4>');
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
