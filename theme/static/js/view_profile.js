function view_profile(){
    console.log("{% url '/profile/' %}")
    window.location.href = "/users/profile/";
}