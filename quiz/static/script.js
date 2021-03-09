window.onload = initall;

var  saveBookButton ;

function initall() {
    saveBookButton=document.getElementById('save_ans')
    saveBookButton.onclick = save_ans;
}

function save_ans() {
    var ans = $("input:radio[name=name]:checked").val()
    alert("answer submited go next")
    var url = '/saveans?ans='+ans
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
    
  };
  req.open("GET", url, true);
  req.send();
}