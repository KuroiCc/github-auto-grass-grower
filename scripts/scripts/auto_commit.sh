cd /repo
git pull
python3 /scripts/writefile.py "/repo/${records_file_path:-"records.txt"}" "${human_like:-0}"
git add .
git commit -m "${commit_mesg:-"auto commit"}"
git push