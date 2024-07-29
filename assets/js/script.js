document.addEventListener('DOMContentLoaded', function() {
  const pageData = document.getElementById('page-data');
  const bibcode = pageData ? pageData.getAttribute('data-bibcode') : null;

  if (!bibcode) {
    console.error('Bibcode not found.');
    return;
  }

  // Construct the path to the metadata.json file
  const metadataPath = `metadata.json`;

  fetch(metadataPath)
    .then(response => response.json())
    .then(data => {
      if (!data.support_dict) {
        console.error('support_dict not found in metadata.json.');
        return;
      }

      const container = document.getElementById('instruments-container');
      const instruments = {};

      data.support_dict.forEach(item => {
        if (!instruments[item.instrument]) {
          instruments[item.instrument] = [];
        }
        instruments[item.instrument].push(`<b>${item.parameter}:</b> ${item.quote}`);
      });

      Object.keys(instruments).forEach(instrument => {
        const tooltipText = instruments[instrument].join('<br>');
        const instrumentElement = document.createElement('span');
        instrumentElement.className = 'tooltip';
        instrumentElement.innerHTML = `${instrument}
          <span class="tooltiptext">${tooltipText}</span>`;
        container.appendChild(instrumentElement);
        container.appendChild(document.createElement('br')); // Add line break between instruments
      });
    })
    .catch(error => console.error('Error loading metadata.json:', error));
});
