
const Who_is_grater = (array)=>{
    let element = array[0];
    for(let i=0;i<array.length;i++){
        if(element<array[i]){
            element = array[i];
        }
    }
    return element;
}

const numbers = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10];
const output = Who_is_grater(numbers);
console.log(output);