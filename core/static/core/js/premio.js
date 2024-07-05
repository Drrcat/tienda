$(document).ready(function() {
  $.get('https://fakestoreapi.com/products', function(registros) {
    $('#recuadro-de-ropa').empty();

    $.each(registros, function(i, item) {
      var recuadro = `
        <div class="card col-md-3 col-sm-6 mb-4">
          <img src="${item.image}" class="card-img-top" alt="Producto">
          <div class="card-body">
            <h5 class="card-title">${item.title}</h5>
            <p class="card-text">${item.description}</p>
            <p class="card-text"><strong>$${item.price}</strong></p>
          </div>
        </div>
      `;

      $('#recuadro-de-ropa').append(recuadro);
    });

    setTimeout(function() {
      $('#imagen-de-espera').hide();
      $('#capa-cubre-todo').hide();
    }, 2000);
  });
});


