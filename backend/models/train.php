<?php

session_start();

if(isset($_SESSION["loggedin"]) == FALSE){
	header("Location: ../index.php");
	exit;
}

require_once "./functions.php";

$firstname = $lastname = $gender = $role = "";
$firstname_err = $lastname_err = $gender_err = $role_err = "";

if($_SERVER["REQUEST_METHOD"] == "POST"){

	//validate firstname
	$firstname_len = strlen(trim($_POST["firstname"]));
	if(empty(trim($_POST["firstname"]))){
		$firstname_err = "Please enter first name!";
	}else if($firstname_len > 128){
		$firstname_err = "First name is too long!";
	}else{
		$firstname = trim($_POST["firstname"]);
	}

	//validate lastname
	$lastname_len = strlen(trim($_POST["lastname"]));
	if(empty(trim($_POST["lastname"]))){
		$lastname_err = "Please enter last name!";
	}else if($lastname_len > 128){
		$lastname_err = "Last name is too long!";
	}else{
		$lastname = trim($_POST["lastname"]);
	}

	//validate gender
	$gender_input = trim($_POST["gender"]);
	if(empty(trim($_POST["gender"]))){
		$gender_err = "Please enter gender!";
	}else if($gender_input == "male" || $gender_input == "female"){
		$gender = $gender_input;
	}else{
		$gender_err = "Gender must be inputted 'male' and 'female' only";
	}

	//validate role
	$role_len = strlen(trim($_POST["role"]));
	if(empty(trim($_POST["role"]))){
		$role_err = "Please enter role!";
	}else if($role_len > 128){
		$role_err = "Role is too long!";
	}else{
		$role = trim($_POST["role"]);
	}

	if(empty($firstname_err) && empty($lastname_err) && empty($gender_err) && empty($role_err)){

		$query = "INSERT INTO UserData VALUES (NULL, ?, ?, ?, ?, ?, ?)";

		if($stmt = $conn->prepare($query)){
			$stmt->bind_param("sssssi",
				$param_firstname,
				$param_lastname,
				$param_gender,
				$param_role,
				$param_lastscan,
				$param_lasttemp);

			$param_firstname = $firstname;
			$param_lastname = $lastname;
			$param_gender = $gender;
			$param_role = $role;
			$param_lastscan = date('Y-m-d H:i:s');
			$param_lasttemp = 0;

			if($stmt->execute()){
				$success_mess = "Input accepted, redirecting to the next step...";
				$last_id = $stmt->insert_id;

				//execute python script
				$command = escapeshellcmd("/home/brian/.virtualenvs/hackaton/bin/python ../py_script/train_signal.py 1");
				$output = null;
				$output = shell_exec($command);
				
				if($output == 1){
					echo "Success";
				}else{
					echo $fatalError;
				}

				sleep(3);
				header("Location: ./train_exec.php?id=". $last_id);
			}else{
				echo $stmt->error;
				echo $fatal_error;
			}
			$stmt->close();
		}

	}
	$conn->close();
}

include "../templates/train_input.php";

?>
