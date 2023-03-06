const form = document.querySelector('form');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    // const name = document.getElementById('id_name');
    // const slug = document.getElementById('id_slug');
    // const params = {'name': name.value, 'slug': slug.value};
    params = new FormData(form)
    console.log(...params)
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