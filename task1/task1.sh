mkdir http2
for idx in $(seq 1 1 100)
do
  tcpdump -i eth1 src 10.0.0.1 or dst 10.0.0.1 -w "http2/$(printf "%03d" $idx).pcap" > /dev/null 2>&1 &
  sleep 0.5
  curl --http2 10.0.0.1 > /dev/null 2>&1 &&
  sleep 2
  kill "$!" > /dev/null 2>&1
done

mkdir quic
for idx in $(seq 1 1 100)
do
  tcpdump -i eth1 src 10.0.0.1 or dst 10.0.0.1 -w "quic/$(printf "%03d" $idx).pcap" > /dev/null 2>&1 &
  sleep 0.5
  ~/cs341-23s-lab2/QUIC/quic_client --host=10.0.0.1 --port=6121 https://www.example.org/ --disable_certificate_verification > /dev/null 2>&1 &&
  sleep 2
  kill "$!" > /dev/null 2>&1
done
