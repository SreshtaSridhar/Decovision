const express = require('express');
const multer = require('multer');
const path = require('path');
const { processImage } = require('./imageProcessor');

const app = express();
const upload = multer({ dest: 'uploads/' });

app.use(express.static(path.join(__dirname, 'public')));

app.post('/process', upload.single('image'), (req, res) => {
    const imageFile = req.file;
    const description = req.body.description;

    processImage(imageFile.path, description)
        .then(result => {
            res.json(result);
        })
        .catch(error => {
            console.error('Error processing image:', error);
            res.status(500).send('Error processing image');
        });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
