<?php
session_start();

if(isset($_SESSION["loggedin"]) == FALSE){
	header("Location: ../index.php");
	exit;
}

require_once "./functions.php";
?>

<!DOCTYPE html>
<html lang="en">
  
<head>
<title>e-Eyes</title>
<meta charset="utf-8">
<meta name="viewport" content="width-device-width initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="css/style1.css">
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.0/css/all.css" integrity="sha384-lZN37f5QGtY3VHgisS14W3ExzMWZxybE1SJSEsQp9S+oqd12jhcu+A56Ebc1zFSJ" crossorigin="anonymous">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

<script src="js/index.js"></script>
</head>

<body>
<nav class="navbar navbar-expand-sm bg-info navbar-dark navbar-static-top">
<a class="navbar-brand" href="index.html">e-Eyes</a>
<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
<span class="navbar-toggler-icon"></span>
</button>
<div class="collapse navbar-collapse" id="collapsibleNavbar">
<ul class="navbar-nav">
<li class="nav-item">
<a class="nav-link" href="index.php">HOME</a>
</li>
<li class="nav-item">
<a class="nav-link" href="about.php">ABOUT</a>
</li>
</ul>
<ul class="navbar-nav ml-auto">
<li class="nav-item">
<a class="nav-link" href="#"><img src="logout.png" width=20px height=20px></img>LOGOUT</a>
</li>
</ul>
</div>
</nav>

<?php

$query = 
"SELECT
    UserScanPhoto.PhotoDir,
    UserScanPhoto.PhotoName,
    UserScan.FirstName,
    UserScan.LastName,
    UserScan.Gender,
    UserScan.Role,
    UserScan.ScanDate,
    UserScan.Temperature
FROM
    UserScan,
    UserScanPhoto
WHERE
    UserScan.UserId = UserScanPhoto.UserId";

$stmt = $conn->query($query);

if($stmt->num_rows > 0){
    echo <<< EOT		
        <table class="table table-bordered">
		<thead>
            <tr>
                <th>No</th>
                <th>Photo</th>
                <th>Name</th>
                <th>Gender</th>
                <th>Role</th>
                <th>Scan Date</th>
                <th>Temperature</th>
            </tr>
		</thead>
    EOT;

    $i = 0;

    while($row = $stmt->fetch_assoc()){
        $i++;

        if($row["Temperature"] >= 38){
            $temp_message = "<font color='red'>". $row["Temperature"] ."</font>";
        }else{
            $temp_message = $row["Temperature"];
        }

        echo "<tbody>
			<tr>
                <td>" . $i . "</td>
                <td><img src='../" . $row["PhotoDir"] . $row["PhotoName"] . "'></td>
                <td>". $row["FirstName"] ." ". $row["LastName"] . "</td>
                <td>". $row["Gender"] ."</td>
                <td>". $row["Role"] ."</td>
                <td>". $row["ScanDate"] ."</td>
                <td>". $temp_message ."</td>
            <tr>
			</tbody>";
    
    }
    echo "</table>";
}else{
    echo "0 results";
}

?>


<div class="jumbotron text-center text-white bg-dark" style="margin-bottom:0">
  <p>Copyright ©2021</p>
</div>

<script>

</script>

</body>
</html>
