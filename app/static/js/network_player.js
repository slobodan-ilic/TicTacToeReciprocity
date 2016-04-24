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

function UpdateBoardOnSocketIO(data) {
    var result = data.result;
    if ((result != 'Player X Turn') &&
            (result != 'Player O Turn')) {
        $('#frm_get_result').submit();
    }
    var m = data.updated_board.length;
    for (var i=0; i<m; i++) {
        var row = data.updated_board[i];
        var n = row.length;
        for (var j=0; j<n; j++) {
            var index = i * m + j;
            var pos = row[j];
            var html;
            var strBtnSelector = '#btn_' + index;
            if (pos[2] == 'O') {
                html = '<i class="glyphicon glyphicon-unchecked"></i>';
                $(strBtnSelector).html(html);
                $(strBtnSelector).attr('disabled', 'disabled');
            }
            else if (pos[2] == 'X') {
                html = '<i class="glyphicon glyphicon-remove"></i>';
                $(strBtnSelector).html(html);
                $(strBtnSelector).attr('disabled', 'disabled');
            }
        }
    }
}
