const 
    express = require('express'),
    fs = require('fs'),
    path = require('path'),
    request = require('request'),
    bodyParser = require('body-parser'),
    app = express(),
    server = app.listen(3000);

const htmlPath = path.join(__dirname, 'web');

fs.writeFile('data.json', '00', (err) => {  
    if (err)
        throw err;
});

app.use(express.static(htmlPath));
app.use(bodyParser.urlencoded({extended : true}));
app.post("/data", function(request, response) {
    let data = request.body;
    console.log(data);
    let binData = "";
    if (data.isOn == "true")
        binData += 1
    else
        binData += 0
    if (data.isPaused == "true")
        binData += 1;
    else
        binData += 0;
    console.log(binData)
    fs.writeFile('data.json', binData, (err) => {  
        if (err)
            throw err;
    });
 });