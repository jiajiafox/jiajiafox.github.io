<!--
5 + 5 = 10 <br>
5 + 5 = <?php print 5+5;?> <br>
5 + <?php print "5 = ".(5+5);?> <br>
<?php 
print "this's a book";
?><br>


<?php
print strlen("stanley");
print trim(" 中文計算一個字=3")
?><br>


<?php
  $sch=1;
  $cla=78;
  $AveS=32.33;
  $總人數=$sch*$cla*$AveS;
  print "總學生人數=$總人數";
?><br>

<?php 
$a=28;
$b=3;
  if($a>$b){
    print "28大於3答案是true";
      }else {
    print "28大於3答案是false";
  }
?><br>


<?php
$msg="哈囉大家好";
$c=mb_strlen($msg);
  if($c>10){
    print "這個字串有" . $c . "個字，大於10";
      }else if($c<10){
    print "這個字串有" . $c ."個字，小於10";
      }else{
    print "這個字串有" . $c . "個字，等於10";
  }
?><br>


<select >
  <?php
    $i=0;
    while($i<=10){
      echo "<option>$i</option>";
      $i++;
    }
  ?>
</select>
<br>

<select>
  <?php
    for($a=0;$a<=30;$a++){
      $b="<option>".$a."</option>";
      echo "$b";
    }
?>
</select>
<br>
-->


<!--
<?php
$a=['windows','MacOS','Linux'];
$a[3]='UNIX';
print_r($a);
?><br>
<?php
$a=array('windows','MacOS','Linux');
$a[3]='UNIX';
print_r($a);
?><br>
<?php
$a=array(0=>'windows',
         1=>'MacOS',
         2=>'Linux');
$a[3]='UNIX';
print_r($a);
?><br>
-->

<?php
$a=['inform1'=>'name',
   'inform2'=>'age',
   'inform3'=>'address',
   'inform4'=>'phone',
   'inform5'=>'email'];

print_r($a);
?>