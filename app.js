// const num = 5;
// num = 40;

// console.log(num);

// let name = "SADID";
// name = "Abdullah";
// console.log(name);

// const countryName = "Bangladesh"

// const country = `My country is ${countryName}`;
// console.log(country)

// const numbers = [1,2,3,4,5,6,7,8,9,10];
// const numbers2 = [11,12,13,14,15,16,17,18,19];

// console.log([...numbers,...numbers2])

// const person = {
//     name:"Test",
//     age:10,
//     friends:["korim","rahim","jabbar"],
// };

// const {friends,age} = person;

// console.log(friends);

// const names = ["Korim","lorem10,mfsfwrfwerfwe"];
// const [a,b,c] = names;
// console.log(a);

// function sum(num1,num2){
//     const result = num1+num2;
//     return result;
// }

// const output = sum(10,20);
// console.log(output)

// const sum2 = (sum1,sum2) => sum1+sum2;

// const output2 = sum2(10,20);
// console.log(output2)

const products = [
    {id:1,name:"xiaomi",description:"This is xiaomi",price:500,color:"black"},
    {id:2,name:"Iphone",description:"This is Iphone",price:800,color:"golden"},
    {id:3,name:"xiaomi",description:"This is xiaomi",price:500,color:"black"},
    {id:4,name:"Iphone",description:"This is Iphone",price:1000,color:"gray"},
    {id:5,name:"xiaomi",description:"This is xiaomi",price:500,color:"black"},
]

// for(let i=0;i<products.length;i++){
//     const element = products[i];
//     if (element.id==3){
//         console.log(element);
//     }
// }

// const result = products.find(product=>product.id==10);
// console.log(result)

// const result = products.filter(product=>product.color=='black');
// console.log(result);

// const result = products.map(product=>product.id*2)
// console.log(result);

// const result = products.forEach(product=>{
//     console.log(product.id);
// })
// console.log(result);


// const oddEven  = (array)=>{
//     let evenNumber = [];
//     let oddNumber = [];

//     for(let i=0;i<array.length;i++){
//         const element = array[i];
//         if (element%2==0){
//             evenNumber.push(element);
//         }
//         else{
//             oddNumber.push(element);
//         }
//     }
//     return oddNumber;
// }

// const numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26];

// const result = oddEven(numbers);
// console.log(result)

const checkFriends=(array)=>{
    let biggestName  = array[0];
    for(let i=0;i<array.length;i++){
        if(array[i].length>biggestName.length){
            biggestName=array[i];
        }
    }
    return biggestName;
}

const friends = ["Rohim","korim","jobbar","salam","borkot","preo","bangladesh"];
const bigfriends = checkFriends(friends);
console.log("from 134",bigfriends);
alert();