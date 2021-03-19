function ageindays(){
    var bitrhday= prompt("what is your date of birth");
    var ageindayss=(2020-bitrhday)*365;
    ///sending data into the html.
    var h1=document.createElement('h2');
    var textanswer=document.createTextNode("you are " + ageindayss+ 'days old');
    console.log(textanswer)
    h1.setAttribute('id','ageindays'); // us h1 tag mai id add kr rhay hain.
    h1.appendChild(textanswer);  //us h1 tag mai data enter kr rahay hain.
    document.getElementById('flex-box-result').appendChild(h1); //us div ko fetch kr kay us k andar ye h1 add krdega 
    //console.log(ageindayss);// isko html mai kessay bhejengay.
}

function generatecat(){
    //for(var i=0;i<5;i++){
        var image=document.createElement('img');
        var div = document.getElementById("cat-gen");
        image.src="https://media2.giphy.com/media/f8ywYgttpGzzVPH5AO/source.gif"
        div.appendChild(image)
    //}
}