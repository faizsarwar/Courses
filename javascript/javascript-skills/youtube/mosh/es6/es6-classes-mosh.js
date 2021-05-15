//  problem why to use classes

// const person={
//     name:"Faiz",
//     walk(){
//         console.log("walk");
//     }
// }

// const person2={
//     name:"Faiz",
    
// }


////        SOLUTION OF CODE REPITION

class code{
    constructor(name){
        this.name=name
    }
    walk(){
        console.log("walk");
    }
}
const person1=new code("faiz")   //sode repeatition say bach jaingay hm class use kr kay
console.log(person1)


//////              INHERITANCE

class teacher extends code{
    constructor(name,degree){
        super(name);
        this.degree=degree
    }

    teach(){
        console.log("teach");
    }
}

const Teacher=new teacher("faiz","Msc")

console.log(Teacher)


