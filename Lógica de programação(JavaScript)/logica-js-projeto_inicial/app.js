alert('Boas Vindas. Você conseguirá descobrir o numero? ')
let tentativas = 0
let numeroEscolhido;
let minimo = 0
let maximo = 0;
let numeroSecreto = Math.floor(Math.random() * maximo + minimo);

while(numeroSecreto!== numeroEscolhido){
    tentativas++;
    numeroEscolhido = prompt(`Digite um numero de ${minimo} a ${maximo}: `);
numeroescolhido = parseInt(numeroEscolhido);
if(isNaN(numeroEscolhido) || numeroEscolhido < minimo || numeroEscolhido > maximo ){
numeroEscolhido = prompt(`Numero Invalido. Digite um numero de ${minimo} a ${maximo}: `)
}

if(numeroSecreto == numeroEscolhido){
    break;
}else{
    if(numeroescolhido>numeroSecreto){
        alert(`Numero Secreto é menor que ${numeroEscolhido} `);
    }else{
       alert(`Numero Secreto é maior que ${numeroEscolhido} `);
    }
}

}
let ntentativas = tentativas > 1 ? "tentativa" : "tentativas";
alert(`Você descobriu o numero secreto ${numeroSecreto} com ${tentativas} ${ntentativas}`);





