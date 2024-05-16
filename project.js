const load_products=()=>{
    fetch("https://fakestoreapi.com/products")
    .then((data)=>data.json())
    .then((product)=>{
        show_products(product);
    })
}

load_products()
const show_products = (products)=>{
    products.forEach((product)=>{
        const div = document.createElement("div");
        const container = document.getElementById("product_container");

        div.classList.add("prd_div");
        div.innerHTML=`
        <div class="img_class">
            <img src="${product.image}"></img>
        </div>
        <h1>Title : ${product.title}</h1>
        <p>Price : ${product.price}</p>
        <div class="btn_cls">
            <button class="btn btn-secondary" onclick="addToCart('${product.title}',${product.price})">Add to cart</button>
            <button class="btn btn-info" data-bs-toggle="modal" data-bs-target="#exampleModal" onclick="getDetails('${product.id}')">Details</button>
            <!-- Modal -->
            <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel"></h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div id="modal_body" class="modal-body">
                    
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Save changes</button>
                  </div>
                </div>
              </div>
            </div>
        </div>
        `
        container.appendChild(div);
    })
}

const addToCart = (title,price)=>{
    const div = document.createElement("div");
    const cart_div = document.getElementById("cart_div");
    div.classList.add("cart_div");
    div.innerHTML = `
        <h3>Title : ${title.slice(10)}</h3>
        <p>Price : <span class="price">${price}</span></p>
    `
    cart_div.appendChild(div);
    totalCost();
}

const totalCost = ()=>{
   let cost = 0;
   const elements = document.getElementsByClassName("price");
    for(const element of elements){
        cost+=parseFloat(element.innerText)
    }

   document.getElementById("total_cost").innerText = cost.toFixed(2);
}

const getDetails = (id)=>{
    fetch(`https://fakestoreapi.com/products/${id}`)
    .then((product)=>product.json())
    .then((data)=>{
       const modal_body = document.getElementById("modal_body");
       modal_body.innerHTML = `
            <div class="col-md-6 d-flex align-items-center">
                <img class="w-75" src="${data.image}"></img>
            </div>
           <div class="px-2 col-md-6">
                <h3 class="fs-5"><span class="fs-bold fw-3">Title</span> : ${data.title}</h3>
                <h4><span class="fw-bold">Category</span> : ${data.category}</h4>
                <p><span class="fw-bold">Description : </span>${data.description}</p>
                <p><span class="fw-bold">Price</span> : ${data.price}$</p>
                <p><span class="fw-bold">Rating</span> : ${data.rating.rate}</p>
           </div>
        `
        const exampleModalLabel = document.getElementById("exampleModalLabel");
        exampleModalLabel.innerText = `${data.title}`
        // modal_body.appendChild(modal_Inner_div);
    })
}