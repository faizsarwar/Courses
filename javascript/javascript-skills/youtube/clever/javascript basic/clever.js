console.log("hello");
//alert('hello');

//variables
var b='smoothie';
console.log(b);



//html mai script ka tag hamesha sb say end mai add krte hain


//how to take input via alert

// var age=prompt("what is your age  ??")


// // changing an elemnet by id of an html tag
// document.getElementById('some').innerHTML = age;


//Numbers in javascript
var num1=10;
num1++; //adding one digit

num1+=22  //adding any other number to current value

num1--; //decreasing one digit
console.log(num1)


//Functions
function fun(){
    console.log("this is a function");
}

//caling a function
//fun();

// function greeting(){
//     var name = prompt('what is your name');
//     var result= "hello "+name;
//     console.log(result) 
// }

//greeting();


// //arguments in a function
// function sumnumbers(num1,num2){
//     console.log(num1+num2)    
// }

//sumnumbers(5,8);


//loops in python

//while loops

// let num = 0;

// while (num<10){
//     console.log(num);
//     num+=1;
// }

// //For loops
// for (let num =0;num<10;num++){
//     console.log(num)
// }

//data types
var age=20 //number
var name1='faiz' //string
var fullname={first:"faiz",last:"sarwar"}  //object
let groceries=['apple ',' banana'," oranges"]; //array
let truth =false; //boolean
let random;
let nothing=null;  //no value


// console.log(name1.length)  //TO TAKE LENGTH
// console.log(name1.indexOf("a")) //gives index of a object if not present than gives negative value
// console.log(name1.slice(1,3)) //slicing an object
// console.log(name1.replace("a",'1'))  // replace the first part with sceond
// console.log(name1.charAt(2)) //fetching at index 2
//console.log(name1[2]) //fecthing at index 2 (again)
//console.log(name1.split("")) //spliting a string


//ways of creating an array
let fruits=['apples','bananas','oranges']
fruits=new Array('apples','bananas','oranges')
//alert(fruits[1])

// for(var i=0;i<fruits.length;i++){
//     console.log(fruits[i])
// }

// let x =fruits.pop()  // gives and removes the last element 
// fruits.shift()  //gives and removes teh first element
// fruits.push('new')  //appends in a list
// fruits.unshift("pie")  //adds from left side of an array

// let vegetabels=['poatato','tomato']
// let all_items=fruits.concat(vegetabels)  //adding to arrays

// let num2=[1,2,3,9,8,0,5,3]
// sorted_num=num2.sort(function(a,b){ return a-b})   //sorting numbers in asscending order
// console.log(sorted_num)
// sorted_num=num2.sort(function(a,b){ return b-a})   //sorting numbers in desscending order


// Objects in javascript

//dict
let student={
    first:'faiz',
    last:'sarwar',
    studentinfo:function(){
        return this.first+"\n"+this.last;   //this is equivalent to self
    }
}

student.first='ali'  //changing the vaue of the key
console.log(student.studentinfo())


// let age1=prompt("what is your age")
// // if  statemnets
// // && (AND)
// // || (OR)
// if( (age1>=18) && (age1<=35) ){
//     status='target demo';
// }
// else{
//     status='not my audience';
// }
// console.log(status)


// switch satemnets
//weekdays vs weekend
switch(6){   //6 ko check krega ju case match hugya whi exceute huga
    case 0:
        text='weekend'
        break;
    case 5:
        text='weekend'
        break;
    case 6:
        text='weekend'
        break;
    default:
        text='weekday'
}

console.log(text)


