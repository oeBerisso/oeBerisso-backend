function prepareModal( id, active){
    $(`#active${id}`).click(function(){
        $(`#active-modal${id}`).modal({
            onApprove : function(){
                try{
                    var url = active ? `usuarios/${id}/desactivar` : `usuarios/${id}/activar`
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
    $(`#edit${id}`).click(function(){
        $(`#roles-modal${id}`).modal({
            onApprove : function(){
                try{
                    var url = active ? `usuarios/${id}/desactivar` : `usuarios/${id}/activar`
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