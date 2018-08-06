---
title: Reddit Comment Cleaner
layout: reddit
---

This tool deletes all of your reddit comments.

This process cannot be stopped once started.

<div id="display-result">
<p><a href="javascript:doubleCheck();">Click here to delete your comments</a></p>
</div>
<script>
    function doubleCheck(){
        var x=document.getElementById('display-result');
        x.innerHTML='<p>Are you sure?</p><p><a href="javascript:imSure();">Yes</a> / <a href="javascript:nope();">No</a></p>';
    }
    function nope(){
        var x=document.getElementById('display-result')
        x.innerHTML='<p><a href="javascript:doubleCheck();">Click here to delete your comments</a></p>';
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
        x.innerHTML='<p>captainmeta4.me is now deleting your comments. This message will update when the process is complete</p>'
    }
</script>
