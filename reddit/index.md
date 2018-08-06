---
title: Reddit Webtools
---

# Reddit Webtools

<div id="display-identity"></div>
<script>
    function loadView(){
        var query=window.location.href.split("?")[1]
        var url="https://api.captainmeta4.me/reddit/identity"
        if (Boolean(query)) {
            url=url+"?"+query
        }
        var r = new XMLHttpRequest();
        r.open("GET", url);
        r.onload=function displayView(){
            var x = document.getElementById('display-identity');
            x.innerHTML=r.response;
        }
        r.withCredentials=true;
        r.send();
    }
    loadView()
</script>

[Click here to authenticate with reddit to use these tools.](https://www.reddit.com/api/v1/authorize?client_id=YMMmOZqjTL5FLA&duration=permanent&redirect_uri=https%3A%2F%2Fapi.captainmeta4.me%2Freddit%2Fredirect&response_type=code&scope=identity+read+edit&state=x)

Tool|Description
-|-
[Comment Cleaner](./comment_cleaner) | Deletes all of your existing comments. Yes, *all* of them.
