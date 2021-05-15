const Student = require("../models/user-model");
// const Users=require("../models/user-model");



//for password decryption use this
const bcr=require("bcryptjs")  // password mai : bcr.hashsync(type,value of hahs 10,20 etc)




exports.createRec=(req,res)=>{           //export ka mtlb isko public kia hai
    if(!req.body.email){
        return res.send("Please provide the email !!")   //agr data mai email show nhi hugi tu ye error dega
    } 
    else if(!req.body.password){
        return res.send("Please provide the password !!")   //agr data mai email show nhi hugi tu ye error dega
    }
    else{
    const student=new Student({
        email:req.body.email,
        password:bcr.hashSync(req.body.password,10),   //password save krlega lk show hash wala krega
        age:req.body.age,
        name:req.body.name,
        gender:req.body.gender,
        isActive:req.body.isActive,
        usertype:req.body.usertype

    });
    student
    .save()
    .then((data)=>{
        res.send('data added'+data)
    })
    .catch((e)=>{
        console.log(e)
    })

}
}

exports.findAllRec=(req,res)=>{
    Student.find()
    .then((studets)=>{
        res.send(studets)
    })
    .catch((e)=>{
        console.log(e)
    })

}

exports.findone=(req,res)=>{
    Student.findById(req.params.id)   //id ka mtlb post k url wala /:id
    .then((studet)=>{
        res.send(studet)
    })
    .catch((e)=>{
        return res.status(404).send("Error while finding the Records!!!");  //agr error 404 huga to ye response send huga hata dengay tu sb mai chlega
        //console.log(e)
    })
}

exports.deleteRec=(req,res)=>{
    Student.findByIdAndRemove(req.params.id)
    .then((student)=>{
        req.send("student is deleted")
    })
    .catch((e)=>{
        return res.status(404).send("Error while deleting the Records!!!");  //agr error 404 huga to ye response send huga hata dengay tu sb mai chlega
        //console.log(e)
    })
}

exports.updateRec=(req,res)=>{
    Student.findByIdAndUpdate(req.params.id,req.body,{new:true})
    .then((std)=>{
        res.send("updated student is :"+  std);
    })
    .catch((e)=>{
        return res.status(404).send("Error while deleting the Records!!!");  //agr error 404 huga to ye response send huga hata dengay tu sb mai chlega
    })
}