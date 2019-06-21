<?php
/*
 * 本文件包含调用及连接API的函数，
 * 同时包含数字签名验证以及生成数字签名的函数，用于保证通信安全。
 */
require "./config.php";
require "utility.php";


function post_to_payjs(array $data, $url) {
   /*
    * 函数post_to_payjs()是用于将数据发送给API服务器
    * 参数$data是一个包含所有API请求参数的数组，其数组下标是对应API请求的参数名，数组数据则对应API参数数据，
    * 具体请参考https://payjs.cn/help，注意，$data中记得添加数字签名。
    * 参数$url是API服务器地址。
    * 返回数据是一个来自API服务器的对象，具体请参考API文档。
    * 其返回数据已经通过了数字签名认证，从这个函数返回的数据是确保安全的。一旦检测到签名不正确，为了保障您的数据安全，函数会自动报错切停止运行。
    */
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
    $rst = json_decode(curl_exec($ch));
    curl_close($ch);
     if(sign_verify_for_object($rst)){
         return $rst;
     }else{
         echo $GLOBALS['sign_verification_error_msg'];
         die();
     }
}


function sign(array $attributes) {
   /*
    * 函数sign()是用于生成数字签名。
    * 其参数是一个包含所有API请求参数的数组，其数组下标是对应API请求的参数名，数组数据则对应API参数数据。
    * 返回值是对应这个请求参数的签名，数据类型为String
    */
    ksort($attributes);
    $sign = strtoupper(md5(urldecode(http_build_query($attributes)) . '&key=' . $GLOBALS['config_key']));
    return $sign;
}


function sign_verify_for_object($attributes){
   /*
    * 函数sign_verify()是一个用于验证数字签名的函数
    * 参数$attributes是一个来自API返回的对象，具体请参考API文档。
    * 当验证成功时，返回true。
    * 当验证失败时，返回false，意味着有人动过这个传来的数据。
    */
    $arr = object_to_array($attributes);
    $sign_verify = $arr['sign'];
    unset($arr['sign']);
    if(sign($arr) == $sign_verify){
        return TRUE;
    }else{
        return FALSE;
    }
}

function sign_verify_for_array($arr){
    /*
     * 函数sign_verify()是一个用于验证数字签名的函数
     * 参数$attributes是一个来自API返回的对象，具体请参考API文档。
     * 当验证成功时，返回true。
     * 当验证失败时，返回false，意味着有人动过这个传来的数据。
     */
    $sign_verify = $arr['sign'];
    unset($arr['sign']);
    if(sign($arr) == $sign_verify){
        return TRUE;
    }else{
        return FALSE;
    }
}