---
title: Reddit Comment Cleaner
---

This tool deletes all of your reddit comments.

This process cannot be stopped once started.

<div id="display-result">
<p><a href="javascript:doubleCheck();">Click here to delete your comments</a></p>
</div>
<script>
    function doubleCheck(){
        var link=document.getElementByID('display-result');
        link.innerHTML='<p>Are you sure? <a href="javascript:imSure();">Yes</a> / <a href="javascript:nope();">No</a></p>'
    }
    function nope(){
        var link=document.getElementByID('display-result')
        link.innerHTML='<p><a href="javascript:doubleCheck();">Click here to delete your comments</a></p>'
    }
    function imSure(){
        var url="https://api.captainmeta4.me/reddit/identity"
        var r = new XMLHttpRequest();
        r.open("GET", url);
        r.onload=function displayView(){
            var x = document.getElementById('display-result');
            x.innerHTML=r.response;
        }
        r.withCredentials=true;
        r.send();
    }
</script>
