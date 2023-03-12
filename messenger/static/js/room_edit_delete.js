const room_id = document.getElementById('room_id');

const redirect_url = 'http://127.0.0.1:8000/rooms/';
const api_url = `http://127.0.0.1:8000/api/v1/rooms/${room_id.textContent}/`;
const del_btn = document.getElementById('delete_room');
let request_data;
const input_room_name = document.getElementById('id_name');

window.onload = async () => {
   await fetch(api_url, {

}).then(async (response) => {
    return await response.json();
}).then((data) => {
    console.log(data);
    request_data = data;
    input_room_name.value = data.name;
    // console.log(data.slug)
})};

const btn = document.getElementById('edit_room');

btn.addEventListener('click', async (e) => {
    e.preventDefault();
    let params;
    params = {
        'id': request_data.id,
        'name': input_room_name.value,
        'slug': input_room_name.value,
        'creator': request_data.creator,
    };
    await fetch(api_url, {
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(params),
    }).then(async (response) => {
        return await response.json();
    }).then((data) => {
        console.log(data);
        window.location.href = redirect_url;
    }).catch((err) => {
        console.log(err);
    });
});



del_btn.addEventListener('click', (e) => {
    e.preventDefault();
    fetch(api_url, {
        method: 'DELETE',
    }).then( (response) => {
        response.json()
    }).then((data) => {
        console.log(data);
        window.location.href = redirect_url;
    }).catch((err) => {
        console.log(err);
    });
});



// const onclick = (e) => {
//     if (e.target.className.includes('delete_room')) {
//         e.preventDefault();
        
//         const api_url = `http://127.0.0.1:8000/api/v1/rooms/${e.target.id}/`;
//         const response = fetch(api_url, {
            
//         method: 'DELETE',
        
//     }).then((response) => {
//         // console.log(response.status)
//         window.location.reload();
//         return response.json();

//     }).catch((err) => {
//         console.log(err);
//     }); 

//     };
//     return false;
// };

// window.addEventListener('click', onclick)

// const editRoom = (e) => {
    
//     if (e.target.className.includes('edit_room')){
//       let roomName = e.target.getAttribute("data-room-name");
//       let roomId = e.target.getAttribute("data-room-id");
//       document.getElementById('edit_room_name').value = roomName;
//       const modalBody = document.getElementById('ModalEditDeleteRoom');
//       console.log(document.querySelector('modal-body'));

//       window.addEventListener('click', acceptEditRoom);
      
//     }};

// window.addEventListener('click', editRoom)

// const acceptEditRoom = (e) => {
//     const btn = document.querySelector('.js_submit');
    
//     console.log(btn);
// }


// form.addEventListener('submit', (e) => {
//     e.preventDefault();
    
//     params = new FormData(form)
//     params.set('id', params.get('id'));
//     params.set('creator', user_id.textContent);
//     params.set('slug', params.get('name'));
    
//     const redirect_url = 'http://127.0.0.1:8000/rooms/';
//     const api_url = 'http://127.0.0.1:8000/api/v1/rooms/';

//     const response = fetch(api_url, {
//         method: 'POST',
//         body: params,
        
//     }).then((response) => {
        
//         return response.json();
//     }).then((data) => {
//         window.location.href = redirect_url + data.id
//         console.log(data);
//     }).catch((err) => {
//         console.log(err);
//     }); 
// });