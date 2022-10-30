
let searchForm = document.getElementById("search_player_form");
let searchInput = document.getElementById("search_players_input");
let results = document.getElementById("search_player_result");
let csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;

const sendSearchData = (player_name) => {
    $.ajax({
        type: 'POST',
        url: 'playerSearch/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'player_name': player_name,
        },
        success: (response) => {
 
            const data = response.data;
            
            if (Array.isArray(data)) {
                results.innerHTML = "";
                data.forEach(player=>{
                results.innerHTML += `
                <div class="row justify-content-start mt-2 mb-2">
                <div class="col-2">
                    <img src="${player.player_face_url}" class="img-fluid">
                </div>
                <div class="col-5">
                <p class="mt-3"><b>${player.long_name}</b><br>
                <i>${player.club_name}</i><br>
                <button type="button" class="btn btn-light btn-sm mt-1" disabled>${player.player_position}</button>
                </p>
                </div>
                <div class="col-2">
                <button type="button" class="btn btn-light mt-3" disabled>${player.overall}</button>
                <button type="button" class="btn btn-light mt-3" disabled>${player.potential}</button>
                </div>
                <div class="col-2">
                <button type="button" class="btn btn-light mt-3" disabled>
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-calendar-date-fill" viewBox="0 0 16 16">
                <path d="M4 .5a.5.5 0 0 0-1 0V1H2a2 2 0 0 0-2 2v1h16V3a2 2 0 0 0-2-2h-1V.5a.5.5 0 0 0-1 0V1H4V.5zm5.402 9.746c.625 0 1.184-.484 1.184-1.18 0-.832-.527-1.23-1.16-1.23-.586 0-1.168.387-1.168 1.21 0 .817.543 1.2 1.144 1.2z"></path>
                <path d="M16 14V5H0v9a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2zm-6.664-1.21c-1.11 0-1.656-.767-1.703-1.407h.683c.043.37.387.82 1.051.82.844 0 1.301-.848 1.305-2.164h-.027c-.153.414-.637.79-1.383.79-.852 0-1.676-.61-1.676-1.77 0-1.137.871-1.809 1.797-1.809 1.172 0 1.953.734 1.953 2.668 0 1.805-.742 2.871-2 2.871zm-2.89-5.435v5.332H5.77V8.079h-.012c-.29.156-.883.52-1.258.777V8.16a12.6 12.6 0 0 1 1.313-.805h.632z"></path>
                </svg>
                ${player.age}
              </button>
                </div>
                
                
                
                </div>`;
                });
            }else{
                if (searchInput.value.length > 0){
                    results.innerHTML = `<b>${data}</b>`;
                }else{
                    results.classList.add('not-visible');
                }
            }
        },
        error: (err) => {
            console.log(err);
        }
    })
}

searchInput.addEventListener('keyup', e=>{
    if (results.classList.contains("not-visible")){
        results.classList.remove("not-visible");
    }
    sendSearchData(e.target.value);
});