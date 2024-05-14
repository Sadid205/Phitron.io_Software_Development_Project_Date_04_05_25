const GreaterName = (array)=>{
    let element = array[0];
    for(i=0;i<array.length;i++){
        if (array[i].length>element.length){
            element = array[i];
        }
    }
    return element
}


var friends = ["rahim", "karim", "abdul", "sadsd", "heroAlom"];

const output = GreaterName(friends);
console.log(output);