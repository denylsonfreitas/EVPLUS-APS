function salvar_perfil(){
    var form = $('#form_perfil');
    var url = form.attr('action');
    var data = form.serialize();
    $.post(url, data, function(response){
        if(response.status == 'success'){
            alert('Perfil salvo com sucesso!');
        }else{
            alert('Erro ao salvar perfil!');
        }
    }, 'json');
}