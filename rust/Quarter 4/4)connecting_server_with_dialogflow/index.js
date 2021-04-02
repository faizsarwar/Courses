const {WebhookClient}=require("dialogflow-fulfillment");
const { request, response } = require("express");
const express=require("express");
const app=express();


// dialogflow app pr post ki request bhejegaa

app.get("/",(req,res)=>{
    res.send("Server Is UP");
})


app.post("/webhook",express.json(),(request,response)=>{          //fulfillment mai bhi url mai /webhook lagana huga 
    const agent=new WebhookClient({request:request,response:response});
    function fallback(agent){
        agent.add("your bot does not understand this");
    }

    function welcome(agent){
        agent.add("welcome to piaic Backend bot !!!");
    }

    function userDetails(agent){
        // let user_name= agent.parameters["person"].name;       // is ka mtlb person ka peremeter fetch huga consoe ki trha yhn pr  // object hai isko convert krna parayga (.name  laga kr)
        let user_city=agent.parameters["geo-city"];
        let user_name=agent.parameters["person"];  
        // jb tk ye doo details nhi ayngi agay hi barayga
        agent.add('welcome to piaic Backend bot to '+user_name+"  from "+user_city);
        console.log("hello")
    }

    function calculation(agent){
        let number1=agent.parameters["number"];
        let number2=agent.parameters["number_01"];
        let sum=number1+number2;
        agent.add("the sum is "+sum);
    }

    let intentMap= new Map();
    intentMap.set("Default Fallback Intent",fallback);    //ju name intent ka dailog flow ai huga whi dena hai ,ju function call krwana hai wo
    intentMap.set("Default Welcome Intent",welcome);
    intentMap.set("userDetails",userDetails);//
    intentMap.set("calculation",calculation);
    agent.handleRequest(intentMap)
})


app.listen(4000,()=>{
    console.log("server is up on 4000")
})