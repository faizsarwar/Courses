function* generatorFn() {
    yield "Ali";
    yield "Faiz";
    yield "Salman";
    yield "Ayesha";
    yield "Aamna";
}

let gen = generatorFn();

for(var n of gen) {
    console.log(n);
}