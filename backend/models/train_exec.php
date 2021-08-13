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
	<title>
		Train
	</title>
</head>
<body>
<form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]) . "?id=" . $last_id; ?>" method="post">
	<input type="submit" name="exec" value="Start" />
	<input type="submit" name="cancel" value="Reset" />
</form>
</body>
</html>
