---
layout: reddit
title: Clear Unmoderated
---

This tool approves all items in a subreddit's unmoderated queue.

<p>Subreddit:</p>
<input type="text" name="subreddit" id="sub-input"><br>
<button type="button" onClick="hitAPI()">Clear Unmod</button>
<div id="display-result"><div>
<script>
function hitAPI() {
    var sub = document.getElementById('sub-input').value
    var x= new XMLHttpRequest();
    x.open("POST", "https://api.captainmeta4.me/reddit/clear_unmod");
    x.setRequestHeader('Content-Type', 'application/json');
    r.onload=function displayView(){
        var y = document.getElementById('display-result');
        y.innerHTML=r.response;
    }
    x.send(JSON.stringify({"subreddit": sub}));
}
</script>
