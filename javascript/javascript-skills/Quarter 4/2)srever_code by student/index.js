const express = require("express");  //module add
const app = express();               //creating object for express

app.use(express.json());             //to use middleware

var student=[
    {id:1, name : "ali"},
    {id:2, name : "faiz"},
    {id:3, name : "salman"}
]


//get is used fow fecthing data
app.get("/home",function(re ,res){  //ES5      function mai (URI ,callback fn, middelware)
    res.send("hello from basic function")
});


app.get("/",function(re ,res){ 
    console.log("student list fetch")  //termiba pe print hug ajb bhi koi request aygi
    res.send("The studets available in batch are "+JSON.stringify(student))
});



//aik tareeka aur bhi hai
app.get("/arrow",(re ,res)=>{   //ES6
    var objectdetails={
        "NAME":"FAIZ",
        "AGE":23,
    }
    res.send("hello from basic arrow function"+JSON.stringify(objectdetails))   //aik say zayada response is trha bhejengay 

});

app.listen(5000,function(){    // enivorment set krega 
    console.log("server is up for port 5000 ye terminal pe show huga")  //saray log terminal pe hi show huga
})   //first parameter is our port second is our function
 

// post is used to send data
app.post("/student",(req,res)=>{
    var student1={
        id : student.length+1,
        name: req.body.name   //recieving name from frontend or postman
    }
    student.push(student1);    // appneding student array above
    console.log("the current students are "+student.length)  //ye console pe show huga
    res.send("The studet is Added ")    // frontend pe jaiga
});



//update  data with put
app.put("/student/:id",(req,res)=>{        //id mtlb id kesath uri
    var student1 =student.find(s => s.id === parseInt(req.params.id) ) //us id ko search kr ra hai aur usko match kr raha hai requested id say
    student1.name=req.body.name;  //updating the requested name
    console.log(req.params.id)   //put request walay uri mai ju id hai wo dega
    res.send("Id is recieved")  //body mai send huga 

})  


//delete data 
app.delete("/student/:id",(req,res)=>{        //id mtlb id kesath uri
    var student1 =student.find(s => s.id === parseInt(req.params.id)) //us id ko search kr ra hai aur usko match kr raha hai requested id say
    var index=student.indexOf(student1);   //getting index of requested student
    student.splice(index,1); // 1 ka mtlb aik record hatana hai bs
    res.send("record is deleted")
})