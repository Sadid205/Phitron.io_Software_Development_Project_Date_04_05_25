

const sort_array = (array)=>{
    for(i=0;i<array.length;i++){
        for(j=i+1;j<array.length;j++){
            const temp = array[i];
            if(array[i]>array[j]){
                array[i]=array[j];
                array[j] = temp;
            }
        }
    }
    return array ;
}



const numbers = [17, 4, 10, 6, 20, 8, 15, 1, 3, 19, 14, 11, 7, 5, 13, 2, 9, 18, 12, 16]
const output = sort_array(numbers);
console.log(output);

