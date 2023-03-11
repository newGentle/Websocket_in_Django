
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

const editRoom = (e) => {
    
    if (e.target.className.includes('edit_room')){
      let roomName = e.target.getAttribute("data-room-name");
      document.getElementById('edit_room_name').value = roomName;
      
      
    }};

window.addEventListener('click', editRoom)