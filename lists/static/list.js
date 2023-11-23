window.Superlists = {};

window.Superlists.updateItems = (url) => {
	$.get(url).done((response) => {
		var rows = '';
		for (var i=0; i < response.length; i++) {
			var item = response[i];
			rows += '\n<tr><td>' + (i+1) + ': ' + item.text + '</td></tr>';
		}
		$('#id_list_table tbody').html(rows);
	})
}

window.Superlists.initialize = (url) => {	
	$('input[name="text"]').on('focus', () => {
		$('.has-error').hide();
	})
	$('input[name="text"]').on('keypress', () => {
		$('.has-error').hide();
	});
	if (url) {
		window.Superlists.updateItems(url);
		var form = $('#id_item_form');
		form.on('submit', (event) => {
			event.preventDefault();
			$.post(url, {
				'text': form.find('input[name="text"]').val(),
				'csrfmiddlewaretoken': form.find('input[name="csrfmiddlewaretoken"]').val(),
			}).done(() => {
				window.Superlists.updateItems(url);
				$('.has-error').hide();
				$('.has-error .help-block').text('');
			}).fail((response) => {
				$('.has-error').show();
				$('.has-error .help-block').text(response.responseJSON.error);
			})
		})
	}
};

