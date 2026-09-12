function confirmarOperacao() {
    const numero1 = document.getElementById("numero1").value;
    const numero2 = document.getElementById("numero2").value;

    if (numero1 === "" || numero2 === "") {
        alert("Preencha os dois números!");
        return false;
    }

    return true;
}
