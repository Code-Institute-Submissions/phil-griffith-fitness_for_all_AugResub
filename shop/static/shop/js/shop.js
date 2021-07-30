$(document).ready(function () {
    $( ".del_prod" ).click(function() {
    console.log("Delete clicked");
    var product_id = $(this).prev('input[name="product_id"]').val();
    console.log(product_id)
    $('input[name="product_id"]').val(product_id);

    });

    $( "#test" ).click(function() {
        console.log("Delete clicked");
        var product_id = $(this).prev('input[name="product_id"]').val();
    
        $("#modal_body").html(product_id);
    });
});