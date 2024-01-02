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
?>


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
?>


<select >
  <?php
    $i=0;
    while($i<=10){
      echo "<option>$i</option>";
      $i++;
    }
  ?>
</select>


<select>
  <?php
    for($a=0;$a<=30;$a++){
      $b="<option>".$a."</option>";
      echo "$b";
    }
?>
</select>