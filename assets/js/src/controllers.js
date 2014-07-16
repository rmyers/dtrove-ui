'use strict';

/* Controllers */


function DashboardController($resource, $scope, Cluster, Datastore) {
  Cluster.query({}, function(data){
    $scope.clusters = data;
  });
  Datastore.query({}, function(data){
    $scope.datastores = data;
  });
  $scope.newCluster = new Cluster();
  $scope.submit = function () {
    var new_cluster = new Cluster($scope.newCluster);
    new_cluster.datastore_id = new_cluster.datastore.id;
    new_cluster.$save();
    $scope.clusters.push(new_cluster);
    $scope.newCluster = new Cluster();
  };

}

DashboardController.$inject = ['$resource', '$scope', 'Cluster', 'Datastore'];
