$(document).ready(function() {
    function copyAndInsertDiv(containerClass, parentDiv) {
        // 1. Divs der angegebenen Klasse im Parent-Div finden
        const divsToCopy = parentDiv.querySelectorAll(`.${containerClass}`);
      
        // 2. Anzahl der Divs ermitteln
        const numDivs = divsToCopy.length;
      
        // 3. Falls kein Div vorhanden, abbrechen
        if (numDivs === 0) {
          return;
        }
      
        // 4. Letztes Div ermitteln
        const lastDiv = divsToCopy[numDivs - 1];
      
        // 5. Letztes Div klonen
        const clonedDiv = lastDiv.cloneNode(true);
      
        // 6. Event-Handler kopieren (falls vorhanden)
        for (const clonedInput of clonedDiv.querySelectorAll('input')) {
          clonedInput.addEventListener('change', event);
        }
      
        // 7. Geklontes Div am Ende des Parent-Divs einfügen
        parentDiv.appendChild(clonedDiv);
      }

    const containerClass = 'cost-position-container';
    const parentDiv = document.querySelector('#container');
    
    document.querySelector('#add-position').addEventListener('click', () => {
      copyAndInsertDiv(containerClass, parentDiv);
    });
});





