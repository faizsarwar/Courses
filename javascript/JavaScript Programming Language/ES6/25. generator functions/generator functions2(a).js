function* generatorFn() {
    yield 4;
    yield 7;
    yield 9;

    return 8;
}

let generator = generatorFn();

console.log(generator.next());    //{ value: 4, done: false }
console.log(generator.next());    //{ value: 7, done: false }
console.log(generator.next());    //{ value: 9, done: false }
console.log(generator.next());    //{ value: 8, done: true }