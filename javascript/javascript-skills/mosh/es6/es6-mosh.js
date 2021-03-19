
////////////        defining variables

const { filter } = require("minimatch")

//var----> function tk scope 
//let----> block tk scope
//const--> block tk scope 

function sayhello(){
    for(var i=0;i<5;i++){
        console.log(i)
    }
    console.log(i)  // yhn bhi accessable huga i 
}


//  Var: the variable defined is visible in the entire function.
//  Let: the variable defined is visible only in the block it is defined in.
//  Const: makes the variable a constant
//  Use const over let and let over var wherever possible

// sayhello()

// const person={
//     name:"Faiz",
//     Walk() {
//         console.log(this);
//     }    // called as methods
// }

// person.Walk()  //acess
// person.name=""  //acess


//////////////////////       objects

// Above is an object with 1 property and 2 methods.
// Another way defining a method member in an object is:
// walk: function() {} //not recommended
// * Invoking method of an object: person.walk()
// * Accessing property of object
//     ** When the property is known in advance: person["name"]
//     ** When the property is not known in advance: person[variable.value] //variable.value == "name


///                 This keyword

// const person = {
//     "name": "Mosh",
//     walk() {
//         console.log(this)
//     }
// }

// this in the function walk always refers to the object which invoked it, and by default by the global object (window)
// person.walk() => the person object is printed on console, since the function walk is invoked by person object and thus "this" represent it here.
// const walk1 = person.walk //not calling the function, only assiging variable walk1 the function walk
// walk1()	=> undefined is printed since the default object is the global object and "this"  represents it here.
// If strict mode is not enabled, it will return window object instead of undefine
// * All functions in JS are object which have member functions like bind.
// const walk1 = person.walk.bind(person)
// here bind function on walk sets the "this" in it as the reference to the object that is passed to it.


////                Arrow Functions

// const suqare= function(number){
//    return number*number;
// }

// const suqare= (number)=>{
//     return number*number;
// }

// const suqare=(number)=>number*number
// console.log(suqare(4))


// const jobs=[
//     {id :1,isActive:true},
//     {id :2,isActive:true},
//     {id :3,isActive:false}
// ]

//const actievjobs=jobs.filter(function(jobs){return jobs.isActive;})  //filter jobs where is avtive is true

//const actievjobs=jobs.filter(jobs=>(jobs.isActive))
//console.log(actievjobs)


////            arrow function with this keyword

// const person={
//     talk() {
//         setTimeout(() => {
//             console.log("this",this);    
//         }, 1000);
        
//     }
// };

// person.talk();


//const colors=['red','yellow','blue'];
// const items =colors.map(function(colors){
//     return "<li>"+colors+"</li>";
// });

//const items =colors.map((colors)=>"<li>"+colors+"</li>");

// const items =colors.map((colors)=>"<li>${colors}</li>"); //template literals

// console.log(items)

////            Object destructuring
const address={
    street:"d",
    city:"D",
    country:"dD"
}


// const street=address.street;
// const city=address.city;
// const country=address.country;

//or

//const {street,city,country}=address; //teeno variables mai values save hujaingi

// const {street:st}=address   //saving  value of street of address in st variable
 
// console.log(st)


////            spread operator

// const first=[1,2,3]
// const second=[4,5,6]

//const combined=first.concat(second)  //combining one ad two
// const combined=[...first,...second]     //by spread method
// const combined=[...first,"a",...second]    //we can add elements in between
// console.log(combined)

////            clone
// const clone=[...first]
// console.log(clone)

// const first={name: "faiz"}
// const second={job: "programmer"}

// const combined ={...first,...second}

// console.log(combined)