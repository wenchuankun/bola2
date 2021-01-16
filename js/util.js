function validaLogin() {
    var nombreUsuario = document.getElementById('txtrut');
    var contraseña = document.getElementById('txtContraseña');

    if (nombreUsuario.value == "") {
        alert("Ingrese su rut");
        nombreUsuario.focus();
        return false;
    }

    if (contraseña.value == "") {
        alert("Ingrese su contraseña");
        contraseña.focus();
        return false;
    }
}



$(function(){
    $("#btnlimpiar").click(function(){
        $('input').val('');
    });

})

