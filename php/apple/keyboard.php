<?php    
    // This is the data you want to pass to Python
    $data = $_GET["search"];
    
    // Execute the python script with the JSON data
    $result = shell_exec('python ../../python/apple/keyboard.py ' . escapeshellarg(json_encode($data)));
    
    header('Location: ' . $_SERVER['HTTP_REFERER']);
?>