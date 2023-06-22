function mostrarHora() {
    var fecha = new Date();
    var hora = fecha.getHours();
    var minutos = fecha.getMinutes();
    var segundos = fecha.getSeconds();
    hora = hora < 10 ? '0' + hora : hora;
    minutos = minutos < 10 ? '0' + minutos : minutos;
    segundos = segundos < 10 ? '0' + segundos : segundos;
    var horaActual = hora + ':' + minutos + ':' + segundos;
    document.getElementById("reloj").innerHTML = horaActual;
}
setInterval(mostrarHora, 1000);

function validarFormulario() {
    // Obtener referencias a los campos del formulario
    var nombre = document.getElementById('nombre').value;
    var apellido = document.getElementById('apellido').value;
    var edad = document.getElementById('edad').value;
    var gmail = document.getElementById('gmail').value;
    var fechaNacimiento = document.getElementById('fecha-nacimiento').value;
    var pais = document.getElementById('pais').value;
    var descripcion = document.getElementById('descripcion').value;

    // Realiza las validaciones necesarias
    if (nombre === '') {
        alert('Por favor, ingresa tu nombre.');
        return false; // Evita el envío del formulario
    }

    if (apellido === '') {
        alert('Por favor, ingresa tu apellido.');
        return false;
    }

    if (edad === '') {
        alert('Por favor, ingresa tu edad.');
        return false;
    }

    // Realiza más validaciones según tus necesidades

    // Si todas las validaciones pasan, puedes enviar el formulario
    alert('Formulario válido. Enviando...');
    return true;
}

