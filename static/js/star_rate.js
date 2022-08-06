const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')
const sub_btn = document.getElementById('sub_btn')
const who = document.getElementById('who').value

const form = document.querySelector('.rate-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const arr = [one, two, three, four, five]

const handle_star_select = (size) => {
    const children = arr
    for (let i = 0; i<children.length; i++){
        if(i<=size){
            children[i].classList.add('checked')
        }else{
            children[i].classList.remove('checked')
        }
    }
}


const handle_select = (selection) => {
    switch(selection){
        case 'first':{
            handle_star_select(0)
            return
        }
        case 'second':{
            handle_star_select(1)
            return
        }
        case 'third':{
            handle_star_select(2)
            return
        }
        case 'fourth':{
            handle_star_select(3)
            return
        }
        case 'fifth':{
            handle_star_select(4)
            return
        }
    }
}

const get_numeric_value = (string_value) =>{
    let numeric_value;
    if(string_value === 'first') {
        numeric_value = 1
    }
    else if(string_value === 'second') {
        numeric_value = 2
    }
    else if(string_value === 'third') {
        numeric_value = 3
    }
    else if(string_value === 'fourth') {
        numeric_value = 4
    }
    else if(string_value === 'fifth') {
        numeric_value = 5
    }
    else{
        numeric_value = 0
    }
    return numeric_value
}


let is_submit = false
arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
    handle_select(event.target.id)
    

    arr.forEach(item=> item.addEventListener('click',(event)=>{
        const val = event.target.id
        
        form.addEventListener('submit',e=>{
            e.preventDefault()
            if (is_submit){
                return
            }
            is_submit=true
            const comment = document.getElementById('comment').value
            const hide = $('#flexSwitchCheckChecked').prop('checked')
            const id = e.target.id
            const val_num = get_numeric_value(val)
            const url = 'http://127.0.0.1:8000/'+document.title+'/page/'+who

            $.ajax({
                type:'POST',
                url: url,
                data:{
                    'csrfmiddlewaretoken':csrf[0].value,
                    'val':val_num,
                    'comment':comment,
                    'hide':hide,
                    'who':who,
                },
                success: function(response) {
                    location.reload()

                },

                error: function(error) {
                    alert("Hata oluştu tekrar deneyiniz")
                    location.reload()

                },

            })
        })
        
    }))
}))
