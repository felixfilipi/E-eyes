<?php

require_once "../models/functions.php";
session_start();

$userId = htmlspecialchars($_SESSION["id"]);

$_SESSION = array();

session_destroy();
header("Location: ../index.php");
exit;

?>
