function fire(x) {
    function processData(data) {
        // taking care of data
    }

    function handler() {
        if(this.status == 200 &&
        this.responseXML != null &&
        this.responseXML.getElementById('test').textContent) {
        // success!
        processData(this.responseXML.getElementById('test').textContent);
        } else {
        // something went wrong
        
        }
    }
    var client = new XMLHttpRequest();
        client.onload = handler;
        client.open("GET", x);
        client.send();
};

function loadtemp(){
    $('#temperature').load('/php/temperature.php')
};
function loadpage(x){
    window.location.href = x;
};
var onlongtouch; 
var timer, lockTimer;
var touchduration = 800; //length of time we want the user to touch before we do something

function touchstart() {
    fire('/php/apple/menu_start.php')
}

function touchend() {
    fire('/php/apple/menu_stop.php')
}

function touchstartb() {
    fire('/php/apple/play_start.php')
}

function touchendb() {
    fire('/php/apple/play_stop.php')
}


document.addEventListener("DOMContentLoaded", function(event) { 
    document.getElementById("menu").addEventListener("touchstart", touchstart, false);
    document.getElementById("menu").addEventListener("touchend", touchend, false);
    document.getElementById("play").addEventListener("touchstart", touchstartb, false);
    document.getElementById("play").addEventListener("touchend", touchendb, false);
});
function loadtemp(){
    $('#temperature').load('/php/temperature.php')
};

$(document).ready(function(){
    (function($) {
    var IS_IOS = /iphone|ipad/i.test(navigator.userAgent);
    $.fn.nodoubletapzoom = function() {
        if (IS_IOS)
        $(this).bind('touchstart', function preventZoom(e) {
            var t2 = e.timeStamp
            , t1 = $(this).data('lastTouch') || t2
            , dt = t2 - t1
            , fingers = e.originalEvent.touches.length;
            $(this).data('lastTouch', t2);
            if (!dt || dt > 500 || fingers > 1) return; // not double-tap

            e.preventDefault(); // double tap - prevent the zoom
            // also synthesize click events we just swallowed up
            $(this).trigger('click').trigger('click');
        });
    };
    })(jQuery);

    loadtemp();
    setInterval(function(){
        loadtemp() // this will run after every XX seconds
    }, 10000);
});