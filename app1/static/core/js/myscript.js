$('.plus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var elm=this.parentNode.children[2]
    // console.log(id);
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id:id,
            
        },
        success:function(data){
            console.log(data);
            elm.innerText=data.quantity
            // document.getElementById('quantity').innerText=data.quantity
            document.getElementById('amount').innerText=data.amount
            document.getElementById('total-amount').innerText=data.total_amount
        }

    })

})

$('.minus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var elm=this.parentNode.children[2]
    // console.log(id);
    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            prod_id:id,
            
        },
        success:function(data){
            console.log(data);
            elm.innerText=data.quantity
            // document.getElementById('quantity').innerText=data.quantity
            document.getElementById('amount').innerText=data.amount
            document.getElementById('total-amount').innerText=data.total_amount
        }

    })

})


