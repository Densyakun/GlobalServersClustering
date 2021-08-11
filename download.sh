curl https://wp-public.s3.amazonaws.com/pings/pings-2020-07-19-2020-07-20.csv.gz -o pings.csv.gz
curl https://wp-public.s3.amazonaws.com/pings/servers-2020-07-19.csv -o servers.csv

gzip -d pings.csv.gz
