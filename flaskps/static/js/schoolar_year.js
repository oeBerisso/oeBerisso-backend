function prepareSchoolarModal(id){
    console.log(id)
    $(`#btn-${id}`).click(function(){
        console.log(`Click: ${id}`)
        $(`#${id}`).modal('show');      
    });
}
