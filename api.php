<?php
header("Content-Type: application/json");
header("Access-Control-Allow-Origin: *"); 


$json = file_get_contents('php://input');
$data = json_decode($json, true);

if (isset($data['text_input'])) {
    $textInput = $data['text_input'];
    
   
    $safeInput = escapeshellarg($textInput);

    
    $command = "python main.py $safeInput 2>&1";
    $output = shell_exec($command);


    if ($output) {
        
        echo $output;
    } else {
        echo json_encode(["error" => "Python execution failed"]);
    }
} else {
    echo json_encode(["error" => "No text_input provided"]);
}
?>