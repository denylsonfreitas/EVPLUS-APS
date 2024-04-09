function salvar_perfil(){
    form = document.getElementById('form-salvar-perfil');
    form.submit();
}

function exibirPopup() {
    alert("Conta alterada com sucesso!");
}

document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        var alertContainer = document.getElementById('alert-container');
        alertContainer.innerHTML = '';
    }, 7000);
});