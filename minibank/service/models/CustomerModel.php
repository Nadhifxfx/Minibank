<?php
class CustomerModel {
    private $conn;
    public function __construct($db) { $this->conn = $db; }

    public function login($username, $pin) {
        $sql = "SELECT id, customer_name, customer_username, mb_status 
                FROM m_customer WHERE customer_username=? AND customer_pin=?";
        $stmt = $this->conn->prepare($sql);
        $stmt->bind_param("ss", $username, $pin);
        $stmt->execute();
        return $stmt->get_result()->fetch_assoc();
    }
}
?>
