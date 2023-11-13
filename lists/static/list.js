window.Superlists = {};

window.Superlists.initialize = () => {	
	$('input[name="text"]').on('focus', () => {
		$('.has-error').hide();
	})
	$('input[name="text"]').on('keypress', () => {
		$('.has-error').hide();
	});
};
