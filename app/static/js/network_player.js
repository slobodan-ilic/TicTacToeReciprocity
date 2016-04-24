function InviteNetworkPlayer(invitedUserName) {
    try {
        var socket = SetupSocketIOConnection();
        socket.emit('Invite Network Player',
            {
                invitedUserName: invitedUserName
            });
    }
    catch (err) {
        alert(err.message);
    }
}

function SetupSocketIOConnection() {
    try {
        var socket = io.connect('http://' + document.domain + ':' +
            location.port + '/Reciprocity');
        return socket;
    }
    catch (err) {
        alert(err.message);
    }
}
