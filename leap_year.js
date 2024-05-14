const LeapYear = (year)=>{
    if((year%400==0) || (year%100!=0 && year%4==0)){
        console.log("Leap Year");
    }
    else{
        console.log("Isn't Leap Year.");
    }
}


LeapYear(1600)