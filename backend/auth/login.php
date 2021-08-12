<?php
session_start();

if(isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true){
	header("location: ../index.php");
	exit;
}

require_once "../models/functions.php";

$username = $password = "";
$username_err = $password_err = "";

if($_SERVER["REQUEST_METHOD"] == "POST"){
    
    //validate username
    if(empty(trim($_POST["username"]))){
        $username_err = "Please enter field!";
    }else{
        $username = trim($_POST["username"]);
    }

    //validate password
    if(empty(trim($_POST["password"]))){
        $password_err = "Please enter field!";
    }else{
        $password = trim($_POST["password"]);
    }

    
    if(empty($username_arr) && empty($password_err)){
        
        $query = "SELECT AdminId, AdminUser, AdminPass FROM Admin WHERE AdminUser = ?";

        if($stmt = $conn->prepare($query)){
            $stmt->bind_param("s", $param_user);
            $param_user = $username;

            if($stmt->execute()){
                $stmt->store_result();

                if($stmt->num_rows == 1){
                    $stmt->bind_result($id, $username, $hashed_pass);
                    if($stmt->fetch()){
                            if(password_verify($password, $hashed_pass)){
    session_start();
    $_SESSION["loggedin"] = TRUE;
    $_SESSION["id"] = $id;
    $_SESSION["username"] = $username;

    header("Location: ../index.php");
}else{
    $password_err = "Password invalid";
}
                    }
                }else{
                    $username_err = "Username not found!";
                }
            }else{
                die($fatal_error);
            }
            $stmt->close();

        }
    }
    $conn->close();
}

include "../templates/login.php";

?>
