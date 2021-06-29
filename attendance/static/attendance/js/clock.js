function time(){
    var now = new Date();
    document.getElementById("time").innerHTML = now.toLocaleString();
}
setInterval('time()',1000);