#![feature(proc_macro_hygiene, decl_macro)]
use rocket::http::RawStr;
use std::fs::File;
use std::error::Error;
use std::io::prelude::*;
use std::collections::HashMap;
use rocket_contrib::templates::Template;
use rppal::gpio::Gpio;
use serde::Serialize;

#[macro_use] extern crate rocket;


fn string_to_static_str(s: String) -> &'static str {
    Box::leak(s.into_boxed_str())
}



fn play()-> Result<(), Box<dyn Error>>{
    let mut state="ON";
        let mut pin = Gpio::new()?.get(4)?.into_output();
        pin.set_high();
    while state=="ON"{
        println!("on hua aaww  {}",state);
        let mut file=File::open("state.txt").expect("error opnening state file");
        let mut contents=String::new();
        file.read_to_string(&mut contents).expect("error reading state file");    
        state=string_to_static_str(contents);
    }
        pin.set_low();
        pin.set_reset_on_drop(true);
        println!("exiting now");
        Ok(())
}


#[get("/")]
fn index() -> Template {
    let mut file=File::open("state.txt").expect("w");
    let mut contents=String::new();
    file.read_to_string(&mut contents).expect("w");

    #[derive(Serialize)]
    struct Context {
        first_name: String,
        state: String
      }
    let context = Context {
        first_name: String::from("Faiz"),
        state: contents
      };
      Template::render("home", context)     // khali dictionary ya struct ayga bs
}

#[get("/<name>")]
fn switch1(name: &RawStr)->Template{
    let mut state;
    
    if name.as_str()=="on"{
    state="ON"; 
    let mut file=File::create("state.txt").expect("ee");
    file.write_all(b"ON").expect("error writting");
    play();
    let x11=[("name", "Faiz"),("last_name","Faiz"),("state",&state)];    
    let context: HashMap<&str, &str> = x11
    .iter().cloned().collect();
    return Template::render("switch1", &context);    
    }      
  

    else if name.as_str()=="off"{
        println!("OFF");
        let mut file=File::create("state.txt").expect("ee");
        file.write_all(b"OFF").expect("error writting");
        state="OFF";
        let x11=[("name", "Faiz"),("last_name","Faiz"),("state",&state)];
        let context: HashMap<&str, &str> = x11
        .iter().cloned().collect();
        return Template::render("switch1", &context);   
    }
    
    
    else if name.as_str()=="favicon.ico"{
        let mut file=File::open("state.txt").expect("w");
        let mut contents=String::new();
        file.read_to_string(&mut contents).expect("w");    
        state=string_to_static_str(contents);
        let x=[("name", "Faiz"),("last_name","Faiz"),("state",&state)];
        let context: HashMap<&str, &str> = x
        .iter().cloned().collect();
       return Template::render("switch1", &context);      
    }
    
    
    else{
        let mut file=File::open("state.txt").expect("w");
        let mut contents=String::new();
        file.read_to_string(&mut contents).expect("w");    
        state=string_to_static_str(contents);
        let x=[("name", "Faiz"),("last_name","Faiz"),("state",&state)];
        let context: HashMap<&str, &str> = x
        .iter().cloned().collect();
       return Template::render("switch1", &context);    
    }
}


fn main() {
    rocket::ignite().mount("/", routes![index,switch1]).attach(Template::fairing()).launch();
}
