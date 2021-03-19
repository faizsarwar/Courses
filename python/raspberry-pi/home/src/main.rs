#![feature(proc_macro_hygiene, decl_macro)]
use std::fs::File;
use std::io::prelude::*;
use rust_gpiozero::*;
use std::collections::HashMap;
use rocket_contrib::templates::Template;
// use rocket_contrib::serve::StaticFiles;
use serde::Serialize;

#[macro_use] extern crate rocket;

#[get("/")]
fn index() -> Template {
    // let mut led = LED::new(17);
    // led.on();

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
    
    // let context: HashMap<&str, &str> = [("name", "Faiz")]
    // .iter().cloned().collect();
    Template::render("home", context)    
}

#[get("/on")]
fn On()->Template{
    // let mut led=LED::new(4);
    // led.on();

    let mut file=File::create("state.txt").expect("ee");
    file.write_all(b"ON");


    let context: HashMap<&str, &str> = [("name", "Faiz"),("last_name","Faiz")]
    .iter().cloned().collect();

    Template::render("home_on", &context)    
}


#[get("/off")]
fn Off()->Template{
    // let mut led=LED::new(4);
    // led.off();

    let mut file=File::create("state.txt").expect("ee");
    file.write_all(b"OFF");

    let context: HashMap<&str, &str> = [("name", "Faiz"),("last_name","Faiz")]
    .iter().cloned().collect();

    Template::render("home_off", &context)    
}


fn main() {
    rocket::ignite().mount("/", routes![index,On,Off]).attach(Template::fairing()).launch();
}