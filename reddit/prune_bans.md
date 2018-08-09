---
title: Prune Subreddit Bans
layout: reddit
---

This tool checks users in a subreddit ban list, and removes (unbans) accounts that are deleted, suspended, or shadowbanned.

This process cannot be stopped once started.

<p>Subreddit:</p>
<input type="text" name="subreddit" id="sub-input"><br>
<button type="button" onClick="hitAPI()">Prune Bans</button>
<div id="display-result"><div>
<script>
function hitAPI() {
    var sub = document.getElementById('sub-input').value
    var x= new XMLHttpRequest();
    x.open("POST", "https://api.captainmeta4.me/reddit/prune_bans");
    x.withCredentials=true;
    x.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
    x.onload=function displayView(){
        var y = document.getElementById('display-result');
        y.innerHTML=x.response;
    }
    var data = "subreddit="+sub
    x.send(data);
    var y = document.getElementById('display-result');
    y.innerHTML="<p>Sending...</p>";
}
