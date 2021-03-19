// package.json mai main ko change krna parayga index.js say app.js
const express= require("express");
const app=express();
const bodyParser=require("body-parser")

app.use(bodyParser.json())   //middle ware for recieving data

app.use(bodyParser.urlencoded({extended: false}))

app.get("/",(req,res)=>{
    res.send("Home Page")
})


const db= require("./db")

app.listen(4000,()=>{
    console.log("Server is up on 4000")
})