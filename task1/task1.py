import dpkt
import matplotlib.pyplot as plt

http2LoadingTime = []
for idx in range(1, 100):
  start = None
  end = None
  for ts, pkt in dpkt.pcap.Reader(open("http2/{:03d}.pcap".format(idx),'rb')):
    if not start:
      start = ts
    end = ts
  http2LoadingTime.append(end - start)

quic2LoadingTime = []
for idx in range(1, 100):
  start = None
  end = None
  for ts, pkt in dpkt.pcap.Reader(open("quic/{:03d}.pcap".format(idx),'rb')):
    if not start:
      start = ts
    end = ts
  quic2LoadingTime.append(end - start)

plt.boxplot([http2LoadingTime, quic2LoadingTime], showfliers=False)
plt.xticks([1, 2],['HTTP/2', 'QUIC'])

plt.show()
plt.savefig('task1.png')
