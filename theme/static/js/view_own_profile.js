function view_own_profile(){
    window.location.href = "/users/" + JSON.parse(document.getElementById('username').textContent) + "/";
}