/**
* DelPostController
* @namespace thinkster.posts.controllers
*/
(function () {
  'use strict';

  angular
    .module('thinkster.posts.controllers')
    .controller('DelPostController', DelPostController);

  DelPostController.$inject = ['$location', '$rootScope', '$routeParams', '$scope', 'Authentication', 'Snackbar', 'Posts'];

  /**
  * @namespace DelPostController
  */
  function DelPostController($location, $rootScope, $routeParams, $scope, Authentication, Snackbar, Posts) {
    var vm = this;
    var username = $routeParams.username;
    var post_id = $routeParams.post_id;

    vm.distroy_post = distroy_post;
    vm.post_id = post_id;
    console.info('username ' + username);

    activate();


    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated.
    * @memberOf thinkster.profiles.controllers.ProfileSettingsController
    */
    function activate() {
      var authenticatedAccount = Authentication.getAuthenticatedAccount();

      // Redirect if not logged in
      if (!authenticatedAccount) {
        $location.url('/');
        Snackbar.error('You are not authorized to Delete this post.');
      } else {
        // Redirect if logged in, but not the owner of this profile.
        if (authenticatedAccount.username !== username) {
          $location.url('/');
          Snackbar.error('You are not authorized to Delete this post.');
        }
      }

    }

    /**
    * @name distroy_post
    * @desc delete a new Post
    * @memberOf thinkster.posts.controllers.DelPostController
    */
    function distroy_post() {
      $rootScope.$broadcast('post.deleted', {
        content: vm.content,
        author: {
          username: Authentication.getAuthenticatedAccount().username
        }
      });

      //$scope.closeThisDialog();
      //alert(Authentication.getAuthenticatedAccount().username);
      Posts.distroy_post(vm.post_id).then(deletePostSuccessFn, deletePostErrorFn);


      /**
      * @name deletePostSuccessFn
      * @desc Show snackbar with success message
      */
      function deletePostSuccessFn(data, status, headers, config) {
         $location.url('/');
         Snackbar.show('Success! Post deleted.');
      }


      /**
      * @name deletePostErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function deletePostErrorFn(data, status, headers, config) {
        $rootScope.$broadcast('post.deleted.error');
         $location.url('/');
         Snackbar.error(data.error);
      }
    }
  }
})();