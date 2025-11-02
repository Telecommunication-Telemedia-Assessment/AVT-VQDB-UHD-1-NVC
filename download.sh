base_url="https://avtshare01.rz.tu-ilmenau.de/avt-vqdb-uhd-1-nvc"

wget -q --show-progress -r -l1 -np -nH --cut-dirs=1 -R "*.html*" -A "*.mkv" -c -P . "${base_url}/decoded/"
wget -q --show-progress -r -l1 -np -nH --cut-dirs=1 -R "*.html*" -A "*.mkv" -c -P . "${base_url}/original/"