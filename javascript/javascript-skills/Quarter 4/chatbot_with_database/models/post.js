const mongoose =require("mongoose");
const postSchema=new mongoose.Schema({
    name:{
       type: String,
        required: true,
    }, 
    email:{
        type: String,
         required: true,
    },
    Person:{
        type: Number,
         required: true,
    },
    roomtype:{
        type: String,
         required: true,
    },
    
    });

mongoose.model('ReqData',postSchema)   // ReqData k naam say table banaiga database mai aur data store huga whn