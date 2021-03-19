
//      module2
// importing person module
import { Person }  from "./person";

//export keyword to make it public 
export class Teacher extends Person{
    constructor(name,degree){
        super(name);
        this.degree=degree
    }

    teach(){
        console.log("teach");
    }
}