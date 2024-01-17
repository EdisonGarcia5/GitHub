
function cargarDatos() { //cargar los datos y mostrarlos en la tabla.
    fetch('tabla_comida.json') // obtener el contenido del archivo que se esta solicitando.
        .then(response => response.json()) // convierte la respuesta a formato JSON.
        .then(data => {

            // se crea una variables "tabla" y asigna un nombre "document".
            const tabla = document.getElementById('tableComida');//la variable "tabla" al almacena el ID "tableComida" del html.
            data.forEach(element => {
                let fila = tabla.insertRow();//inserta filas de la tabla.
                let celdaAlimento = fila.insertCell(); //agrega las celdas correspondientes del archivo JSON.
                let celdaProteina = fila.insertCell();

                //inserta los registros en las celdas del archivo JSON.
                celdaAlimento.textContent = element.Alimento;
                celdaProteina.textContent = element.Proteína;  
            });
        })
        .catch(error => console.error('Error:', error)); //si tiene errores lo muestra.
}

window.onload = cargarDatos; //se ejecutará cuando la ventana (página web) se haya cargado por completo.
