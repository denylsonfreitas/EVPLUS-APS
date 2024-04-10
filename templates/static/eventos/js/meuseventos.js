function confirmarCancelar(eventoId) {
    // Defina a variável eventoId para ser usada dentro do modal
    window.eventoId = eventoId;
    // Mostrar o modal
    document.getElementById("modalCancelar").style.display = "block";
}

function fecharModalCancelar() {
    // Fechar o modal
    document.getElementById("modalCancelar").style.display = "none";
}

function cancelarInscricao(eventoId) {
    // Redirecionar para a view para cancelar a inscrição
    window.location.href = "{% url 'eventos:cancelar_inscricao' evento_id=0 %}".replace('0', eventoId);
}
