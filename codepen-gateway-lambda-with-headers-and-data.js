// This is the code that will be run in the browser

// POST
var xhr = new XMLHttpRequest();
xhr.open('POST', 'https://luuopszkbj.execute-api.us-east-1.amazonaws.com/dev/compare-yourself');
xhr.onreadystatechange = function (event) {
  console.log(event.target.response);
}
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.send(JSON.stringify({age: 26, height: 71, income: 2100}));

// DELETE
var xhr = new XMLHttpRequest();
xhr.open('DELETE', 'https://luuopszkbj.execute-api.us-east-1.amazonaws.com/dev/compare-yourself');
xhr.onreadystatechange = function (event) {
  console.log(event.target.response);
}
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.send();


// GET - ALL
var xhr = new XMLHttpRequest();
xhr.open('GET', 'https://luuopszkbj.execute-api.us-east-1.amazonaws.com/dev/compare-yourself/all');
xhr.onreadystatechange = function (event) {
  console.log(event.target.response);
}
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.send();


// GET - Single
var xhr = new XMLHttpRequest();
xhr.open('GET', 'https://luuopszkbj.execute-api.us-east-1.amazonaws.com/dev/compare-yourself/single');
xhr.onreadystatechange = function (event) {
  console.log(event.target.response);
}
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.send();

// GET - random request
var xhr = new XMLHttpRequest();
xhr.open('GET', 'https://luuopszkbj.execute-api.us-east-1.amazonaws.com/dev/compare-yourself/lorum');
xhr.onreadystatechange = function (event) {
  console.log(event.target.response);
}
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.send();