$(function () {
	$('[data-decrease]').click(decrease);
	$('[data-increase]').click(increase);
	$('[data-value]').change(valueChange);
});

$('.image1').each(function (index, value1) {
	$(value1).addClass('d-none');

});

function decrease() {
	var value = $(this).parent().find('[data-value]').val();
	if (value > 0) {
		value--;
		$(this).parent().find('[data-value]').val(value);

	}

	$('.image1').each(function (index, value1) {
		if (index == value) {
			$(value1).addClass('d-none');
		}
	});
}

function increase() {
	var value = $(this).parent().find('[data-value]').val();
	if (value < 6) {
		value++;
		$(this).parent().find('[data-value]').val(value);
	}
	$('.image1').each(function (index, value1) {
		if (index == value - 1) {
			$(value1).removeClass('d-none');
		}
	});
}

function valueChange() {
	var value = $(this).val();
	if (value == undefined || isNaN(value) == true || value <= 0) {
		$(this).val(0);
	} else if (value >= 6) {
		$(this).val(6);
	}
}
$(document).ready(function () {
	$(".btnCalculate").click(function () {
		var str = parseInt($(".input1").val()) / parseInt($(".input2").val());
		if (isNaN($(".input1").val()) || isNaN($(".input2").val()) ||  parseInt($(".input1").val())< parseInt($(".input2").val())) {
			$('.alertform1').removeClass('d-none');
			$('.alertform2').addClass('d-none');
			$('.alertText1').html('Hesablamada problem baş verdi!');
		} else {
			$('.alertform1').addClass('d-none');
			$('.alertform2').removeClass('d-none');
			$('.alertText2').html('Hər gün ən az ' + parseInt(str) + ' səhifə oxumalısınız!')

		}

	});
});
$(document).ready(function () {

	$(".btnStart").click(function () {

		$('.form-div').removeClass('d-none');
		$('.btnFinish').removeClass('d-none');
		$('.btnStart').addClass('d-none');


	});
	$(".btnFinish").click(function () {

		$('.form-div').addClass('d-none');
		$('.btnFinish').addClass('d-none');
		$('.btnStart').removeClass('d-none');


	});


});