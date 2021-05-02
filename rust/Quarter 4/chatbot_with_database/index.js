const mongoose= require('mongoose');
const bodyparser=require("body-parser");
const express=require('express');
const {WebhookClient}=require('dialogflow-fulfillment');
const { response } = require('express');
const app=express().use(bodyparser.json())                  //app.use() wlai line ki jaga ye bhi likh sktay hain

require('./mongoose');
require('./models/post');

var model=mongoose.model("ReqData")

app.post("/webhook",express.json(),(request,response,next)=>{
    const agent= new WebhookClient({request:request,response:response})


    function welcome(agent){
        agent.add("welcome")
    }

    function HotelBook(agent){
        let name = agent.parameters.person;
        let email = agent.parameters.email;
        let persons = agent.parameters.persons;
        let roomtype = agent.parameters.RoomTypes;
        // agent.add(`thank you ${name.name} you haveve  booked ${persons} people room of type ${roomtype}   we will inform you on ${email}`)
        let data ={
            //dialogflow mai ju data manga hai hmnay us squence say set krengay isko bhi
            name:name.name, //object hai isliye isko covert krna huga string mai
            email:email,
            Person:persons, //mongose mai person ka p capital tha islye yhn capital krngay
            roomtype:roomtype
        }
        return savedata(data)
        .then((resvalue=>{
            return agent.add(`${resvalue}`)
        }))
        .catch(()=>{
               return agent.add("Record Is Not Inserted")
            })
    }


    let intentMap=new Map();
    intentMap.set("Default Welcome Intent",welcome)
    intentMap.set("Book-Hotel",HotelBook)

    agent.handleRequest(intentMap)


})

function savedata(data){   //baqi crud operation isi trha hungay
    let promise=new Promise((resolve,reject)=>{
        var savedata=new model(data);
        savedata.save()
        .then((resultdata=>{
            console.log(resultdata)
            resolve(`thank you ${data.name} you haveve  booked ${data.persons} people room of type ${data.roomtype}   we will inform you on ${data.email}`) //dilaogflow pr response
        }))
        .catch((e)=>{
            reject(e)
        })
    })
    return promise
}



app.listen(5000,()=>{
    console.log("Server is Up on 5000")
})