<?php
$host = "localhost";
$user = "minibank_user"; // user MySQL kamu
$pass = "passwordku123"; // password user MySQL
$db   = "minibank";      // database MySQL kamu

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    die(json_encode(["status" => "error", "message" => "Koneksi ke database gagal: " . $conn->connect_error]));
}
?>
