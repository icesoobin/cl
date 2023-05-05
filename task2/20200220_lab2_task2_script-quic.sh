for idx in $(seq 1 1 100)
do
  ~/cs341-23s-lab2/QUIC/quic_client --host=10.0.0.1 --port=6121 https://www.example.org/ --disable_certificate_verification > /dev/null 2>&1 || break
done

