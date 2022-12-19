
// ============ PLAYER POSITION ============
let player_position = document.getElementById('player_position').innerText;
console.log(player_position);

let positions=['cf','lcf','lf','ls','lw','rcf','rf','rs','rw','st','cam','cdm','cm','lam','lcam','lcdm','lcm','ldm','lm','lwm','ram','rcam','rcdm','rcm','rdm','rm','rwm','cb','lb','lcb','lwb','rb','rcb','rwb','sw','gk','sub'];

const positions_upper = positions.map(element => {
    return element.toUpperCase();
  });
var position_index = positions_upper.findIndex(element => element.includes(player_position))

let badge = document.getElementById('player_position');
badge.classList.add(positions[position_index]);

// ===========================================

// ============ PLAYER SKILLS =================

let player_skill = parseInt(document.getElementById('player_skill').value);
let skill_conteiner =  document.getElementById('skill_stars');

var player_skill_stars = "";

for (let i = 0; i < player_skill; i++) {
    player_skill_stars += `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-star-fill" viewBox="0 0 16 16">
    <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"></path>
  </svg>`;
}

for (let i = 0; i < 5-player_skill; i++) {
    player_skill_stars += `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-star" viewBox="0 0 16 16">
    <path d="M2.866 14.85c-.078.444.36.791.746.593l4.39-2.256 4.389 2.256c.386.198.824-.149.746-.592l-.83-4.73 3.522-3.356c.33-.314.16-.888-.282-.95l-4.898-.696L8.465.792a.513.513 0 0 0-.927 0L5.354 5.12l-4.898.696c-.441.062-.612.636-.283.95l3.523 3.356-.83 4.73zm4.905-2.767-3.686 1.894.694-3.957a.565.565 0 0 0-.163-.505L1.71 6.745l4.052-.576a.525.525 0 0 0 .393-.288L8 2.223l1.847 3.658a.525.525 0 0 0 .393.288l4.052.575-2.906 2.77a.565.565 0 0 0-.163.506l.694 3.957-3.686-1.894a.503.503 0 0 0-.461 0z"></path>
  </svg>`;
}

skill_conteiner.innerHTML = player_skill_stars;

// ===========================================

// ============ PLAYER WEAK FOOT =============

let player_weak_foot = parseInt(document.getElementById('player_foot').value);
let weak_foot_conteiner =  document.getElementById('foot_stars');

var player_foot_stars = "";

for (let i = 0; i < player_weak_foot; i++) {
    player_foot_stars += `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-star-fill" viewBox="0 0 16 16">
    <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"></path>
  </svg>`;
}

for (let i = 0; i < 5-player_weak_foot; i++) {
  player_foot_stars += `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-star" viewBox="0 0 16 16">
  <path d="M2.866 14.85c-.078.444.36.791.746.593l4.39-2.256 4.389 2.256c.386.198.824-.149.746-.592l-.83-4.73 3.522-3.356c.33-.314.16-.888-.282-.95l-4.898-.696L8.465.792a.513.513 0 0 0-.927 0L5.354 5.12l-4.898.696c-.441.062-.612.636-.283.95l3.523 3.356-.83 4.73zm4.905-2.767-3.686 1.894.694-3.957a.565.565 0 0 0-.163-.505L1.71 6.745l4.052-.576a.525.525 0 0 0 .393-.288L8 2.223l1.847 3.658a.525.525 0 0 0 .393.288l4.052.575-2.906 2.77a.565.565 0 0 0-.163.506l.694 3.957-3.686-1.894a.503.503 0 0 0-.461 0z"></path>
</svg>`;
}

weak_foot_conteiner.innerHTML = player_foot_stars;

// ===========================================

/// CHANGE NUMBER TO A VALUE IN EUROS 

function toEuros(number) {
  const formatter = new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR',  maximumFractionDigits:0});
  return formatter.format(number);
}
let number = document.getElementById('player_value').innerText;

let value = toEuros(number);

document.getElementById('player_value').innerText = value;
console.log(value);