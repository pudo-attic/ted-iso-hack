
python make_list.py
wget -c -P isos -i iso_list.txt

mkdir -p mnt
mkdir -p data

for ISO in isos/*; do
  echo $ISO
  sudo mount -o rw $ISO mnt
  for DIRX in mnt/*/*; do
    if [ -d "$DIRX/TED-XML" ]; then
      FN=`ls "$DIRX/TED-XML"`
      cd data
      tar xvfzk ../$DIRX/TED-XML/$FN
      cd ..
    fi
  done
  sudo umount mnt
done
