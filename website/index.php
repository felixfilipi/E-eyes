<?php

require_once "./models/functions.php";
session_start();

$loggedin = "";

if(isset($_SESSION["loggedin"]) == TRUE){
    $loggedin = TRUE;
    $admin_id = htmlspecialchars($_SESSION["id"]);
}else{
    $loggedin = FALSE;
}

if($loggedin){
    include "./templates/main_menu.php";
}else{
    header("Location: ./auth/login.php");
    exit;
}

?>
