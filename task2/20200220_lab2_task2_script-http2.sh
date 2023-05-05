for idx in $(seq 1 1 100)
do
  curl --http2 10.0.0.1 > /dev/null 2>&1 || break
done

