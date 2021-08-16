<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
Setting up database...
<br>
<?php
    require_once "./functions.php";

    createTable(
        "Admin",
        "AdminId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        AdminUser VARCHAR(128) NOT NULL,
        AdminPass VARCHAR(128) NOT NULL"
    );

    createTable(
        "Recordings",
        "VideoId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        VideoName VARCHAR(128) NOT NULL,
        VideoDir VARCHAR(256) NOT NULL,
        VideoTaken DATETIME NOT NULL"
    );

    createTable(
        "UserData",
        "UserId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        FirstName VARCHAR(128) NOT NULL,
        LastName VARCHAR(128),
        Gender VARCHAR(12),
        Age INT,
        Address VARCHAR(256),
        Role VARCHAR(128),
        LastScan DATETIME NOT NULL"
    );

    createTable(
        "UserPhoto",
        "PhotoId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        PhotoName VARCHAR(128) NOT NULL,
        PhotoDir VARCHAR(256) NOT NULL"
    );

    createTable(
        "UserDataset",
        "UserId INT NOT NULL,
        PhotoId INT NOT NULL,
        PhotoTaken DATETIME NOT NULL,
        FOREIGN KEY (UserId) REFERENCES UserData(UserId),
        FOREIGN KEY (PhotoId) REFERENCES UserPhoto(PhotoId)"
    );

    createTable(
        "UserScan",
        "UserId INT NOT NULL,
        FirstName VARCHAR(128) NOT NULL,
        LastName VARCHAR(128),
        Gender VARCHAR(12),
        Age INT,
        Address VARCHAR(256),
        Role VARCHAR(128),
        ScanDate DATETIME NOT NULL,
        FOREIGN KEY (UserId) REFERENCES UserData(UserId)"
    );

    createTable(
        "UserScanPhoto",
        "PhotoScanId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        UserId INT NOT NULL,
        PhotoName VARCHAR(128) NOT NULL,
        PhotoDir VARCHAR(256) NOT NULL,
        FOREIGN KEY (UserId) REFERENCES UserData(UserId)"
    );

?>

<br>
...done!
<h4>Database Created!</h4>

<?php

require_once "./functions.php";

$username = $password = $confirm_password = "";
$username_err = $password_err = $confirm_password_err = "";

if($_SERVER["REQUEST_METHOD"] == "POST"){

    // validate inputted username

    $username_len = strlen(trim($_POST["username"]));
    if(empty(trim($_POST["username"]))){
        $username_err = "Please enter username!";
    }else if($username_len < 8){
        $username_err = "Username must have at least 8 characters!";
    }else if($username_len > 128){
        $username_err = "Username length is maxed (128 characters)!";
    }else{
        $username = trim($_POST["username"]);
    }

    // validate inputted password

    $password_len = strlen(trim($_POST["password"]));
    if(empty(trim($_POST["password"]))){
        $password_err = "Please enter password!";
    }else if(strlen(trim($_POST["password"])) < 8){
        $password_err = "Password must have at least 8 characters!";
    }else if(strlen(trim($_POST["password"])) > 128){
        $password_err = "Password length is maxed (128 characters)!";
    }else{
        $password = trim($_POST["password"]);
    }

    // validate confirmed password

    // $value = $_POST["confirm_password"] ?? '';
    // echo $value;
    if(empty(trim($_POST["confirm_password"]))){
        $confirm_password_err = "Please confirm password!";
    }else{
        $confirm_password = trim($_POST["confirm_password"]);
        if(empty($password_err) && ($password != $confirm_password)){
            $confirm_password_err = "Password did not match!";
        }
    }

    if(empty($username_err) && empty($password_err) && empty($confirm_password_err)){

        $query = "INSERT INTO Admin VALUES(NULL, ?, ?)";

        if($stmt = $conn->prepare($query)){
            $stmt->bind_param("ss", $param_username, $param_password);

            $param_username = $username;
            $param_password = password_hash($password, PASSWORD_DEFAULT);

            if($stmt->execute()){
                $success_mess = "Register success!, redirecting to login page...";
                sleep(5);
                header("location: ../auth/login.php");
            }else{
                echo $stmt->error;
                echo $fatal_error;
            }
            $stmt->close();
        }

    }
    $conn->close();
}

include "../templates/register.php";

?>
