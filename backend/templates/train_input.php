<html>
    <head>
        <title>Training Inputs</title>
    </head>
<body>
    <div>
        <p>input new user's data:</p>
        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method = "post">
        <div class="form-group <?php echo (!empty($firstname_err)) ? 'has-error' : ''; ?>">
            <label>First Name</label>
            <input type="text" name="firstname" class="form-control" value="<?php echo $firstname; ?>">
            <span class="help-block"><?php echo $firstname_err ?></span>
        </div><br>

        <div class="form-group <?php echo (!empty($lastname_err)) ? 'has-error' : ''; ?>">
            <label>Last Name</label>
            <input type="text" name="lastname" class="form-control" value="<?php echo $lastname; ?>">
            <span class="help-block"><?php echo $lastname_err ?></span>
        </div></br>

        <div class="form-group <?php echo (!empty($gender_err)) ? 'has-error' : ''; ?>">
            <label>Gender</label>
            <input type="text" name="gender" class="form-control" value="<?php echo $gender; ?>">
            <span class="help-block"><?php echo $gender_err ?></span>
        </div><br>

        <div class="form_group <?php echo (!empty($role_err)) ? 'has-error' : ''; ?>">
            <label>Role</label>
            <input type="text" name="role" class="form-control" value="<?php echo $role; ?>">
            <span class="help-block"><?php echo $role_err ?></span>
        </div><br>

        <div class="form-group">
            <input type="submit" class="btn btn-primary" value="Submit">
            <input type="reset" class="btn btn-default" value="Reset">
        </div>
    </div>
</body>
</html>
