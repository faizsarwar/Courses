const mongoose=require('mongoose');
const stdschema=new mongoose.Schema({
    name:String,
    //id: Number,  //number integer type hai
    //age;Float32Array 
    //is_married:Boolean
})
const Student = mongoose.model("student",stdschema);
module.exports=Student;

