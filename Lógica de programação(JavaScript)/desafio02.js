/*
Pergunte ao usuário qual é o dia da semana. Se a resposta for "Sábado" ou "Domingo", mostre "Bom fim de semana!". Caso contrário, mostre "Boa semana!".

Verifique se um número digitado pelo usuário é positivo ou negativo. Mostre um alerta informando.

Crie um sistema de pontuação para um jogo. Se a pontuação for maior ou igual a 100, mostre "Parabéns, você venceu!". Caso contrário, mostre "Tente novamente para ganhar.".

Crie uma mensagem que informa o usuário sobre o saldo da conta, usando uma template string para incluir o valor do saldo.

Peça ao usuário para inserir seu nome usando prompt. Em seguida, mostre um alerta de boas-vindas usando esse nome.
*/ 

let dia = prompt("Dia da semana:");
if(dia === "domingo" || dia === "sabado") {
alert("Bom fim de semana!")
}else{
    alert("Boa semana!")
}

let numero = prompt("Numero:");
if(numero< 0) {
alert("Negativo")
}else{
    alert("Positivo")
}

let pontuacao = prompt("Pontuação:");
if(pontuacao< 99) {
alert("Tente novamente para ganhar.")
}else{
    alert("Parabéns, você venceu!")
}

let saldo = prompt("Saldo:");
alert(`Saldo: R$ ${saldo}`) ;

let nome= prompt("Nome:");
alert(`Boa-vindas ${nome}`) ;
