<!DOCTYPE html>
<html lang="en">
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

<section class="vh-100">
  <div class="container py-5 h-100">
    <div class="row d-flex align-items-center justify-content-center h-100">
      <div class="col-md-8 col-lg-7 col-xl-6">
        <img src="../images/resources/logoproduk.jpeg" class="img-fluid" alt="Logo e-Eyes">
      </div>
      <div class="col-md-7 col-lg-5 col-xl-5 offset-xl-1">
        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
		<h3 center class="text-dark">LOGIN PAGE</h3>
		<br>
          <div class="form-outline mb-4">
            <input type="text" id="formusername" name="username" placeholder="Username" class="form-control" value="<?php echo $username; ?>">
            <span class="help-block text-danger"><?php echo $username_err ?></span><br>
          </div>

          <div class="form-outline mb-4">
            <input type="password" placeholder="Password" id="formpassword" name="password" class="form-control" value="<?php echo $password; ?>">
            <span class="help-block text-danger"><?php echo $password_err; ?></span>
          </div>
		  
		  <div class="form-outline mb-4">
            <a href="../models/setup.php">Don't have an account? Register here.</a>
          </div>
          <button type="submit" class="btn btn-primary btn-lg btn-block">Login</button>
		  
        </form>
      </div>
    </div>
  </div>
</section>

</body>
</html>
