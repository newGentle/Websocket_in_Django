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
  chatSocket.onopen = (e) => {
    ScrollingToBottom();
  };

  chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    if (data.message) {
      let owner = 'offset-md-8 col-md-4 mb-2 me-2';
      let others = 'col-md-4 mb-2 ms-2';
      let sender = '';
      let rightOwner = '' 
      let br = '';
      if (username == data.username) {
        sender = owner;
        rightOwner = 'class="float-end me-3"';
        br = '<br>'
      }
      else {
        sender = others
      };
      document.querySelector("#chat-text").querySelector('.container').innerHTML +=
        (   
        "<div class='row'>" + 
        "<div class='" + sender +"'>" +
        "<div class='p-2 rounded text-bg-dark'>" +
        "<p " + rightOwner + ">" + data.username + "</p> "+ br +"<hr>" + 
        data.message +
        "</div></div></div>"
        );
        
        ScrollingToBottom();
        document.getElementById("input").focus();
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
};

function ScrollingToBottom() {
  let messagesBox = document.getElementById('chat-text');
  messagesBox.scrollTop = messagesBox.scrollHeight;
};

const getUsername = (e) => {
  if (e.target.className.includes('js_get-username')){
    const text = e.target.textContent.trim() + ' <= ';
    document.getElementById('input').value = text
    document.getElementById("input").focus();
  }
  
  // console.log(e.target.textContent);
};

window.addEventListener('click', getUsername);

