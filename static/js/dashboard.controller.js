(function () {
    'use strict';

    angular.module('dashboard.demo')
        .controller('DashboardController',
                    ['$scope', '$http', '$location', '$routeParams', 'Login', DashboardController]);

    function DashboardController($scope, $http, $location, $routeParams, Login) {
        $scope.add = function (list, title) {
            var record = {
                id: "3", 
                amount: 300,
                currency: "USD",
                issuer: "HSBC",
                time: "2016-01-21T11:21:00Z",
                active: true
            };

            $http.post('/dashboard/cashagreement/', record)
                .then(function (response) {
                    list.records.push(response.data);
                },
                function(){
                    alert('Could not create record: ' + response.data);
                }
            );

        };


        activate();

        function activate() {
            if (!Login.isLoggedIn()) {
                $location.url('/login');
            }

            $scope.project = {name: "Loading.."};
            $scope.logout = Login.logout;

            var url = '/dashboard/cashagreement/' + $routeParams.id + '/';
            $http.get(url).then(
                function (response) {
                    $scope.project = response.data;
                }, function(){
                    alert('Could not load record :(');
                }
            );
        }
    }

}());
