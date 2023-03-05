const btn = document.getElementById('btn');

btn.addEventListener('click', (e) => {
    e.preventDefault();

    const name = document.getElementById('id_name');
    const slug = document.getElementById('id_slug');
    const params = {'name': name.value, 'slug': slug.value};

    console.log(JSON.stringify(params))
    // const response = fetch('http://127.0.0.1:8000/api/rooms/', {
    //     method: 'POST',
    //     body: JSON.stringify(params),
    // });
    // return response.json();
})