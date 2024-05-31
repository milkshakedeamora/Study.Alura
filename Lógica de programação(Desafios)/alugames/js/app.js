function alterarStatus(indice) {

    div = document.querySelector(`#game-${indice} div`);
    p = document.querySelector(`#game-${indice} a`);
    if (div.classList.contains('dashboard__item__img--rented')) {
        div.classList.remove('dashboard__item__img--rented');
        p.classList.remove('dashboard__item__button--return');
        p.textContent = "Alugar";

    } else {
        div.classList.add('dashboard__item__img--rented');
        p.classList.add('dashboard__item__button--return');
        p.textContent = "Devolver";
    }
}

