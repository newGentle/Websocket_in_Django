const form = document.querySelector('form');
const user_id = document.getElementById('user_id');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    
    params = new FormData(form)
    params.set('id', params.get('id'));
    params.set('creator', user_id.textContent);
    params.set('slug', params.get('name'));
    
    const redirect_url = 'http://127.0.0.1:8000/rooms/';
    const api_url = 'http://127.0.0.1:8000/api/v1/rooms/';

    const response = fetch(api_url, {
        method: 'POST',
        body: params,
        
    }).then((response) => {
        
        return response.json();
    }).then((data) => {
        window.location.href = redirect_url + data.id
        console.log(data);
    }).catch((err) => {
        console.log(err);
    }); 
});