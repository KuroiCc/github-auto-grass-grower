git config --global user.name ${git_name:-"docker-github-auto-grass-grower"}
git config --global user.email ${email:-"noemail"}
git clone ${repo_url:?"repo url has not been set"} repo
echo "init git done."
sed -i "$ c${gpu_schedule:-"0 12 * * *"} /bin/sh /scripts/auto_commit.sh" var/spool/cron/crontabs/root
crond -b
