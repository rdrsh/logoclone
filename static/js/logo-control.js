function setLogoControl($el) {
	var sForm = '<form id="logo-form"><input id="logo-q"/> <input id="logo-button" type="button" value="Поиск"/></form>'
	var sDrag = '<div id="drag"><table><tr><td id="logo-td-1"></td><td id="logo-td-2"></td></tr></table></div>'
	$($el).hide().after(sForm+sDrag)//.show()
	
	var idList = $($el).val()
	$.get('/ajax/logo/'+idList+'', function(html){
		$('#logo-td-2').html(html)
		REDIPS.drag.init();
	})
	
	$('#logo-button').click(function(){
		var q = $('#logo-q').val()
		$.post('/ajax/logo/', { q:q }, function(html){
			$('#logo-td-1').html(html)
			REDIPS.drag.init();
		});
	});
	
	REDIPS.drag.myhandler_dropped = function() {
		var idList = []
		$('#logo-td-2 img').each(function(){
			var id = $(this).attr('id').replace('logo-', '')
			idList.push(id)
		})
		$($el).val(idList.join(','))
	}
} 