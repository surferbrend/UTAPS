var httpProxy = require('http-proxy');

var endpoint  = {
    host:   '155.98.12.127', //of webservice
    port:   80, 
    prefix: '/api/queryall/?format=json'  //all my webservices are accessed through this path
}

app.use(function(req, res) {
    if (req.url.indexOf(endpoint.prefix) === 0) {
        proxy.proxyRequest(req, res, endpoint);
    }
});
