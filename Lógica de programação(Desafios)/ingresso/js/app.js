function comprar() {
    var qtdCompra = parseInt(document.querySelector('#qtd').value)
    var tipo = document.querySelector('#tipo-ingresso').value
    var qtdIngresso = parseInt(document.querySelector(`#qtd-${tipo}`).textContent)
    if (qtdCompra > qtdIngresso || qtdCompra < 1) {
        alert("Quantidade Inválida para compra.")

    }
    else {
        document.querySelector(`#qtd-${tipo}`).textContent = qtdIngresso - qtdCompra;
    }
    document.querySelector('#qtd').value = ""
}