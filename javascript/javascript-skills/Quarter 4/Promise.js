const { promises } = require("fs");
const { resolve } = require("path");

// var assignmet = true;

// var result= new Promise(function(resolve,rejects){
// if (assignmet){
// resolve("it is completed")
// }
// else{
// rejects("it is not completed")
// }
// });



// var getprom=function(){
//     result
//     .then((data)=>{
//         console.log("data is working")
//         console.log(data)
//     })
//     .catch((err)=>{
//         console.log(err)
//     })
// };

// getprom()




let assignmet=true;

var result=new Promise(function(resolve,rejects){
    if(assignmet){
        resolve("hello")
    }
    else{
        rejects("It is not working")
    }
});


var getPromise=function(){
result
.then((data)=>{
    console.log("hello again")
    console.log(data)
})   
.catch((err)=>{
   console.log(err);

})
}

getPromise()