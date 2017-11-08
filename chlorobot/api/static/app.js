var app = angular.module('app', ['ngResource']);

app.config(function($resourceProvider, $httpProvider) {
	$resourceProvider.defaults.stripTrailingSlashes = false;
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

app.controller('AppCtrl', function($scope, $resource, API) {

	API.query({"endpoint":"logs", 'ordering' : 'create_datetime'}).$promise.then(
		function(data) {
			$scope.instances = data;
		},
		function(error) {
			console.log(error);
		}
	);

	const webSocketBridge = new channels.WebSocketBridge();

	webSocketBridge.connect('/ws/');

	webSocketBridge.socket.addEventListener('open', function() {
		console.log("Connected to WebSocket");
	})

	webSocketBridge.listen(function(action, stream) {
		console.log(action, stream);
	});

	webSocketBridge.demultiplex('log', function(action, stream) {
		console.log(action, stream);
	});

});



app.factory('API', function($resource) {
	return $resource('/api/v1/:endpoint\/', {endpoint:'@endpoint'});
});

