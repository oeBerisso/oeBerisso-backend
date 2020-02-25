function prepareModal(id){
    $(`#delete${id}`).click(function(){
        $(`#delete-modal${id}`).modal({
            onApprove : function(){
                try{
                    var url = `/instrumento/${id}/eliminar`
                    fetch(url,{
                        method: 'POST'
                    }).then((response)=>{
                        window.location.href = response.url
                    })
                } 
                catch(e){
                    console.log('ocurrio un error', e)
                } finally {
                    return true
                }
            }
        }).modal('show');      
    });
    $(`#show${id}`).click(function(){
        $(`#profile-modal${id}`).modal({
            onApprove : function(){
                try{
                    var url = `/instrumento/${id}/ver_perfil`
                    fetch(url,{
                        method: 'POST'
                    }).then((response)=>{
                        window.location.href = response.url
                    })
                } 
                catch(e){
                    console.log('ocurrio un error', e)
                } finally {
                    return true
                }
            }
        }).modal('show');      
    });
}

