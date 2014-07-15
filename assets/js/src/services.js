'use strict';

/* Services */


// Demonstrate how to register services
// In this case it is a simple value service.
angular.module('myApp.services', ['ngResource']).
  factory('Cluster', function($resource) {
      return $resource('/api/clusters/:clusterId', {}, {});
  }).
  factory('Datastore', function($resource) {
  	return $resource('/api/datastores/:datastoreId', {}, {});
  });
