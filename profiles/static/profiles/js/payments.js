// Code taken from Code Institute Boutique Ado project

// Handle form submit

var form = $('#signup_form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
});

// var signup_form = document.getElementById('signup_form');

// signup_form.addEventListener('submit', function(ev) {
//     console.log("HELLO")
//     ev.preventDefault();
    // card.update({ 'disabled': true});
    // $('#submit-button').attr('disabled', true);
    // // $('#payment-form').fadeToggle(100);
    // $('#loading-overlay').fadeToggle(100);

    // // var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // // From using {% csrf_token %} in the form
    // var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    // var postData = {
    //     'csrfmiddlewaretoken': csrfToken,
    //     'client_secret': clientSecret,
    //     // 'save_info': saveInfo,
    // };
    // // var url = '/checkout/cache_checkout_data/';

    // $.post(url, postData).done(function () {
    //     stripe.confirmCardPayment(clientSecret, {
    //         payment_method: {
    //             card: card,
    //             billing_details: {
    //                 name: $.trim(form.full_name.value),
    //                 phone: $.trim(form.phone_number.value),
    //                 email: $.trim(form.email.value),
    //                 address:{
    //                     line1: $.trim(form.street_address1.value),
    //                     line2: $.trim(form.street_address2.value),
    //                     city: $.trim(form.town_or_city.value),
    //                     country: $.trim(form.country.value),
    //                     state: $.trim(form.county.value),
    //                 }
    //             }
    //         },
    //         // shipping: {
    //         //     name: $.trim(form.full_name.value),
    //         //     phone: $.trim(form.phone_number.value),
    //         //     address: {
    //         //         line1: $.trim(form.street_address1.value),
    //         //         line2: $.trim(form.street_address2.value),
    //         //         city: $.trim(form.town_or_city.value),
    //         //         country: $.trim(form.country.value),
    //         //         postal_code: $.trim(form.postcode.value),
    //         //         state: $.trim(form.county.value),
    //         //     }
    //         },
    //     }).then(function(result) {
    //         if (result.error) {
    //             var errorDiv = document.getElementById('card-errors');
    //             var html = `
    //                 <span class="icon" role="alert">
    //                 <i class="fas fa-times"></i>
    //                 </span>
    //                 <span>${result.error.message}</span>`;
    //             $(errorDiv).html(html);
    //             $('#payment-form').fadeToggle(100);
    //             $('#loading-overlay').fadeToggle(100);
    //             card.update({ 'disabled': false});
    //             $('#submit-button').attr('disabled', false);
    //         } else {
    //             if (result.paymentIntent.status === 'succeeded') {
    //                 form.submit();
    //             }
    //         }
    //     });
    // }).fail(function () {
    //     // just reload the page, the error will be in django messages
    //     location.reload();
    // })
});