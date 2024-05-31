let quantidade;
let min;
let max;
let numeros = [];
function capturarValor() {

    quantidade = parseInt(document.querySelector('#quantidade').value);
    min = parseInt(document.querySelector('#de').value);
    max = parseInt(document.querySelector('#ate').value);
}
function numeroSelecionar() {

    var numero = Math.floor(Math.random() * (max - min + 1) + min)
    if (numeros.includes(numero)) {
        return numeroSelecionar()
    } else {
        numeros.push(numero);


    }


}
function sortear() {
    capturarValor();
    if (min >= max || quantidade >= (max - min) || quantidade < 1) {
        document.querySelector('#resultado').innerHTML = ` <label class ="texto__paragrafo"> Valores Inválidos. Impossivél sortear.</label> `
    } else {

        for (var i = 0; i < quantidade; i++) {

            numeroSelecionar()
        }
        document.querySelector('#resultado').innerHTML = ` <label class ="texto__paragrafo"> Números Sorteados : ${numeros} </label> `
    }

    alterarBotao('#btn-sortear');
    alterarBotao('#btn-reiniciar');
}

function alterarBotao(seletor) {
    var botao = document.querySelector(seletor);
    if (botao.classList.contains('container__botao-desabilitado')) {
        botao.classList.remove('container__botao-desabilitado')
        botao.classList.add('container__botao')
    } else {
        botao.classList.remove('container__botao')
        botao.classList.add('container__botao-desabilitado')
    }
}
function reiniciar() {
    alterarBotao('#btn-sortear');
    alterarBotao('#btn-reiniciar');
    document.querySelector('#resultado').innerHTML = ' <label class="texto__paragrafo">Números sorteados:  nenhum até agora</label>';
    document.querySelector('#quantidade').value = "";
    document.querySelector('#de').value = "";
    document.querySelector('#ate').value = "";
    numeros = [];

}

