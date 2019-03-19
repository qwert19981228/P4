/*滚动事件*/
window.onscroll = function () {
    var top = document.documentElement.scrollTop || document.body.scrollTop || window.pageYOffset;
    console.log(top);

    var title = document.getElementById('title');
    var proview = document.getElementById('view');

    if (top >= 300){
        title.style.position = 'fixed';
        title.style.top = '0px';
    }else if (top < 300){
        title.style.position = 'static';
    }

    if (top > 150 && top <= 900){
        proview.style.position = 'fixed';
        proview.style.top = '100px'
    }else if (top > 900) {
        proview.style.position = 'relative';
        proview.style.top = '850px'
    }else if (top < 150){
        proview.style.position = 'relative';
        proview.style.top = '0px'
    }
};
