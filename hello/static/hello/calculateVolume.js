$(document).ready(function() {
    const elements = document.querySelectorAll('.volume-parameter');

    for (const element of elements) {
    element.addEventListener('change', (event) => {
        // Hier deine Funktion zum Bearbeiten des Events
        document.getElementById('kubatur').innerHTML = "Kubatur: " + Math.round((document.getElementsByName('Length')[0].value * document.getElementsByName('Width')[0].value * document.getElementsByName('Height')[0].value) * 100) / 100 + " m³"
    });
    }

});