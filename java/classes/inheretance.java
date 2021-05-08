package classes;

public class w {  //object class
public static void main(String[] args){
    C b = new C();  // B ka constructor call huga  wo A kay constructor ko call krega aur wo object k constructor ko call krega  
    apple c=new apple(1,2,3);
}
}

class A{

    A(){  //constuctor khud inheret nhi huta extends k baad bhi          //implicitly ya explicitly call krna parayga
        super();   //ye by default likha huta hai likho ya na likho      //upr constructor ko call krega yani object
        System.out.println("Zero in A class");
    }
}


class B extends A {

    B(){ 
        super();   //ye by default likha huta hai likho ya na likho     //by default upar walay constructor ko call krta hai
        // this();  //agr super likha hu to this nhi likh sktay agr this likhengay tu super hat jaiga 
        System.out.println("zero in B class");
    }
}

class C extends B{
    C(){                    // super call huga b mai jaiga phr b say a mai jaiga a execute huga phr b phr c
        System.out.println("zero in C class");
    }


    //agr b mai koi method likh huga aur A mai bhi wji method with same signature likha huga tu b wala pkrega a wala nhi sirf a kay object kilye A wala pkrega lkn @override lagaingay
}   //agr uper wala bhi call krna huga tu super.m1 krengay 





// polymorphism

//----------------finding errors
class fruit{
    private int a,b;
    public fruit(String name){         // 1 parameter ka constructor banaingay to zero bhi bnana parayga wrna 0 parameter constructor remove hujaiga  aur eeror ayga
        System.out.println("Fruit constructor invoked");
        System.out.println(name);
    }

    fruit(int a,int b){
        // this("some type of fruit"); //1 paramater wlaa constructor call huga ab
        this.a=a;
        this.b=b;
    } // 0 constructor parameter banakay bhi error remove krsktay hain
}

class apple extends fruit{
    int c;
    apple(int a,int b, int c){
        // super();  // by default ye likha wa hai 0 parameter constructor call kr raha lkn wo present hi nhi hai
        // super("hi from apple"); //ab 1 parameter constructor call huga 
        super(a,b);  // do parameter uper wali class keliye 
        this.c=c;    // aik parameter neechay wali class keliye 
    }
}

