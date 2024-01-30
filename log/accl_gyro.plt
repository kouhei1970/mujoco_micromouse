set xrange [0:70]
set grid

set multiplot layout 3,2  #multiplotの開始、縦3横1自動配置


plot "accel07.log" u 1:2 w l title "ax"

plot "accel07.log" u 1:5 w l title "gx"

plot "accel07.log" u 1:3 w l title "ay"


plot "accel07.log" u 1:6 w l title "gy"

plot "accel07.log" u 1:4 w l title "az"

plot "accel07.log" u 1:7 w l title "gz"

unset multiplot           #multiplotの終了