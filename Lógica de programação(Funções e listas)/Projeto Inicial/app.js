/*let titulo = document.querySelector('h1');
let paragrafo = document.querySelector('p');
titulo.innerHTML = 'Jogo do número secreto'
paragrafo.innerHTML = 'Escolha um número de 0 a 10'*/
let sorteados = [];
let numeroSecreto = gerarNumeroAleatorio();
let numeroEscolhido;
let tentativas = 0;
mensagemInicial();
function exibirTexto(seletor, texto){
    document.querySelector(seletor).innerHTML=texto;
    responsiveVoice.speak(texto,'Brazilian Portuguese Female')
}

function gerarNumeroAleatorio(){
    console.log("Entrou")
    let numeroAtual = Math.floor(Math.random()*10+1)
    if(sorteados.includes(numeroAtual)){
        console.log("Entrou")
        gerarNumeroAleatorio();

    }else{
        console.log("Falhou")
        sorteados.push(numeroAtual);
        return numeroAtual;

    }
    
}
function verificarChute(){

numeroEscolhido = document.querySelector('input').value;
numeroEscolhido = parseInt(numeroEscolhido);
if(numeroEscolhido < 1|| numeroEscolhido >10){
    exibirTexto('p',`O número não é válido .`)

}else{
    tentativas++;
    if(numeroEscolhido == numeroSecreto){
        var texto = tentativas > 1? "tentativa":"tentativas"
        exibirTexto('p',`Você acertou o número com ${tentativas} ${texto} .`)
        finalizar()
    }else{
        var texto = numeroEscolhido < numeroSecreto? "maior":"menor";
        exibirTexto('p',`O número secreto é ${texto} que ${numeroEscolhido}`)
    }
}
}

function limparInput(){
    document.querySelector('input').value = "";
}

function resetar(){
    document.querySelector('#reiniciar').setAttribute('disabled',true)
    document.querySelector('.container__botao').removeAttribute('disabled');
    document.querySelector('input').style.display='block';
    mensagemInicial();
}
function finalizar(){
    document.querySelector('.container__botao').setAttribute('disabled',true)
    document.querySelector('#reiniciar').removeAttribute('disabled');
    document.querySelector('input').style.display='none';
}

function mensagemInicial(){
    exibirTexto('h1','Jogo do número secreto');
exibirTexto('p','Escolha um número de 0 a 10');
}

function reiniciarJogo(){
    numeroSecreto = gerarNumeroAleatorio();
    limparInput();
    tentativas = 0;
    resetar();
  
    
}
