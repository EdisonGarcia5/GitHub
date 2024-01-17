
function cargarDatos() { //cargar los datos y mostrarlos en la tabla.

    fetch('tabla_comida.json') // obtener el contenido del archivo que se esta solicitando.
    
        .then(response => response.json()) // convierte la respuesta a formato JSON.
        
        //data es un array
        .then(data => {

            // se crea una variables "tabla" y asigna un nombre "document".
            const tabla = document.getElementById('tableComida');//la variable "tabla" al almacena el ID "tableComida" del html.
           
            //es un método que ejecuta una función para cada elemento en un "array" y element es el nombre asignado.
            data.forEach(element => {
                let fila = tabla.insertRow();//inserta filas de la tabla.

                // es un método que crea y devuelve una nueva celda (<td>) que luego se inserta en la fila.
                let celdaAlimento = fila.insertCell(); 
                let celdaProteina = fila.insertCell();

                //inserta los registros en las celdas del archivo JSON.
                celdaAlimento.textContent = element.Alimento; //los element "Alimento" y "Proteína", son las propiedades de cada elemento en el array "data".
                celdaProteina.textContent = element['Proteína por cada 100 g de alimento']; //
            });
        })
        .catch(error => console.error('Error:', error)); //si tiene errores lo muestra.
}

window.onload = cargarDatos; //se ejecutará cuando la ventana (página web) se haya cargado por completo.
