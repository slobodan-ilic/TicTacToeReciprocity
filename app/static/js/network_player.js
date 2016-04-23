function InviteNetworkPlayer(invitedUserName) {
    try {
        var socket = io.connect('http://' + document.domain + ':' +
            location.port + '/Reciprocity');
        socket.emit('Invite Network Player',
            {
                invitedUserName: invitedUserName
            });
    }
    catch (err) {
        alert(err.message);
    }
}
