(function () {
    if(!window.bookmarklet) {
        bookmarklets_js = document.body.appendChild(document.createElement('script'));
        bookmarklets_js.src = "//127.0.0.1/static/js/bookmarklet.js?r="+Math.floor(Math.round()*9999999999999999);
        window.bookmarklets = true;
    }
    else {
        bookmarkletLaunch();
    }
})();