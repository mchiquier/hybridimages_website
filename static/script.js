$( document ).ready(function(){
$("#form").submit(function(e) {
    alert("abc");


    var form = $(this);
    var url = form.attr('action');

    $.ajax({
           type: "GET",
           url: url,
           data: form.serialize(), // serializes the form's elements.
           success: function(data)
           {
               alert(data); // show response from the php script.
               console.log("Changing src to" + data);
               document.getElementById("resilt-image").src = data;
               console.log("Changed src to" + data);
           }
         });

    e.preventDefault(); // avoid to execute the actual submit of the form.
});
}); 