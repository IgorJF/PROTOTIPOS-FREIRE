
function fadeInImages() {
    var images = document.querySelectorAll('.imgs');

    images.forEach(function(img, index) {
        var rect = img.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom >= 0) {
            img.style.opacity = 1;
        }
    });
}

window.addEventListener('load', fadeInImages);

window.addEventListener('scroll', function() {
    setTimeout(fadeInImages, 100);
});
