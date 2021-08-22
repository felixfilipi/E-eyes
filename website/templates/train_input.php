<html>
    <head>
        <title>e-Eyes</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width-device-width initial-scale=1">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
		<link rel="stylesheet" href="../styles/style1.css">
		<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.0/css/all.css" integrity="sha384-lZN37f5QGtY3VHgisS14W3ExzMWZxybE1SJSEsQp9S+oqd12jhcu+A56Ebc1zFSJ" crossorigin="anonymous">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

		<script src="../styles/index.js"></script>
    </head>
<body>
<script src="../styles/logoutfunc.js"> </script>

<nav class="navbar navbar-expand-sm navbar-dark navbar-static-top" style="background: #356BF3;">
<a class="navbar-brand" href="../index.php"><img src="../images/resources/ketokan.png" alt="logo" style="width:60px;" /></a>
<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
<span class="navbar-toggler-icon"></span>
</button>
<div class="collapse navbar-collapse" id="collapsibleNavbar">
<ul class="navbar-nav">
<li class="nav-item">
<a class="nav-link" href="../index.php">HOME</a>
</li>
<li class="nav-item">
<a class="nav-link" href="../about.php">ABOUT</a>
</li>
</ul>
<ul class="navbar-nav ml-auto">
<li class="nav-item">
<a class="nav-link" id="logout" href="../auth/logout.php" onclick="logout"><img src="../images/resources/logout.png" width=20px height=20px></img>LOGOUT</a>
</li>
</ul>
</div>
</nav>
	
    <div class="container mt-5">
  <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method = "post">
  <div class="form-row <?php echo (!empty($firstname_err)) ? 'has-error' : ''; ?>">
	  <div class="col">
		<label for="firstname" class="mb-2 mr-sm-2 mt-2 text-dark">Firstname : </label>
	  </div>
	  <div class="col">
		<input class="form-control mb-2 mr-sm-2 mt-2" type="text" value="<?php echo $firstname; ?>" name="firstname" placeholder="Input First Name">
		<span class="help-block"><?php echo $firstname_err ?></span>
	  </div>
  </div>
  <div class="form-row <?php echo (!empty($lastname_err)) ? 'has-error' : ''; ?>">
	<div class="col">
		<label for="lastname" class="mb-2 mr-sm-2 mt-2 text-dark">Lastname : </label>
	</div>
	<div class="col">
		<input class="form-control mb-2 mr-sm-2 mt-2" type="text" value="<?php echo $lastname; ?>" name="lastname" placeholder="Input Last Name">
		<span class="help-block"><?php echo $lastname_err ?></span>
	</div>
  </div>
  <div class="form-row <?php echo (!empty($gender_err)) ? 'has-error' : ''; ?>">
	<div class="col">
		<label for="gender" class="mb-2 mr-sm-2 mt-2 text-dark">Gender : </label>
	</div>
	<div class="col">
		<input class="form-control mb-2 mr-sm-2 mt-2" type="text" value="<?php echo $gender; ?>" name="gender" placeholder="Input Gender">
		<span class="help-block"><?php echo $gender_err ?></span>
	</div>
  </div>
  <div class="form-row <?php echo (!empty($role_err)) ? 'has-error' : ''; ?>">
	<div class="col">
		<label for="role" class="mb-2 mr-sm-2 mt-2 text-dark">Role : </label>
	</div>
	<div class="col">
		<input class="form-control mb-2 mr-sm-2 mt-2" type="text" value="<?php echo $role; ?>" name="role" placeholder="Input Role">
		<span class="help-block"><?php echo $role_err ?></span>
	</div>
  </div>
  <br>
  <button type="submit" class="btn btn-success mb-2 mt-2">Submit</button>
  <button type="reset" class="btn btn-danger ml-2 mb-2 mt-2">Cancel</button>
  </form>
</div>


<div class="jumbotron text-center text-white bg-dark" style="margin-bottom:0">
  <p style="font-family: Courier New;">Cool-e Incorporation</p>
  <p style="font-family: Arial; font-size: 10pt;">Copyright ©2021</p>
</div>

</body>
</html>
