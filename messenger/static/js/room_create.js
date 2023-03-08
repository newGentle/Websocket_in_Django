const form = document.querySelector('form');
const user_id = document.getElementById('user_id');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    
    params = new FormData(form)
    params.set('slug', params.get('name'));
    params.set('creator', user_id.textContent)

    // params.set('members', user_id.textContent)
    // const params = {'name': name.value, 'slug': slug.value};
    // console.log(...params)

    const response = fetch('http://127.0.0.1:8000/api/rooms/', {
        method: 'POST',
        body: params,
    }).then((response) => {
        return response.json();
    }).then((data) => {
        console.log(data);
        
    }).catch((err) => {
        console.log(err);
    }); 
});