function openSubmenu(element) {
    var submenu = element.querySelector('.submenu');
    submenu.classList.remove('submenu-close');
    submenu.classList.add('submenu-open');
}

function closeSubmenu(element) {
    var submenu = element.querySelector('.submenu');
    setTimeout(function() {
        submenu.classList.remove('submenu-open');
        submenu.classList.add('submenu-close');
    }, 10000); 
}
