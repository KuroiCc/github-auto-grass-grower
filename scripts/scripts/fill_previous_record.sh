if [ ! $1 ]; then
    echo 'ERROR: need to specify from day'
    exit
fi

if [ ! $1 ]; then
    echo 'ERROR: need to specify continuous days'
    exit
fi

from_day=$1
continuous_days=$2

now_time=$(date +"%G-%m-%d %H:%M:%S")

date -s $from_day

for i in $(seq 1 $continuous_days); do
    time=$(date +"%G-%m-%d" -d tomorrow)
    date -s "$time"
    /bin/sh /scripts/auto_commit.sh
done

date -s "$now_time"
