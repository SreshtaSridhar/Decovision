document.getElementById('cameraAccess').addEventListener('click', () => {
  // Access the camera
  navigator.mediaDevices.getUserMedia({ video: true })
      .then((stream) => {
          // Handle the camera stream
          console.log('Camera accessed');
      })
      .catch((error) => {
          console.error('Error accessing camera:', error);
      });
});

document.getElementById('decorationForm').addEventListener('submit', (event) => {
  event.preventDefault();
  const description = document.getElementById('description').value;
  const imageFile = document.getElementById('imageUpload').files[0];

  // Process the image and description
  if (imageFile) {
      const formData = new FormData();
      formData.append('image', imageFile);
      formData.append('description', description);

      fetch('/process', {
          method: 'POST',
          body: formData
      })
      .then(response => response.json())
      .then(data => {
          displayOutput(data);
      })
      .catch(error => {
          console.error('Error processing request:', error);
      });
  }
});

function displayOutput(data) {
  const outputDiv = document.getElementById('output');
  outputDiv.innerHTML = `
      <h2>Decoration Preview</h2>
      <img src="${data.decoratedImage}" alt="Decorated Image">
      <h3>Details</h3>
      <p>${data.details}</p>
  `;
}
