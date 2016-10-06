$('#submit-survey').on('click', function submitSurvey() {
	var gender = $("input[name=gender]").val();
	var color = $("input[name=color]").val();
	var school = $("input[name=school]").val();
	var company = $("input[name=company]").val();
	var feBefore = $("input[name=front-end-before]").val();
	var feAfter = $("input[name=front-end-after]").val();
	var frontendlan = $("input[name=frontendlan]").val();

	$.post("submit-survey",
	{gender:gender,
		color:color,
		school:school,
		company:company,
		feBefore:feBefore,
		feAfter:feAfter,
		frontendlan:frontendlan},
		function(data){
			$("html").html(data);
		})
	// not working...?
	

});

$("#results-email-container").on('click', '#email-results-button', function emailResults() {
	console.log($(this));
});

$("#site-title-wrapper").on('click', function goHome() {
	window.location.href = '/';
});

$(document).ready(function applySliderLabels() {
	var currentValue = $("#fe-before").val();
	$("#fe-before").next().html(currentValue);

	currentValue = $("#fe-after").val();
	$("#fe-after").next().html(currentValue);
});


$("input[type='range']").on('change', function updateLabel() {
	var currentValue = $(this).val();
	$(this).next().html(currentValue);
});