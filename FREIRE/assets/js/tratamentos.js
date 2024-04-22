document.addEventListener('DOMContentLoaded', function () {
    var tratamentoCards = document.querySelectorAll('.tratamento-card');

    tratamentoCards.forEach(function (card) {
        var imagem = card.querySelector('img');
        var infoTratamento = card.querySelector('.info-tratamento');
        
        card.addEventListener('click', function () {
            var link = card.querySelector('a');
            if (link) {
                var href = link.getAttribute('href');
                if (href) {
                    window.location.href = href;
                }
            }
        });

        imagem.addEventListener('mouseenter', function() {
            infoTratamento.style.backgroundColor = 'rgba(46, 46, 46, 0)';
        });
        
        imagem.addEventListener('mouseleave', function() {
            infoTratamento.style.backgroundColor = 'rgba(46, 46, 46, 0.5)';
        });
    });
});
