const nombre = document.getElementById("nombre");

nombre.addEventListener("input", function(){

    this.value = this.value.replace(/[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]/g, '');

});