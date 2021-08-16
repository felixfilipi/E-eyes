$(function(){
	$('a#logout').click(function(){
	if(confirm("Are you sure want to logout?")) {
	return true;
	}
	return false;
	});
});