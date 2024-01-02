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