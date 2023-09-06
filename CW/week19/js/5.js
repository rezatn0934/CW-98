let password = document.getElementById("password")
let username = document.getElementById('username')
let chbx = document.getElementById('checkbox1')


if (getCookie('username') || getCookie('password')) {
  if (location.href != '2.html') location.replace('1..html')
}

document.getElementById('btn1').addEventListener('click', myFunction)

function myFunction() {
    if (chbx.checked) {
        setCookie('username', username, 10);
        setCookie('password', password, 10);
    }
}

function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    let expires = "expires=" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}
