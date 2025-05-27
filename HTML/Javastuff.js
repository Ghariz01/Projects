function validate() {
    const us = document.getElementById('us').value;
    const em = document.getElementById('em').value;
    const pw = document.getElementById('pw').value;
    if (pw=='123' && em=='user@gmail.com') {
        sessionStorage.setItem('us',us);
        window.location.href = "Main Page.html";
    } else {
        alert("Something Wrong!")
    } 
  
}

function bravo() {
    const headline = document.getElementById('h1');
    const us = sessionStorage.getItem('us');
    headline.innerHTML = `Welcome ${us}`;
}


let inverse = true

function darkmode() {
    if(inverse) {
        document.body.style.backgroundColor = 'black';
        document.body.style.color = 'white';
    } else {
        document.body.style.backgroundColor = 'aquamarine';
        document.body.style.color = 'black';
    } 
    inverse=!inverse;
}
function SetRating() {
   const Rating = document.getElementById('Rating').value;
   const text = document.getElementById('p');
   text.innerHTML = `You rated us ${Rating}`;
}


function Change() {
    var newText = document.getElementById('Keimeno').value;
    document.getElementById('Allagitext').innerHTML = newText;
    document.getElementById('Keimeno').value = "";
}

