<?php
include_once(__DIR__ . '/../models/CustomerModel.php');

class CustomerController {
    private $customerModel;
    public function __construct($db) {
        $this->customerModel = new CustomerModel($db);
    }

    public function login($username, $pin) {
        $user = $this->customerModel->login($username, $pin);
        if ($user) {
            return ["status" => "success", "data" => $user];
        } else {
            return ["status" => "failed", "message" => "Username atau PIN salah"];
        }
    }
}
?>
