module.exports = function(RED) {
    function WampBrokerNode(n) {
        RED.nodes.createNode(this,n);
        this.url = n.url;
        this.realm = n.realm;
    }
    RED.nodes.registerType("wamp-broker", WampBrokerNode);
}