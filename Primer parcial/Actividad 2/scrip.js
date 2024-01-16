
function cargarDatos() {
    fetch('tabla_comida.json')
        .then(response => response.json())  
        .then(data => {
            const tabla = document.getElementById('tableComida');
            data.forEach(element => {
                let fila = tabla.insertRow();
                let celdaAlimento = fila.insertCell();
                let celdaProteina = fila.insertCell();  

                celdaAlimento.textContent = element.Alimento;
                celdaProteina.textContent = element.Proteína;  
            });
        })
        .catch(error => console.error('Error:', error));
}

window.onload = cargarDatos;
