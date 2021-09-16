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
<a class="nav-link" href="./index.php">HOME</a>
</li>
<li class="nav-item">
<a class="nav-link active" href="./about.php">ABOUT</a>
</li>
</ul>
<ul class="navbar-nav ml-auto">
<li class="nav-item">
<a class="nav-link" id="logout" href="./auth/logout.php" onclick="logout"><img src="./images/resources/logout.png" width=20px height=20px></img>LOGOUT</a>
</li>
</ul>
</div>
</nav>

<div class="about-section" style="background: #F3BD35;">
  <h1 class="text-dark">ABOUT US</h1>
  <p class="text-dark">Problems recording attendance in your place</p>
  <p class="text-dark">This website is the solution</p>
</div>

<h2 style="text-align:center" class="mt-5">Our Team</h2>
<div class="cards-wrapper mb-5">
    <div class="card bg-info" style="width: 250px">
      <img src="./images/resources/Felix1.jpeg" alt="Felix Filipi" style="width:100%">
      <div class="container"><br>
        <h4>Felix Filipi</h4>
        <p class="title">Project Manager & Machine Learning</p>
      </div>
    </div>


    <div class="card bg-info" style="width: 250px">
      <img src="./images/resources/Febrian.jpeg" alt="Febrian Nugroho" style="width:100%">
      <div class="container"><br>
        <h4>Febrian Nugroho</h4>
        <p class="title">Backend Developer</p>
      </div>
    </div>
  
    <div class="card bg-info" style="width: 250px">
      <img src="./images/resources/Christoper.jpg" alt="Christoper Luis Alexander" style="width:100%">
      <div class="container"><br>
        <h4>Christoper Luis Alexander</h4>
        <p class="title">Frontend Developer</p>
      </div>
    </div>
</div>

<div class="jumbotron text-center text-white bg-dark" style="margin-bottom:0">
  <p style="font-family: Courier New;">Cool-e Incorporation</p>
  <p style="font-family: Arial; font-size: 10pt;">Copyright ©2021</p>
</div>

<script>

</script>

</body>
</html>
