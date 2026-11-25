#!/bin/bash
cd ~/eigen_video
mkdir -p seg
rm -f seg/*.mp4
A=audio/final
V=media/videos

# join Scene 4 steps a-d into one audio file
printf "file 's4a.wav'\nfile 's4b.wav'\nfile 's4c.wav'\nfile 's4d.wav'\n" > $A/list4.txt
ffmpeg -y -loglevel error -f concat -safe 0 -i $A/list4.txt -c copy $A/s4abcd.wav

dur() { ffprobe -v error -show_entries format=duration -of csv=p=0 "$1"; }

seg() {
  name=$1; v=$2; a=$3; d=$4
  vd=$(dur "$v"); ad=$(dur "$a")
  T=$(awk -v vd=$vd -v ad=$ad -v d=$d 'BEGIN{t=ad+d+0.5; if (vd>t) t=vd; printf "%.3f", t}')
  pad=$(awk -v T=$T -v vd=$vd 'BEGIN{printf "%.3f", T-vd}')
  ms=$(awk -v d=$d 'BEGIN{printf "%d", d*1000}')
  ffmpeg -y -loglevel error -i "$v" -i "$a" \
    -filter_complex "[0:v]tpad=stop_mode=clone:stop_duration=$pad[v];[1:a]adelay=${ms}:all=1,apad[a]" \
    -map "[v]" -map "[a]" -t $T \
    -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -r 60 \
    -c:a aac -b:a 192k -ar 48000 -ac 2 "seg/$name.mp4"
  echo "$name: video ${vd}s | audio ${ad}s (+${d}s delay) -> segment ${T}s | held last frame ${pad}s"
}

seg 01 $V/scenes2/1080p60/Scene1Hook.mp4        $A/s1.wav     10
seg 02 $V/scenes2/1080p60/Scene2Concept.mp4     $A/s2.wav     0.3
seg 03 $V/scenes/1080p60/Scene3.mp4             $A/s3a.wav    0.3
seg 04 $V/scenes4/1080p60/Scene3Columns.mp4     $A/s3b.wav    0.3
seg 05 $V/scenes2/1080p60/Scene3TestVector.mp4  $A/s3c.wav    0.3
seg 06 $V/scenes2/1080p60/Scene3EigenLines.mp4  $A/s3d.wav    0.3
seg 07 $V/scenes2/1080p60/Scene3Compress.mp4    $A/s3e.wav    0.3
seg 08 $V/scenes3/1080p60/Scene4Algebra2.mp4    $A/s4abcd.wav 0.3
seg 09 $V/scenes3/1080p60/Scene4Decomp2.mp4     $A/s4e.wav    0.3
seg 10 $V/scenes2/1080p60/Scene5Interpret.mp4   $A/s5.wav     0.3
seg 11 $V/scenes2/1080p60/Scene6Summary.mp4     $A/s6.wav     0.3

for f in seg/*.mp4; do echo "file '$(basename $f)'"; done > seg/list.txt
ffmpeg -y -loglevel error -f concat -safe 0 -i seg/list.txt -c copy final_video.mp4
echo "FINAL LENGTH: $(dur final_video.mp4) seconds"
