<?php
session_start();

if(isset($_SESSION["loggedin"]) == FALSE){
	header("Location: ../index.php");
	exit;
}

require_once "./functions.php";
?>

<html>
	<head>
		<title>Scan Result</title>
	</head>
<style>
table, th, td {
	border: 1px solid black;
}
</style>
<body>
<a href="../index.php">Go back</a>

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
        <table>
            <tr>
                <th>No</th>
                <th>Photo</th>
                <th>Name</th>
                <th>Gender</th>
                <th>Role</th>
                <th>Scan Date</th>
                <th>Temperature</th>
            </tr>
    EOT;

    $i = 0;

    while($row = $stmt->fetch_assoc()){
        $i++;

        if($row["Temperature"] >= 38){
            $temp_message = "<font color='red'>". $row["Temperature"] ."</font>";
        }else{
            $temp_message = $row["Temperature"];
        }

        echo "<tr>
                <td>" . $i . "</td>
                <td><img src='../" . $row["PhotoDir"] . $row["PhotoName"] . "'></td>
                <td>". $row["FirstName"] ." ". $row["LastName"] . "</td>
                <td>". $row["Gender"] ."</td>
                <td>". $row["Role"] ."</td>
                <td>". $row["ScanDate"] ."</td>
                <td>". $temp_message ."</td>
            <tr>";
    
    }
    echo "</table>";
}else{
    echo "0 results";
}

?>
</body>
</html>
