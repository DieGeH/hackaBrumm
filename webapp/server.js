const 
    express = require('express'),
    fs = require('fs'),
    path = require('path'),
    request = require('request'),
    bodyParser = require('body-parser'),
    app = express(),
    server = app.listen(3000);

const htmlPath = path.join(__dirname, 'web');

app.use(express.static(htmlPath));
app.use(bodyParser.urlencoded({extended : true}));
app.post("/data", function(request, response) {
    let data = request.body;
    console.log(data);
    fs.writeFile('data.json', JSON.stringify(data), (err) => {  
        if (err)
            throw err;
    });
 });