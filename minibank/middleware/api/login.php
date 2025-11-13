<?php
header('Content-Type: application/json');
include_once("../config/config.php");

$data = json_decode(file_get_contents("php://input"), true);
$username = $data["username"];
$pin = $data["pin"];

$url = $SERVICE_URL . "/api/customer/login_service.php";
$options = [
    'http' => [
        'header'  => "Content-Type: application/json\r\n",
        'method'  => 'POST',
        'content' => json_encode(["username" => $username, "pin" => $pin])
    ]
];
$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);

echo $result;
?>
