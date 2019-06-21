# PHP Connect To WeChat Pay API For PayJs
一个可以直接接入系统的PayJs的微信支付接口的PHP代码。<br>

暂时这个不存在任何安全问题。
# 如何布置？
1，编辑config.php，设置里面的信息，文件内有注释来指示你怎么改。<br>
2，编辑action.php，这个里面放置你自己需要运行的PHP代码，并且里面有你需要的变量，以及什么时候被执行，文件内有注释来指示你怎么做。（当然，你可以忽略这个）<br>
3，复制整个项目到你的网站根目录或者任意一个位置，但必须能够访问得到。<br>
# 如何使用？
使用前，请确保布置完毕。<br>
使用方法：访问xxx.com/aaa/PHP-Connect-To-WeChat-Pay-API-For-PayJs/index.php?money=100&title=支付标题<br>
其中：xxx.com/aaa/PHP-Connect-To-WeChat-Pay-API-For-PayJs/是你访问到这个PHP的URL以及页面路径。<br>

访问时，请确保有两个参数？money=100&title=XXX<br>
money参数指要支付多少钱，单位为分。<br>
title指即将显示在微信支付手机上的支付标题。<br>

# 我们还没做的：
2，我们正在解决手机移动设备的访问。<br>

# 使用前，请注意：
Session变量：<br>
$_SESSION['payjs_payment_info'] 
和
$_SESSION['payjs_paid'] <br>
我已经用了，所以别占这两个变量。<br>

使用异步账单通知时，把这个站点的文件的PHP读写权限开启。<br>

最后 ，一定要看config.php和action.php的注释
