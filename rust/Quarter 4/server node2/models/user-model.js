const mongoose=require("../db")   //folder say bhr janay keliye do bar . lagaingay
const stdschema = new mongoose.schema({
    name:String,
    email:String,
    age:Number,
    isActive:Boolean,
    // usertype:"Admin"    //setting default value
    usertype:{
        desc:"User roles",
        trim: true,
        type: String,
        enum: ["Admin","User","Guest"],
        default:"User",
        required:true
    }
},
{
strict:true,
version:false,
timestamps:{
createdAt:"CreatedTime",
updatedAt:"LastUpdatedTime"
}
})


const Student=mongoose.model("students",stdschema);
module.exports=Student;