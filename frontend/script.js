function votar(candidato) {
    const eleitorId = document.getElementById("eleitor_id").value.trim();
    
    if (!eleitorId) {
        alert("Digite seu ID de eleitor!");
        return;
    }

    fetch("/votar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            eleitor_id: eleitorId,
            voto: candidato
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("mensagem").textContent = data.mensagem || data.erro;
    })
    .catch(error => {
        console.error("Erro ao votar:", error);
    });
}
