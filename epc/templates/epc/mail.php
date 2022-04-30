<?php
//get data from form

$name = $_POST['name'];
$email= $_POST['email'];
$message= $_POST['message'];
$number= $_POST['mobile'];
$to = "annalurusudarsan@gmail.com";
$subject = "Mail From SmartJob";
$txt ="Name = ". $name . "\r\n  Email = " . $email . "\r\n Message =" . $message."\r\n Mobile Number=" . $number;
$headers = "From: noreply@ysmartjob.com" . "\r\n" .
"CC: somebodyelse@example.com";
if($email!=NULL){
    mail($to,$subject,$txt,$headers);
}
//redirect
header("Location:thankyou.html");
?>