if [ ! $1 ]; then
    echo 'ERROR: Need to apply loop param'
    exit
fi

if [ $1 -gt 365 ]; then
    echo 'over 365'
    exit
fi

now_time=$(date +"%G-%m-%d %H:%M:%S")

path="test/records-${now_time}.txt"

date -s "2020-01-01"

for i in $(seq 1 $1); do
    time=$(date +"%G-%m-%d" -d tomorrow)
    date -s "$time"
    python3 /scripts/writefile.py "${path}" "0"
done

date -s "$now_time"
python3 /scripts/simulation.py "${path}"
