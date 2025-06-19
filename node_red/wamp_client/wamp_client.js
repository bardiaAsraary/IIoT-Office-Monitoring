// wamp-client.js
const autobahn = require('autobahn');

const connection = new autobahn.Connection({
    url: 'ws://localhost:8080/ws', // change to your WAMP router address
    realm: 'realm1'
});

connection.onopen = function (session) {
    console.log('Connected to WAMP router.');

    // Subscribe to a topic
    session.subscribe('com.myapp.topic1', function (args) {
        console.log('Received event:', args[0]);
    });
};

connection.onclose = function () {
    console.log('Connection closed');
};

connection.open();
