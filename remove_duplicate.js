const RemoveDuplicate = (array)=>{
    const new_array= [];
    array.forEach(value=>{
        if(new_array.includes(value)==false){
            new_array.push(value);
        }
    })
    return new_array;
}


const numbers = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10];
const output = RemoveDuplicate(numbers);
console.log(output)