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
        <h1>Title:${product.title}</h1>
        <p>Price:${product.price}</p>
        <div class="btn_cls">
            <button>Buy Now</button>
            <button>Add to cart</button>
        </div>
        `
        container.appendChild(div);
    })
}