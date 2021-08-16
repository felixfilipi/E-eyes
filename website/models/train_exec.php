<?php

$last_id = $_GET["id"];
session_start();

if(isset($_SESSION["loggedin"]) == FALSE){
	header("Location: ../index.php");
	exit;
}

require_once "./functions.php";

if($_SERVER["REQUEST_METHOD"] == "POST"){

	if(isset($_POST["exec"])){

		$command = escapeshellcmd("/home/brian/.virtualenvs/hackaton/bin/python ../py_script/send_data.py " . $last_id);
		$output = null;
		$output = shell_exec($command);
		print($output);

	}else if(isset($_POST["cancel"])){
		//cancel and delete data
		print_r("CANCEL");

	}

}

?>

<html>
<head>
	<title>e-Eyes</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width-device-width initial-scale=1">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="stylesheet" href="../styles/style1.css">
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.0/css/all.css" integrity="sha384-lZN37f5QGtY3VHgisS14W3ExzMWZxybE1SJSEsQp9S+oqd12jhcu+A56Ebc1zFSJ" crossorigin="anonymous">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

	<script src="../styles/index.js"></script>
</head>

<body>
<script src="../styles/logoutfunc.js"> </script>

<nav class="navbar navbar-expand-sm navbar-dark navbar-static-top" style="background: #356BF3;">
<a class="navbar-brand" href="../index.php"><img src="../images/resources/coole.png" alt="logo" style="width:60px;"></a>
<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
<span class="navbar-toggler-icon"></span>
</button>
<div class="collapse navbar-collapse" id="collapsibleNavbar">
<ul class="navbar-nav">
<li class="nav-item">
<a class="nav-link" href="../index.php">HOME</a>
</li>
<li class="nav-item">
<a class="nav-link" href="../about.php">ABOUT</a>
</li>
</ul>
<ul class="navbar-nav ml-auto">
<li class="nav-item">
<a class="nav-link" id="logout" href="../auth/logout.php" onclick="logout"><img src="../images/resources/logout.png" width=20px height=20px></img>LOGOUT</a>
</li>
</ul>
</div>
</nav>

<div class="container mt-5">
<h3 class="text-dark">Please click "Start" to start training data and "Reset" to reset data</h3>
<form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]) . "?id=" . $last_id; ?>" method="post">
	<input type="submit" class="btn btn-success mb-2 mt-2" name="exec" value="Start" />
	<input type="submit" class="btn btn-danger ml-2 mb-2 mt-2" name="cancel" value="Reset" />
</form>
</div>

<div class="jumbotron text-center text-white bg-dark" style="margin-bottom:0">
  <p>Cool-e Incorporation</p>
  <p>Copyright ©2021</p>
</div>

</body>
</html>
