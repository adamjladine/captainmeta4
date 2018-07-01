---
title: Using Github to Host Your Writing
---

# Using Github to Host Your Writing

Effective 06 June 2018, the Reddit user agreement will be claiming additional intellectual property rights over creative works posted to reddit. To avoid surrendering these rights to reddit, many authors want to find alternative hosts for their writing.

The Github user agreement allows you to retain your rights over creative works hosted on github. Github also hosts user sites, and is a good solution for hosting creative writing.

1. [Create a Github account](https://github.com/join) if you don't have one already.

2. [Open my writing template](https://github.com/captainmeta4/hfy-template) and fork it. This is my custom implementation of the Github Pages "Minimal" theme, in use throughout this site.

3. Open repository settings. Under "Github Pages", click "Change Theme" and select the "Minimal" theme. (You can select a different theme if you really want to, but you will need to delete the customization files located at `_layouts/default.html` and `assets/css/style.scss`.)

3. If you **will not** be using a custom domain name, rename your repository to "<username>.github.io", where <username> is **your** username.

4. If you **will** be using a custom domain name, create the following DNS records (where "<username>" is your github username):

    Name|Type|Data
    -|-|-
    @|A|185.199.108.153
    |||185.199.109.153
    |||185.199.110.153
    |||185.199.111.153
    www|CNAME|<username>.github.io

    Then, create a new file called `CNAME` at the top level of the repository. Paste in the custom domain.
