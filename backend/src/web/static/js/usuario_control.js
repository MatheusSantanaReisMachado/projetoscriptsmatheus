var myApp = angular.module('myApp', [], function($interpolateProvider) {
	$interpolateProvider.startSymbol('{_');
	$interpolateProvider.endSymbol('_}');
});

function controller($scope, $http){

	$scope.usuarios = []
	$http.get('/listar/listar').success(function (json){
		$scope.usuarios = json;
	})

	$scope.editarUsuario = function(usuario){
		usuario.editando = true;
	}

	$scope.salvarUsuario = function(){

		var usuario = {"nome":$scope.inputNome,
				    "email":$scope.inputEmail};

		$http.post('/listar/salvar', usuario).success(function (json){

			usuario.id = json.idUsuario;
			usuario.editando = false;
			$scope.usuarios.push(usuario);

			$scope.inputNome = "";
			$scope.inputEmail = "";

		});

	}

	$scope.confirmarEdicao = function(usuario){

        usuario.editando = false;

		params =  {"idUsuario":usuario.id,
				     "nome":usuario.nome,
				    "email":usuario.email}

		$http.post('/listar/editar', params );
	}

	$scope.removerElemento = function(usuario, index){

		$scope.usuarios.splice(index, 1);
		usuario.editando = false;

		$http.post('/listar/remover', {"idUsuario":usuario.id});
	}



}