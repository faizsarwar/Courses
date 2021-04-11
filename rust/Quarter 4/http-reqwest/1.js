// const request1 = require('request');
// var req=request1('http://localhost:8030/ON/1');
// setTimeout(() =>{ 
//   console.log('timeout beyond time');
// if (req.response==undefined){

//   req.abort()
// }
// }, 1000);

var state = 'ON';
var switchnumber="1"; 
var s = `http://localhost:8030/${state}/${switchnumber}`;
console.log(s); // prints hello John, how are you doi

