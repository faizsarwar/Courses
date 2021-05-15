// package.json mai main ko change krna parayga index.js say app.js
const express= require("express");
const app=express();
const bodyParser=require("body-parser")
const userController=require("./controllers/user_controller")


app.use(bodyParser.json())   //middle ware for recieving data

app.use(bodyParser.urlencoded({extended: false}))


const db= require("./db")

app.use("/",require("./user_routes"))

app.listen(8000,()=>{
    console.log("Server is up on 4000")
})