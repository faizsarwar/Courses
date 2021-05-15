const mongoose=require("../db")   //folder say bhr janay keliye do bar . lagaingay
const stdschema = new mongoose.Schema(
    {
    name:String,
    email:{
        type: String,
        required:true,   //email zarori hai skay baghair data add nhi krega
        trim:true        //extra space hata k save krega
    },
    age:Number,
    isActive:Boolean,
    password:String,
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

// const Student=mongoose.model("students",stdschema);
module.exports=mongoose.model("students",stdschema);