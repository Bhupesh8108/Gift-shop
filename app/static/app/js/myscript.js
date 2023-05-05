$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 3,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 5,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 7,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})


$('.plus-cart').click(function() {
    var id = $(this).attr("value").toString();
    var eml = this.parentNode.children[2]

    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            "produc_id":id 
        },
        success: function(data) {
            eml.innerText = data.quantity;
        document.getElementById("amount").innerText = data.price;
    document.getElementById("total").innerText = data.total;}
    })
})


$('.minus-cart').click(function() {
    var id = $(this).attr("value").toString();
    console.log(id);
    var eml = this.parentNode.children[2]

    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            "produc_id":id 
        },
        success: function(data) {
            console.log(data);
            eml.innerText = data.quantity;
        document.getElementById("amount").innerText = data.price;
    document.getElementById("total").innerText = data.total;}
    })
})


$('.remove-cart').click(function() {
    var id = $(this).attr("value").toString();
    console.log(id);
    var eml = this.parentNode.children[2]

    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            "produc_id":id 
        },
        success: function(data) {
            console.log(data);
            eml.innerText = data.quantity;
        document.getElementById("amount").innerText = data.price;
    document.getElementById("total").innerText = data.total;}
    })
})


