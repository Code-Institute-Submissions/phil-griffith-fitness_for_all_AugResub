$(document).ready(function () {
    $( ".del_workout" ).click(function() {
    console.log("Delete clicked");
    var workout_id = $(this).prev('input[name="workout_id"]').val();
    console.log(workout_id)
    $('input[name="workout_id"]').val(workout_id);

    $( ".test" ).click(function() {
        console.log("Delete clicked");

    });
});
});