---
title: Patreon Rewards
---

<iframe id="iframe-patreon" src="https://api.captainmeta4.me/patreon" style="display:none"></iframe>
<script>
function displayContent() {
    var x = document.getElementById("iframe-patreon").srcdoc;
    document.getElementById("display-patreon").innerHTML = x;
}
</script>
<div id="display-patreon" onload="displayContent()"></div>
