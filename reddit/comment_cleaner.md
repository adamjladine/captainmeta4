---
title: Reddit Comment Cleaner
layout: reddit
---

This tool deletes all of your reddit comments.

This process cannot be stopped once started.

<div id="display-result">
<button type="button" onClick="doubleCheck()">Click here to delete your comments</button>
</div>
<script>
    function doubleCheck(){
        var x=document.getElementById('display-result');
        x.innerHTML='Are you sure?</p><p><button type="button" onClick="imSure()">Yes</button><button type="button" onClick="nope()">No</button>';
    }
    function nope(){
        var x=document.getElementById('display-result')
        x.innerHTML='<button type="button" onClick="doubleCheck()">Click here to delete your comments</button>';
    }
    function imSure(){
        var url="https://api.captainmeta4.me/reddit/clean_comments"
        var r = new XMLHttpRequest();
        r.open("POST", url);
        r.onload=function displayView(){
            var x = document.getElementById('display-result');
            x.innerHTML=r.response;
        }
        r.withCredentials=true;
        r.send();
        var x = document.getElementById('display-result');
        x.innerHTML='<p>captainmeta4.me is now deleting your comments. This message will update when the process is complete.</p>'
    }
</script>
