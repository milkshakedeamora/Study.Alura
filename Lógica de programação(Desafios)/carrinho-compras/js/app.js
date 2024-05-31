function adicionar(){
    var quantidade = parseInt(document.querySelector('#quantidade').value)
    if(isNaN(quantidade)){
        alert("Quantidade Inválida")

    }else{
    var produto = document.querySelector('#produto').value    
    var produtoNome = produto.split('-')[0];
    var produtoValor = produto.split('R$')[1];
    var textHTML = `<br><span class="texto-azul"> ${quantidade}x </span> ${produtoNome} <span class="texto-azul"> R$ ${produtoValor}</span>`
    document.querySelector('.carrinho__produtos__produto').innerHTML+=textHTML;
    var total = document.querySelector('#valor-total');
    var valorTotal = total.textContent.split("R$")[1]
    total.textContent = `R$ ${parseFloat(valorTotal)+(parseInt(produtoValor)*quantidade)}` 
    }
    document.querySelector('#quantidade').value =""
}
function limpar(){
    document.querySelector('.carrinho__produtos__produto').innerHTML="";
    document.querySelector('#valor-total').textContent = 'R$0'
    document.querySelector('#quantidade').value =""
}