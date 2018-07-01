---
title: Using Github to Host Your Writing
---

# Using Github to Host Your Writing

Effective 06 June 2018, the Reddit user agreement will be claiming additional intellectual property rights over creative works posted to reddit. To avoid surrendering these rights to reddit, many authors want to find alternative hosts for their writing.

The Github user agreement allows you to retain your rights over creative works hosted on github. Github also hosts user sites, and is a good solution for hosting creative writing.

1. [Create a Github account](https://github.com/join) if you don't have one already.

2. [Open my writing template](https://github.com/captainmeta4/hfy-template) and fork it. This is my custom implementation of the Github Pages "Minimal" theme, in use throughout this site.

3. Open repository settings. Under "Github Pages", click "Change Theme" and select the "Minimal" theme. (You can select a different theme if you really want to, but you will need to delete the customization files located at `_layouts/default.html` and `assets/css/style.scss`.)

3. If you **will not** be using a custom domain name, rename your repository to `<username>`.github.io, where `<username>` is **your** username.

4. If you **will** be using a custom domain name, create the following DNS records (where `<username>` is your github username):

    Name|Type|Data
    -|-|-
    @|A|185.199.108.153
    ||185.199.109.153
    ||185.199.110.153
    ||185.199.111.153
    www|CNAME|<username>.github.io

    Then, create a new file called `CNAME` at the top level of the repository. Paste in the custom domain.

5. Rework the contents of the `/books/` folder as needed to contain your writing:

    Contents|Github File Location|Public URL
    -|-|-
    List of your books|/books/index.md|/books
    Book overview|/books/book_name/index.md|/books/book_name
    Individual Chapter|/books/book_name/1.md|/books/book_name/1
    
    Individual chapters should be named `1.md`, `2.md`, `3.md`, etc. This, combined with the `chapter` tag at the top of each chapter file, will allow Jekyll to automatically generate First/Previous/Next links. The `series_title` and `series_url` tags let Jekyll add links to chapter pages to view the book overview pages.
    
6. (Optional) Go to [Google Analytics](http://analytics.google.com). Create a new tracking account. Once you have your Google Analytics site ID, paste the provided snippet of code into the `<head>` section at `_layouts/default.html`
