var express = require('express');
var app = express();

app.use(express.static('public'));
app.get('/', express.static('public/index.html'));
app.use('/lib', express.static('bower_components'));

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
})