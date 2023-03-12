const room_id = document.getElementById('room_id');
const form = document.querySelector('form');

const redirect_url = 'http://127.0.0.1:8000/rooms/';
const api_url = `http://127.0.0.1:8000/api/v1/rooms/${room_id.textContent}/?format=json`;
const del_btn = document.getElementById('delete_room');
let request_data;
print(api_url)
console.log(api_url);

fetch(api_url, {

}).then((response) => {
    return response.json();
}).then((data) => {
    console.log(data);
    request_data = data;
    const input_room_name = document.getElementById('id_name');
    input_room_name.value = data.name;
    console.log(data.slug)
});


form.addEventListener('submit', (e) => {
    
    const params = new FormData(form);
    params.append('id', data.id);
    params.append('name', input_room_name.value);
    params.append('slug', input_room_name.value);
    params.append('creator', data.creator);
    
    fetch(api_url, {
        method: 'PUT',
        body: params,
    }).then((response) => {
        return response.json();
    }).then((data) => {
        console.log(data);
    }).catch((err) => {
        console.log(err);
    });
});





del_btn.addEventListener('click', () => {
    fetch(api_url, {
        method: 'DELETE',
    }).then((response) => {
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