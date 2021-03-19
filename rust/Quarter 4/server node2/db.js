const mongoose = require("mongoose");
mongoose.connect("mongodb://localhost:27017/local?readPreference=primary&appname=MongoDB%20Compass&ssl=false",{ useNewUrlParser: true , useUnifiedTopology: true },
(err)=>{
    if (!err){
        console.log('database connected')
    }
    else{
        console.log('Database not connected')
    }
}
)

module.exports=mongoose;   // is say ye export hugya hai ab dosri file mai use huskta hai