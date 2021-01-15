function validaLogin() {
    var nombreUsuario = document.getElementById('txtNombreUsuario');
    var contraseña = document.getElementById('txtContraseña');

    if (nombreUsuario.value == "") {
        alert("Ingrese su nombre de usuario");
        nombreUsuario.focus();
        return false;
    }

    if (contraseña.value == "") {
        alert("Ingrese su contraseña");
        contraseña.focus();
        return false;
    }
}

let validarRut = () => {
    let rutvalido = true;

    try {

        let rutCompleto = document.getElementById("rut").value + "-" + document.getElementById("dv").value;

        // Se genera un objeto rut
        let rut = {
            number: document.getElementById("rut").value,
            dv: document.getElementById("dv").value
        };

        let sum = 0;
        let multiply = 2;

        // Calcular rut
        for (let i = 1; i <= rut.number.length; i++) {
            let index = multiply * rutCompleto.charAt(rut.number.length - i);

            sum = sum + index;

            if (multiply < 7) multiply = multiply + 1;
            else multiply = 2;
        }

        // Obtener identificador 
        let awaitedDigit = 11 - (sum % 11);

        // Convertir letras a numeros
        rut.dv = rut.dv === "k" || rut.dv === "K" ? 10 : rut.dv;
        rut.dv = rut.dv === 0 ? 11 : rut.dv;

        // El rut no es valido si el numero ingresado es diferente al calculo
        if (awaitedDigit != rut.dv) throw 0;
    } catch {
        rutvalido = false;
    }

    return rutvalido;
}

let setErrorMessage = () => {

    if (!validarRut() && !!document.getElementById("dv").value) {
        alert("El rut no es valido")
    }
};

let enviarDatos = function(e) {
    console.log("No se enviará nada")

    if (!validarRut()) {
        e.preventDefault();

        return;


    }
    alert("Datos enviados correctamente")



}