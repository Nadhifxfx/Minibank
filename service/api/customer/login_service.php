<?php
header('Content-Type: application/json');
include_once("../../config/db.php");
include_once("../../controllers/CustomerController.php");

$data = json_decode(file_get_contents("php://input"), true);
$username = $data["username"];
$pin = $data["pin"];

$controller = new CustomerController($conn);
$response = $controller->login($username, $pin);
echo json_encode($response);
?>
