const mongoose = require('mongoose');
const Student = require("./model");
mongoose.connect("mongodb://localhost:27017/local?readPreference=primary&appname=MongoDB%20Compass&ssl=false",{ useNewUrlParser: true , useUnifiedTopology: true })
const express=require("express");
const app=express();
app.use(express.json());


app.get('/students',async(req,res)=>{         // jb /student pr koi request aygi tu ye function call huga
    const std=await Student.find({})  // students ko find krega aur std mai store kradega  
    res.send(std)
})

app.post('/student',(req,res)=>{
    const stdname=new Student(req.body);
    stdname.save()
    .then(()=>{
        res.send("user saved success")
    })
    .catch((err)=>{console.log("error",err)})
})

app.put("/student/:id",(req,res)=>{     //put ka mtlb update
    Student.findByIdAndUpdate(req.params.id,req.body)   //req.parms.id say id ajaigi
    .then((data)=>{
        res.send("record updated")
    })
})

app.delete("/student/:id",(req,res)=>{
    Student.findByIdAndDelete(req.params.id,req.body)
    .then((user)=>{
        res.send("Data deleted")
    })
})




app.listen(8000,()=>{
    console.log("server")
})