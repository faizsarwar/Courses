const userController=require("./controllers/user_controller")
const express=require("express")
const router =express.Router();

// app.get("/",(req,res)=>{
//     res.send("Home Page")
// })

router.get("/",userController.findAllRec)

router.post("/",userController.createRec)

router.post("/:id",userController.findone)

router.get("/:id",userController.deleteRec)     // bs app ki jaga router ajaiagay

router.post("/update/:id",userController.updateRec)    // (app.js mai likhengay app.use("/",require("./user_routes"))


module.exports = router  // saray url export hujaingay (exports s k sath likhengay)  