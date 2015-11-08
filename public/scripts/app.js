$(function () {
  var root = document.getElementById("content");

  var App = React.createClass({
    render: function () {
      return (
        <div>
          Hello, world!
        </div>
      );
    }
  });

  React.render(<App/>, root);
})