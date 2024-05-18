
const searchByName = ()=>{
    const search_input = document.getElementById("search_input");
    const removeChild = document.getElementById("all_teams")
    removeChild.innerHTML = " ";
    fetch(`https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p=${search_input.value}`)
    .then((obj)=>obj.json())
    .then((obj)=>{
        if(obj.player==null){
            const all_teams = document.getElementById("all_teams");
            all_teams.innerHTML = `
                <h1 class="text-center">No player found with this name</h1>
            `
        }else{
            obj.player.forEach((data)=>{
                const all_teams = document.getElementById("all_teams");
                const div = document.createElement("div");
                div.classList.add("myCard")
                let paragraph = data.strDescriptionEN;
                let words;
                let tenWords;
                let TenWordsString ;
                if(paragraph!=null){
                    words = paragraph.split(' ');
                    tenWords = words.slice(0,10);
                    TenWordsString=tenWords.join(' ');
                }
                else{
                    TenWordsString = "Description is empty"
                }
    
                div.innerHTML = `
                    <img class="m-auto pt-2 card-img-top" src="${data.strThumb}"></img>
                    <div class="card-body mt-1">
                        <h4 class="fs-6"><span class="fw-bold">Player Name :</span> ${data.strPlayer}</h4>
                        <h4 class="fs-6"><span class="fw-bold">Nationality :</span> ${data.strNationality}</h4>
                        <h4 class="fs-6"><span class="fw-bold">Team :</span> ${data.strTeam}</h4>
                        <h4 class="fs-6"><span class="fw-bold">Sports :</span> ${data.strSport}</h4>
                        <h4 class="fs-6"><span class="fw-bold">Salary :</span> ${data.strWage}</h4>
                        <h4 class="fs-6"><span class="fw-bold">Description : </span>${TenWordsString}</h4>
                        <h4 class="fs-6"><span class="fw-bold">Gender :</span> ${data.strGender}</h4>
                        <span class="fs-2"><a target="_blank" href="${data.strFacebook}"><i class="fa-brands fa-facebook"></i></a></span>
                        <span  class="fs-2 ms-3"><a href="${data.strTwitter}"><i class="fa-brands fa-twitter"></i></a></span>
                        <div class="d-flex w-100 justify-content-between">
                            <button onclick="addToGroup('${data.strThumb}','${data.strPlayer}')" class="btn btn-info fw-bold">Add to group</button>
                            <button onclick="showDetails(${data.idPlayer})" class="btn btn-secondary fw-bold" data-bs-toggle="modal" data-bs-target="#exampleModal">See Details</button>
                        </div>
                    </div>
                `
                all_teams.appendChild(div);
           })
        }
        
    })
}

const showDetails = (playerId) => {
    const modal_body = document.getElementById("modal_body");
    const exampleModalLabel = document.getElementById("exampleModalLabel");
    fetch(`https://www.thesportsdb.com/api/v1/json/3/lookupplayer.php?id=${playerId}`)
    .then((obj)=>obj.json())
    .then((obj)=>{
        exampleModalLabel.innerHTML = `
            <h2>${obj.players[0].strPlayer}</h2>
        `
        let paragraph = obj.players[0].strDescriptionEN;
        let words;
        let tenWords;
        let TenWordsString ;
        if(paragraph!=null){
        words = paragraph.split(' ');
        tenWords = words.slice(0,50);
        TenWordsString=tenWords.join(' ');
        }
        else{
            TenWordsString = "Description is empty"
        }
        modal_body.innerHTML = `
                    <img class="card-img-top" src="${obj.players[0].strThumb}" alt="${obj.players[0].strPlayer}'s photo"></img>
                    <div class="card-body mt-1">
                        <h4 class="fs-6"><span class="fw-bold">Player Name :</span> ${obj.players[0].strPlayer}</h4>
                        <h4 class="fs-6"><span class="fw-bold">Birth Location :</span> ${obj.players[0].strBirthLocation}</h4>
                        <h4 class="fs-6"><span class="fw-bold">Status :</span> ${obj.players[0].strStatus}</h4>
                        <h4 class="fs-6"><span class="fw-bold">Signed Date :</span> ${obj.players[0].dateSigned}</h4>
                        <h4 class="fs-6"><span class="fw-bold">Born :</span> ${obj.players[0].dateBorn}</h4>
                        <h4 class="fs-6"><span class="fw-bold">Description : </span>${TenWordsString}</h4>
                        <h4 class="fs-6"><span class="fw-bold">Status :</span> ${obj.players[0].strStatus}</h4>
                        <span class="fs-2"><a target="_blank" href="${obj.players[0].strFacebook}"><i class="fa-brands fa-facebook"></i></a></span>
                        <span  class="fs-2 ms-3"><a href="${obj.players[0].strTwitter}"><i class="fa-brands fa-twitter"></i></a></span>
                        <span  class="fs-2 ms-3"><a href="${obj.players[0].strInstagram}"><i class="fa-brands fa-instagram"></i></a></span>
                    </div>
                    

        `
    })
}

let count = 0
const addToGroup = (player_img,player_name)=>{
    if(count>11){
        return
    }
    count++;
    if(count<=11){
        const total_cnt = document.getElementById("total_cnt");
        total_cnt.innerText = count;
        const group_div = document.getElementById("group_div");
        const div = document.createElement("div");
       
        div.classList.add("inner_group_div");
        div.innerHTML = `
            <div class="img_div">
                <img src="${player_img}"></img>
            </div>
            <div class="text_div">
                <p class="fw-bold">${player_name}</p>
            </div>
        `
        group_div.appendChild(div);
    }else{
        const group_div = document.getElementById("group_div");
        const div = document.createElement("div");
        div.classList.add("shadow-lg")
        div.classList.add("p-3")
        div.innerHTML = `
            <p class="fw-bold text-center">You can not add more than 11 players</p>
        `
        alert("You can not add more than 11 players!")
        group_div.appendChild(div);
    }
}

const getAllPlayers =()=>{
    fetch("https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p=Goo")
    .then((obj)=>obj.json())
    .then((obj)=>{
        for(let i=0;i<10;i++)
            {                
                const all_teams = document.getElementById("all_teams");
                const div = document.createElement("div");
                div.classList.add("myCard")
                let paragraph = obj.player[i].strDescriptionEN;
                let words;
                let tenWords;
                let TenWordsString ;
               if(paragraph!=null){
                words = paragraph.split(' ');
                tenWords = words.slice(0,10);
                TenWordsString=tenWords.join(' ');
               }
               else{
                TenWordsString = "Description is empty"
               }

                div.innerHTML = `
                    <img class="m-auto pt-2 card-img-top" src="${obj.player[i].strThumb}"></img>
                    <div class="card-body mt-1">
                        <h4 class="fs-6"><span class="fw-bold">Player Name :</span> ${obj.player[i].strPlayer}</h4>
                        <h4 class="fs-6"><span class="fw-bold">Nationality :</span> ${obj.player[i].strNationality}</h4>
                        <h4 class="fs-6"><span class="fw-bold">Team :</span> ${obj.player[i].strTeam}</h4>
                        <h4 class="fs-6"><span class="fw-bold">Sports :</span> ${obj.player[i].strSport}</h4>
                        <h4 class="fs-6"><span class="fw-bold">Salary :</span> ${obj.player[i].strWage}</h4>
                        <h4 class="fs-6"><span class="fw-bold">Description : </span>${TenWordsString}</h4>
                        <h4 class="fs-6"><span class="fw-bold">Gender :</span> ${obj.player[i].strGender}</h4>
                        <span class="fs-2"><a target="_blank" href="${obj.player[i].strFacebook}"><i class="fa-brands fa-facebook"></i></a></span>
                        <span  class="fs-2 ms-3"><a href="${obj.player[i].strTwitter}"><i class="fa-brands fa-twitter"></i></a></span>
                        <div class="d-flex w-100 justify-content-between">
                            <button onclick="addToGroup('${obj.player[i].strThumb}','${obj.player[i].strPlayer}')" class="btn btn-info fw-bold">Add to group</button>
                            <button onclick="showDetails(${obj.player[i].idPlayer})" class="btn btn-secondary fw-bold" data-bs-toggle="modal" data-bs-target="#exampleModal">See Details</button>
                        </div>
                    </div>
                `
                all_teams.appendChild(div);
                
            }
    })
}

getAllPlayers();