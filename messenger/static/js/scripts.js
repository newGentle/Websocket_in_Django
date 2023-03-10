"use stricts";

// let a = JSON.parse(document.getElementById('rooms').textContent)

const checker = document.getElementById("room") !== null;
console.log(checker);
if (checker) {
  const username = JSON.parse(document.getElementById("user_username").textContent);
  const room = JSON.parse(document.getElementById("room").textContent);
  
  const dt = fetch(`http://127.0.0.1:8000/api/v1/rooms/${room}/?format=json`)
    .then((response) => {
      console.log(response);
      return response.json();
    })
    .then((data) => {
      console.log(data);
      // for (let item of data.room) {
      //     let room = document.querySelector('.room');
      //     room.innerHTML += '<div>' + item + '</div>';
      // };
    });

  const chatSocket = new WebSocket(
    "ws://" + window.location.host + "/ws/api/v1/rooms/" + room + "/"
  );
  // chatSocket.onopen = (e) => {
  //   chatSocket.send(
  //     JSON.stringify({
  //       username: "akbar",
  //       message: "Hello",
  //     })
  //   );
  // };

  chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    if (data.message) {
      document.querySelector("#chat-text").innerHTML +=
        ('<div class="rounded text-bg-secondary float-end">' + data.username +' : '+ data.message + '</div>');
    } else {
      alert("empty");
    }
  };
  document.querySelector("#submit").onclick = function (e) {
    e.preventDefault();
    const messageInput = document.querySelector("#input")
    const message = messageInput.value;
    chatSocket.send(JSON.stringify({
        'message': message,
        'username': username,
        'room': room
      }));
    messageInput.value = '';
    return false;
  };
  chatSocket.onclose = function (e) {
    console.error("The socket closed unexpectedly", e);
  };

  // const jtext = JSON.parse(dt);
}
