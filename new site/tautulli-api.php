<?php

// For example: http://localhost:8181
define('TAUTULLI_URL', 'http://stats.efcinema.com');

// tautulli/settings#tab_tabs-web_interface
define('TAUTULLI_TOKEN', 'fc2dd1b2e23741f78b58b3422a56eaa5');

$post = $_POST['postData'];

$defaults = array(
  CURLOPT_URL             => TAUTULLI_URL . '/api/v2?apikey='. TAUTULLI_TOKEN .'&' . http_build_query($post),
  CURLOPT_HEADER          => 0,
  CURLOPT_RETURNTRANSFER  => true,
  CURLOPT_CONNECTTIMEOUT  => 30,
  CURLOPT_TIMEOUT         => 30,
  CURLOPT_FAILONERROR     => true,
);

$ch = curl_init();
curl_setopt_array($ch, $defaults);
$resultstr = curl_exec($ch);
curl_close($ch);

echo $resultstr;

// EOF
