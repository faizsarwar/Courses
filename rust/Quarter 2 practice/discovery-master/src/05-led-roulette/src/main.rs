#![deny(unsafe_code)]
#![no_main]
#![no_std]

use aux5::{entry, prelude::*, Delay, Leds};

#[entry]
fn main() -> ! {
    // let _y;
    // let x = 42;
    // _y = x;

    // // infinite loop; just so we don't leave this stack frame
    // loop {}
        let (mut delay, mut leds): (Delay, Leds) = aux5::init();
    
        let half_period = 500_u16;
    
        loop {
            
            leds[0].on();
            delay.delay_ms(half_period);
    
            leds[0].off();
            delay.delay_ms(half_period);
        }
    }
    
