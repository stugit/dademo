(function () {
    'use strict';

    angular.module('dashboard.demo', ['ngRoute'])
        .controller('DashboardController',
            ['$scope', '$http', 'Login', DashboardController]);

    function DashboardController($scope, $http, Login) {
        $scope.add = function (list, title) {
            var record = {
                list: list.id,
                title: title
            };

            $http.post('/dashboard/cashagreement/', record)
                .then(function (response) {
                        list.record.push(response.data);
                    },
                    function () {
                        alert('Could not create record: ');
                    }
                );

        };


        Login.redirectIfNotLoggedIn();
        $scope.data = [];
        $scope.logout = Login.logout;
        $scope.sortBy = 'story_points';
        $scope.reverse = true;
        $scope.showFilters = false;


        $http.get('/dashboard/cashagreement/').then(
            function (response) {
                $scope.data = response.data;
            }
        );


        $scope.submit = function() {
            alert("Submit");
        }
    }

}());