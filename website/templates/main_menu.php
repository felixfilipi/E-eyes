<!DOCTYPE html>
<html lang="en">
  
<head>
<title>e-Eyes</title>
<meta charset="utf-8">
<meta name="viewport" content="width-device-width initial-scale=1">
<meta name="dicoding:email" content="felixfilipi4@gmail.com">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="./styles/style1.css">
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.0/css/all.css" integrity="sha384-lZN37f5QGtY3VHgisS14W3ExzMWZxybE1SJSEsQp9S+oqd12jhcu+A56Ebc1zFSJ" crossorigin="anonymous">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

<script src="./styles/index.js"></script>
</head>

<body>
<script src="./styles/logoutfunc.js"> </script>

<nav class="navbar navbar-expand-sm navbar-dark navbar-static-top" style="background: #356BF3;">
<a class="navbar-brand" href="./index.php"><img src="./images/resources/ketokan.png" alt="logo" style="width:60px;" /></a>
<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
<span class="navbar-toggler-icon"></span>
</button>
<div class="collapse navbar-collapse" id="collapsibleNavbar">
<ul class="navbar-nav">
<li class="nav-item">
<a class="nav-link active" href="./index.php">HOME</a>
</li>
<li class="nav-item">
<a class="nav-link" href="./about.php">ABOUT</a>
</li>
</ul>
<ul class="navbar-nav ml-auto">
<li class="nav-item">
<a class="nav-link" id="logout" href="./auth/logout.php" onclick="logout"><img src="./images/resources/logout.png" width=20px height=20px></img>LOGOUT</a>
</li>
</ul>
</div>
</nav>

<div class="container">
  <img src="./images/resources/bg1.jpg" alt="Background" style="width:100%; height:350px;">
  <div class="centered"><img src="./images/resources/coole(8).jpg" alt="logo" style="width:150px;" /></div>
</div>

<div class="container">
<div id="carouselExampleControls" class="carousel slide" data-ride="carousel" data-interval="false">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <div class="cards-wrapper">
      <a href="./models/camerastream.php">
          <div class="card card-box rounded-lg" style="background: #C0D9F1;">
            <img src="./images/resources/camera.png" class="card-img-top mx-auto d-block" style="width:140px;" alt="camera-stream">
            <div class="card-body">
              <h5 class="card-title text-dark">CCTV</h5>
              <p class="card-text text-dark">Streaming camera in real-time</p>
			  <p class="card-text" style="color: #C0D9F1;">Some quick example text to build on the card title and</p>
            </div>
          </div>
      </a>
      <a href="./models/user_database.php">
      <div class="card rounded-lg" style="background: #E68E8E">
	  <br>
        <img src="./images/resources/database.png" class="card-img-top mx-auto d-block" style="width:140px; height:152px" alt="database">
        <div class="card-body">
          <h5 class="card-title text-dark">Database</h5>
          <p class="card-text text-dark">View data from database</p>
		  <p class="card-text" style="color:#E68E8E;">Some quick example text to build on the card title and</p>
        </div>
      </div>
      </a>
      <a href="./models/scan_result.php">
        <div class="card rounded-lg" style="background:#36F3BC;">
          <img src="./images/resources/scan.png" class="card-img-top mx-auto d-block" style="width:140px;" alt="scan-result">
          <div class="card-body">
            <h5 class="card-title text-dark">Scan Result</h5>
            <p class="card-text text-dark">View presence data on the day</p>
			<p class="card-text" style="color:#36F3BC;">Some quick example text to build on the card title and</p>
          </div>
        </div>
      </a>
    </div>
    </div>
    <div class="carousel-item">
      <div class="cards-wrapper">
        <a href="./models/train.php">
          <div class="card card-box rounded-lg" style="background: #C0D9F1;">
            <img src="./images/resources/training.png" class="card-img-top mx-auto d-block" style="width:140px;" alt="training">
            <div class="card-body">
              <h5 class="card-title text-dark">Training</h5>
              <p class="card-text text-dark">Start training the data</p>
			  <p class="card-text" style="color: #C0D9F1;">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
            </div>
          </div>
      </a>
      <a href="./models/downloadrecording.php">
        <div class="card rounded-lg" style="background:#36F3BC;">
		<br>
          <img src="./images/resources/download.png" class="card-img-top mx-auto d-block" style="width:140px; height:144px;" alt="download-recording">
          <div class="card-body mt-2">
            <h5 class="card-title text-dark">Download Recording</h5>
            <p class="card-text text-dark">Download your recording</p>
			<p class="card-text" style="color:#36F3BC;">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          </div>
        </div>
      </a>
      </div>
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
</div>
    
<div class="jumbotron text-center text-white bg-dark" style="margin-bottom:0">
  <p style="font-family: Courier New;">Cool-e Incorporation</p>
  <p style="font-family: Arial; font-size: 10pt;">Copyright ©2021</p>
</div>

</body>
</html>
