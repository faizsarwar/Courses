import * as x from './1.js';
x.msg();

//OR
import ('./1.js').then(msg => { msg.abc() } );