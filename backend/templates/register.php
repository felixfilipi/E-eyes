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
        <img src="../images/resources/logoproduk.jpeg" class="img-fluid" alt="Phone image">
      </div>
      <div class="col-md-7 col-lg-5 col-xl-5 offset-xl-1">
        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method = "post">
		<h3 center class="text-dark">REGISTER PAGE</h3>
		<br>
          <div class="form-outline mb-4 <?php echo (!empty($username_err)) ? 'has-error' : ''; ?>">
            <input type="text" name="username" id="formusername" placeholder="Username" class="form-control" value="<?php echo $username; ?>">
            <span class="help-block text-danger"><?php echo $username_err; ?></span><br>
          </div>

          <div class="form-outline mb-4 <?php echo (!empty($password_err)) ? 'has-error' : ''; ?>">
            <input type="password" placeholder="Password" id="formpassword" name="password" class="form-control" value="<?php echo $password; ?>">
            <span class="help-block text-danger"><?php echo $password_err; ?></span><br>
          </div>
		  
		  <div class="form-outline mb-4 <?php echo (!empty($confirm_password_err)) ? 'has-error' : ''; ?>">
            <input type="password" placeholder="Confirm Password" id="formconfirmpassword" name="confirm_password" class="form-control" value="<?php echo $confirm_password; ?>">
			<span class="help-block text-danger"><?php echo $confirm_password_err; ?></span><br>
          </div>

          <button type="submit" class="btn btn-primary btn-lg btn-block">Submit</button>
		  <button type="reset" class="btn btn-danger btn-lg btn-block">Reset</button>
        </form>
      </div>
    </div>
  </div>
</section>

</body>
</html>
