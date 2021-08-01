$(document).ready(function () {
    $( ".del_workout" ).click(function() {
        var workout_id = $(this).prev('input[name="workout_id"]').val();
        $('input[name="workout_id"]').val(workout_id);
    });
});