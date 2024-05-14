const Grade=(mark)=>{
    if (mark>=80&&mark<100){
        console.log("You have got A+.")
    }
    else if(mark>=70&&mark<80){
        console.log("You have got A");
    }
    else if(mark>=60&&mark<70){
        console.log("You have got AB");
    }
    else if(mark>=50&&mark<60){
        console.log("You have got B");
    }
    else if(mark>=40&&mark<50){
        console.log("You have got C");
    }
    else if(mark>=33&&mark<40){
        console.log("You have got D");
    }
    else if(mark<33){
        console.log("Failed!");
    }
}

Grade(33)