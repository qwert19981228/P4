window.onscroll = function () {
    var top = document.documentElement.scrollTop || document.body.scrollTop || window.pageYOffset;
    var bartop = document.getElementById('bartop');

    if (top >= 850){
        bartop.style.display = 'block';
    }else if (top < 800){
        bartop.style.display = 'none';
    }
};