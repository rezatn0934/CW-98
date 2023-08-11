let p = document.getElementById("test")

document.getElementById('btn1').addEventListener('click', myFunction)
function myFunction() {
    if (p.style.display == 'none'){
        p.style.display = 'block';
    }
    else {
        p.style.display = 'none';
    }

};