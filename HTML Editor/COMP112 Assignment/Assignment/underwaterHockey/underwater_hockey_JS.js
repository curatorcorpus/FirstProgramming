/* JavaScript */

    function Divs() {
        var divs= $('#news div'),
            now = divs.filter(':visible'),
            next = now.next().length ? now.next() : divs.first(),
            speed = 1000;
    
        now.fadeOut(30000);
        next.fadeIn(30000);
    }
    
    $(function () {
        setInterval(Divs, 1400);
    });