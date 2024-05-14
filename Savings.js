
const Savings = (allPayments,LivingCost)=>{
    if(Array.isArray(allPayments)==true&&Number.isInteger(LivingCost)==true){
        allPayments.map((value,index,arr)=>{
            if(value>=3000){
                const tax = value*(20/100);
                const available = value-tax;
                arr[index] = available;
            }
        })
        let TotalSavings = 0;
        allPayments.map((value)=>{
            TotalSavings+=value;
        })
        if(TotalSavings-LivingCost<=0){
            return "earn more";
        }
        else{
            return TotalSavings-LivingCost;
        }

    }else{
        return "invalid input";
    }
}


const output1 = Savings([1000,2000,3000],5400);
const output2 = Savings([1000,2000,2500],5000);
const output3 = Savings([900,2700,3400],10000);
const output4 = Savings(100,[900,2700,3400]);
console.log(output1)
console.log(output2)
console.log(output3)
console.log(output4)

