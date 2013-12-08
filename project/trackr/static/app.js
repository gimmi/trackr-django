'use strict';

angular.module('app', ['ngRoute']).config(['$routeProvider', function (rp) {
	rp.when('/search', { templateUrl: 'search.html', controller: 'appSearchCtrl' });
	rp.when('/item/:id', { templateUrl: 'viewitem.html', controller: 'appViewItemCtrl' });
	rp.otherwise({ redirectTo: '/search' });
}]);

angular.module('app').factory('appDataSvc', [function () {
	var body = 'Ignorant branched humanity led now marianne too strongly entrance. Rose to shew bore no ye of paid rent form. Old design are dinner better nearer silent excuse. She which are maids boy sense her shade. Considered reasonable we affronting on expression in. So cordial anxious mr delight. Shot his has must wish from sell nay. Remark fat set why are sudden depend change entire wanted. Performed remainder attending led fat residence far.';

	return {
		data: [
			{ id: 123, title: 'The proliferation of politics is unorthodox in its smugness.', body: body, tags: [{ type: 'default', name: 'Default' }, { type: 'primary', name: 'primary' }] },
			{ id: 456, title: 'The ecology of sensibility is very nearly doctrinal in its nobility.', body: body, tags: [{ type: 'success', name: 'success' }, { type: 'info', name: 'info' }] },
			{ id: 789, title: 'The sanctimoniousness of morphology is obtuse in its relativity.', body: body, tags: [{ type: 'warning', name: 'warning' }, { type: 'danger', name: 'danger' }] }
		]
	};
}]);

angular.module('app').controller('appSearchCtrl', ['$scope', 'filterFilter', 'appDataSvc', function (scope, filterFilter, appDataSvc) {
	scope.searchText = '';
	scope.results = [];

	scope.search = function () {
		console.log(scope.searchText);
		scope.results = filterFilter(appDataSvc.data, scope.searchText);
	};
}]);

angular.module('app').controller('appViewItemCtrl', ['$scope', '$routeParams', 'appDataSvc', function (scope, routeParams, appDataSvc) {
	scope.item = appDataSvc.data.filter(function (x) { return x.id == routeParams.id; })[0];
}]);
