var dashboardSocket;
function DashboardSocket() {
    dashboardSocket = new WebSocket(`ws://127.0.0.1:8000/socket/dashboard`);
    dashboardSocket.onopen = function(event) {
        connectDataDashboard();
    };

    dashboardSocket.onclose = function(event) {
        setTimeout(function() {
            DashboardSocket();
        }, 1000);
    }

    dashboardSocket.onmessage = function(event) {
        setupDataDashboard(event);
    };

    dashboardSocket.onerror = function(event) {
        dashboardSocket.close();
    }
}

function setupDataDashboard(data) {
    console.log("DATA", data)
}
function fetchDataDashboard() {
    var msg = {
        "type": "fetch"
    }
    dashboardSocket.send(JSON.stringify(msg))
}
function connectDataDashboard() {
    var msg = {
        "type": "connect"
    }
    dashboardSocket.send(JSON.stringify(msg))
}

DashboardSocket();