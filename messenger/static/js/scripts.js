"use stricts";

// let a = JSON.parse(document.getElementById('rooms').textContent)

const checker = document.getElementById("room") !== null;
console.log(checker);
if (checker) {
  let c = JSON.parse(document.getElementById("user_username").textContent);
  const room = JSON.parse(document.getElementById("room").textContent);
  
  const dt = fetch(`http://127.0.0.1:8000/api/rooms/${room}/?format=json`)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log(data.room.members);
      // for (let item of data.room) {
      //     let room = document.querySelector('.room');
      //     room.innerHTML += '<div>' + item + '</div>';
      // };
    });

  const chatSocket = new WebSocket(
    "ws://" + window.location.host + "/ws/api/rooms/" + room + "/"
  );
  chatSocket.onopen = (e) => {
    chatSocket.send(
      JSON.stringify({
        username: "akbar",
        message: "Hello",
      })
    );
  };

  chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    if (data.message) {
      document.querySelector("#chat-text").innerHTML +=
        data.username + data.message + "<br>";
    } else {
      alert("empty");
    }
    console.log("onMessage", e);
  };

  chatSocket.onclose = function (e) {
    console.error("The socket closed unexpectedly", e);
  };

  // const jtext = JSON.parse(dt);
}
