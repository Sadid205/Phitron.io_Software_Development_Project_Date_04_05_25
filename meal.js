const show_details = (id)=>{
    fetch(`https://www.themealdb.com/api/json/v1/1/lookup.php?i=${id}`)
    .then((data)=>data.json())
    .then((product)=>{
        const meals_object = product.meals[0]
        const product_details = document.getElementById("product_details");
        product_details.innerHTML = `
            <div class="d-flex justify-content-center">
                <img class="w-50 p-4" src="${meals_object.strMealThumb}"></img>
            </div>
           <div class="text-center">
                <h5 class="fw-bold">Food Name : <span class="fw-light"> ${meals_object.strMeal}</span></h5>
                <h5 class="fw-bold">Food Category : <span class="fw-light">${meals_object.strCategory}</span></h5>
                <h5 class="fw-bold">Origin : <span class="fw-light">${meals_object.strArea}</span></h5>
                <h5 class="fw-bold">Food Tag : <span class="fw-light">${meals_object.strTags}</span></h5>
                <h5 class="fw-bold">Youtube Link : <a href="${meals_object.strYoutube}"><span class="fw-light">${meals_object.strYoutube}</span></a></h5>
                <p>Food Instructions : <span class="fw-light">${meals_object.strInstructions}</span></p>
           </div>
        `
    })
}

const showAllProducts = (data)=>{
    data.forEach((item)=>{
        const div = document.createElement("div");
        const prd_list = document.getElementById("prd_list");
        div.classList.add("items_div");
        div.classList.add("col-md-3");
        div.classList.add("m-2");
        div.classList.add("p-2");
        div.classList.add("card");

        div.innerHTML = `
            <img src="${item.strMealThumb}" class="card-img-top p-4 m-auto" alt="card-image">
            <div class="card-body">
              <h5 class="card-title">Name : ${item.strMeal}</h5>
              <h5 class="card-text">Category : ${item.strCategory}</h5>
              <a onclick="show_details(${item.idMeal})" href="#" class="btn btn-success fw-bold">Details</a>
            </div>
        `
        prd_list.appendChild(div);
    })
}

const getAllProduct = ()=>{
    const input_field = document.getElementById("user_input");
    const value = input_field.value
   if(value){
    fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${value}`)
    .then(res => res.json())
    .then(data => {
       showAllProducts(data.meals);
    })
    input_field.value = " "
   }else{
    console.log("Input field is empty!")
   }
   
}
