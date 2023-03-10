
const onclick = (e) => {
    if (e.target.className.includes('delete_room')) {
        e.preventDefault();
        
        const api_url = `http://127.0.0.1:8000/api/v1/rooms/${e.target.id}/`;
        const response = fetch(api_url, {
            
        method: 'DELETE',
        
    }).then((response) => {
        // console.log(response.status)
        window.location.reload();
        return response.json();

    }).catch((err) => {
        console.log(err);
    }); 

    };
    return false;
};

window.addEventListener('click', onclick)

// delete_room_btn.onclick = function (e) {
//     console.log(e);
// }
// delete_room_btn.addEventListener('click', (e) => {
//     // e.preventDefault();
    
//     console.log('ok')
    // params.set('id', params.get('id'));
    // params.set('creator', user_id.textContent);
    // params.set('slug', params.get('name'));
    
    // const redirect_url = 'http://127.0.0.1:8000/rooms/';
    // const api_url = 'http://127.0.0.1:8000/api/v1/rooms/';

    // const response = fetch(api_url, {
    //     method: 'DELETE',
    //     body: params,
        
    // }).then((response) => {
        
    //     return response.json();
    // }).then((data) => {
    //     window.location.href = redirect_url + data.id
    //     console.log(data);
    // }).catch((err) => {
    //     console.log(err);
    // }); 
// });