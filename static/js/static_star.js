const div_rate = document.getElementsByName('rate')


const handle_star_select = (size,arr) => {
    const children = arr
    for (let i = 0; i<children.length; i++){
        if(i<=size){
            children[i].classList.add('checked')
        }else{
            children[i].classList.remove('checked')
        }
    }
}

div_rate.forEach(item=>{
    const rate = item.children[0].value
    const span1 = item.children[1]
    const span2 = item.children[2]
    const span3 = item.children[3]
    const span4 = item.children[4]
    const span5 = item.children[5]
    const arr = [span1, span2, span3, span4, span5]
    handle_star_select(rate-1,arr)
})