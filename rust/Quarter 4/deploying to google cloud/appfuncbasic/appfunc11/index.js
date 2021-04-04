// module.exports = async function (context, req) {
//     context.log('JavaScript HTTP trigger function processed a request.');

//     const name = (req.query.name || (req.body && req.body.name));
//     const responseMessage = name
//         ? "Hello, " + name + ". This HTTP triggered function executed successfully."
//         : "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.";

//     context.res = {
//         // status: 200, /* Defaults to 200 */
//         body: responseMessage
//     };
// }

const { dialogflow }=require("actions-on-google");
const express=require("express");
const { createHandler }=require("azure-function-express");
const app=dialogflow();
app.intent('Default Welcome Intent',conv=>{
    // conv.parameters  say data catch krsktay hain
    conv.add("Hello this is microsoft beckend")
});
//put other intet handlers here
const expressApp=express();
expressApp.post('/api/appfunc11',app);
module.exports=createHandler(expressApp);